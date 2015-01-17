
class Item():

    def __init__(item=None,slotType=None,tradeable=None,included=None):
        self.item = item
        self.slotType = slotType
        self.tradeable = tradeable
        self.included = included

    def parseFromInput(self,stream):
        self.item = stream.readInt()
        self.slotType = stream.readInt()
        self.tradeable = stream.readBoolean()
        self.included = stream.readBoolean()
        

    
