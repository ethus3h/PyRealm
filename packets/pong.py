from packet import Packet

class PongPacket(Packet):
    
    def __init__(self, serial=None, time=None):
        self.serial = serial
        self.time = time
    
    def writeToOutput(self, stream):
        stream.writeInt(self.serial)
        stream.writeInt(self.time)
