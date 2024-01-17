from enum import Enum


class Event(Enum):
    INVALID = 0
    MONSTER = 1
    REST = 2
    SHOP = 3
    TREASURE = 4
    NEOW = 5
    OMINOUS_FORGE = 6
    PLEADING_VAGRANT = 7
    ANCIENT_WRITING = 8
    OLD_BEGGAR = 9
    BIG_FISH = 10
    BONFIRE_SPIRITS = 11
    COLOSSEUM = 12
    CURSED_TOME = 13
    DEAD_ADVENTURER = 14
    DESIGNER_IN_SPIRE = 15
    AUGMENTER = 16
    DUPLICATOR = 17
    FACE_TRADER = 18
    FALLING = 19
    FORGOTTEN_ALTAR = 20
    THE_DIVINE_FOUNTAIN = 21
    GHOSTS = 22
    GOLDEN_IDOL = 23
    GOLDEN_SHRINE = 24
    WING_STATUE = 25
    KNOWING_SKULL = 26
    LAB = 27
    THE_SSSSSERPENT = 28
    LIVING_WALL = 29
    MASKED_BANDITS = 30
    MATCH_AND_KEEP = 31
    MINDBLOOM = 32
    HYPNOTIZING_COLORED_MUSHROOMS = 33
    MYSTERIOUS_SPHERE = 34
    THE_NEST = 35
    NLOTH = 36
    NOTE_FOR_YOURSELF = 37
    PURIFIER = 38
    SCRAP_OOZE = 39
    SECRET_PORTAL = 40
    SENSORY_STONE = 41
    SHINING_LIGHT = 42
    THE_CLERIC = 43
    THE_JOUST = 44
    THE_LIBRARY = 45
    THE_MAUSOLEUM = 46
    THE_MOAI_HEAD = 47
    THE_WOMAN_IN_BLUE = 48
    TOMB_OF_LORD_RED_MASK = 49
    TRANSMORGRIFIER = 50
    UPGRADE_SHRINE = 51
    VAMPIRES = 52
    WE_MEET_AGAIN = 53
    WHEEL_OF_CHANGE = 54
    WINDING_HALLS = 55
    WORLD_OF_GOOP = 56

    def __int__(self):
        return self.value


EVENTIDSTRINGS = ["INVALID", "MONSTER", "REST", "SHOP", "TREASURE", "NEOW", "Accursed Blacksmith", "Addict",
                  "Back to Basics", "Beggar", "Big Fish", "Bonfire Elementals", "Colosseum", "Cursed Tome",
                  "Dead Adventurer", "Designer", "Drug Dealer", "Duplicator", "Face Trader", "Falling",
                  "Forgotten Altar", "Fountain of Cleansing", "Ghosts", "Golden Idol", "Golden Shrine", "Golden Wing",
                  "Knowing Skull", "Lab", "Liars Game", "Living Wall", "Masked Bandits", "Match and Keep", "Mindbloom",
                  "Mushrooms", "Mysterious Sphere", "Nest", "Nloth", "Note For Yourself", "Purifier", "Scrap Ooze",
                  "Secret Portal", "Sensory Stone", "Shining Light", "The Cleric", "The Joust", "The Library",
                  "The Mausoleum", "The Moai Head", "The Woman in Blue", "Tomb of Lord Red Mask", "Transmorgrifier",
                  "Upgrade Shrine", "Vampires", "WeMeetAgain", "Wheel of Change", "Winding Halls", "World of Goop"]

