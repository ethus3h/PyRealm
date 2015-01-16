import packet

class HelloPacket(Packet):
    bytez = None
    
    buildVersion = None
    gameId = None
    guid = None
    randomInt = None
    password = None
    secret = None
    keyTime = None
    key = None
    obf1 = None
    obf2 = None
    obf3 = None
    obf4 = None
    obf5 = None
    obf6 = None
    
    def writeToOutput(self, outputstream):
        bytez = outputstream.data
        outputstream.writeUTF(self.buildVersion)
        outputstream.writeInt(self.gameId)
        outputstream.writeUTF(self.guid)
        outputstream.writeInt(self.randomInt)
        outputstream.writeUTF(self.password)
        outputstream.writeUTF(self.secret)
        
        outputstream.writeInt(self.keyTime)
        outputstream.writeShort(len(self.key))
        outputstream.write(self.key)
        
        outputstream.writeInt(len(self.obf1))
        outputstream.write(self.obf1)
        
        outputstream.writeUTF(self.obf2)
        outputstream.writeUTF(self.obf3)
        outputstream.writeUTF(self.obf4)
        outputstream.writeUTF(self.obf5)
        outputstream.writeUTF(self.obf6)

    def parseFromInput(self, inputstream):
        self.buildVersion = inputstream.readUTF()
        self.gameId = inputstream.readInt()
        self.guid = inputstream.readUTF()
        self.randomInt = inputstream.readInt()
        self.password = inputstream.readUTF()
        self.secret = inputstream.readUTF()
        self.keyTime = inputstream.readInt()
        self.key = inputstream.read(inputstream.readShort(), True)
        self.obf1 = inputstream.read(inputstream.readInt())
        self.obf2 = inputstream.readUTF()
        self.obf3 = inputstream.readUTF()
        self.obf4 = inputstream.readUTF()
        self.obf5 = inputstream.readUTF()
        self.obf6 = inputstream.readUTF()
