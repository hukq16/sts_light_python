from enum import Enum


class MonsterId(Enum):
    INVALID = 0
    ACID_SLIME_L = 1
    ACID_SLIME_M = 2
    ACID_SLIME_S = 3
    AWAKENED_ONE = 4
    BEAR = 5
    BLUE_SLAVER = 6
    BOOK_OF_STABBING = 7
    BRONZE_AUTOMATON = 8
    BRONZE_ORB = 9
    BYRD = 10
    CENTURION = 11
    CHOSEN = 12
    CORRUPT_HEART = 13
    CULTIST = 14
    DAGGER = 15
    DARKLING = 16
    DECA = 17
    DONU = 18
    EXPLODER = 19
    FAT_GREMLIN = 20
    FUNGI_BEAST = 21
    GIANT_HEAD = 22
    GREEN_LOUSE = 23
    GREMLIN_LEADER = 24
    GREMLIN_NOB = 25
    GREMLIN_WIZARD = 26
    HEXAGHOST = 27
    JAW_WORM = 28
    LAGAVULIN = 29
    LOOTER = 30
    MAD_GREMLIN = 31
    MUGGER = 32
    MYSTIC = 33
    NEMESIS = 34
    ORB_WALKER = 35
    POINTY = 36
    RED_LOUSE = 37
    RED_SLAVER = 38
    REPTOMANCER = 39
    REPULSOR = 40
    ROMEO = 41
    SENTRY = 42
    SHELLED_PARASITE = 43
    SHIELD_GREMLIN = 44
    SLIME_BOSS = 45
    SNAKE_PLANT = 46
    SNEAKY_GREMLIN = 47
    SNECKO = 48
    SPHERIC_GUARDIAN = 49
    SPIKER = 50
    SPIKE_SLIME_L = 51
    SPIKE_SLIME_M = 52
    SPIKE_SLIME_S = 53
    SPIRE_GROWTH = 54
    SPIRE_SHIELD = 55
    SPIRE_SPEAR = 56
    TASKMASTER = 57
    THE_CHAMP = 58
    THE_COLLECTOR = 59
    THE_GUARDIAN = 60
    THE_MAW = 61
    TIME_EATER = 62
    TORCH_HEAD = 63
    TRANSIENT = 64
    WRITHING_MASS = 65


MONSTERIDSTRINGS = ["INVALID = 0", "ACID_SLIME_L", "ACID_SLIME_M", "ACID_SLIME_S", "AWAKENED_ONE", "BEAR",
                    "BLUE_SLAVER", "BOOK_OF_STABBING", "BRONZE_AUTOMATON", "BRONZE_ORB", "BYRD", "CENTURION", "CHOSEN",
                    "CORRUPT_HEART", "CULTIST", "DAGGER", "DARKLING", "DECA", "DONU", "EXPLODER", "FAT_GREMLIN",
                    "FUNGI_BEAST", "GIANT_HEAD", "GREEN_LOUSE", "GREMLIN_LEADER", "GREMLIN_NOB", "GREMLIN_WIZARD",
                    "HEXAGHOST", "JAW_WORM", "LAGAVULIN", "LOOTER", "MAD_GREMLIN", "MUGGER", "MYSTIC", "NEMESIS",
                    "ORB_WALKER", "POINTY", "RED_LOUSE", "RED_SLAVER", "REPTOMANCER", "REPULSOR", "ROMEO", "SENTRY",
                    "SHELLED_PARASITE", "SHIELD_GREMLIN", "SLIME_BOSS", "SNAKE_PLANT", "SNEAKY_GREMLIN", "SNECKO",
                    "SPHERIC_GUARDIAN", "SPIKER", "SPIKE_SLIME_L", "SPIKE_SLIME_M", "SPIKE_SLIME_S", "SPIRE_GROWTH",
                    "SPIRE_SHIELD", "SPIRE_SPEAR", "TASKMASTER", "THE_CHAMP", "THE_COLLECTOR", "THE_GUARDIAN",
                    "THE_MAW", "TIME_EATER", "TORCH_HEAD", "TRANSIENT", "WRITHING_MASS"]

MONSTERHPRANGE = [[[0, 0], [0, 0]], [[65, 69], [68, 72]], [[28, 32], [29, 34]], [[8, 12], [9, 13]],
                  [[300, 300], [300, 320]], [[38, 52], [40, 44]], [[46, 50], [48, 52]], [[160, 164], [168, 172]],
                  [[300, 300], [320, 320]], [[52, 58], [54, 60]], [[25, 31], [26, 33]], [[76, 80], [76, 83]],
                  [[95, 99], [98, 103]], [[750, 750], [800, 800]], [[48, 54], [50, 56]], [[20, 25], [20, 25]],
                  [[48, 56], [50, 59]], [[250, 250], [265, 265]], [[250, 250], [265, 265]], [[30, 30], [30, 35]],
                  [[13, 17], [14, 18]], [[22, 28], [24, 28]], [[500, 500], [520, 520]], [[11, 17], [12, 18]],
                  [[140, 148], [145, 155]], [[82, 86], [85, 90]], [[21, 25], [22, 26]], [[250, 250], [264, 264]],
                  [[40, 44], [42, 46]], [[109, 111], [112, 115]], [[44, 48], [46, 50]], [[20, 24], [21, 25]],
                  [[48, 52], [50, 54]], [[48, 56], [50, 58]], [[185, 185], [200, 200]], [[90, 96], [92, 102]],
                  [[30, 30], [34, 34]], [[10, 15], [11, 16]], [[46, 50], [48, 52]], [[180, 190], [190, 200]],
                  [[29, 35], [31, 38]], [[35, 39], [37, 41]], [[38, 42], [39, 45]], [[68, 72], [70, 75]],
                  [[12, 15], [13, 17]], [[140, 140], [150, 150]], [[75, 79], [78, 82]], [[10, 14], [11, 15]],
                  [[114, 120], [120, 125]], [[20, 20], [20, 20]], [[42, 56], [44, 60]], [[64, 70], [67, 73]],
                  [[28, 32], [29, 34]], [[10, 14], [11, 15]], [[170, 170], [190, 190]], [[110, 110], [125, 125]],
                  [[160, 160], [180, 180]], [[54, 60], [57, 64]], [[420, 420], [440, 440]], [[282, 282], [300, 300]],
                  [[240, 240], [250, 250]], [[300, 300], [300, 300]], [[456, 456], [480, 480]], [[38, 40], [40, 45]],
                  [[999, 999], [999, 999]], [[160, 160], [175, 175]]]
