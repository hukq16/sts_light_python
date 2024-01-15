from enum import Enum

#
# Created by gamerpuppy on 7/9/2021.
#



class sts: #this class replaces the original namespace 'sts'

    class Key(Enum):
        EMERALD_KEY = 0
        RUBY_KEY = 1
        SAPPHIRE_KEY = 2
        INVALID = 3

    class ChestSize(Enum):
        SMALL = 0
        MEDIUM = 1
        LARGE = 2
        INVALID = 3

    class HpType(Enum):
        CEIL = 0
        FLOOR = 1
        ROUND = 2

    SMALL_CHEST_CHANCE = 50
    MEDIUM_CHEST_CHANCE = 33
    LARGE_CHEST_CHANCE = 17

    CHESTRELICTIERCHANCES = [[75, 25], [35, 50], [0, 75]]

    CHESTGOLDCHANCES = [50, 35, 50]
    CHESTGOLDAMOUNTS = [25, 50, 75]

    CHESTSIZEENUMNAMES = ["SMALL", "MEDIUM", "LARGE", "INVALID"]
    CHESTSIZENAMES = ["Small", "Medium", "Large", "INVALID"]


