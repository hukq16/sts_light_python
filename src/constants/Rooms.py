from enum import Enum


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
    def __int__(self):
        return self.value


ROOMSTRINGS = ["SHOP", "REST", "EVENT", "ELITE", "MONSTER", "TREASURE", "BOSS", "BOSS_TREASURE", "NONE", "INVALID"]


def getRoomSymbol(room):
    if room == Room.NONE:
        return 'N'
    elif room == Room.EVENT:
        return '?'
    elif room == Room.MONSTER:
        return 'M'
    elif room == Room.ELITE:
        return 'E'
    elif room == Room.REST:
        return 'R'
    elif room == Room.SHOP:
        return '$'
    elif room == Room.TREASURE:
        return 'T'
    elif room == Room.BOSS:
        return 'B'
    else:
        return 'I'
