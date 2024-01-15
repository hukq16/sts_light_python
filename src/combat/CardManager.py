from sts import *

#
# Created by gamerpuppy on 7/24/2021.
#

#
# Created by gamerpuppy on 7/24/2021.
#





class sts: #this class replaces the original namespace 'sts'

# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class GameContext
# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class Card

    class CardManager:

        def __init__(self):
            # instance fields found by C++ to Python Converter:
            self.nextUniqueCardId = 0
            self.cardsInHand = 0
            self.hand = [None for _ in range(sts.CardManager.MAX_HAND_SIZE)]
            self.limbo = [None for _ in range(sts.CardManager.MAX_HAND_SIZE)]
            self.stasisCards = [CardId.INVALID, CardId.INVALID]
            self.drawPile = fixed_list()
            self.discardPile = fixed_list()
            self.exhaustPile = fixed_list()
            self.drawPile = []
            self.discardPile = []
            self.exhaustPile = []
            self.handNormalityCount = 0
            self.handPainCount = 0
            self.strikeCount = 0
            self.handBloodCardCount = 0
            self.drawPileBloodCardCount = 0
            self.discardPileBloodCardCount = 0


        MAX_HAND_SIZE = 10
        MAX_GROUP_SIZE = 64



# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_card_manager_use_fixed_list
##else
##endif

        def init(self, gc, bc):

            #    masterDeckSize = gc.deck.size()
            self.nextUniqueCardId = gc.deck.size()
            self.handPainCount = 1 if False else 0
            self.handNormalityCount = 1 if False else 0
            self.strikeCount = 0

            idxs = fixed_list(gc.deck.size())
            for i, unusedItem in enumerate(idxs):
                idxs.set(i, i)
            java.Collections.shuffle(idxs.begin(), idxs.end(), java.Random(bc.shuffleRng.randomLong()))

            self.drawPile.resize(len(gc.deck))
            self.discardPile.clear()
            self.exhaustPile.clear()

            normalCount = 0
            isInnateMemo = [False for _ in range(Deck.MAX_SIZE)]

            for i, unusedItem in enumerate(gc.deck):
                deckIdx = idxs.get(i)
                deckCard = gc.deck.cards.get(deckIdx)
                #        if (deckCard.isStrikeCard()) { ++strikeCount; } do at createDeckCardInstanceInDrawPile

                isBottled = deckIdx in gc.deck.bottleIdxs
                isInnateMemo[i] = deckCard.isInnate() or isBottled

                if not isInnateMemo[i]:
                    normalCount += 1

            normalIdx = 0
            innateIdx = normalCount

            for i, unusedItem in enumerate(gc.deck):
                deckIdx = idxs.get(i)
                deckCard = gc.deck.cards.get(deckIdx)

                if isInnateMemo[i]:
                    self.createDeckCardInstanceInDrawPile(deckCard, deckIdx, innateIdx)
                    innateIdx += 1
                else:
                    self.createDeckCardInstanceInDrawPile(deckCard, deckIdx, normalIdx)
                    normalIdx += 1

            innateCount = innateIdx - normalCount
            if innateCount > bc.player.cardDrawPerTurn:
                bc.addToBot(Actions.DrawCards(innateCount-bc.player.cardDrawPerTurn))

        def createDeckCardInstanceInDrawPile(self, card, deckIdx, drawIdx):
            c = self.drawPile.get(drawIdx)
            c = CardInstance(card)
            c.setUniqueId(deckIdx)
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if card.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to create invalid deck instance in draw pile" << std::endl
                False = assert()
##endif
            self.notifyAddCardToCombat(c)
            self.notifyAddToDrawPile(c)

        def createTempCardInDrawPile(self, idx, c):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to create invalid card in draw pile" << std::endl
                False = assert()
##endif

# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: c.uniqueId = static_cast<short>(nextUniqueCardId++);
            c.uniqueId = short(int((self.nextUniqueCardId)))
            self.nextUniqueCardId += 1
            self.notifyAddCardToCombat(c)
            self.notifyAddToDrawPile(c)
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.drawPile.insert(self.drawPile.begin()+idx, c)

        def createTempCardInDiscard(self, c):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: c.uniqueId = static_cast<short>(nextUniqueCardId++);
            c.uniqueId = short(int((self.nextUniqueCardId)))
            self.nextUniqueCardId += 1
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to create invalid card in discard" << std::endl
                False = assert()
