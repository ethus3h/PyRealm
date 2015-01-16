from packet import Packet

class OtherhitPacket(Packet):
    
    def __init__(self, time=None, bulletId=None, objectId=None, targetId=None):
        self.time = time
        self.bulletId = bulletId
        self.objectId = objectId
        self.targetId = targetId
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
        stream.writeByte(self.bulletId)
        stream.writeInt(self.objectId)
        stream.writeInt(self.targetId)
