from packet import Packet

class PlayerhitPacket(Packet):
    
    def __init__(self, bulletId=None, objectId=None):
        self.bulletId = bulletId
        self.objectId = objectId
    
    def writeToOutput(self, stream):
        stream.writeByte(self.bulletId)
        stream.writeInt(self.objectId)