##endif
            self.notifyAddCardToCombat(c)
            self.notifyAddToDiscardPile(c)
            self.discardPile.append(c)

        def createTempCardInHand(self, c):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: c.uniqueId = static_cast<short>(nextUniqueCardId++);
            c.uniqueId = short(int((self.nextUniqueCardId)))
            self.nextUniqueCardId += 1
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to create invalid card in hand" << std::endl
                False = assert()
##endif
            self.notifyAddCardToCombat(c)
            self.notifyAddToHand(c)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: hand[cardsInHand++] = c;
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
            self.hand[self.cardsInHand].copy_from(c)
            self.cardsInHand += 1


        # **************** START Remove Methods ****************

        def removeFromDrawPileAtIdx(self, idx):
            self.notifyRemoveFromDrawPile(self.drawPile.get(idx))
            self.drawPile.pop(idx)

        def popFromDrawPile(self):
            c = self.drawPile[len(self.drawPile) - 1]
            self.notifyRemoveFromDrawPile(c)
            self.drawPile.pop(len(self.drawPile) - 1)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: return c;
            return sts.CardInstance(c)

        def removeFromHandAtIdx(self, idx):
            self.notifyRemoveFromHand(self.hand[idx])
            self.eraseAtIdxInHand(idx)

        def removeFromHandById(self, uniqueId):
            i = 0
            while i < self.cardsInHand:
                if self.hand[i].getUniqueId() == uniqueId:
                    self.notifyRemoveFromHand(self.hand[i])
                    self.eraseAtIdxInHand(i)
                i += 1

        def removeFromDiscard(self, idx):
            self.notifyRemoveFromDiscardPile((self.discardPile.begin()+idx))
            self.discardPile.pop(idx)

        def removeFromExhaustPile(self, idx):
            self.exhaustPile.pop(idx)


        # **************** END Remove Methods ****************

        # **************** START Move Methods ****************

        def moveToHand(self, c):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert self.cardsInHand < 10
##endif
            self.notifyAddToHand(c)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: hand[cardsInHand++] = c;
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
            self.hand[self.cardsInHand].copy_from(c)
            self.cardsInHand += 1

        def moveToExhaustPile(self, c):
            self.notifyRemoveFromCombat(c)
            self.exhaustPile.append(c)

        def insertToDrawPile(self, drawPileIdx, c):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                search.g_debug_scum_search.printSearchStack(std::cerr)
                std::cerr << "attempted to insert invalid card to draw pile" << std::endl
                False = assert()
##endif
            self.notifyAddToDrawPile(c)
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.drawPile.insert(self.drawPile.begin()+drawPileIdx, c)

        def moveToDrawPileTop(self, c):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to move invalid card to draw pile" << std::endl
                False = assert()
##endif
            self.notifyAddToDrawPile(c)
            self.drawPile.append(c)

        def shuffleIntoDrawPile(self, cardRandomRng, c):
            if not self.drawPile:
                self.moveToDrawPileTop(c)
            else:
                idx = cardRandomRng.random(int((len(self.drawPile)-1)))
                self.insertToDrawPile(idx, c)

        def moveToDiscardPile(self, c):
            # todo check flurries, weave
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to move invalid card to discard pile" << std::endl
                False = assert()
##endif
            self.notifyAddToDiscardPile(c)
            self.discardPile.append(c)

        def moveDiscardPileIntoToDrawPile(self):
            if not self.drawPile:
                self.drawPileBloodCardCount = self.discardPileBloodCardCount
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: drawPile = discardPile;
                self.drawPile.copy_from(self.discardPile)

            else:
                for c in self.discardPile:
                    self.moveToDrawPileTop(c)

            self.discardPileBloodCardCount = 0
            self.discardPile.clear()

        # **************

        # **************** END Move Methods ****************


        # **************** BEGIN NOTIFY METHODS ****************

        def notifyAddCardToCombat(self, c):
            if c.isStrikeCard():
                self.strikeCount += 1

        def notifyRemoveFromCombat(self, c):
            if c.isStrikeCard():
                self.strikeCount -= 1

        def notifyAddToHand(self, c):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to notify of invalid card in hand" << std::endl
                False = assert()
