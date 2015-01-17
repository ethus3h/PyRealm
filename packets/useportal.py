from packet import Packet

class UseportalPacket(Packet):
    
    def __init__(self, objectId=None):
        self.objectId = objectId
    
    def writeToOutput(self, stream):
        stream.writeInt(self.objectId)
