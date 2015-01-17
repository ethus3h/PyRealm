from packet import Packet
from data import item

class TradestartPacket(Packet):
    
    def __init__(self, myItems=None, yourItems=None, yourName=None):
        if not myItems:
            myItems = []
        if not yourItems:
            yourItems = []

        self.myItems = myItems
        self.yourItems = yourItems
        self.yourName = yourName
    
    def writeToOutput(self, stream):
        for i in xrange(0,stream.readShort()):
            self.myItems.append(item.Item().parseFromInput(stream))

        self.yourName = stream.readUTF()

        for i in xrange(0,stream.readShort()):
            self.yourItems.append(item.Item().parseFromInput(stream))
