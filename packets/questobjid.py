from packet import Packet

class QuestobjidPacket(Packet):
    
    def __init__(self, objectId=None):
        self.objectId = objectId
    
    def parseFromInput(self, stream):
        self.objectId = stream.readInt()
