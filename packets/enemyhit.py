from packet import Packet

class EnemyhitPacket(Packet):
    
    def __init__(self, time=None, bulletId=None, targetId=None, kill=None):
        self.time = time
        self.bulletId = bulletId
        self.targetId = targetId
        self.kill = kill
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
        stream.writeByte(self.bulletId)
        stream.writeInt(self.targetId)
        stream.writeBoolean(self.kill)
