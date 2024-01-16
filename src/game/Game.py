from sts import *

import math

#
# Created by gamerpuppy on 6/24/2021.
#


#
# Created by gamerpuppy on 7/3/2021.
#





class sts: #this class replaces the original namespace 'sts'

    COLORLESS_RARE_CHANCE = 0.30

    class SeedHelper: #this class replaces the original namespace 'SeedHelper'
        SEED_BASE = 35

        @staticmethod
        def getDigitValue(c):
            if c < 'A':
                return c - '0'
            if c < 'O':
                return c - 'A' + 10
            return c - 'A' + 9

        @staticmethod
        def getString(seed):
            CHARS = "0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"

            uSeed = seed
            str = ""

            loop_condition = True
            while loop_condition:
                rem = int((math.fmod(uSeed, sts.SeedHelper.SEED_BASE)))
                uSeed /= sts.SeedHelper.SEED_BASE
                str += CHARS[rem]
                loop_condition = uSeed != 0

            i = 0
# C++ TO PYTHON CONVERTER TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            while i < len(str) / 2:
                std::swap(str[i], str[len(str) - 1 - i])
                i += 1
            return str

        @staticmethod
        def getLong(seed):
            ret = 0
            it = seed.begin()
            while it is not seed.end():
                ret *= ulong(sts.SeedHelper.SEED_BASE)
                c = toupper(*it)
                value = getDigitValue(c)
                ret += ulong(value)
                it += 1
            return ret

    @staticmethod
    def getAnyColorCard(cardRng, rarity):
        if rarity == sts.CardRarity.COMMON:
                cardRng.randomLong()
                idx = cardRng.random(int((sts.AnyColorTypeCardPool.COMMONPOOLSIZE-1)))
                return sts.AnyColorTypeCardPool.COMMONCARDS[idx]

        elif rarity == sts.CardRarity.UNCOMMON:
                cardRng.randomLong()
                idx = cardRng.random(int((sts.AnyColorTypeCardPool.UNCOMMONPOOLSIZE-1)))
                return sts.AnyColorTypeCardPool.UNCOMMONCARDS[idx]

        elif rarity == sts.CardRarity.RARE:
                cardRng.randomLong()
                idx = cardRng.random(int((sts.AnyColorTypeCardPool.RAREPOOLSIZE-1)))
                return sts.AnyColorTypeCardPool.RARECARDS[idx]

        else:
            return sts.CardId.INVALID

    @staticmethod
    def getRandomClassCardOfTypeAndRarity(cardRng, cc, type, rarity):
        size = sts.TypeRarityCardPool.getPoolSize(cc, type, rarity)
        idx = cardRng.random(size-1)
        return sts.TypeRarityCardPool.getCardFromPool(cc, type, rarity, idx)

    @staticmethod
    def getRandomClassCardOfRarity(rng, cc, rarity):
        groupSize = sts.RarityCardPool.getPoolSize(cc, rarity)
        idx = rng.random(groupSize-1)
        return RarityCardPool.getCardFromPool(cc, rarity, idx)

    @staticmethod
    def getRandomColorlessCardNeow(rng, rarity):
        size = sts.ColorlessRarityCardPool.getGroupSize(rarity)
        idx = rng.random(size-1)
        return sts.ColorlessRarityCardPool.getCardAt(rarity, idx)

    @staticmethod
    def getColorlessCardFromPool(cardRng, rarity):
        idx = cardRng.random(sts.ColorlessRarityCardPool.getGroupSize(rarity) - 1)
        return sts.ColorlessRarityCardPool.getCardAt(rarity, idx)

    @staticmethod
    def getRandomCurse(cardRng):
        idx = cardRng.random(sts.CURSECARDPOOLSIZE-1)
        return sts.CURSECARDPOOL[idx]

    @staticmethod
    def getRandomCurse(rng, exclude):
        idx = rng.random(sts.CURSECARDPOOLSIZE-2)
        if sts.CURSECARDPOOL[idx] == exclude:
            return sts.CURSECARDPOOL[idx+1]
        else:
            return sts.CURSECARDPOOL[idx]

    @staticmethod
    def getTrulyRandomCard(cardRandomRng, cc):
        idx = cardRandomRng.random(sts.TrulyRandomCardPool.getPoolSizeForClass(cc)-1)
        return sts.TrulyRandomCardPool.getPoolForClass(cc)[idx]

    @staticmethod
    def returnTrulyRandomColorlessCardFromAvailable(rng, exclude):
        idx = rng.random(sts.SRCCOLORLESSCARDPOOLSIZE-2)
        if sts.SRCCOLORLESSCARDPOOL[idx] == exclude:
            return sts.SRCCOLORLESSCARDPOOL[idx + 1]
        else:
            return sts.SRCCOLORLESSCARDPOOL[idx]

    @staticmethod
    def getTrulyRandomColorlessCardInCombat(cardRandomRng):
        poolSize = sts.CombatColorlessCardPool.getPoolSize()
        idx = cardRandomRng.random(poolSize-1)
        return sts.CombatColorlessCardPool.getCardAt(auto(idx))

    @staticmethod
    def getTrulyRandomCardInCombat(cardRandomRng, cc):
        poolSize = sts.CombatCardPool.getPoolSize(cc)
        idx = cardRandomRng.random(poolSize-1)
        return sts.CombatCardPool.getCardAt(cc, auto(idx))

    @staticmethod
    def getTrulyRandomCardInCombat(cardRandomRng, cc, type):
        poolSize = sts.CombatTypeCardPool.getPoolSize(cc, type)
        idx = cardRandomRng.random(poolSize-1)
        return sts.CombatTypeCardPool.getCardAt(cc, type, auto(idx))

    # using hacky arguments: status = colorless cards, invalid = any type

    @staticmethod
    def generateDiscoveryCards(cardRandomRng, cc, type):
        cardCount = 0
        cards = [None for _ in range(3)]

        while cardCount < 3:
            id = 0
            if type == sts.CardType.INVALID:
                id = getTrulyRandomCardInCombat(cardRandomRng, cc)

            elif type == sts.CardType.STATUS:
                id = getTrulyRandomColorlessCardInCombat(cardRandomRng)

            else:
                id = getTrulyRandomCardInCombat(cardRandomRng, cc, type)


            haveDuplicate = False
            for i in range(0, cardCount):
                if cards[i] == id:
                    haveDuplicate = True
                    break

            if not haveDuplicate:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: cards[cardCount++] = id;
                cards[cardCount] = id
                cardCount += 1

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
        for x in cards:
            if x == sts.CardId.INVALID:
                False = assert()
