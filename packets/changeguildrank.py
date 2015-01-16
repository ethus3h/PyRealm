from packet import Packet

class ChangeguildrankPacket(Packet):
    
    def __init__(self, name=None, guildRank=None):
        self.name = name
        self.guildRank = guildRank
    
    def writeToOutput(self, stream):
        stream.writeUTF(self.name)
        stream.writeInt(self.guildRank)
