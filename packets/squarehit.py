from packet import Packet

class SquarehitPacket(Packet):
    
    def __init__(self, time=None, bulletId=None, objectId=None):
        self.time = time
        self.bulletId = bulletId
        self.objectId = objectId
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
        stream.writeByte(self.bulletId)
        stream.writeInt(self.objectId)
