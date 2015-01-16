
class SlotObject():

    def __init__(objectId=None,objectType=None,slotId=None):
        self.objectId = objectId
        self.objectType = objectType
        self.slotId = slotId

    def writeToOutput(self,stream):
        stream.writeInt(self.objectId)
        stream.writeByte(self.slotId)
        stream.writeShort(self.objectType)
        

    
