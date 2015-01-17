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
