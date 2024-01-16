﻿from enum import Enum


class RelicId(Enum):
    # battle relics -- relics which state is needed in battle
    AKABEKO = 0
    ART_OF_WAR = 1
    BIRD_FACED_URN = 2
    BLOODY_IDOL = 3
    BLUE_CANDLE = 4
    BRIMSTONE = 5
    CALIPERS = 6
    CAPTAINS_WHEEL = 7
    CENTENNIAL_PUZZLE = 8
    CERAMIC_FISH = 9
    CHAMPION_BELT = 10
    CHARONS_ASHES = 11
    CHEMICAL_X = 12
    CLOAK_CLASP = 13
    DARKSTONE_PERIAPT = 14
    DEAD_BRANCH = 15
    DUALITY = 16
    ECTOPLASM = 17
    EMOTION_CHIP = 18
    FROZEN_CORE = 19
    FROZEN_EYE = 20
    GAMBLING_CHIP = 21
    GINGER = 22
    GOLDEN_EYE = 23
    GREMLIN_HORN = 24
    HAND_DRILL = 25
    HAPPY_FLOWER = 26
    HORN_CLEAT = 27
    HOVERING_KITE = 28
    ICE_CREAM = 29
    INCENSE_BURNER = 30
    INK_BOTTLE = 31
    INSERTER = 32
    KUNAI = 33
    LETTER_OPENER = 34
    LIZARD_TAIL = 35
    MAGIC_FLOWER = 36
    MARK_OF_THE_BLOOM = 37
    MEDICAL_KIT = 38
    MELANGE = 39
    MERCURY_HOURGLASS = 40
    MUMMIFIED_HAND = 41
    NECRONOMICON = 42
    NILRYS_CODEX = 43
    NUNCHAKU = 44
    ODD_MUSHROOM = 45
    OMAMORI = 46
    ORANGE_PELLETS = 47
    ORICHALCUM = 48
    ORNAMENTAL_FAN = 49
    PAPER_KRANE = 50
    PAPER_PHROG = 51
    PEN_NIB = 52
    PHILOSOPHERS_STONE = 53
    POCKETWATCH = 54
    RED_SKULL = 55
    RUNIC_CUBE = 56
    RUNIC_DOME = 57
    RUNIC_PYRAMID = 58
    SACRED_BARK = 59
    SELF_FORMING_CLAY = 60
    SHURIKEN = 61
    SNECKO_EYE = 62
    SNECKO_SKULL = 63
    SOZU = 64
    STONE_CALENDAR = 65
    STRANGE_SPOON = 66
    STRIKE_DUMMY = 67
    SUNDIAL = 68
    THE_ABACUS = 69
    THE_BOOT = 70
    THE_SPECIMEN = 71
    TINGSHA = 72
    TOOLBOX = 73
    TORII = 74
    TOUGH_BANDAGES = 75
    TOY_ORNITHOPTER = 76
    TUNGSTEN_ROD = 77
    TURNIP = 78
    TWISTED_FUNNEL = 79
    UNCEASING_TOP = 80
    VELVET_CHOKER = 81
    VIOLET_LOTUS = 82
    WARPED_TONGS = 83
    WRIST_BLADE = 84

    # end of battle relics
    BLACK_BLOOD = 85
    BURNING_BLOOD = 86
    MEAT_ON_THE_BONE = 87
    FACE_OF_CLERIC = 88

    # beginning of battle relics
    ANCHOR = 89
    ANCIENT_TEA_SET = 90
    BAG_OF_MARBLES = 91
    BAG_OF_PREPARATION = 92
    BLOOD_VIAL = 93
    BOTTLED_FLAME = 94
    BOTTLED_LIGHTNING = 95
    BOTTLED_TORNADO = 96
    BRONZE_SCALES = 97
    BUSTED_CROWN = 98
    CLOCKWORK_SOUVENIR = 99
    COFFEE_DRIPPER = 100
    CRACKED_CORE = 101
    CURSED_KEY = 102
    DAMARU = 103
    DATA_DISK = 104
    DU_VU_DOLL = 105
    ENCHIRIDION = 106
    FOSSILIZED_HELIX = 107
    FUSION_HAMMER = 108
    GIRYA = 109
    GOLD_PLATED_CABLES = 110
    GREMLIN_VISAGE = 111
    HOLY_WATER = 112
    LANTERN = 113
    MARK_OF_PAIN = 114
    MUTAGENIC_STRENGTH = 115
    NEOWS_LAMENT = 116
    NINJA_SCROLL = 117
    NUCLEAR_BATTERY = 118
    ODDLY_SMOOTH_STONE = 119
    PANTOGRAPH = 120
    PRESERVED_INSECT = 121
    PURE_WATER = 122
    RED_MASK = 123
    RING_OF_THE_SERPENT = 124
    RING_OF_THE_SNAKE = 125
    RUNIC_CAPACITOR = 126
    SLAVERS_COLLAR = 127
    SLING_OF_COURAGE = 128
    SYMBIOTIC_VIRUS = 129
    TEARDROP_LOCKET = 130
    THREAD_AND_NEEDLE = 131
    VAJRA = 132

    # out of battle relics
    ASTROLABE = 133
    BLACK_STAR = 134
    CALLING_BELL = 135
    CAULDRON = 136
    CULTIST_HEADPIECE = 137
    DOLLYS_MIRROR = 138
    DREAM_CATCHER = 139
    EMPTY_CAGE = 140
    ETERNAL_FEATHER = 141
    FROZEN_EGG = 142
    GOLDEN_IDOL = 143
    JUZU_BRACELET = 144
    LEES_WAFFLE = 145
    MANGO = 146
    MATRYOSHKA = 147
    MAW_BANK = 148
    MEAL_TICKET = 149
    MEMBERSHIP_CARD = 150
    MOLTEN_EGG = 151
    NLOTHS_GIFT = 152
    NLOTHS_HUNGRY_FACE = 153
    OLD_COIN = 154
    ORRERY = 155
    PANDORAS_BOX = 156
    PEACE_PIPE = 157
    PEAR = 158
    POTION_BELT = 159
    PRAYER_WHEEL = 160
    PRISMATIC_SHARD = 161
    QUESTION_CARD = 162
    REGAL_PILLOW = 163
    SSSERPENT_HEAD = 164
    SHOVEL = 165
    SINGING_BOWL = 166
    SMILING_MASK = 167
    SPIRIT_POOP = 168
    STRAWBERRY = 169
    THE_COURIER = 170
    TINY_CHEST = 171
    TINY_HOUSE = 172
    TOXIC_EGG = 173
    WAR_PAINT = 174
    WHETSTONE = 175
    WHITE_BEAST_STATUE = 176
    WING_BOOTS = 177

    CIRCLET = 178
    RED_CIRCLET = 179
    INVALID = 180
    def __int__(self):
        return self.value


