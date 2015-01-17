
class StatData():
    MAX_HEALTH = 0
    HEALTH = 1
    SIZE = 2
    MAX_MANA = 3
    MANA = 4
    EXPERIENCE_GOAL = 5
    EXPERIENCE = 6
    CURRENT_LEVEL = 7
    SLOT_1 = 8
    SLOT_2 = 9
    SLOT_3 = 10
    SLOT_4 = 11
    SLOT_5 = 12
    SLOT_6 = 13
    SLOT_7 = 14
    SLOT_8 = 15
    SLOT_9 = 16
    SLOT_10 = 17
    SLOT_11 = 18
    SLOT_12 = 19
    TOTAL_ATTACK = 20
    TOTAL_DEFENCE = 21
    TOTAL_SPEED = 22
    UNKNOWN_23 = 23
    UNKNOWN_24 = 24
    UNKNOWN_25 = 25
    TOTAL_VITALITY = 26
    TOTAL_WISDOM = 27
    TOTAL_DEXTERITY = 28
    UNKNOWN_29 = 29
    STARS = 30
    NAME = 31
    MAIN_DYE = 32
    ACCESSORY_DYE = 33
    UNKNOWN_34 = 34
    GOLD = 35
    UNKNOWN_36 = 36
    UNKNOWN_37 = 37
    UNKNOWN_38 = 38
    TOTAL_FAME = 39
    UNKNOWN_40 = 40
    UNKNOWN_41 = 41
    UNKNOWN_42 = 42
    UNKNOWN_43 = 43
    UNKNOWN_44 = 44
    UNKNOWN_45 = 45
    BONUS_HEALTH = 46
    BONUS_MANA = 47
    BONUS_ATTACK = 48
    BONUS_DEFENCE = 49
    BONUS_SPD = 50
    BONUS_VIT = 51
    BONUS_WISDOM = 52
    BONUS_DEXTERITY = 53
    UNKNOWN_54 = 54
    UNKNOWN_55 = 55
    UNKNOWN_56 = 56
    FAME = 57
    FAME_GOAL = 58
    GLOW = 59
    UNKNOWN_60 = 60
    UNKNOWN_61 = 61
    GUILD = 62
    GUILD_RANK = 63
    UNKNOWN_64 = 64
    PET_SKIN = 65
    BACKPACK_1 = 71
    BACKPACK_2 = 72
    BACKPACK_3 = 73
    BACKPACK_4 = 74
    BACKPACK_5 = 75
    BACKPACK_6 = 76
    BACKPACK_7 = 77
    BACKPACK_8 = 78
    BACKPACK = 79
    SKIN = 80
    PET_ID = 81
    PET_SKIN = 82
    PET_TYPE = 83
    PET_RARITY = 84
    PET_MAX_LEVEL = 85
    PET_UNK1 = 86
    PET_SKILL1_FOOD = 87
    PET_SKILL2_FOOD = 88
    PET_SKILL3_FOOD = 89
    PET_SKILL1_LEVEL = 90
    PET_SKILL2_LEVEL = 91
    PET_SKILL3_LEVEL = 92
    PET_SKILL1_TYPE = 93
    PET_SKILL2_TYPE = 94
    PET_SKILL3_TYPE = 95

    def __init__(i = 0):
        self.i = i
        self.intValue = None
        self.stringValue = None
    
    def isUTFData(self, i):
        if i == 31 or i == 62 or i == 82 or i == 38 or i == 54:
            return True
        return False

    def parseFromInput(self, stream):
        i = stream.readByte()
        if isUTFData():
            self.stringValue = stream.readUTF()
        else:
            self.intValue = stream.readInt()

    def writeToOutput(self, stream):
        stream.writeByte(self.i)
        if isUTFData():
            stream.writeUTF(self.stringValue)
        else:
            stream.writeInt(self.intValue)
