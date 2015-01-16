packet = '~\xe1\xd0c\xa5\xc3\x15%}\xbc\xb9\xa8\x10\x9e{@\xf4\x193\x0b\xf3\xed.b]\x1c\x1b\xfb\xd8.\x12\x8c\xf6/\x8a\xc6P\xc0|#\xb0y\xa0is\xe1\xdd\x9f\xccm@\xac\xa1\x95\xd5o\xcc\xadn\xc1\x116\xa7\x08\xcc/\xe5#\xfaS\xbd\x04\x0e&\x9dRVP\x02\xee\\\xb5\xcb-)\x97\xca\xc8\x16HE`\xce\xacVP\xa0D\x00\x97z\xe0\xcb\xe9\xa2\x87\xdfM\xef=\xd7\x96"\x9cI\x94\x10_\x13\xc3\x94KD1\xb6\xfeV\xad\xcd\xf3_\xe9\xf1\xa3\xc0\xc8\'\x93\xe3p\r4H`\x9c\xa1\x1fK\xe7\'\xee4e1\xac\xcbw6\x9a\xa9\xcf\xc5E1\xa9\x05\xf8\\\xcf;7\x9a\x0ek@\xd64y\x8a\xcd\x05\x84P\x88#\x94\x13\xf5\xa3S\xbf\xf2Y\xfc\x8b\xd9\x1f\xaa\x82 \xc9\x97\x98\x01t\xd0\xa7\xc3f\x80\x9fo4b\xe8\xeb\xc4\xc3U\xdd\xa3\xf5\x04\xca\xedG\x146\xe6\x94K;\xea\xd4\\\xd3\xdf\x08Bz%h\xc5\xc8\xc9;\xa3|\x83`\x0b\x9d\x90\xaf\t\x91\r\xac\'\x1bA\xa6\xf8\xe7\xc3\'\x97PV\x93\x05\x96\xff\x97\xf7LE\x15\xcf^\x88A\x18G\x13\xe4\xe8\x19\x87\x960\x04\xaa\xb6\xefO\xf8@F:[\x13\xcc\x11\x12\x16s.X\xc3c%\xc0\x12\xbd\xaf\t\xa2O\xbcZ\x88\t\xf1\xc8\xa1<\xf64T\x1e\r\xecZ\x96\xd0\xadP\xac\xa2\x83\x98\xe4\xbf\x96\xb3\xf7Z\xd1~\xa7#\rc\x95\xe7m\x1cSl\xc2gBMt\xd9\x17\xe95}c\x86S\xd7\xabx\x9aT\x1a\x84\xcd\x0ei}\x87iL\x16J\x87*\xbba@\x82\t'

from bytestream import ByteStream
import re
import subprocess
import random
import time
import binascii
import constants
from base64 import b64encode

def getRandomFloat():
    return random.randint(0,100)/100

def RSA_encrypt(string):
    key = RSA(constants.RSA_KEY_EXPONENT, constants.RSA_KEY_MODULUS)
    a = ByteStream()
    b = ByteStream()
    a.write(string)
    key.encrypt(a,b)
    return b64encode(b.asString())

class Random():
    def __init__(self,):
        self.psize = 256
        self.pool = ByteStream()
        self.pptr = 0
        self.seeded = False
        while self.pptr < self.psize:
            t = 65536*getRandomFloat()
            self.pool[self.pptr] = t >> 8
            self.pptr += 1
            self.pool[self.pptr] = t&255
            self.pptr += 1
        self.pptr = 0
        self.seed()
        self.state = ARC4(self.pool.data)

    def seed(self):
        x = int(round(time.time()*1000))
        self.pool[self.pptr] ^= x & 255
        self.pptr += 1
        self.pool[self.pptr] ^= (x>>8)&255
        self.pptr += 1
        self.pool[self.pptr] ^= (x>>16)&255
        self.pptr += 1
        self.pool[self.pptr] ^= (x>>24)&255
        self.pptr += 1
        self.pptr = self.pptr % self.psize
        self.seeded = True
    
    def nextByte(self):
        return self.state.next_()
        

# Python implementation of the AS3Crypto library tailored for PyRealm
class RSA(): 
    def __init__(self,e,n):
        self.e = e
        self.n = n

    def getBlockSize(self):
        return (long.bit_length(self.n)+7)/8

    def encrypt(self, src, dst):
        bl = self.getBlockSize()
        end = src.available()
        position = 0
        while position<end:
            padding,position = self.rawpad(src,bl,position)
            block = binascii.hexlify(padding.asString())
            if len(block) < 256:
                block += "0"*(256-len(block))
            block = long(block,16)
            chunk = pow(block, self.e, self.n)
            chunkhex = "%x" % chunk
            if len(chunkhex) < 256:
                chunkhex = "0"*(256-len(chunkhex)) + chunkhex
            array = [ord(x) for x in binascii.unhexlify(chunkhex)]
            dst.write(array)
        return dst
            
    def rawpad(self,src,n,p):
        return (src,src.available())

    def pad(self,src,n,p):
        out = ByteStream()
        end = min(src.available(),p+n-11)
        p = end
        i = end-1
        while i>=p and n>11:
            n -= 1
            out[n] = src[i-1]
            position += 1
            i -= 1
            
        n -= 1
        out[n] = 0
        rng = Random()
        x = 0
        while n>2:
            x = rng.nextByte()
            while x == 0:
                x = rng.nextByte()
            n -= 1
            out[n] = x

        n -= 1
        out[n] = 0x02
        out[n] = 0
        return (out,p)

    def doPublic(x):
        pass

def hexToArray(string):
    stream = ByteStream()
    i = 0
    for i in xrange(0,len(string),2):
        stream.writeByte(int(string[i:i+2],16))
    return stream.data

def stringToArray(string):
    stream = ByteStream()
    stream.write(string)
    return stream.data

def getCipher(array):
    if isinstance(array, str):
        array = hexToArray(array)
    return ARC4(array)
    
class ARC4():
    def __init__(self, key):
        self.S = []
        for i in xrange(0,256):
            self.S.append(i)
        j = 0
        for i in xrange(0,256):
            j = (j + self.S[i] + key[i%len(key)]) & 255
            t = self.S[i]
            self.S[i] = self.S[j]
            self.S[j] = t
        self.i = 0
        self.j = 0

    def next_(self):
        self.i = (self.i+1)&255
        self.j = (self.j+self.S[self.i])&255
        t = self.S[self.i]
        self.S[self.i] = self.S[self.j]
        self.S[self.j] = t
        return self.S[(t+self.S[self.i])&255]
    
    def encrypt(self, block):
        if isinstance(block,str):
            block = stringToArray(block)
        if isinstance(block,ByteStream):
            block = block.data
        i = 0
        while i<len(block):
            block[i] = block[i] ^ self.next_()
            i += 1
        return block

    def decrypt(self, block):
        return self.encrypt(block)
            
