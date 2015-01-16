from twisted.internet import reactor, protocol
from twisted.internet.endpoints import TCP4ClientEndpoint
import struct
import packets
import constants
from bytestream import ByteStream
import crypto
import os
import urllib2
from listeners import *
policy = """<?xml version="1.0"?><!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">  <cross-domain-policy>  <site-control permitted-cross-domain-policies="master-only"/>  <allow-access-from domain="*" to-ports="*" /></cross-domain-policy>\n\x00""" 

realpacket = [0,6,50,55,46,50,46,49,255,255,255,254,0,172,113,90,49,82,83,120,66,104,68,115,82,68,122,51,89,115,65,117,115,75,85,122,51,67,99,99,79,109,57,98,75,50,87,118,110,77,83,66,78,121,78,99,77,47,74,89,111,87,55,121,57,82,98,73,107,65,103,70,85,87,84,99,116,90,88,97,97,86,72,120,90,54,50,55,107,89,112,76,77,55,110,80,88,115,69,83,70,80,52,74,79,84,84,51,70,119,83,115,52,103,115,120,74,103,90,73,99,81,100,89,49,112,119,112,87,68,57,67,99,115,122,117,82,104,99,83,86,111,118,66,43,98,80,121,76,75,120,51,66,118,111,72,111,107,117,49,76,115,106,47,55,104,110,119,109,90,103,98,57,112,115,113,89,102,97,80,55,67,112,53,111,61,29,56,66,175,0,172,70,69,89,89,47,53,86,105,54,52,50,119,113,80,103,119,83,114,56,75,112,111,90,100,122,89,43,120,65,48,110,81,83,116,43,107,73,120,90,110,84,56,71,109,52,99,100,73,97,81,47,108,117,56,43,88,87,109,69,74,109,82,110,110,90,43,90,122,49,82,119,75,112,100,79,100,87,88,84,68,115,81,52,76,72,77,76,111,84,105,101,68,74,98,79,73,104,49,105,105,122,51,108,107,77,108,119,103,77,47,108,117,80,80,51,43,107,50,104,77,83,82,114,114,98,43,85,122,102,65,68,51,118,74,49,79,49,69,54,111,89,78,52,50,54,103,65,115,111,43,115,115,47,56,67,97,87,54,43,108,105,120,78,75,48,99,68,43,69,43,103,61,58,2,118,238,0,0,255,255,255,255,0,0,0,0,0,0,0,0,0,5,114,111,116,109,103,0,0,0,5,114,111,116,109,103,0,0]


class ClientHandler():

    def __init__(self, clients=[]):
        self.clients = clients

    def createClient(self, email, password):
        factory = PyRealmFactory(email,password)
        self.clients.append(factory)
        return factory

    def getConnected(self):
        connectedList = []
        for client in self.clients:
            if client.protocolInstance.connected:
                connectedList.append(client)
        return connectedList

