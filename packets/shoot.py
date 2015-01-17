from packet import Packet
from data import location

class ShootPacket(Packet):
    
    def __init__(self, bulletId=None, ownerId=None, bulletType=None, startingPos=None, angle=None, damage=None, numShots=None, angleInc=None):
        self.bulletId = bulletId
        self.ownerId = ownerId
        self.bulletType = bulletType
        if not startingPos:
            startingPos = location.Location()
        self.startingPos = startingPos
        self.angle = angle
        self.damage = damage
        self.numShots = numShots
        self.angleInc = angleInc
    
    def parseFromInput(self, stream):
        self.bulletId = stream.readUnsignedByte()
        self.ownerId = stream.readInt()
        self.bulletType = stream.readUnsignedByte()
        self.startingPos.parseFromInput(stream)
        self.angle = stream.readFloat()
        self.damage = stream.readShort()

        if stream.available() > 0:
            self.numShots = stream.readUnsignedByte()
            self.angleInc = stream.readFloat()
        else:
            self.numShots = 1
            self.angleInc = 0
