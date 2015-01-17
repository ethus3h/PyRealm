from packet import Packet
from data import status

class NewtickPacket(Packet):
    
    def __init__(self, tickId=None, tickTime=None, statuses=None):
        self.tickId = tickId
        self.tickTime = tickTime
        if not statuses:
            statuses = []
        self.statuses = statuses
    
    def parseFromInput(self, stream):
        self.tickId = stream.readInt()
        self.tickTime = stream.readInt()

        for i in xrange(0,stream.readShort()):
            self.statuses.append(status.Status().parseFromInput(stream))
        
