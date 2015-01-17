from packet import Packet

class DamagePacket(Packet):
    
    def __init__(self, targetId=None,effects=None,damageAmount=None,kill=None,bulletId=None,objectId=None):
        self.targetId = targetId
        if not effects:
            effects = []
        self.effects = effects
        self.damageAmount = damageAmount
        self.kill = kill
        self.bulletId = bulletId
        self.objectId = objectId
    
    def parseFromInput(self, stream):
        self.targetId = stream.readInt()
        for i in xrange(0,stream.readUnsignedByte()):
            self.effects.append(stream.readUnsignedByte())

        self.damageAmount = stream.readUnsignedShort()
        self.kill = stream.readBoolean()
        self.bulletId = stream.readUnsignedByte()
        self.objectId = stream.readInt()
