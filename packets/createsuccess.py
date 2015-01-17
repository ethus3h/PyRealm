from packet import Packet

class CreatesuccessPacket(Packet):
    
    def __init__(self, objectId=None, charId=None):
        self.objectId = objectId
        self.charId = charId

    def parseFromInput(self, stream):
        self.objectId = stream.readInt()
        self.charId = stream.readInt()
