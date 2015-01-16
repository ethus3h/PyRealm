from twisted.internet import reactor, protocol
import struct
from packets import *
from streams import ByteInput, ByteOutput
from rc4 import RC4
policy = """<?xml version="1.0"?><!DOCTYPE cross-domain-policy SYSTEM "/xml/dtds/cross-domain-policy.dtd">  <cross-domain-policy>  <site-control permitted-cross-domain-policies="master-only"/>  <allow-access-from domain="*" to-ports="*" /></cross-domain-policy>\n\x00""" 

class PyRealmProtocol(protocol.Protocol):

    packetLength = 0
    packetId = 0
    packetBytes = ""
    inputstream = ByteInput()
    outputstream = ByteOutput()
    
    def dataReceived(self, data):
        print("PYREALM PACKET\n\tid: {}".format(ord(data[4])))
        self.inputstream.append(data)
        self.packetLength = self.inputstream.readInt()-5
        self.packetId = self.inputstream.read()
        
        if not len(self.packetBytes) == self.packetLength:
            self.packetBytes += self.inputstream.read(min(self.inputstream.length(), self.packetLength-len(self.packetBytes)))
            print "Read {}/{} bytes".format(len(self.packetBytes), self.packetLength)

        if len(self.packetBytes) == self.packetLength:
            packet = create(ord(self.packetId))
            packetByteArray = [ord(x) for x in self.packetBytes]
            packetInputStream = ByteInput()
            self.from_client.cipher(packetByteArray)
            print packetByteArray
            packetInputStream.fromArray(packetByteArray)
            packet.parseFromInput(packetInputStream)
            self.packetLength = 0
            self.packetId = 0
            self.packetBytes = ""
            self.handlePacket(packet)
            print "--------"*3
            
    def connectionMade(self):
        print("PYREALM CONNECTION")

    def handlePacket(self, packet):
        print("NEW PACKET: " + packet.__class__.__name__)
        print "buildVersion: " + packet.buildVersion
        print "gameId: " + str(packet.gameId)
        print packet.guid
        print packet.randomInt
        print packet.password
        print packet.secret
        print packet.keyTime
        print packet.key
        print "obf1: " + repr(packet.obf1)
        print "obf2: " + repr(packet.obf2)
        print packet.obf3
        print packet.obf4
        print packet.obf5
        print packet.obf6
        

class PyRealmFactory(protocol.ServerFactory):
    protocol = PyRealmProtocol
    from_client_key = [ord(x) for x in "311f80691451c71d09a13a2a6e".decode("hex")]
    to_client_key = [ord(x) for x in "72c5583cafb6818995cdd74b80".decode("hex")]
    
    def buildProtocol(self, addr):
        p = PyRealmProtocol()
        p.from_client = RC4(self.from_client_key)
        p.to_client = RC4(self.to_client_key)
        return p
        

class PolicyFileProtocol(protocol.Protocol):

    def dataReceived(self,data):
        print("POLICYFILE: " + repr(data))
        if data == "<policy-file-request/>\x00":
            self.transport.write(policy)

            
def main():
    init("packets.xml")
    factory = PyRealmFactory()
    factory2 = protocol.ServerFactory()
    factory2.protocol = PolicyFileProtocol
    reactor.listenTCP(843,factory2)
    reactor.listenTCP(2050,factory)
    print "Running server..."
    reactor.run()


if __name__ == '__main__':
    main()
