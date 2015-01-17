
class DeathPacket():
    def __init__(self, accountId=None, charId=None, killedBy=None, obf1=None, obf2=None, obf3=None):
        self.accountId = accountId
        self.charId = charId
        self.killedBy = killedBy
        self.obf1 = obf1
        self.obf2 = obf2
        self.obf3 = obf3

    def parseFromInput(self,stream):
        self.accountId = stream.readUTF()
        self.charId = stream.readInt()
        self.obf1 = stream.readInt()
        self.obf2 = stream.readInt()
        self.obf3 = self.obf2 != 1
