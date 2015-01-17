from packet import Packet

class AllyshootPacket(Packet):
    
    def __init__(self, bulletId=None, ownerId=None, containerType=None, angle=None):
        self.bulletId = bulletId
        self.ownerId = ownerId
        self.containerType = containerType
        self.angle = angle
    
    def parseFromInput(self, stream):
        self.bulletId = stream.readUnsignedByte()
        self.ownerId = stream.readInt()
        self.containerType = stream.readShort()
        self.angle = stream.readFloat()
