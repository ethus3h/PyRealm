from packet import Packet

class MapinfoPacket(Packet):
    
    def __init__(self):
        self.name = None
        self.width = None
        self.height = None
        self.fp = None
        self.background = None
        self.allowPlayerTeleport = None
        self.showDisplays = None
        self.clientXML = None
        self.extraXML = None
        self.obf1 = None
        self.obf2 = None
    
    def writeToOutput(self, stream):
        pass

    def parseFromInput(self, stream):
        self.width = stream.readInt()
        self.heihgt = stream.readInt()
        self.name = stream.readUTF()
        self.obf1 = stream.readUTF()
        self.fp = stream.readUnsignedInt()
        self.background = stream.readInt()
        self.obf2 = stream.readInt()
        self.allowPlayerTeleport = stream.readBoolean()
        self.showDisplays = stream.readBoolean()
