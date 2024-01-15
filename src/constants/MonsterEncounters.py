from enum import Enum

#
# Created by gamerpuppy on 6/24/2021.
#



class sts: #this class replaces the original namespace 'sts'

    class MonsterEncounter(Enum):
        INVALID = 0
        # Act 1 Weak
        CULTIST = 1
        JAW_WORM = 2
        TWO_LOUSE = 3
        SMALL_SLIMES = 4
        BLUE_SLAVER = 5
        GREMLIN_GANG = 6
        LOOTER = 7
        LARGE_SLIME = 8
        LOTS_OF_SLIMES = 9
        EXORDIUM_THUGS = 10
        EXORDIUM_WILDLIFE = 11
        RED_SLAVER = 12
        THREE_LOUSE = 13
        TWO_FUNGI_BEASTS = 14
        GREMLIN_NOB = 15
        LAGAVULIN = 16
        THREE_SENTRIES = 17
        SLIME_BOSS = 18
        THE_GUARDIAN = 19
        HEXAGHOST = 20

        # Act 2
        SPHERIC_GUARDIAN = 21
        CHOSEN = 22
        SHELL_PARASITE = 23
        THREE_BYRDS = 24
        TWO_THIEVES = 25
        CHOSEN_AND_BYRDS = 26
        SENTRY_AND_SPHERE = 27
        SNAKE_PLANT = 28
        SNECKO = 29
        CENTURION_AND_HEALER = 30
        CULTIST_AND_CHOSEN = 31
        THREE_CULTIST = 32
        SHELLED_PARASITE_AND_FUNGI = 33
        GREMLIN_LEADER = 34
        SLAVERS = 35
        BOOK_OF_STABBING = 36
        AUTOMATON = 37
        COLLECTOR = 38
        CHAMP = 39

        # Act 3
        THREE_DARKLINGS = 40
        ORB_WALKER = 41
        THREE_SHAPES = 42
        SPIRE_GROWTH = 43
        TRANSIENT = 44
        FOUR_SHAPES = 45
        MAW = 46
        SPHERE_AND_TWO_SHAPES = 47
        JAW_WORM_HORDE = 48
        WRITHING_MASS = 49
        GIANT_HEAD = 50
        NEMESIS = 51
        REPTOMANCER = 52
        AWAKENED_ONE = 53
        TIME_EATER = 54
        DONU_AND_DECA = 55

        # Act 4
        SHIELD_AND_SPEAR = 56
        THE_HEART = 57

        # Events
        LAGAVULIN_EVENT = 58
        COLOSSEUM_EVENT_SLAVERS = 59
        COLOSSEUM_EVENT_NOBS = 60
        MASKED_BANDITS_EVENT = 61
        MUSHROOMS_EVENT = 62
        MYSTERIOUS_SPHERE_EVENT = 63

    MONSTERENCOUNTERSTRINGS = ["INVALID", "Cultist", "Jaw Worm", "Two Louse", "Small Slimes", "Blue Slaver", "Gremlin Gang", "Looter", "Large Slime", "Lots Of Slimes", "Exordium Thugs", "Exordium Wildlife", "Red Slaver", "Three Louse", "Two Fungi Beasts", "Gremlin Nob", "Lagavulin", "Three Sentries", "Slime Boss", "The Guardian", "Hexaghost", "Spheric Guardian", "Chosen", "Shell Parasite", "Three Byrds", "Two Thieves", "Chosen And Byrds", "Sentry And Sphere", "Snake Plant", "Snecko", "Centurion And Healer", "Cultist And Chosen", "Three Cultist", "Shelled Parasite And Fungi", "Gremlin Leader", "Slavers", "Book Of Stabbing", "Automaton", "Collector", "Champ", "Three Darklings", "Orb Walker", "Three Shapes", "Spire Growth", "Transient", "Four Shapes", "Maw", "Sphere And Two Shapes", "Jaw Worm Horde", "Writhing Mass", "Giant Head", "Nemesis", "Reptomancer", "Awakened One", "Time Eater", "Donu And Deca", "Shield And Spear", "The Heart", "LAGAVULIN_EVENT", "COLOSSEUM_EVENT_SLAVERS", "COLOSSEUM_EVENT_NOBS", "MASKED_BANDITS_EVENT", "MUSHROOMS_EVENT", "MYSTERIOUS_SPHERE_EVENT"]

    MONSTERENCOUNTERENUMNAMES = ["INVALID", "CULTIST", "JAW_WORM", "TWO_LOUSE", "SMALL_SLIMES", "BLUE_SLAVER", "GREMLIN_GANG", "LOOTER", "LARGE_SLIME", "LOTS_OF_SLIMES", "EXORDIUM_THUGS", "EXORDIUM_WILDLIFE", "RED_SLAVER", "THREE_LOUSE", "TWO_FUNGI_BEASTS", "GREMLIN_NOB", "LAGAVULIN", "THREE_SENTRIES", "SLIME_BOSS", "THE_GUARDIAN", "HEXAGHOST", "SPHERIC_GUARDIAN", "CHOSEN", "SHELL_PARASITE", "THREE_BYRDS", "TWO_THIEVES", "CHOSEN_AND_BYRDS", "SENTRY_AND_SPHERE", "SNAKE_PLANT", "SNECKO", "CENTURION_AND_HEALER", "CULTIST_AND_CHOSEN", "THREE_CULTIST", "SHELLED_PARASITE_AND_FUNGI", "GREMLIN_LEADER", "SLAVERS", "BOOK_OF_STABBING", "AUTOMATON", "COLLECTOR", "CHAMP", "THREE_DARKLINGS", "ORB_WALKER", "THREE_SHAPES", "SPIRE_GROWTH", "TRANSIENT", "FOUR_SHAPES", "MAW", "SPHERE_AND_TWO_SHAPES", "JAW_WORM_HORDE", "WRITHING_MASS", "GIANT_HEAD", "NEMESIS", "REPTOMANCER", "AWAKENED_ONE", "TIME_EATER", "DONU_AND_DECA", "SHIELD_AND_SPEAR", "THE_HEART", "LAGAVULIN_EVENT", "COLOSSEUM_EVENT_SLAVERS", "COLOSSEUM_EVENT_NOBS", "MASKED_BANDITS_EVENT", "MUSHROOMS_EVENT", "MYSTERIOUS_SPHERE_EVENT"]

    class MonsterEncounterPool: #this class replaces the original namespace 'MonsterEncounterPool'
        WEAKENEMIES = [[ME.CULTIST, ME.JAW_WORM, ME.TWO_LOUSE, ME.SMALL_SLIMES, 0], [ ME.SPHERIC_GUARDIAN, ME.CHOSEN, ME.SHELL_PARASITE, ME.THREE_BYRDS, ME.TWO_THIEVES ], [ME.THREE_DARKLINGS, ME.ORB_WALKER, ME.THREE_SHAPES, 0, 0]]
        WEAKWEIGHTS = [[1.0/4, 1.0/4, 1.0/4, 1.0/4, 0], [ 1.0/5, 1.0/5, 1.0/5, 1.0/5, 1.0/5 ], [1.0/3, 1.0/3, 1.0/3, 0, 0]]
        weakCount = [4, 5, 3]

        STRONGENEMIES = [[ ME.GREMLIN_GANG, ME.LOTS_OF_SLIMES, ME.RED_SLAVER, ME.EXORDIUM_THUGS, ME.EXORDIUM_WILDLIFE, ME.BLUE_SLAVER, ME.LOOTER, ME.LARGE_SLIME, ME.THREE_LOUSE, ME.TWO_FUNGI_BEASTS ], [ME.CHOSEN_AND_BYRDS, ME.SENTRY_AND_SPHERE, ME.CULTIST_AND_CHOSEN, ME.THREE_CULTIST, ME.SHELLED_PARASITE_AND_FUNGI, ME.SNECKO, ME.SNAKE_PLANT, ME.CENTURION_AND_HEALER, 0, 0], [ME.SPIRE_GROWTH, ME.TRANSIENT, ME.FOUR_SHAPES, ME.MAW, ME.SPHERE_AND_TWO_SHAPES, ME.JAW_WORM_HORDE, ME.THREE_DARKLINGS, ME.WRITHING_MASS, 0, 0]]
        STRONGWEIGHTS = [[ 1.0/16, 1.0/16, 1.0/16, 1.5/16, 1.5/16, 2.0/16, 2.0/16, 2.0/16, 2.0/16, 2.0/16 ], [2.0/29, 2.0/29, 3.0/29, 3.0/29, 3.0/29, 4.0/29, 6.0/29, 6.0/29, 0, 0], [1.0/8, 1.0/8, 1.0/8, 1.0/8, 1.0/8, 1.0/8, 1.0/8, 1.0/8, 0, 0]]
        strongCount = [10, 8, 8]

        elites = [[ ME.GREMLIN_NOB, ME.LAGAVULIN, ME.THREE_SENTRIES ], [ ME.GREMLIN_LEADER, ME.SLAVERS, ME.BOOK_OF_STABBING ], [ ME.GIANT_HEAD, ME.NEMESIS, ME.REPTOMANCER ]]

    @staticmethod
    def isBossEncounter(e):
        return e == sts.MonsterEncounter.SLIME_BOSS or e == sts.MonsterEncounter.HEXAGHOST or e == sts.MonsterEncounter.THE_GUARDIAN or e == sts.MonsterEncounter.CHAMP or e == sts.MonsterEncounter.COLLECTOR or e == sts.MonsterEncounter.AUTOMATON or e == sts.MonsterEncounter.DONU_AND_DECA or e == sts.MonsterEncounter.TIME_EATER or e == sts.MonsterEncounter.AWAKENED_ONE or e == sts.MonsterEncounter.THE_HEART





