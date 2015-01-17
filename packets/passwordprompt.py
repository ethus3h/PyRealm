from packet import Packet

class PasswordpromptPacket(Packet):
    
    def __init__(self, cleanPasswordStatus=None):
        self.cleanPasswordStatus = cleanPasswordStatus

    def parseFromInput(self,stream):
        self.cleanPasswordStatus = stream.readInt()