##endif
        return list(cards)

    @staticmethod
    def returnRandomRelicTier(relicRng, act):
        commonChance = 0 if act == 4 else 50
        uncommonChance = 100 if act == 4 else 33

        roll = relicRng.random(0,99)
        if roll < commonChance:
            return sts.RelicTier.COMMON
        elif roll < uncommonChance+commonChance:
            return sts.RelicTier.UNCOMMON
        else:
            return sts.RelicTier.RARE


    @staticmethod
    def returnRandomRelicTierElite(relicRng):
        roll = relicRng.random(99)
        if roll < 50:
            return sts.RelicTier.COMMON
        elif roll > 82:
            return sts.RelicTier.RARE
        else:
            return sts.RelicTier.UNCOMMON

    @staticmethod
    def returnRandomPotion(potionRng, cc, limited = False):
        rarity = 0

        roll = potionRng.random(0,99)
        if roll < 65:
            rarity = sts.PotionRarity.COMMON
        elif roll < 90:
            rarity = sts.PotionRarity.UNCOMMON
        else:
            rarity = sts.PotionRarity.RARE

        return returnRandomPotionOfRarity(potionRng, rarity, cc, limited)

    @staticmethod
    def returnRandomPotionOfRarity(potionRng, rarity, cc, limited = False):
        # this is dumb.
        temp = getRandomPotion(potionRng, cc)
        spamCheck = limited
        while sts.POTIONRARITIES[int(temp)] != rarity or spamCheck:
            spamCheck = limited
            temp = getRandomPotion(potionRng, cc)
            if temp != sts.Potion.FRUIT_JUICE:
                spamCheck = False
        return temp

    @staticmethod
    def getRandomPotion(potionRng, cc):
        idx = potionRng.random(sts.PotionPool.POOLSIZE-1) # all characters have 33 possible potions
        return sts.PotionPool.getPotionForClass(cc, idx)

    @staticmethod
    def getRandomFace(relics, miscRng):
        tmpList = fixed_list()

        if not relics.has(sts.RelicId.CULTIST_HEADPIECE):
            tmpList.push_back(sts.RelicId.CULTIST_HEADPIECE)

        if not relics.has(sts.RelicId.FACE_OF_CLERIC):
            tmpList.push_back(sts.RelicId.FACE_OF_CLERIC)

        if not relics.has(sts.RelicId.GREMLIN_VISAGE):
            tmpList.push_back(sts.RelicId.GREMLIN_VISAGE)

        if not relics.has(sts.RelicId.NLOTHS_HUNGRY_FACE):
            tmpList.push_back(sts.RelicId.NLOTHS_HUNGRY_FACE)

        if not relics.has(sts.RelicId.SSSERPENT_HEAD):
            tmpList.push_back(sts.RelicId.SSSERPENT_HEAD)

        if tmpList.empty():
            tmpList.push_back(sts.RelicId.CIRCLET)

        java.Collections.shuffle(tmpList.begin(), tmpList.end(), java.Random(miscRng.randomLong()))
        return tmpList.get(0)

    @staticmethod
    def getStartCardForEvent(cc):
        cards = [(int)sts.CardId.BASH, sts.CardId.NEUTRALIZE, sts.CardId.ZAP, (int)sts.CardId.ERUPTION]
        return cards[int(cc)]

    @staticmethod
    def getRandomChestSize(treasureRng):
        roll = treasureRng.random(99)
        if roll < sts.SMALL_CHEST_CHANCE:
            return sts.ChestSize.SMALL

        elif roll < sts.SMALL_CHEST_CHANCE + sts.MEDIUM_CHEST_CHANCE:
            return sts.ChestSize.MEDIUM

        else:
            return sts.ChestSize.LARGE

    @staticmethod
    def getMatryoshkaRelicTier(relicRng):
        if relicRng.randomBoolean(0.75):
            return sts.RelicTier.COMMON
        else:
            return sts.RelicTier.UNCOMMON

    @staticmethod
    def getUpgradedCardChance(act, ascension):
        if act < 2:
            return 0.0
        elif act == 2:
            if ascension < 12:
                return 0.25
            else:
                return 0.125
        else:
            if ascension < 12:
                return 0.50
            else:
                return 0.25


