from packet import Packet

class EditaccountlistPacket(Packet):
    
    def __init__(self, accountListId=None, add=None, objectId=None):
        self.accountListId = accountListId
        self.add = add
        self.objectId = objectId
    
    def writeToOutput(self, stream):
        stream.writeInt(self.name)
        stream.writeBoolean(self.add)
        stream.writeInt(self.objectId)
