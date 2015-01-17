from packet import Packet
from data import location

class QuestfetchresponsePacket(Packet):
    
    def __init__(self, tier=None, goal=None, description=None, image=None):
        self.tier = tier
        self.goal = goal
        self.description = description
        self.image = image
    
    def parseFromInput(self, stream):
        self.tier = stream.readInt()
        self.goal = stream.readUTF()
        self.description = stream.readUTF()
        self.image = stream.readUTF()
