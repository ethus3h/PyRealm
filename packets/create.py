from packet import Packet

class CreatePacket(Packet):
    
    def __init__(self, classType=None, skinType=None):
        self.classType = classType
        self.skinType = skinType
    
    def writeToOutput(self, stream):
        stream.writeShort(self.classType)
        stream.writeShort(self.skinType)
