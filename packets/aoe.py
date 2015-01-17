from packet import Packet
from data import location

class AoePacket(Packet):
    
    def __init__(self, pos=None, radius=None, damage=None, effect=None, duration=None, origType=None):
        if not pos:
            pos = location.Location()
        self.pos = pos
        self.radius = radius
        self.damage = damage
        self.effect = effect
        self.duration = duration
        self.origType = origType

    def parseFromInput(self, stream):
        self.pos.parseFromInput(stream)
        self.radius = stream.readFloat()
        self.damage = stream.readUnsignedShort()
        self.effect = stream.readUnsignedByte()
        self.duration = stream.readFloat()
        self.origType = stream.readUnsignedShort()
