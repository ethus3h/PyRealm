
class JoinguildPacket():
    def __init__(self,guildName=None):
        self.guildName = guildName

    def writeToOutput(self,stream):
        stream.writeUTF(self.guildName)
