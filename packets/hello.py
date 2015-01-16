from packet import Packet
import math
import random

class HelloPacket(Packet):
    
    def __init__(self):
        self.buildVersion = None
        self.gameId = None
        self.guid = None
        self.password = None
        self.secret = None
        self.keyTime = None
        self.key = None
        self.obf1 = None
        self.obf2 = None
        self.obf3 = None
        self.obf4 = None
        self.obf5 = None
        self.obf6 = None
    
    def writeToOutput(self, stream):
        stream.writeUTF(self.buildVersion)
        stream.writeInt(self.gameId)
        stream.writeUTF(self.guid)
        stream.writeInt(int(math.floor((random.randint(0,100)/100)*1000000000)))
        stream.writeUTF(self.password)
        stream.writeInt(int(math.floor((random.randint(0,100)/100)*1000000000)))
        stream.writeUTF(self.secret)
        stream.writeInt(self.keyTime)
        stream.writeShort(len(self.key))
        stream.write(self.key)
        
        stream.writeInt(len(self.obf1))
        stream.write(self.obf1)
        
        stream.writeUTF(self.obf2)
        stream.writeUTF(self.obf3)
        stream.writeUTF(self.obf4)
        stream.writeUTF(self.obf5)
        stream.writeUTF(self.obf6)

    def parseFromInput(self, stream):
        self.buildVersion = stream.readUTF()
        self.gameId = stream.readInt()
        self.guid = stream.readUTF()
        stream.readInt()
        self.password = stream.readUTF()
        stream.readInt()
        self.secret = stream.readUTF()
        self.keyTime = stream.readInt()
        self.key = stream.read(stream.readShort())
        self.obf1 = stream.read(stream.readInt())
        self.obf2 = stream.readUTF()
        self.obf3 = stream.readUTF()
        self.obf4 = stream.readUTF()
        self.obf5 = stream.readUTF()
        self.obf6 = stream.readUTF()
