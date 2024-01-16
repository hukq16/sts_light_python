from enum import Enum


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
    def __int__(self):
        return self.value


MONSTERENCOUNTERSTRINGS = ["INVALID", "Cultist", "Jaw Worm", "Two Louse", "Small Slimes", "Blue Slaver", "Gremlin Gang",
                           "Looter", "Large Slime", "Lots Of Slimes", "Exordium Thugs", "Exordium Wildlife",
                           "Red Slaver", "Three Louse", "Two Fungi Beasts", "Gremlin Nob", "Lagavulin",
                           "Three Sentries", "Slime Boss", "The Guardian", "Hexaghost", "Spheric Guardian", "Chosen",
                           "Shell Parasite", "Three Byrds", "Two Thieves", "Chosen And Byrds", "Sentry And Sphere",
                           "Snake Plant", "Snecko", "Centurion And Healer", "Cultist And Chosen", "Three Cultist",
                           "Shelled Parasite And Fungi", "Gremlin Leader", "Slavers", "Book Of Stabbing", "Automaton",
                           "Collector", "Champ", "Three Darklings", "Orb Walker", "Three Shapes", "Spire Growth",
                           "Transient", "Four Shapes", "Maw", "Sphere And Two Shapes", "Jaw Worm Horde",
                           "Writhing Mass", "Giant Head", "Nemesis", "Reptomancer", "Awakened One", "Time Eater",
                           "Donu And Deca", "Shield And Spear", "The Heart", "LAGAVULIN_EVENT",
                           "COLOSSEUM_EVENT_SLAVERS", "COLOSSEUM_EVENT_NOBS", "MASKED_BANDITS_EVENT", "MUSHROOMS_EVENT",
                           "MYSTERIOUS_SPHERE_EVENT"]

MONSTERENCOUNTERENUMNAMES = ["INVALID", "CULTIST", "JAW_WORM", "TWO_LOUSE", "SMALL_SLIMES", "BLUE_SLAVER",
                             "GREMLIN_GANG", "LOOTER", "LARGE_SLIME", "LOTS_OF_SLIMES", "EXORDIUM_THUGS",
                             "EXORDIUM_WILDLIFE", "RED_SLAVER", "THREE_LOUSE", "TWO_FUNGI_BEASTS", "GREMLIN_NOB",
                             "LAGAVULIN", "THREE_SENTRIES", "SLIME_BOSS", "THE_GUARDIAN", "HEXAGHOST",
                             "SPHERIC_GUARDIAN", "CHOSEN", "SHELL_PARASITE", "THREE_BYRDS", "TWO_THIEVES",
                             "CHOSEN_AND_BYRDS", "SENTRY_AND_SPHERE", "SNAKE_PLANT", "SNECKO", "CENTURION_AND_HEALER",
                             "CULTIST_AND_CHOSEN", "THREE_CULTIST", "SHELLED_PARASITE_AND_FUNGI", "GREMLIN_LEADER",
                             "SLAVERS", "BOOK_OF_STABBING", "AUTOMATON", "COLLECTOR", "CHAMP", "THREE_DARKLINGS",
                             "ORB_WALKER", "THREE_SHAPES", "SPIRE_GROWTH", "TRANSIENT", "FOUR_SHAPES", "MAW",
                             "SPHERE_AND_TWO_SHAPES", "JAW_WORM_HORDE", "WRITHING_MASS", "GIANT_HEAD", "NEMESIS",
                             "REPTOMANCER", "AWAKENED_ONE", "TIME_EATER", "DONU_AND_DECA", "SHIELD_AND_SPEAR",
                             "THE_HEART", "LAGAVULIN_EVENT", "COLOSSEUM_EVENT_SLAVERS", "COLOSSEUM_EVENT_NOBS",
                             "MASKED_BANDITS_EVENT", "MUSHROOMS_EVENT", "MYSTERIOUS_SPHERE_EVENT"]


