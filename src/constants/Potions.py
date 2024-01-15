from enum import Enum



class Potion(Enum):
    INVALID = 0
    EMPTY_POTION_SLOT = 1
    AMBROSIA = 2
    ANCIENT_POTION = 3

    ATTACK_POTION = 4
    BLESSING_OF_THE_FORGE = 5
    BLOCK_POTION = 6
    BLOOD_POTION = 7

    BOTTLED_MIRACLE = 8
    COLORLESS_POTION = 9
    CULTIST_POTION = 10
    CUNNING_POTION = 11

    DEXTERITY_POTION = 12
    DISTILLED_CHAOS = 13
    DUPLICATION_POTION = 14
    ELIXIR_POTION = 15

    ENERGY_POTION = 16
    ENTROPIC_BREW = 17
    ESSENCE_OF_DARKNESS = 18
    ESSENCE_OF_STEEL = 19

    EXPLOSIVE_POTION = 20
    FAIRY_POTION = 21
    FEAR_POTION = 22
    FIRE_POTION = 23

    FLEX_POTION = 24  # called SteroidPotion in game code
    FOCUS_POTION = 25
    FRUIT_JUICE = 26
    GAMBLERS_BREW = 27

    GHOST_IN_A_JAR = 28
    HEART_OF_IRON = 29
    LIQUID_BRONZE = 30
    LIQUID_MEMORIES = 31

    POISON_POTION = 32
    POTION_OF_CAPACITY = 33
    POWER_POTION = 34
    REGEN_POTION = 35

    SKILL_POTION = 36
    SMOKE_BOMB = 37
    SNECKO_OIL = 38
    SPEED_POTION = 39

    STANCE_POTION = 40
    STRENGTH_POTION = 41
    SWIFT_POTION = 42
    WEAK_POTION = 43


potionNames = ["INVALID", "EMPTY_POTION_SLOT", "Ambrosia", "Ancient Potion", "Attack Potion", "Blessing Of The Forge",
               "Block Potion", "Blood Potion", "Bottled Miracle", "Colorless Potion", "Cultist Potion",
               "Cunning Potion", "Dexterity Potion", "Distilled Chaos", "Duplication Potion", "Elixir Potion",
               "Energy Potion", "Entropic Brew", "Essence Of Darkness", "Essence Of Steel", "Explosive Potion",
               "Fairy Potion", "Fear Potion", "Fire Potion", "Flex Potion", "Focus Potion", "Fruit Juice",
               "Gamblers Brew", "Ghost In A Jar", "Heart Of Iron", "Liquid Bronze", "Liquid Memories", "Poison Potion",
               "Potion Of Capacity", "Power Potion", "Regen Potion", "Skill Potion", "Smoke Bomb", "Snecko Oil",
               "Speed Potion", "Stance Potion", "Strength Potion", "Swift Potion", "Weak Potion"]

potionIds = ["INVALID_ID", "EMPTY_POTION_ID", "Ambrosia", "Ancient Potion", "AttackPotion", "BlessingOfTheForge",
             "Block Potion", "BloodPotion", "BottledMiracle", "ColorlessPotion", "CultistPotion", "CunningPotion",
             "Dexterity Potion", "DistilledChaos", "DuplicationPotion", "ElixirPotion", "Energy Potion", "EntropicBrew",
             "EssenceOfDarkness", "EssenceOfSteel", "Explosive Potion", "FairyPotion", "FearPotion", "Fire Potion",
             "SteroidPotion", "FocusPotion", "Fruit Juice", "GamblersBrew", "GhostInAJar", "HeartOfIron",
             "LiquidBronze", "LiquidMemories", "Poison Potion", "PotionOfCapacity", "PowerPotion", "Regen Potion",
             "SkillPotion", "SmokeBomb", "SneckoOil", "SpeedPotion", "StancePotion", "Strength Potion", "Swift Potion",
             "Weak Potion"]

