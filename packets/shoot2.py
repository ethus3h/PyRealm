from packet import Packet
from data import location

class Shoot2Packet(Packet):
    
    def __init__(self, bulletId=None, ownerId=None, containerType=None, startingPos=None, angle=None, damage=None):
        self.bulletId = bulletId
        self.ownerId = ownerId
        self.containerType = containerType
        if not startingPos:
            startingPos = location.Location()
        self.startingPos = startingPos
        self.angle = angle
        self.damage = damage
    
    def parseFromInput(self, stream):
        self.bulletId = stream.readUnsignedByte()
        self.ownerId = stream.readInt()
        self.containerType = stream.readUnsignedByte()
        self.startingPos.parseFromInput(stream)
        self.angle = stream.readFloat()
        self.damage = stream.readShort()
