from packet import Packet

class PlayershootPacket(Packet):
    
    def __init__(self, time=None, bulletId=None, containerType=None, startingPos=None, angle=None):
        self.time = time
        self.bulletId = bulletId
        self.containerType = containerType
        self.startingPos = startingPos
        self.angle = angle
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
        stream.writeByte(self.bulletId)
        stream.writeShort(self.containerType)
        self.startingPos.writeToOutput(stream)
        stream.writeFloat(self.angle)