class PyRealmConnection(protocol.Protocol):

    def __init__(self):
        self.connected = False
        self.packetLength = -1
        self.packetId = -1
        self.packetBytes = ""
        self.inputstream = ByteStream()
        self.outputstream = ByteStream()
        self.packetQueue = []
        self.latest = {}

    def addPacket(self, packet):
        self.packetQueue.append(packet)

    def connectionMade(self):
        print(self.email.split("@")[0] + " connected!")
        self.connected = True
        self.triggerListener("onConnect")
        
    def connectionLost(self, reason):
        self.connected = False
        print(self.email.split("@")[0] + " lost connection.")
        self.triggerListener("onDisconnect")
        
    def dataReceived(self, data):
        self.inputstream.write(data)
        print self.inputstream.data
        while True:

            if not self.connected:
                break
            
            if self.packetLength == -1:
                self.packetLength = self.inputstream.readInt

                if self.inputstream.available() < 4:
                    break
                self.packetLength = self.inputstream.readInt()


            if self.inputstream.available() < self.packetLength-4:
                break


            self.packetId = self.inputstream.readUnsignedByte()

            packet = packets.create(self.packetId)

            if self.packetLength-5 > 0:
                data = ByteStream(self.inputstream.read(self.packetLength-5))

            self.from_server.encrypt(data)

            packet.parseFromInput(data)
            self.handlePacket(packet)

    def writePacket(self, packet):
        output = ByteStream()
        packet.writeToOutput(output)
        packetByteArray = output.data
        self.to_server.encrypt(packetByteArray)
        output = ByteStream(packetByteArray)
        print "SENDING PACKET"
        print "LENGTH: " + str(len(packetByteArray))
        print "ID: " + str(packet.getId())
        self.transport.write(struct.pack(">i", len(packetByteArray)+5))
        self.transport.write(chr(packet.getId()))
        self.transport.write(output.asString())

    def handlePacket(self, packet):
        print("NEW PACKET: " + packet.__class__.__name__)
        if isinstance(packet, packets.MapinfoPacket):
            self.triggerListener("onLoad", packet)
            self.latest[str(packet.getId())] = packet

    def fetchXML(self):
        xml = util.readURL(constants.CHARLIST_FORMAT.format(self.email,self.password))
        

    def hello(self,key=None,keyTime=-1,gameId=-2):
        if not key:
            key = []
        hello = packets.HelloPacket()
        hello.buildVersion = constants.VERSION
        hello.gameId = gameId
        hello.secret = ""
        hello.guid = crypto.RSA_encrypt(self.email)
        hello.password = crypto.RSA_encrypt(self.password)
        hello.key = key
        hello.keyTime = keyTime
        hello.obf1 = ""
        hello.obf2 = ""
        hello.obf3 = "rotmg"
        hello.obf4 = ""
        hello.obf5 = "rotmg"
        hello.obf6 = ""
        self.writePacket(hello)

class PyRealmFactory(protocol.ClientFactory):
    protocol = PyRealmConnection
    listeners = []

    def __init__(self,email, password):
        self.email = email
        self.password = password

    def addListener(self, listener):
        self.listeners.append(listener)
        self.protocolInstance.listeners.append(listener)
    
    def buildProtocol(self, addr):
        p = PyRealmConnection()
        p.to_server = crypto.getCipher(constants.OUT_CIPHER)
        p.from_server = crypto.getCipher(constants.IN_CIPHER)
        p.email = self.email
        p.password = self.password
        p.factory = self
        p.listeners = self.listeners
        p.addListener = self.addListener
        p.triggerListener = self.triggerListener
        self.protocolInstance = p
        return p

    def triggerListener(self, name, *args):
        for listener in self.listeners:
            func = getattr(listener, name)
            if func:
                func(*args)

    def clientConnectionLost(self, connector, reason):
        self.ip = None
        self.port = None
        
    def startedConnecting(self, connector):
        self.connector = connector

    def disconnect(self):
        if self.protocolInstance.connected and self.connector:
            self.connector.disconnect()

    def connect(self, ip, port):
        self.ip = ip
        self.port = port
        reactor.connectTCP(ip, port, self)

class PolicyClient(protocol.Protocol):

    def connectionMade(self):
        self.sendMessage()

    def sendMessage(self):
        self.transport.write("<policy-file-request/>\x00")

    def dataReceived(self, data):
        print data
        self.factory.connector.disconnect()
        handler = ClientHandler()
        factory = handler.createClient("b1@rotmgmuleverifier.appspotmail.com", "123456asd1")
        factory.listeners.append(TestListener(factory))
        factory.connect("54.195.96.152", 2050)

class PolicyFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        client = PolicyClient()
        client.factory = self
        return client

    def startedConnecting(self, connector):
        self.connector = connector

                    
def main():
    packets.init(os.getcwd()+"\\packets.xml")
    handler = ClientHandler()
    factory = handler.createClient("b1@rotmgmuleverifier.appspotmail.com", "123456asd1")
    factory.listeners.append(TestListener(factory))
    factory.connect("54.195.96.152", 2050)
    reactor.run()

if __name__ == '__main__':
    main()