##endif

            if c.isBloodCard():
                self.handBloodCardCount += 1

            if c.id == CardId.NORMALITY:
                self.handNormalityCount += 1

            elif c.id == CardId.PAIN:
                self.handPainCount += 1


        def notifyRemoveFromHand(self, c):
            if c.isBloodCard():
                self.handBloodCardCount -= 1

            if c.id == CardId.NORMALITY:
                self.handNormalityCount -= 1

            elif c.id == CardId.PAIN:
                self.handPainCount -= 1


        def notifyAddToDrawPile(self, c):

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to notify of invalid card in draw pile" << std::endl
                False = assert()
##endif

            if c.isBloodCard():
                self.drawPileBloodCardCount += 1

        def notifyRemoveFromDrawPile(self, c):
            if c.isBloodCard():
                self.drawPileBloodCardCount -= 1

        def notifyAddToDiscardPile(self, c):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if c.getId() == CardId.INVALID:
                std::cerr << *g_debug_bc << '\n'
                search.g_debug_scum_search.printSearchStack(std::cerr, True)
                std::cerr << "attempted to notify of invalid card in discard pile" << std::endl
                False = assert()
##endif

            if c.isBloodCard():
                self.discardPileBloodCardCount += 1

        def notifyRemoveFromDiscardPile(self, c):
            if c.isBloodCard():
                self.discardPileBloodCardCount -= 1

        # **************


        # **************** END NOTIFY METHODS ****************

        def eraseAtIdxInHand(self, idx):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if idx >= self.cardsInHand:
                False = assert()
