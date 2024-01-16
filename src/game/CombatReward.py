#
# Created by gamerpuppy on 7/7/2021.
#




from sts import *

def addGold(goldAmt):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: gold[goldRewardCount++] = goldAmt;
    gold[goldRewardCount] = goldAmt
    goldRewardCount += 1

def addRelic(relic):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: relics[relicCount++] = relic;
    relics[relicCount] = relic
    relicCount += 1

def addPotion(potion):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: potions[potionCount++] = potion;
    potions[potionCount] = potion
    potionCount += 1

def addCardReward(reward):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: cardRewards[cardRewardCount++] = reward;
    cardRewards[cardRewardCount] = reward
    cardRewardCount += 1

def removeGoldReward(idx):
    if idx == 0 and goldRewardCount == 2:
        gold[0] = gold[1]
    goldRewardCount -= 1

def removeCardReward(removeIdx):
    i = removeIdx
    while i < cardRewardCount:
        cardRewards[i] = cardRewards[i+1]
        i += 1
    cardRewardCount -= 1

def removeRelicReward(removeIdx):
    i = removeIdx
    while i < relicCount-1:
        relics[i] = relics[i+1]
        i += 1
    relicCount -= 1

def removePotionReward(idx):
    while idx + 1 < potionCount:
        potions[idx] = potions[idx+1]
        idx += 1
    potionCount -= 1

def clear():
    goldRewardCount = 0
    cardRewardCount = 0
    relicCount = 0
    potionCount = 0
    emeraldKey = False
    sapphireKey = False

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int Rewards::getTotalCount() const
def getTotalCount():
    return goldRewardCount + potionCount + cardRewardCount + (1 if sapphireKey else 0) + (1 if emeraldKey else 0)

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: str Rewards::toString() const
def toString():
    ss = std::stringstream()
    ss << "Rewards { \n"
    i = 0
    while i < cardRewardCount:
        ss << '\t'
        writeCardReward(ss, cardRewards[i])
        ss << '\n'
        i += 1

    i = 0
    while i < goldRewardCount:
        ss << '\t'
        g = gold[i]
        ss << str(g) << "g" << '\n'
        i += 1

    i = 0
    while i < potionCount:
        ss << '\t'
        p = potions[i]
        ss << potionNames[int(p)] << '\n'
        i += 1

    i = 0
    while i < relicCount:
        ss << '\t'
        r = relics[i]
        ss << relicNames[int(r)] << '\n'
        i += 1

    if emeraldKey:
        ss << "emerald key\n"
    if sapphireKey:
        ss << "sapphire key\n"

    ss << "}\n"

    return ss.str()

def __init__(p, count):
    for i in range(0, count):
        addPotion(p[i])

def __init__(relic):
    addRelic(relic)


def __init__(reward):
    addCardReward(reward)