class RelicTier(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    BOSS = 3
    SHOP = 4
    STARTER = 5
    SPECIAL = 6
    INVALID = 7
    def __int__(self):
        return self.value


relicTierStrings = ["Common", "Uncommon", "Rare", "Boss", "Shop", "Starter", "Special", "Invalid"]
relicEnumNames = ["AKABEKO", "ART_OF_WAR", "BIRD_FACED_URN", "BLOODY_IDOL", "BLUE_CANDLE", "BRIMSTONE", "CALIPERS",
                  "CAPTAINS_WHEEL", "CENTENNIAL_PUZZLE", "CERAMIC_FISH", "CHAMPION_BELT", "CHARONS_ASHES", "CHEMICAL_X",
                  "CLOAK_CLASP", "DARKSTONE_PERIAPT", "DEAD_BRANCH", "DUALITY", "ECTOPLASM", "EMOTION_CHIP",
                  "FROZEN_CORE", "FROZEN_EYE", "GAMBLING_CHIP", "GINGER", "GOLDEN_EYE", "GREMLIN_HORN", "HAND_DRILL",
                  "HAPPY_FLOWER", "HORN_CLEAT", "HOVERING_KITE", "ICE_CREAM", "INCENSE_BURNER", "INK_BOTTLE",
                  "INSERTER", "KUNAI", "LETTER_OPENER", "LIZARD_TAIL", "MAGIC_FLOWER", "MARK_OF_THE_BLOOM",
                  "MEDICAL_KIT", "MELANGE", "MERCURY_HOURGLASS", "MUMMIFIED_HAND", "NECRONOMICON", "NILRYS_CODEX",
                  "NUNCHAKU", "ODD_MUSHROOM", "OMAMORI", "ORANGE_PELLETS", "ORICHALCUM", "ORNAMENTAL_FAN",
                  "PAPER_KRANE", "PAPER_PHROG", "PEN_NIB", "PHILOSOPHERS_STONE", "POCKETWATCH", "RED_SKULL",
                  "RUNIC_CUBE", "RUNIC_DOME", "RUNIC_PYRAMID", "SACRED_BARK", "SELF_FORMING_CLAY", "SHURIKEN",
                  "SNECKO_EYE", "SNECKO_SKULL", "SOZU", "STONE_CALENDAR", "STRANGE_SPOON", "STRIKE_DUMMY", "SUNDIAL",
                  "THE_ABACUS", "THE_BOOT", "THE_SPECIMEN", "TINGSHA", "TOOLBOX", "TORII", "TOUGH_BANDAGES",
                  "TOY_ORNITHOPTER", "TUNGSTEN_ROD", "TURNIP", "TWISTED_FUNNEL", "UNCEASING_TOP", "VELVET_CHOKER",
                  "VIOLET_LOTUS", "WARPED_TONGS", "WRIST_BLADE", "BLACK_BLOOD", "BURNING_BLOOD", "MEAT_ON_THE_BONE",
                  "FACE_OF_CLERIC", "ANCHOR", "ANCIENT_TEA_SET", "BAG_OF_MARBLES", "BAG_OF_PREPARATION", "BLOOD_VIAL",
                  "BOTTLED_FLAME", "BOTTLED_LIGHTNING", "BOTTLED_TORNADO", "BRONZE_SCALES", "BUSTED_CROWN",
                  "CLOCKWORK_SOUVENIR", "COFFEE_DRIPPER", "CRACKED_CORE", "CURSED_KEY", "DAMARU", "DATA_DISK",
                  "DU_VU_DOLL", "ENCHIRIDION", "FOSSILIZED_HELIX", "FUSION_HAMMER", "GIRYA", "GOLD_PLATED_CABLES",
                  "GREMLIN_VISAGE", "HOLY_WATER", "LANTERN", "MARK_OF_PAIN", "MUTAGENIC_STRENGTH", "NEOWS_LAMENT",
                  "NINJA_SCROLL", "NUCLEAR_BATTERY", "ODDLY_SMOOTH_STONE", "PANTOGRAPH", "PRESERVED_INSECT",
                  "PURE_WATER", "RED_MASK", "RING_OF_THE_SERPENT", "RING_OF_THE_SNAKE", "RUNIC_CAPACITOR",
                  "SLAVERS_COLLAR", "SLING_OF_COURAGE", "SYMBIOTIC_VIRUS", "TEARDROP_LOCKET", "THREAD_AND_NEEDLE",
                  "VAJRA", "ASTROLABE", "BLACK_STAR", "CALLING_BELL", "CAULDRON", "CULTIST_HEADPIECE", "DOLLYS_MIRROR",
                  "DREAM_CATCHER", "EMPTY_CAGE", "ETERNAL_FEATHER", "FROZEN_EGG", "GOLDEN_IDOL", "JUZU_BRACELET",
                  "LEES_WAFFLE", "MANGO", "MATRYOSHKA", "MAW_BANK", "MEAL_TICKET", "MEMBERSHIP_CARD", "MOLTEN_EGG",
                  "NLOTHS_GIFT", "NLOTHS_HUNGRY_FACE", "OLD_COIN", "ORRERY", "PANDORAS_BOX", "PEACE_PIPE", "PEAR",
                  "POTION_BELT", "PRAYER_WHEEL", "PRISMATIC_SHARD", "QUESTION_CARD", "REGAL_PILLOW", "SSSERPENT_HEAD",
                  "SHOVEL", "SINGING_BOWL", "SMILING_MASK", "SPIRIT_POOP", "STRAWBERRY", "THE_COURIER", "TINY_CHEST",
                  "TINY_HOUSE", "TOXIC_EGG", "WAR_PAINT", "WHETSTONE", "WHITE_BEAST_STATUE", "WING_BOOTS", "CIRCLET",
                  "RED_CIRCLET", "INVALID"]
relicNames = ["Akabeko", "Art Of War", "Bird Faced Urn", "Bloody Idol", "Blue Candle", "Brimstone", "Calipers",
              "Captains Wheel", "Centennial Puzzle", "Ceramic Fish", "Champion Belt", "Charons Ashes", "Chemical X",
              "Cloak Clasp", "Darkstone Periapt", "Dead Branch", "Duality", "Ectoplasm", "Emotion Chip", "Frozen Core",
              "Frozen Eye", "Gambling Chip", "Ginger", "Golden Eye", "Gremlin Horn", "Hand Drill", "Happy Flower",
              "Horn Cleat", "Hovering Kite", "Ice Cream", "Incense Burner", "Ink Bottle", "Inserter", "Kunai",
              "Letter Opener", "Lizard Tail", "Magic Flower", "Mark Of The Bloom", "Medical Kit", "Melange",
              "Mercury Hourglass", "Mummified Hand", "Necronomicon", "Nilrys Codex", "Nunchaku", "Odd Mushroom",
              "Omamori", "Orange Pellets", "Orichalcum", "Ornamental Fan", "Paper Krane", "Paper Phrog", "Pen Nib",
              "Philosophers Stone", "Pocketwatch", "Red Skull", "Runic Cube", "Runic Dome", "Runic Pyramid",
              "Sacred Bark", "Self Forming Clay", "Shuriken", "Snecko Eye", "Snecko Skull", "Sozu", "Stone Calendar",
              "Strange Spoon", "Strike Dummy", "Sundial", "The Abacus", "The Boot", "The Specimen", "Tingsha",
              "Toolbox", "Torii", "Tough Bandages", "Toy Ornithopter", "Tungsten Rod", "Turnip", "Twisted Funnel",
              "Unceasing Top", "Velvet Choker", "Violet Lotus", "Warped Tongs", "Wrist Blade", "Black Blood",
              "Burning Blood", "Meat On The Bone", "Face Of Cleric", "Anchor", "Ancient Tea Set", "Bag Of Marbles",
              "Bag Of Preparation", "Blood Vial", "Bottled Flame", "Bottled Lightning", "Bottled Tornado",
              "Bronze Scales", "Busted Crown", "Clockwork Souvenir", "Coffee Dripper", "Cracked Core", "Cursed Key",
              "Damaru", "Data Disk", "Du Vu Doll", "Enchiridion", "Fossilized Helix", "Fusion Hammer", "Girya",
              "Goldplated Cables", "Gremlin Visage", "Holy Water", "Lantern", "Mark Of Pain", "Mutagenic Strength",
              "Neows Lament", "Ninja Scroll", "Nuclear Battery", "Oddly Smooth Stone", "Pantograph", "Preserved Insect",
              "Pure Water", "Red Mask", "Ring Of The Serpent", "Ring Of The Snake", "Runic Capacitor", "Slavers Collar",
              "Sling Of Courage", "Symbiotic Virus", "Teardrop Locket", "Thread And Needle", "Vajra", "Astrolabe",
              "Black Star", "Calling Bell", "Cauldron", "Cultist Headpiece", "Dollys Mirror", "Dream Catcher",
              "Empty Cage", "Eternal Feather", "Frozen Egg", "Golden Idol", "Juzu Bracelet", "Lees Waffle", "Mango",
              "Matryoshka", "Maw Bank", "Meal Ticket", "Membership Card", "Molten Egg", "Nloths Gift",
              "Nloths Hungry Face", "Old Coin", "Orrery", "Pandoras Box", "Peace Pipe", "Pear", "Potion Belt",
              "Prayer Wheel", "Prismatic Shard", "Question Card", "Regal Pillow", "Ssserpent Head", "Shovel",
              "Singing Bowl", "Smiling Mask", "Spirit Poop", "Strawberry", "The Courier", "Tiny Chest", "Tiny House",
              "Toxic Egg", "War Paint", "Whetstone", "White Beast Statue", "Wing Boots", "Circlet", "Red Circlet",
              "Invalid"]
relicIds = ["Akabeko", "Art of War", "Bird Faced Urn", "Bloody Idol", "Blue Candle", "Brimstone", "Calipers",
            "CaptainsWheel", "Centennial Puzzle", "CeramicFish", "Champion Belt", "Charon's Ashes", "Chemical X",
            "CloakClasp", "Darkstone Periapt", "Dead Branch", "Yang", "Ectoplasm", "Emotion Chip", "FrozenCore",
            "Frozen Eye", "Gambling Chip", "Ginger", "GoldenEye", "Gremlin Horn", "HandDrill", "Happy Flower",
            "HornCleat", "HoveringKite", "Ice Cream", "Incense Burner", "InkBottle", "Inserter", "Kunai",
            "Letter Opener", "Lizard Tail", "Magic Flower", "Mark of the Bloom", "Medical Kit", "Melange",
            "Mercury Hourglass", "Mummified Hand", "Necronomicon", "Nilry's Codex", "Nunchaku", "Odd Mushroom",
            "Omamori", "OrangePellets", "Orichalcum", "Ornamental Fan", "Paper Crane", "Paper Frog", "Pen Nib",
            "Philosopher's Stone", "Pocketwatch", "Red Skull", "Runic Cube", "Runic Dome", "Runic Pyramid",
            "SacredBark", "Self Forming Clay", "Shuriken", "Snecko Eye", "Snake Skull", "Sozu", "StoneCalendar",
            "Strange Spoon", "StrikeDummy", "Sundial", "TheAbacus", "Boot", "The Specimen", "Tingsha", "Toolbox",
            "Torii", "Tough Bandages", "Toy Ornithopter", "TungstenRod", "Turnip", "TwistedFunnel", "Unceasing Top",
            "Velvet Choker", "VioletLotus", "WarpedTongs", "WristBlade", "Black Blood", "Burning Blood",
            "Meat on the Bone", "FaceOfCleric", "Anchor", "Ancient Tea Set", "Bag of Marbles", "Bag of Preparation",
            "Blood Vial", "Bottled Flame", "Bottled Lightning", "Bottled Tornado", "Bronze Scales", "Busted Crown",
            "ClockworkSouvenir", "Coffee Dripper", "Cracked Core", "Cursed Key", "Damaru", "DataDisk", "Du-Vu Doll",
            "Enchiridion", "FossilizedHelix", "Fusion Hammer", "Girya", "Cables", "GremlinMask", "HolyWater", "Lantern",
            "Mark of Pain", "MutagenicStrength", "NeowsBlessing", "Ninja Scroll", "Nuclear Battery",
            "Oddly Smooth Stone", "Pantograph", "PreservedInsect", "PureWater", "Red Mask", "Ring of the Serpent",
            "Ring of the Snake", "Runic Capacitor", "SlaversCollar", "Sling", "Symbiotic Virus", "TeardropLocket",
            "Thread and Needle", "Vajra", "Astrolabe", "Black Star", "Calling Bell", "Cauldron", "CultistMask",
            "DollysMirror", "Dream Catcher", "Empty Cage", "Eternal Feather", "Frozen Egg 2", "Golden Idol",
            "Juzu Bracelet", "Lee's Waffle", "Mango", "Matryoshka", "MawBank", "MealTicket", "Membership Card",
            "Molten Egg 2", "Nloth's Gift", "NlothsMask", "Old Coin", "Orrery", "Pandora's Box", "Peace Pipe", "Pear",
            "Potion Belt", "Prayer Wheel", "PrismaticShard", "Question Card", "Regal Pillow", "SsserpentHead", "Shovel",
            "Singing Bowl", "Smiling Mask", "Spirit Poop", "Strawberry", "The Courier", "Tiny Chest", "Tiny House",
            "Toxic Egg 2", "War Paint", "Whetstone", "White Beast Statue", "WingedGreaves", "Circlet", "Red Circlet",
            "INVALID"]
relicTiers = [RelicTier.COMMON, RelicTier.COMMON, RelicTier.RARE, RelicTier.SPECIAL, RelicTier.UNCOMMON,
              RelicTier.SHOP, RelicTier.RARE, RelicTier.RARE, RelicTier.COMMON, RelicTier.COMMON, RelicTier.RARE,
              RelicTier.RARE, RelicTier.SHOP, RelicTier.RARE, RelicTier.UNCOMMON, RelicTier.RARE, RelicTier.UNCOMMON,
              RelicTier.BOSS, RelicTier.RARE, RelicTier.BOSS, RelicTier.SHOP, RelicTier.RARE, RelicTier.RARE,
              RelicTier.RARE, RelicTier.UNCOMMON, RelicTier.SHOP, RelicTier.COMMON, RelicTier.UNCOMMON, RelicTier.BOSS,
              RelicTier.RARE, RelicTier.RARE, RelicTier.UNCOMMON, RelicTier.BOSS, RelicTier.UNCOMMON,
              RelicTier.UNCOMMON, RelicTier.RARE, RelicTier.RARE, RelicTier.SPECIAL, RelicTier.SHOP, RelicTier.SHOP,
              RelicTier.UNCOMMON, RelicTier.UNCOMMON, RelicTier.SPECIAL, RelicTier.SPECIAL, RelicTier.COMMON,
              RelicTier.SPECIAL, RelicTier.COMMON, RelicTier.SHOP, RelicTier.COMMON, RelicTier.UNCOMMON,
              RelicTier.UNCOMMON, RelicTier.UNCOMMON, RelicTier.COMMON, RelicTier.BOSS, RelicTier.RARE,
              RelicTier.COMMON, RelicTier.BOSS, RelicTier.BOSS, RelicTier.BOSS, RelicTier.BOSS, RelicTier.UNCOMMON,
              RelicTier.UNCOMMON, RelicTier.BOSS, RelicTier.COMMON, RelicTier.BOSS, RelicTier.RARE, RelicTier.SHOP,
              RelicTier.UNCOMMON, RelicTier.UNCOMMON, RelicTier.SHOP, RelicTier.COMMON, RelicTier.RARE, RelicTier.RARE,
              RelicTier.SHOP, RelicTier.RARE, RelicTier.RARE, RelicTier.COMMON, RelicTier.RARE, RelicTier.RARE,
              RelicTier.SHOP, RelicTier.RARE, RelicTier.BOSS, RelicTier.BOSS, RelicTier.SPECIAL, RelicTier.BOSS,
              RelicTier.BOSS, RelicTier.STARTER, RelicTier.UNCOMMON, RelicTier.SPECIAL, RelicTier.COMMON,
              RelicTier.COMMON, RelicTier.COMMON, RelicTier.COMMON, RelicTier.COMMON, RelicTier.UNCOMMON,
              RelicTier.UNCOMMON, RelicTier.UNCOMMON, RelicTier.COMMON, RelicTier.BOSS, RelicTier.SHOP, RelicTier.BOSS,
              RelicTier.STARTER, RelicTier.BOSS, RelicTier.COMMON, RelicTier.COMMON, RelicTier.RARE, RelicTier.SPECIAL,
              RelicTier.RARE, RelicTier.BOSS, RelicTier.RARE, RelicTier.UNCOMMON, RelicTier.SPECIAL, RelicTier.BOSS,
              RelicTier.COMMON, RelicTier.BOSS, RelicTier.SPECIAL, RelicTier.SPECIAL, RelicTier.UNCOMMON,
              RelicTier.BOSS, RelicTier.COMMON, RelicTier.UNCOMMON, RelicTier.COMMON, RelicTier.STARTER,
              RelicTier.SPECIAL, RelicTier.BOSS, RelicTier.STARTER, RelicTier.SHOP, RelicTier.BOSS, RelicTier.SHOP,
              RelicTier.UNCOMMON, RelicTier.UNCOMMON, RelicTier.RARE, RelicTier.COMMON, RelicTier.BOSS, RelicTier.BOSS,
              RelicTier.BOSS, RelicTier.SHOP, RelicTier.SPECIAL, RelicTier.SHOP, RelicTier.COMMON, RelicTier.BOSS,
              RelicTier.UNCOMMON, RelicTier.UNCOMMON, RelicTier.SPECIAL, RelicTier.COMMON, RelicTier.SHOP,
              RelicTier.RARE, RelicTier.UNCOMMON, RelicTier.COMMON, RelicTier.COMMON, RelicTier.SHOP,
              RelicTier.UNCOMMON, RelicTier.SPECIAL, RelicTier.SPECIAL, RelicTier.RARE, RelicTier.SHOP, RelicTier.BOSS,
              RelicTier.RARE, RelicTier.UNCOMMON, RelicTier.COMMON, RelicTier.RARE, RelicTier.SHOP, RelicTier.UNCOMMON,
              RelicTier.COMMON, RelicTier.SPECIAL, RelicTier.RARE, RelicTier.UNCOMMON, RelicTier.COMMON,
              RelicTier.SPECIAL, RelicTier.COMMON, RelicTier.UNCOMMON, RelicTier.COMMON, RelicTier.BOSS,
              RelicTier.UNCOMMON, RelicTier.COMMON, RelicTier.COMMON, RelicTier.UNCOMMON, RelicTier.RARE,
              RelicTier.SPECIAL, RelicTier.SPECIAL, RelicTier.INVALID]

# COMMON, UNCOMMON, RARE, BOSS, SHOP, STARTER, SPECIAL
RELICTIERPRICES = [150, 250, 300, 999, 150, 300, 400]


def getRelicName(id):
    return relicNames[int(id)]


def getRelicTier(id):
    return relicTiers[int(id)]


def getRelicBasePrice(id):
    return RELICTIERPRICES[int(getRelicTier(id))]


def isEggRelic(id):
    return id == RelicId.MOLTEN_EGG or id == RelicId.FROZEN_EGG or id == RelicId.TOXIC_EGG