EVENTGAMENAMES = ["INVALID", "MONSTER", "REST", "SHOP", "TREASURE", "NEOW", "Ominous Forge", "Pleading Vagrant",
                  "Ancient Writing", "Old Beggar", "Big Fish", "Bonfire Spirits", "The Colosseum", "Cursed Tome",
                  "Dead Adventurer", "Designer In-Spire", "Augmenter", "Duplicator", "Face Trader", "Falling",
                  "Forgotten Altar", "The Divine Fountain", "Council of Ghosts", "Golden Idol", "Golden Shrine",
                  "Wing Statue", "Knowing Skull", "Lab", "The Ssssserpent", "Living Wall", "Masked Bandits",
                  "Match and Keep", "Mindbloom", "Hypnotizing Colored Mushrooms", "Mysterious Sphere", "The Nest",
                  "N'loth", "Note For Yourself", "Purifier", "Scrap Ooze", "Secret Portal", "Sensory Stone",
                  "Shining Light", "The Cleric", "The Joust", "The Library", "The Mausoleum", "The Moai Head",
                  "The Woman in Blue", "Tomb of Lord Red Mask", "Transmorgrifier", "Upgrade Shrine", "Vampires(?)",
                  "We Meet Again!", "Wheel of Change", "Winding Halls", "World of Goop"]


class EventPools:
    oneTimeEventsAsc0 = [Event.OMINOUS_FORGE, Event.BONFIRE_SPIRITS, Event.DESIGNER_IN_SPIRE, Event.DUPLICATOR,
                         Event.FACE_TRADER, Event.THE_DIVINE_FOUNTAIN, Event.KNOWING_SKULL, Event.LAB, Event.NLOTH,
                         Event.NOTE_FOR_YOURSELF, Event.SECRET_PORTAL, Event.THE_JOUST, Event.WE_MEET_AGAIN,
                         Event.THE_WOMAN_IN_BLUE]
    oneTimeEventsAsc15 = [Event.OMINOUS_FORGE, Event.BONFIRE_SPIRITS, Event.DESIGNER_IN_SPIRE, Event.DUPLICATOR,
                          Event.FACE_TRADER, Event.THE_DIVINE_FOUNTAIN, Event.KNOWING_SKULL, Event.LAB, Event.NLOTH,
                          Event.SECRET_PORTAL, Event.THE_JOUST, Event.WE_MEET_AGAIN, Event.THE_WOMAN_IN_BLUE]

    class Act1:
        events = [Event.BIG_FISH, Event.THE_CLERIC, Event.DEAD_ADVENTURER, Event.GOLDEN_IDOL, Event.WING_STATUE,
                  Event.WORLD_OF_GOOP, Event.THE_SSSSSERPENT, Event.LIVING_WALL, Event.HYPNOTIZING_COLORED_MUSHROOMS,
                  Event.SCRAP_OOZE, Event.SHINING_LIGHT]
        shrines = [Event.MATCH_AND_KEEP, Event.GOLDEN_SHRINE, Event.TRANSMORGRIFIER, Event.PURIFIER,
                   Event.UPGRADE_SHRINE, Event.WHEEL_OF_CHANGE]

    class Act2:
        events = [Event.PLEADING_VAGRANT, Event.ANCIENT_WRITING, Event.OLD_BEGGAR, Event.COLOSSEUM, Event.CURSED_TOME,
                  Event.AUGMENTER, Event.FORGOTTEN_ALTAR, Event.GHOSTS, Event.MASKED_BANDITS, Event.THE_NEST,
                  Event.THE_LIBRARY, Event.THE_MAUSOLEUM, Event.VAMPIRES]
        shrines = [Event.MATCH_AND_KEEP, Event.WHEEL_OF_CHANGE, Event.GOLDEN_SHRINE, Event.TRANSMORGRIFIER,
                   Event.PURIFIER, Event.UPGRADE_SHRINE]

    class Act3:
        events = [Event.FALLING, Event.MINDBLOOM, Event.THE_MOAI_HEAD, Event.MYSTERIOUS_SPHERE, Event.SENSORY_STONE,
                  Event.TOMB_OF_LORD_RED_MASK, Event.WINDING_HALLS]
        shrines = [Event.MATCH_AND_KEEP, Event.WHEEL_OF_CHANGE, Event.GOLDEN_SHRINE, Event.TRANSMORGRIFIER,
                   Event.PURIFIER, Event.UPGRADE_SHRINE]
