from packet import Packet

class TeleportPacket(Packet):
    
    def __init__(self, objectId=None):
        self.objectId = objectId
    
    def writeToOutput(self, stream):
        stream.writeInt(self.objectId)
