from ..constants.Cards import *

class Card:

    def __init__(self, id=None, upgraded=None):
        self.upgraded = False
        self.id = CardId.INVALID
        if id is not None:
            self.id = CardId(id)
            if upgraded is not None:
                self.upgraded = upgraded != 0

        self.misc = 0

    def upgrade(self):
        self.upgraded = True
        if self.id == CardId.SEARING_BLOW:
            self.misc += 1

    def getId(self):
        return self.id

    def getUpgraded(self):
        if self.id == CardId.SEARING_BLOW:
            return self.misc
        else:
            return 1 if self.upgraded else 0

    def isUpgraded(self):
        return self.upgraded

    def isInnate(self):
        return isCardInnate(self.id, self.upgraded)

    def getName(self):
        return getCardName(self.id)

    def getType(self):
        return getCardType(self.id)

    def getRarity(self):
        return getCardRarity(self.id)

    def getBaseDamage(self):
        return cardBaseDamage[1 if self.upgraded else 0][self.id]

    def canUpgrade(self):
        if self.getType() == CardType.ATTACK:
            return (not self.upgraded) or self.getId() == CardId.SEARING_BLOW
        elif (self.getType() == CardType.SKILL) or (self.getType() == CardType.POWER):
            return not self.upgraded

        if self.getType() != CardType.ATTACK and self.getType() != CardType.SKILL and self.getType() != CardType.POWER:
            return False

    def canTransform(self):
        transformable = not (
                self.id == CardId.ASCENDERS_BANE or self.id == CardId.NECRONOMICURSE or self.id == CardId.CURSE_OF_THE_BELL)
        return transformable

    def isStrikeCard(self):
        return isCardStrikeCard(self.id)

    def isStarterStrikeOrDefend(self):
        return isStarterStrikeOrDefend(self.id)

    def isStarterStrike(self):

        return CardId.STRIKE_BLUE <= self.id <= CardId.STRIKE_RED

    def __eq__(self, rhs):
        return self.id == rhs.id and self.misc == rhs.misc and self.upgraded == rhs.upgraded

    def __ne__(self, rhs):
        return not rhs.equals_to(self)

