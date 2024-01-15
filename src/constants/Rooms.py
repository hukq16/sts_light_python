from enum import Enum

#
# Created by gamerpuppy on 6/24/2021.
#



class sts: #this class replaces the original namespace 'sts'

    class Room(Enum):
        SHOP = 0
        REST = 1
        EVENT = 2
        ELITE = 3
        MONSTER = 4
        TREASURE = 5
        BOSS = 6
        BOSS_TREASURE = 7
        NONE = 8
        INVALID = 9

    ROOMSTRINGS = ["SHOP", "REST", "EVENT", "ELITE", "MONSTER", "TREASURE", "BOSS", "BOSS_TREASURE", "NONE", "INVALID"]

    @staticmethod
    def getRoomSymbol(room):
        if room == sts.Room.NONE:
            return 'N'
        elif room == sts.Room.EVENT:
            return '?'
        elif room == sts.Room.MONSTER:
            return 'M'
        elif room == sts.Room.ELITE:
            return 'E'
        elif room == sts.Room.REST:
            return 'R'
        elif room == sts.Room.SHOP:
            return '$'
        elif room == sts.Room.TREASURE:
            return 'T'
        elif room == sts.Room.BOSS:
            return 'B'
        else:
            return 'I'