POTIONENUMNAMES = ["INVALID", "EMPTY_POTION_SLOT", "AMBROSIA", "ANCIENT_POTION", "ATTACK_POTION",
                   "BLESSING_OF_THE_FORGE", "BLOCK_POTION", "BLOOD_POTION", "BOTTLED_MIRACLE", "COLORLESS_POTION",
                   "CULTIST_POTION", "CUNNING_POTION", "DEXTERITY_POTION", "DISTILLED_CHAOS", "DUPLICATION_POTION",
                   "ELIXIR_POTION", "ENERGY_POTION", "ENTROPIC_BREW", "ESSENCE_OF_DARKNESS", "ESSENCE_OF_STEEL",
                   "EXPLOSIVE_POTION", "FAIRY_POTION", "FEAR_POTION", "FIRE_POTION", "FLEX_POTION", "FOCUS_POTION",
                   "FRUIT_JUICE", "GAMBLERS_BREW", "GHOST_IN_A_JAR", "HEART_OF_IRON", "LIQUID_BRONZE",
                   "LIQUID_MEMORIES", "POISON_POTION", "POTION_OF_CAPACITY", "POWER_POTION", "REGEN_POTION",
                   "SKILL_POTION", "SMOKE_BOMB", "SNECKO_OIL", "SPEED_POTION", "STANCE_POTION", "STRENGTH_POTION",
                   "SWIFT_POTION", "WEAK_POTION"]


class PotionRarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    PLACEHOLDER = 3


POTIONRARITIES = [PotionRarity.PLACEHOLDER, PotionRarity.PLACEHOLDER, PotionRarity.RARE, PotionRarity.UNCOMMON,
                  PotionRarity.COMMON, PotionRarity.COMMON, PotionRarity.COMMON, PotionRarity.COMMON,
                  PotionRarity.COMMON, PotionRarity.COMMON, PotionRarity.RARE, PotionRarity.UNCOMMON,
                  PotionRarity.COMMON, PotionRarity.UNCOMMON, PotionRarity.UNCOMMON, PotionRarity.UNCOMMON,
                  PotionRarity.COMMON, PotionRarity.RARE, PotionRarity.RARE, PotionRarity.UNCOMMON, PotionRarity.COMMON,
                  PotionRarity.RARE, PotionRarity.COMMON, PotionRarity.COMMON, PotionRarity.COMMON, PotionRarity.COMMON,
                  PotionRarity.RARE, PotionRarity.UNCOMMON, PotionRarity.RARE, PotionRarity.RARE, PotionRarity.UNCOMMON,
                  PotionRarity.UNCOMMON, PotionRarity.COMMON, PotionRarity.UNCOMMON, PotionRarity.COMMON,
                  PotionRarity.UNCOMMON, PotionRarity.COMMON, PotionRarity.RARE, PotionRarity.RARE, PotionRarity.COMMON,
                  PotionRarity.UNCOMMON, PotionRarity.COMMON, PotionRarity.COMMON, PotionRarity.COMMON]

# common, uncommon, rare
potionRarityPrices = [50, 75, 100]