##endif

            x = idx
            while x < self.cardsInHand-1:
                self.hand[x] = self.hand[x+1]
                x += 1
            self.cardsInHand -= 1

        def getRandomCardIdxInHand(self, rng):
            return rng.random(self.cardsInHand-1)

        def resetAttributesAtEndOfTurn(self):
            i = 0
            while i < self.cardsInHand:
                self.hand[i].setCostForTurn(self.hand[i].cost)
                i += 1

            for c in self.discardPile:
                c.setCostForTurn(c.cost)

            for c in self.drawPile:
                c.setCostForTurn(c.cost)

        # special helpers

        # **************** BEGIN SPECIAL HELPERS ****************

        def draw(self, bc, amount):
            evolve = bc.player.getStatus()
            fireBreathing = bc.player.getStatus()

            for i in range(0, amount):
                c = self.popFromDrawPile()

                if bc.player.hasStatus():
                    if c.cost >= 0:
                        newCost = bc.cardRandomRng.random(3)
                        if c.cost != newCost:
                            c.costForTurn = newCost
                            c.cost = newCost
                        c.freeToPlayOnce = False

                if c.getType() == CardType.SKILL:
                    if bc.player.hasStatus():
                        c.setCostForTurn(-9)

                elif c.getType() == CardType.STATUS:
                    if evolve != 0:
                        bc.addToBot(Actions.DrawCards(evolve))
                    if fireBreathing != 0:
                        bc.addToBot(Actions.DamageAllEnemy(fireBreathing))
                    if c.getId() == CardId.VOID:
                        # game adds action to bottom of the queue but I think it is ok to do directly
                        bc.player.energy = max(0, bc.player.energy-1)

                elif c.getType() == CardType.CURSE:
                    if fireBreathing != 0:
                        bc.addToBot(Actions.DamageAllEnemy(fireBreathing))


                # do we need to check this?
                if self.cardsInHand < 10:
                    self.moveToHand(c)
                else:
                    self.moveToDiscardPile(c)


        def onTookDamage(self):
            # this method will fail catastrophically if the bloodCardCounts are not correct
            hasAnyBloodCards = (self.handBloodCardCount | self.drawPileBloodCardCount | self.discardPileBloodCardCount) != 0
            if not hasAnyBloodCards:
                return

            i = 0
            foundBloodCards = 0
            while foundBloodCards < self.handBloodCardCount:
                if self.hand[i].isBloodCard():
                    self.hand[i].tookDamage()
                    foundBloodCards += 1
                i += 1

            i = 0
            foundBloodCards = 0
            while foundBloodCards < self.drawPileBloodCardCount:
                if self.drawPile.get(i).isBloodCard():
                    self.drawPile.get(i).tookDamage()
                    foundBloodCards += 1
                i += 1

            i = 0
            foundBloodCards = 0
            while foundBloodCards < self.discardPileBloodCardCount:
                if self.discardPile.get(i).isBloodCard():
                    self.discardPile.get(i).tookDamage()
                    foundBloodCards += 1
                i += 1


        # for ritual dagger, rampage
        def findAndUpgradeSpecialData(self, uniqueId, upgradeAmount):

            # special checks for most common scenarios
            if self.discardPile is not None and self.discardPile[len(self.discardPile) - 1].uniqueId == uniqueId:
                Globals.upgrade(self.discardPile[len(self.discardPile) - 1], upgradeAmount)
                return
            if self.exhaustPile is not None and self.exhaustPile[len(self.exhaustPile) - 1].uniqueId == uniqueId:
                Globals.upgrade(self.exhaustPile[len(self.exhaustPile) - 1], upgradeAmount)
                return

            for i in range(int(len(self.discardPile))-2, -1, -1):
                c = self.discardPile.get(i)
                if c.uniqueId == uniqueId:
                    Globals.upgrade(c, upgradeAmount)
                    return

            for i in range(int(len(self.exhaustPile))-2, -1, -1):
                c = self.exhaustPile.get(i)
                if c.uniqueId == uniqueId:
                    Globals.upgrade(c, upgradeAmount)
                    return

            for c in self.drawPile:
                if c.uniqueId == uniqueId:
                    Globals.upgrade(c, upgradeAmount)
                    return

            i = 0
            while i < self.cardsInHand:
                c = self.hand[i]
                if c.uniqueId == uniqueId:
                    Globals.upgrade(c, upgradeAmount)
                    return
                i += 1


        def onBuffCorruption(self):
            # game does modifyCostForCombat here but I don't think its necessary as skills cant cost more than 4?
            i = 0
            while i < self.cardsInHand:
                c = self.hand[i]
                if c.getType() == CardType.SKILL and c.cost > 0:
                    c.cost = 0
                    c.costForTurn = 0
                i += 1

            # probably only need to do hand?

            for c in self.drawPile:
                if c.getType() == CardType.SKILL and c.cost > 0:
                    c.cost = 0
                    c.costForTurn = 0

            for c in self.discardPile:
                if c.getType() == CardType.SKILL and c.cost > 0:
                    c.cost = 0
                    c.costForTurn = 0

            for c in self.exhaustPile:
                if c.getType() == CardType.SKILL and c.cost > 0:
                    c.cost = 0
                    c.costForTurn = 0



    def left_shift(self, os, c):
        os << "CardManager: {"

        os << "\n\tdrawPile: " << c.drawPile.size() << " "
        sts.printArray(os, c.drawPile.begin(), c.drawPile.end())

        os << ",\n\tdiscardPile: " << c.discardPile.size() << " "
        sts.printArray(os, c.discardPile.begin(), c.discardPile.end())

        os << ",\n\texhaustPile: " << c.exhaustPile.size() << " "
        sts.printArray(os, c.exhaustPile.begin(), c.exhaustPile.end())

        os << ",\n\thand: " << c.cardsInHand << " "
        sts.printArray(os, c.hand.begin(), c.hand.begin()+c.cardsInHand)

        os << "\n\tstasisCards{" << c.stasisCards[0] << "," << c.stasisCards[1] << "}"

        os << "\n\t" << "handNormalityCount: " << c.handNormalityCount
        S = ", "
        os << S << "handPainCount: " << c.handPainCount
        os << S << "strikeCount: " << c.strikeCount

        os << S << "handBloodCardCount: " << c.handBloodCardCount
        os << S << "drawPileBloodCardCount: " << c.drawPileBloodCardCount
        os << S << "discardPileBloodCardCount: " << c.discardPileBloodCardCount

        os << "\n}\n"

        return os


# **************** END SPECIAL HELPERS ****************


class sts: #this class replaces the original namespace 'sts'

    #    std::ostream &operator<<(std::ostream &os, const CardInstance &c) {
    #        return os << "("
    #            << c.getName()
    #            << ", uid:" << std::to_string(c.uniqueId)
    #            << ", u:" << std::to_string(c.upgraded)
    #            << ", c:" << c.cost
    #            << ", ct:" << c.costForTurn
    #            << ")";
    #    }

    @staticmethod
    def printArray(os, begin, end):
        os << "{ "
        while begin is not end and begin+1 != end:
            os << *begin << ", "
            begin += 1
        if begin is not end:
            os << *begin
        os << " }"


