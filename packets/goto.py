from packet import Packet
from data import location

class GotoPacket(Packet):
    
    def __init__(self, objectId=None, loc=None):
        self.objectId = objectId
        if not loc:
            loc = location.Location()
        self.loc = loc
        
    
    def parseFromInput(self, stream):
        self.objectId = stream.readInt()
        self.loc.parseFromInput(stream)
