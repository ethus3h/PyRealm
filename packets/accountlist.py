from packet import Packet

class AccountlistPacket(Packet):
    
    def __init__(self, accountListId=None, accountIds=None, lockAction=None):
        self.accountListId = accountListId
        if not accountIds:
            accountIds = []
        self.accountIds = accountIds
        self.lockAction = lockAction
    
    def parseFromInput(self, stream):
        self.accountListId = stream.readInt()
        for i in xrange(0,stream.readShort()):
            self.accountIds.append(stream.readUTF())
        self.lockAction = stream.readInt()
