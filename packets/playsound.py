from packet import Packet

class PlaysoundPacket(Packet):
    
    def __init__(self, ownerId=None, soundId=None):
        self.ownerId = ownerId
        self.soundId = soundId

    def parseFromInput(self, stream):
        self.ownerId = stream.readInt()
        self.soundId = stream.readUnsignedByte()
