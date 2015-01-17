from packet import Packet

class InvitedtoguildPacket(Packet):
    
    def __init__(self, name=None, guildName=None):
        self.name = name
        self.guildName = guildName
    
    def writeToOutput(self, stream):
        self.name = stream.readUTF()
        self.guildName = stream.readUTF()
