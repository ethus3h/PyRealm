from packet import Packet

class NotificationPacket(Packet):
    
    def __init__(self, objectId=None, message=None, color=None):
        self.objectId = objectId
        self.message = message
        self.color = color
    
    def parseFromInput(self, stream):
        self.objectId = stream.readInt()
        self.message = stream.readUTF()
        self.color = stream.readInt()
