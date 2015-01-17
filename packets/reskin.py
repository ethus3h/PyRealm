from packet import Packet

class ReskinPacket(Packet):
    
    def __init__(self, skinId=None):
        self.skinId = skinId
    
    def writeToOutput(self, stream):
        stream.writeInt(self.skinId)

    def parseFromInput(self,stream):
        self.skinId = stream.readInt()
