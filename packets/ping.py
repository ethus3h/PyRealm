from packet import Packet

class PingPacket(Packet):
    
    def __init__(self, serial=None):
        self.serial = serial

    def parseFromInput(self, stream):
        self.serial = stream.readInt()
