from packet import Packet

class ShootackPacket(Packet):
    
    def __init__(self, time=None):
        self.time = time
    
    def writeToOutput(self, stream):
        stream.writeInt(self.time)
