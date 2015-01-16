import struct

str_to_array = lambda x: [ord(y) for y in x]
def array_to_str(arr, uni=False):
    if uni:
        return "".join([unichr(y) for y in arr])
    return "".join([chr(y) for y in arr])


class ByteStream():
    def __init__(self, src=None):
        if not src:
            src = []
        self.data = src

    def writeBoolean(self, var):
        if not isinstance(var, bool):
            raise Exception("Invalid var for writeBoolean, %s".format(type(var)))
            return
        self.write(struct.pack("?", var))
     
    def writeInt(self, var):
        if not isinstance(var, int):
            raise Exception("Invalid var for writeInt, %s".format(type(var)))
            return
        self.write(struct.pack(">i", var))

    def writeUnsignedInt(self, var):
        if not isinstance(var, int):
            raise Exception("Invalid var for writeUnsignedInt, %s".format(type(var)))
            return
        self.write(struct.pack(">I", var))

    def writeFloat(self, var):
        if not isinstance(var, float):
            raise Exception("Invalid var for writeFloat, %s".format(type(var)))
            return
        self.write(struct.pack(">f", var))

    def writeShort(self, var):
        if not isinstance(var, int):
            raise Exception("Invalid var for writeShort, %s".format(type(var)))
            return
        self.write(struct.pack(">h", var))

    def writeUnsignedShort(self, var):
        if not isinstance(var, int):
            raise Exception("Invalid var for writeUnsignedShort, %s".format(type(var)))
            return
        self.write(struct.pack(">H", var))

    def writeByte(self, var):
        if isinstance(var,str):
            var = ord(var)
        elif isinstance(var,unicode):
            var = ord(var)
        self.data.append(var)
            
    def write(self, bytez=[]):
        for i in range(0,len(bytez)):
            self.writeByte(bytez[i])

    def writeUTF(self, var):
        self.writeUnsignedShort(len(var))
        self.write(var)

    def read(self, length):
        var = self.data[0:length]
        self.data = self.data[length:]
        return var

    def readString(self, length):
        var = array_to_str(self.data[0:length])
        self.data = self.data[length:]
        return var

    def readBoolean(self):
        var = struct.unpack(">?", self.readString(1))[0]
        return var
     
    def readInt(self):
        var = struct.unpack(">i", self.readString(4))[0]
        return var

    def readUnsignedInt(self):
        var = struct.unpack(">I", self.readString(4))[0]
        return var

    def readFloat(self):
        var = struct.unpack(">f", self.readString(4))[0]
        return var

    def readShort(self):
        var = struct.unpack(">h", self.readString(2))[0]
        return var

    def readUnsignedShort(self):
        var = struct.unpack(">H", self.readString(2))[0]
        return var

    def readByte(self):
        var = struct.unpack(">b", self.readString(1))[0]
        return var

    def readUnsignedByte(self):
        var = struct.unpack(">B", self.readString(1))[0]
        return var
            
    def read(self, length=1):
        var = self.data[:length]
        self.data = self.data[length:]
        return var

    def readUTF(self):
        length = self.readUnsignedShort()
        text = self.readString(length)
        return text

    def readUTFBytes(self, length):
        text = self.readString(length)
        return text
            
    def append(self, bytez):
        self.data += bytez
            
    def available(self):
        return len(self.data)
        
    def empty(self):
        self.data = []

    def asString(self, uni=False):
        return array_to_str(self.data, uni)

    def __getitem__(self,index):
        return self.data[index]

    def __setitem__(self,index,val):
        if index>=self.available():
            self.data += [0]*(index-self.available()+1)
        self.data[index] = val
