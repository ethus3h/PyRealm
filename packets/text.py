from packet import Packet

class TextPacket(Packet):
    
    def __init__(self, name=None,objectId=None,numStars=None,bubbleTime=None,text=None,cleanText=None):
        self.name = name
        self.objectId = objectId
        self.numStars = numStars
        self.bubbleTime = bubbleTime
        self.text = text
        self.cleanText = cleanText
    
    def parseFromInput(self, stream):
        self.name = stream.readUTF()
        self.objectId = stream.readInt()
        self.numStars = stream.readInt()
        self.bubbleTime = stream.readUnsignedByte()
        self.recipient = stream.readUTF()
        self.text = stream.readUTF()
        self.cleanText = stream.readUTF()