class MonsterEncounterPool:  # this class replaces the original namespace 'MonsterEncounterPool'
    WEAKENEMIES = [
        [MonsterEncounter.CULTIST, MonsterEncounter.JAW_WORM, MonsterEncounter.TWO_LOUSE, MonsterEncounter.SMALL_SLIMES,
         0],
        [MonsterEncounter.SPHERIC_GUARDIAN, MonsterEncounter.CHOSEN, MonsterEncounter.SHELL_PARASITE,
         MonsterEncounter.THREE_BYRDS, MonsterEncounter.TWO_THIEVES],
        [MonsterEncounter.THREE_DARKLINGS, MonsterEncounter.ORB_WALKER, MonsterEncounter.THREE_SHAPES, 0, 0]]
    WEAKWEIGHTS = [[1.0 / 4, 1.0 / 4, 1.0 / 4, 1.0 / 4, 0], [1.0 / 5, 1.0 / 5, 1.0 / 5, 1.0 / 5, 1.0 / 5],
                   [1.0 / 3, 1.0 / 3, 1.0 / 3, 0, 0]]
    weakCount = [4, 5, 3]

    STRONGENEMIES = [
        [MonsterEncounter.GREMLIN_GANG, MonsterEncounter.LOTS_OF_SLIMES, MonsterEncounter.RED_SLAVER,
         MonsterEncounter.EXORDIUM_THUGS, MonsterEncounter.EXORDIUM_WILDLIFE, MonsterEncounter.BLUE_SLAVER,
         MonsterEncounter.LOOTER, MonsterEncounter.LARGE_SLIME, MonsterEncounter.THREE_LOUSE,
         MonsterEncounter.TWO_FUNGI_BEASTS],
        [MonsterEncounter.CHOSEN_AND_BYRDS, MonsterEncounter.SENTRY_AND_SPHERE, MonsterEncounter.CULTIST_AND_CHOSEN,
         MonsterEncounter.THREE_CULTIST,
         MonsterEncounter.SHELLED_PARASITE_AND_FUNGI, MonsterEncounter.SNECKO, MonsterEncounter.SNAKE_PLANT,
         MonsterEncounter.CENTURION_AND_HEALER, 0, 0],
        [MonsterEncounter.SPIRE_GROWTH, MonsterEncounter.TRANSIENT, MonsterEncounter.FOUR_SHAPES, MonsterEncounter.MAW,
         MonsterEncounter.SPHERE_AND_TWO_SHAPES, MonsterEncounter.JAW_WORM_HORDE,
         MonsterEncounter.THREE_DARKLINGS, MonsterEncounter.WRITHING_MASS, 0, 0]]
    STRONGWEIGHTS = [
        [1.0 / 16, 1.0 / 16, 1.0 / 16, 1.5 / 16, 1.5 / 16, 2.0 / 16, 2.0 / 16, 2.0 / 16, 2.0 / 16, 2.0 / 16],
        [2.0 / 29, 2.0 / 29, 3.0 / 29, 3.0 / 29, 3.0 / 29, 4.0 / 29, 6.0 / 29, 6.0 / 29, 0, 0],
        [1.0 / 8, 1.0 / 8, 1.0 / 8, 1.0 / 8, 1.0 / 8, 1.0 / 8, 1.0 / 8, 1.0 / 8, 0, 0]]
    strongCount = [10, 8, 8]

    elites = [[MonsterEncounter.GREMLIN_NOB, MonsterEncounter.LAGAVULIN, MonsterEncounter.THREE_SENTRIES],
              [MonsterEncounter.GREMLIN_LEADER, MonsterEncounter.SLAVERS, MonsterEncounter.BOOK_OF_STABBING],
              [MonsterEncounter.GIANT_HEAD, MonsterEncounter.NEMESIS, MonsterEncounter.REPTOMANCER]]


def isBossEncounter(e):
    return e == MonsterEncounter.SLIME_BOSS or e == MonsterEncounter.HEXAGHOST or e == MonsterEncounter.THE_GUARDIAN or e == MonsterEncounter.CHAMP or e == MonsterEncounter.COLLECTOR or e == MonsterEncounter.AUTOMATON or e == MonsterEncounter.DONU_AND_DECA or e == MonsterEncounter.TIME_EATER or e == MonsterEncounter.AWAKENED_ONE or e == MonsterEncounter.THE_HEART
