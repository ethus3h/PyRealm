from packet import Packet

class GotoackPacket(Packet):
    
    def __init__(self, time=None):
        self.time = time
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
