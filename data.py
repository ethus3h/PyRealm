class StatData():
    MAX_HEALTH,
    HEALTH,SIZE,
    MAX_MANA,
    MANA,
    EXPERIENCE_GOAL,
    EXPERIENCE,
    CURRENT_LEVEL,
    SLOT_1,
    SLOT_2,
    SLOT_3,
    SLOT_4,
    SLOT_5,
    SLOT_6,
    SLOT_7,
    SLOT_8,
    SLOT_9,
    SLOT_10,
    SLOT_11,
    SLOT_12,
    TOTAL_ATTACK,
    TOTAL_DEFENCE,
    TOTAL_SPEED,
    UNKNOWN_23,
    UNKNOWN_24,
    UNKNOWN_25,
    TOTAL_VITALITY,
    TOTAL_WISDOM,
    TOTAL_DEXTERITY,
    UNKNOWN_29,
    UNKNOWN_30,
    NAME,
    UNKNOWN_32,
    UNKNOWN_33,
    UNKNOWN_34,
    REALM_GOLD,
    UNKNOWN_36,
    UNKNOWN_37,
    UNKNOWN_38,
    TOTAL_FAME,
    UNKNOWN_40,
    UNKNOWN_41,
    UNKNOWN_42,
    UNKNOWN_43,
    UNKNOWN_44,
    UNKNOWN_45,
    BONUS_HEALTH,
    BONUS_MANA,
    BONUS_ATTACK,
    BONUS_DEFENCE,
    UNKNOWN_50,
    UNKNOWN_51,
    BONUS_WISDOM,
    BONUS_DEXTERITY,
    UNKNOWN_54,
    UNKNOWN_55,
    UNKNOWN_56,
    FAME,
    FAME_GOAL,
    UNKNOWN_59,
    UNKNOWN_60,
    UNKNOWN_61,
    GUILD,
    GUILD_RANK,
    UNKNOWN_64,
    PET_SKIN = range[67]

    def __init__(i = 0):
        self.i = i
        self.intValue = None
        self.stringValue = None
    
    def isUTFData(self, i):
        if i == 31 or i == 62 or i == 82 or i == 38 or i == 54:
            return True
        return False

    def parseFromInput(self, inputstream):
        i = inputstream.readByte()
        if isUTFData():
            self.stringValue = inputstream.readUTF()
        else:
            self.intValue = inputstream.readInt()

    def writeToOutput(self, outputstream):
        outputstream.writeByte(self.i)
        if isUTFData():
            
        

class Vector3f():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        if isinstance(other, self.__class__):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
            
    def __dec__(self, other):
        if isinstance(other, self.__class__):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'").format(self.__class__, type(other))
