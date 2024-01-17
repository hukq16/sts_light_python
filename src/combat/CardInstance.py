from ..constants.Cards import *
from ..game.Card import Card


class CardInstance:

    # todo dont need all of these, also put in bitset

    def __init__(self, id: CardId = None, upgraded=False, card: Card = None):
        self.id = CardId.INVALID
        self.uniqueId = -1
        self.specialData = 0
        self.cost = 0
        self.costForTurn = 0
        self.upgraded = False
        self.freeToPlayOnce = False
        self.retain = False

        if id is not None:
            self.id = id
            self.upgraded = upgraded
            self.cost = getEnergyCost(id, upgraded)
            self.costForTurn = self.cost
        elif card is not None:
            self.id = card.id
            self.upgraded = card.upgraded
            if self.id == CardId.SEARING_BLOW:
                self.specialData = card.getUpgraded()
            else:
                self.specialData = card.misc

    def getId(self):
        return self.id

    def getType(self):
        return getCardType(self.id)

    def getName(self):
        if self.upgraded:
            pass
        return getCardName(self.id)

    def getUniqueId(self):
        return self.uniqueId

    def isUpgraded(self):
        return self.upgraded

    def getUpgradeCount(self):
        if self.id == CardId.SEARING_BLOW:
            return self.specialData
        else:
            return 1 if self.upgraded & 0x1 else 0

    def canUpgrade(self):
        return ((
                    not self.upgraded) or self.id == CardId.SEARING_BLOW) and self.getType() != CardType.CURSE and self.getType() != CardType.STATUS


    def isEthereal(self):
        return isCardEthereal(self.id, self.upgraded)

    def isStrikeCard(self):
        return isCardStrikeCard(self.id)


    def doesExhaust(self):
        return doesCardExhaust(self.id, self.upgraded)


    def hasSelfRetain(self):
        return doesCardSelfRetain(self.id, self.upgraded)


    def requiresTarget(self):
        return cardTargetsEnemy(self.id, self.isUpgraded())


    def isXCost(self):
        return isXCost(self.id)

    def isBloodCard(self):
        return self.getId() == CardId.BLOOD_FOR_BLOOD or self.getId() == CardId.MASTERFUL_STAB


    def usesSpecialData(self):
        if (self.getId() == CardId.SEARING_BLOW) or (self.getId() == CardId.RAMPAGE) or (
                self.getId() == CardId.GENETIC_ALGORITHM) or (self.getId() == CardId.RITUAL_DAGGER):
            return True

        else:
            return False

    def upgradeBaseCost(self, newBaseCost):
        diff = self.costForTurn - self.cost
        self.cost = newBaseCost
        if self.costForTurn > 0:
            self.costForTurn = max(0, self.cost + diff)

    def updateCost(self, amount):
        tmpCost = max(0, self.cost + amount)
        diff = self.cost - self.costForTurn

        if tmpCost != self.cost:
            self.cost = tmpCost
            self.costForTurn = max(0, self.cost - diff)


    def setCostForCombat(self, newCost):
        # todo should this set costForTurn to newCost? this isn't used exactly like this in game
        self.cost = newCost

    def setCostForTurn(self, newCost):

        if self.costForTurn >= 0:
            self.costForTurn = max(0, newCost)

    def setUniqueId(self, _uniqueId):
        self.uniqueId = _uniqueId

    def upgrade(self):

        # todo assert not upgraded here?
        # not sure where this is used

        if self.id == CardId.SEARING_BLOW:
            self.specialData += 1

        elif self.id == CardId.BLOOD_FOR_BLOOD:  # the game upgrades the cost to 3 if the cost is over 4 but would it ever be higher?
            if (not self.isUpgraded()) and self.cost < 4 and self.cost > 0:
                self.upgradeBaseCost(self.cost - 1)

        elif self.id == CardId.HAVOC:
            if not self.isUpgraded():
                self.upgradeBaseCost(0)

        elif (self.id == CardId.BLIND) or (self.id == CardId.TRIP):
            if not self.isUpgraded():
                # todo change card target here when caching of card info is implemented
                pass

        self.upgraded = True

    def tookDamage(self):
        if self.getId() == CardId.BLOOD_FOR_BLOOD:
            self.updateCost(-1)
        else:
            # masterful stab
            # todo check if it is above a limit
            self.updateCost(1)

    # C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
    # ORIGINAL LINE: std::ostream &printSimpleDesc(std::ostream &os) const
    def printSimpleDesc(self, os):
        print(self.getName())
        if (self.id == CardId.RITUAL_DAGGER) or (self.id == CardId.RAMPAGE):
            print("=")
            print(self.specialData)

        if self.upgraded:
            print("+")
            if self.id == CardId.SEARING_BLOW:
                print(self.upgraded)
        return os

    # def triggerOnExhaust(self, bc):
    #     if self.id == CardId.SENTINEL:
    #         bc.addToTop(Actions.GainEnergy(3 if self.upgraded else 2))
    #     elif self.id == CardId.CURSE_OF_THE_BELL:
    #         bc.addToBot(Actions.MakeTempCardInHand(CardId.CURSE_OF_THE_BELL))

    # def triggerOnManualDiscard(self, bc):
    #     if self.id == CardId.REFLEX:
    #         bc.addToBot(Actions.DrawCards(3 if self.upgraded else 2))
    #     elif self.id == CardId.TACTICIAN:
    #         bc.addToTop(Actions.GainEnergy(2 if self.upgraded else 1))

    def triggerWhenDrawn(self, bc, myHandIdx):

        pass

    # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
    # ORIGINAL LINE: [[nodiscard]] bool isFreeToPlay(const BattleContext &bc) const

    # void CardInstance::triggerWhenDrawn(BattleContext &bc, int myHandIdx) {
    #    switch (id) {
    #        case CardId::ENDLESS_AGONY:
    #            //addToTop((AbstractGameAction)new MakeTempCardInHandAction(makeStatEquivalentCopy()));
    #            bc.addToTop(Actions::MakeTempCardInHand(id, upgraded) );
    #            break;
    #        case CardId::EVISCERATE:
    #            //setCostForTurn(this.cost - GameActionManager.totalDiscardedThisTurn);
    #            costForTurn = this->cost - bc.player.cardsDiscardedThisTurn;
    #            break;
    #
    #        case CardId::DEUS_EX_MACHINA:
    #            bc.addToTop(Actions::MakeTempCardInHand(CardId::MIRACLE, upgraded ? 3 : 2));
    #            bc.addToTop(Actions::ExhaustSpecificCardInHand(myHandIdx) );
    #            break;
    #
    #        case CardId::VOID:
    #            bc.addToBot( [](BattleContext &bc){ bc.player.energy = std::max(0, bc.player.energy-1); } );
    #            break;
    #
    #            // case CardId::DOUBT:
    #            // addToBot((AbstractGameAction)new SetDontTriggerAction(this, false));
    #        default:
    #            break;
    #    }
    # }

    # C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
    # ORIGINAL LINE: bool isFreeToPlay(const BattleContext &bc) const
    def isFreeToPlay(self, bc):
        return self.freeToPlayOnce or self.getType() == CardType.ATTACK and bc.player.hasStatus()

    # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
    # ORIGINAL LINE: [[nodiscard]] bool canUseOnAnyTarget(const BattleContext &bc) const; // not for use in critical path
    # C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
    # ORIGINAL LINE: bool canUseOnAnyTarget(const BattleContext &bc) const
    def canUseOnAnyTarget(self, bc):
        if self.requiresTarget():
            return self.canUse(bc, bc.monsters.getFirstTargetable(), False)
        else:
            return self.canUse(bc, 0, False)

    # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
    # ORIGINAL LINE: [[nodiscard]] bool canUse(const BattleContext &bc, int target, bool inAutoplay) const
    # C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
    # ORIGINAL LINE: bool canUse(const BattleContext &bc, int target, const bool inAutoplay) const
    def canUse(self, bc, target, inAutoplay):
        if self.requiresTarget() and (
                bc.monsters.areMonstersBasicallyDead() or (not bc.monsters.arr[target].isTargetable())):
            return False

        # this is handled elsewhere now
        #    if (purgeOnUse) {
        #        return true
        #    }

        # # todo grand finale, signature move, reflex, deus ex machina, tactician
        # if self.getType() == CardType.ATTACK:
        #     if bc.player.hasStatus():
        #         return False
        #     if self.getId() == CardId.CLASH and not Globals.canUseClash(bc):
        #         return False

        # elif self.getType() == CardType.SKILL:
        #     if self.id == CardId.SECRET_TECHNIQUE:
        #         const
        #         bool
        #         haveSkill = std::find_if(bc.cards.drawPile.begin(), bc.cards.drawPile.end(), lambda
        #             c: c.getType() == CardType.SKILL) is not bc.cards.drawPile.end();  # todo maybe speed up
        #         if not haveSkill:
        #             return False
        #     elif self.id == CardId.SECRET_WEAPON:
        #         const
        #         bool
        #         haveAttack = std::find_if(bc.cards.drawPile.begin(), bc.cards.drawPile.end(), lambda
        #             c: c.getType() == CardType.ATTACK) is not bc.cards.drawPile.end();  # todo maybe speed up
        #         if not haveAttack:
        #             return False

        elif self.getType() == CardType.CURSE:
            if not bc.player.hasRelic():
                return False

        elif self.getType() == CardType.STATUS:
            if (not bc.player.hasRelic()) and self.id != CardId.SLIMED:
                return False

        elif self.getType() == CardType.INVALID:
            return False

        if bc.player.energy < self.costForTurn and (not self.isFreeToPlay(bc)) and not inAutoplay:
            return False

        return True


def left_shift(self, os, c):
    os << "(" << c.getName() << ("+" if c.upgraded else "") << "," << str(c.uniqueId) << "," << int(
        c.cost) << "," << int(c.costForTurn)

    if c.usesSpecialData():
        os << ",s=" << int(c.specialData)
    if c.freeToPlayOnce:
        os << ",f"
    if c.retain:
        os << ",r"
    return os << ")"