def add(r):
    setHasRelic(r.id, True)
    relics.push_back(r)

def remove(r):
    setHasRelic(r, False)
    it = relics.begin()
    while it is not relics.end():
        if it.id == r:
            relics.erase(it)
            break
        it += 1

def replaceRelic(o, r):
    setHasRelic(o, False)
    setHasRelic(r, True)
    for relic in relics:
        if relic.id == r:
            relic.id = r
            break

def setHasRelic(r, value):
    rIdx = int(r)
    if value:
        if rIdx < 64:
            relicBits0 |= 1 << rIdx
        elif rIdx < 128:
            relicBits1 |= 1 << (rIdx-64)
        else:
            relicBits2 |= 1 << (rIdx-128)
    else:
        if rIdx < 64:
            relicBits0 &= ~(1 << rIdx)
        elif rIdx < 128:
            relicBits1 &= ~(1 << (rIdx-64))
        else:
            relicBits2 &= ~(1 << (rIdx-128))

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int RelicContainer::size() const
def size():
    return int(relics.size())

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool RelicContainer::has(RelicId r) const
def has(r):
    rIdx = int(r)
    if rIdx < 64:
        return (relicBits0 & (1 << rIdx)) != 0
    elif rIdx < 128:
        return (relicBits1 & (1 << (rIdx-64))) != 0
    else:
        return (relicBits2 & (1 << (rIdx-128))) != 0

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int RelicContainer::getRelicValue(RelicId r) const
def getRelicValue(r):
    for x in relics:
        if x.id == r:
            return x.data
    return -1

def getRelicValueRef(r):
    for x in relics:
        if x.id == r:
            return x.data
    return relics[0].data