class PotionPool:  # this class replaces the original namespace 'PotionPool'

    potionPool = [
        [Potion.BLOOD_POTION, Potion.ELIXIR_POTION, Potion.HEART_OF_IRON, Potion.BLOCK_POTION, Potion.DEXTERITY_POTION,
         Potion.ENERGY_POTION, Potion.EXPLOSIVE_POTION, Potion.FIRE_POTION, Potion.STRENGTH_POTION, Potion.SWIFT_POTION,
         Potion.WEAK_POTION, Potion.FEAR_POTION, Potion.ATTACK_POTION, Potion.SKILL_POTION, Potion.POWER_POTION,
         Potion.COLORLESS_POTION, Potion.FLEX_POTION, Potion.SPEED_POTION, Potion.BLESSING_OF_THE_FORGE,
         Potion.REGEN_POTION, Potion.ANCIENT_POTION, Potion.LIQUID_BRONZE, Potion.GAMBLERS_BREW,
         Potion.ESSENCE_OF_STEEL, Potion.DUPLICATION_POTION, Potion.DISTILLED_CHAOS, Potion.LIQUID_MEMORIES,
         Potion.CULTIST_POTION, Potion.FRUIT_JUICE, Potion.SNECKO_OIL, Potion.FAIRY_POTION, Potion.SMOKE_BOMB,
         Potion.ENTROPIC_BREW],
        [Potion.POISON_POTION, Potion.CUNNING_POTION, Potion.GHOST_IN_A_JAR, Potion.BLOCK_POTION,
         Potion.DEXTERITY_POTION, Potion.ENERGY_POTION, Potion.EXPLOSIVE_POTION, Potion.FIRE_POTION,
         Potion.STRENGTH_POTION, Potion.SWIFT_POTION, Potion.WEAK_POTION, Potion.FEAR_POTION, Potion.ATTACK_POTION,
         Potion.SKILL_POTION, Potion.POWER_POTION, Potion.COLORLESS_POTION, Potion.FLEX_POTION, Potion.SPEED_POTION,
         Potion.BLESSING_OF_THE_FORGE, Potion.REGEN_POTION, Potion.ANCIENT_POTION, Potion.LIQUID_BRONZE,
         Potion.GAMBLERS_BREW, Potion.ESSENCE_OF_STEEL, Potion.DUPLICATION_POTION, Potion.DISTILLED_CHAOS,
         Potion.LIQUID_MEMORIES, Potion.CULTIST_POTION, Potion.FRUIT_JUICE, Potion.SNECKO_OIL, Potion.FAIRY_POTION,
         Potion.SMOKE_BOMB, Potion.ENTROPIC_BREW],
        [Potion.FOCUS_POTION, Potion.POTION_OF_CAPACITY, Potion.ESSENCE_OF_DARKNESS, Potion.BLOCK_POTION,
         Potion.DEXTERITY_POTION, Potion.ENERGY_POTION, Potion.EXPLOSIVE_POTION, Potion.FIRE_POTION,
         Potion.STRENGTH_POTION, Potion.SWIFT_POTION, Potion.WEAK_POTION, Potion.FEAR_POTION, Potion.ATTACK_POTION,
         Potion.SKILL_POTION, Potion.POWER_POTION, Potion.COLORLESS_POTION, Potion.FLEX_POTION, Potion.SPEED_POTION,
         Potion.BLESSING_OF_THE_FORGE, Potion.REGEN_POTION, Potion.ANCIENT_POTION, Potion.LIQUID_BRONZE,
         Potion.GAMBLERS_BREW, Potion.ESSENCE_OF_STEEL, Potion.DUPLICATION_POTION, Potion.DISTILLED_CHAOS,
         Potion.LIQUID_MEMORIES, Potion.CULTIST_POTION, Potion.FRUIT_JUICE, Potion.SNECKO_OIL, Potion.FAIRY_POTION,
         Potion.SMOKE_BOMB, Potion.ENTROPIC_BREW],
        [Potion.BOTTLED_MIRACLE, Potion.STANCE_POTION, Potion.AMBROSIA, Potion.BLOCK_POTION, Potion.DEXTERITY_POTION,
         Potion.ENERGY_POTION, Potion.EXPLOSIVE_POTION, Potion.FIRE_POTION, Potion.STRENGTH_POTION, Potion.SWIFT_POTION,
         Potion.WEAK_POTION, Potion.FEAR_POTION, Potion.ATTACK_POTION, Potion.SKILL_POTION, Potion.POWER_POTION,
         Potion.COLORLESS_POTION, Potion.FLEX_POTION, Potion.SPEED_POTION, Potion.BLESSING_OF_THE_FORGE,
         Potion.REGEN_POTION, Potion.ANCIENT_POTION, Potion.LIQUID_BRONZE, Potion.GAMBLERS_BREW,
         Potion.ESSENCE_OF_STEEL, Potion.DUPLICATION_POTION, Potion.DISTILLED_CHAOS, Potion.LIQUID_MEMORIES,
         Potion.CULTIST_POTION, Potion.FRUIT_JUICE, Potion.SNECKO_OIL, Potion.FAIRY_POTION, Potion.SMOKE_BOMB,
         Potion.ENTROPIC_BREW]]

    POOLSIZE = 33

    def getPotionForClass(cc, idx):
        return PotionPool.potionPool[int(cc)][idx]



def getPotionName(p):
    return potionNames[int(p)]



def getPotionRarity(p):
    return POTIONRARITIES[int(p)]



def getPotionBaseCost(p):
    return potionRarityPrices[int(getPotionRarity(p))]



def potionRequiresTarget(p):
    if (p == Potion.FEAR_POTION) or (p == Potion.FIRE_POTION) or (p == Potion.POISON_POTION) or (
            p == Potion.WEAK_POTION):
        return True

    else:
        return False
