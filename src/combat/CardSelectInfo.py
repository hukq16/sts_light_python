from enum import Enum

#
# Created by gamerpuppy on 8/24/2021.
#




class sts: #this class replaces the original namespace 'sts'

    class CardSelectTask(Enum):
        INVALID = 0
        ARMAMENTS = 1
        CODEX = 2
        DISCOVERY = 3
        DUAL_WIELD = 4
        EXHAUST_ONE = 5
        EXHAUST_MANY = 6
        EXHUME = 7
        FORETHOUGHT = 8
        GAMBLE = 9
        HEADBUTT = 10
        HOLOGRAM = 11
        LIQUID_MEMORIES_POTION = 12
        MEDITATE = 13
        NIGHTMARE = 14
        RECYCLE = 15
        SECRET_TECHNIQUE = 16
        SECRET_WEAPON = 17
        SEEK = 18
        SETUP = 19
        WARCRY = 20

    CARDSELECTTASKSTRINGS = ["INVALID", "ARMAMENTS", "CODEX", "DISCOVERY", "DUAL_WIELD", "EXHAUST_ONE", "EXHAUST_MANY", "EXHUME", "FORETHOUGHT", "GAMBLE", "HEADBUTT", "HOLOGRAM", "LIQUID_MEMORIES_POTION", "MEDITATE", "NIGHTMARE", "RECYCLE", "SECRET_TECHNIQUE", "SECRET_WEAPON", "SEEK", "SETUP", "WARCRY"]

    class CardSelectInfo:

        def __init__(self):
            # instance fields found by C++ to Python Converter:
            self.cards = [None for _ in range(3)]
            self.canPickZero = False
            self.canPickAnyNumber = False
            self.pickCount = 0
            self.data0 = 0
            self.cardSelectTask = 0



        def discovery_Cards(self):
            return list(self.cards)
        def discovery_CopyCount(self):
            return self.data0
        def dualWield_CopyCount(self):
            return self.data0
        def codexCards(self):
            return list(self.cards)


