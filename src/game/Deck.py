from sts import *

#
# Created by gamerpuppy on 7/10/2021.
#


#
# Created by gamerpuppy on 7/10/2021.
#





class sts: #this class replaces the original namespace 'sts'


# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class Random
# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class GameContext
# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class SelectScreenCard
# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class SaveFile
    class CardPredicate:
        def invoke(self, UnnamedParameter):
            pass



    class Deck:

        def __init__(self):
            # instance fields found by C++ to Python Converter:
            self.cards = fixed_list()
            self.cardTypeCounts = [0, 0, 0, 0]
            self.bottleIdxs = [-1, -1, -1]
            self.upgradeableCount = 0
            self.transformableCount = 0

        MAX_SIZE = 96




        def initFromSaveFile(self, s):
            # the first card with a matching id will be bottled
            bottledCardIds = [(int)s.bottledCards[0], s.bottledCards[1], s.bottledCards[2], (int)CardId.INVALID]

            for c in s.cards:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: obtainRaw(c);
                self.obtainRaw(sts.Card(c))

                if c.getId() == bottledCardIds[int(c.getType())]:
                    self.bottleCard(int((self.cards.size()-1)), c.getType())
                    bottledCardIds[int(c.getType())] = CardId.INVALID

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int size() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int size() const
        def size(self):
            return self.cards.size()

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool hasCurse() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool hasCurse() const
        def hasCurse(self):
            return self.cardTypeCounts[int(CardType.CURSE)] != 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isCardBottled(int idx) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isCardBottled(int idx) const
        def isCardBottled(self, idx):
            return idx == self.bottleIdxs[0] or idx == self.bottleIdxs[1] or idx == self.bottleIdxs[2]

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool anyCardBottled() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool anyCardBottled() const
        def anyCardBottled(self):
            return self.bottleIdxs[0] == -1 or self.bottleIdxs[1] == -1 or self.bottleIdxs[2] == -1

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getUpgradeableCount() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getUpgradeableCount() const
        def getUpgradeableCount(self):
            return self.upgradeableCount

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getTransformableCount(int limit=-1, bool includeBottled=false) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getTransformableCount(int limit =-1, bool includeBottled =false) const
        def getTransformableCount(self, limit = -1, includeBottled = False):
            if includeBottled:
                count = self.transformableCount
                for i in range(0, 3):
                    if self.bottleIdxs[i] != -1:
                        count += 1
                        if limit != -1 and count >= limit:
                            return count
                return count

            else:
                return self.transformableCount

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getCountMatching(const CardPredicate &predicate, int limit=-1) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getCountMatching(const CardPredicate &predicate, int limit=-1) const;
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        getCountMatching(predicate, limit = -1)
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] fixed_list<int, MAX_SIZE> getIdxsMatching(const CardPredicate &p) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: fixed_list<int, Deck::MAX_SIZE> getIdxsMatching(const CardPredicate &p) const
        def getIdxsMatching(self, p):
            list = fixed_list()
            for i, unusedItem in enumerate(self.cards):
                if p(self.cards.get(i)):
                    list.push_back(i)
            return fixed_list(list)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool hasCardForWingStatue() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool hasCardForWingStatue() const
        def hasCardForWingStatue(self):
            for c in self.cards:
                if getBaseDamage(c.getId(), c.getUpgraded()) >= 10:
                    return True
            return False

        def upgradeStrikesAndDefends(self):
            for c in self.cards:
                if c.isStarterStrikeOrDefend() and c.canUpgrade():
                    self.upgradeableCount -= 1
                    c.upgrade()

        def upgradeRandomCards(self, miscRng, count):
            list = self.getUpgradeableCardIdxs()
            java.Collections.shuffle(list.begin(), list.end(), java.Random(miscRng.randomLong()))
            end = min(list.size(), count)
            for i in range(0, end):
                self.upgradeableCount -= 1
                self.cards.get(list.get(i)).upgrade()

        def transformRandomCards(self, miscRng, count):
            # todo
            pass

        def obtain(self, gc, card, count = 1):
            type = card.getType()

            if type == CardType.ATTACK:
                self.transformableCount += count
                self.cardTypeCounts[int(CardType.ATTACK)] += count
                if gc.hasRelic(RelicId.MOLTEN_EGG):
                    card.upgrade()
                elif card.canUpgrade():
                    self.upgradeableCount += count

            elif type == CardType.SKILL:
                self.transformableCount += count
                self.cardTypeCounts[int(CardType.SKILL)] += count
                if gc.hasRelic(RelicId.TOXIC_EGG):
                    card.upgrade()
                elif card.canUpgrade():
                    self.upgradeableCount += count

            elif type == CardType.POWER:
                self.transformableCount += count
                self.cardTypeCounts[int(CardType.POWER)] += count
                if gc.hasRelic(RelicId.FROZEN_EGG):
                    card.upgrade()
                elif card.canUpgrade():
                    self.upgradeableCount += count

            elif type == CardType.CURSE:
                if gc.relics.has(RelicId.OMAMORI):
# C++ TO PYTHON CONVERTER TASK: Python does not have an equivalent to references to value types:
# ORIGINAL LINE: int &omamoriCount = gc.relics.getRelicValueRef(RelicId::OMAMORI);
                    omamoriCount = gc.relics.getRelicValueRef(RelicId.OMAMORI)
                    if omamoriCount > 0:
                        decAmt = min(count, omamoriCount)
                        count -= decAmt
                        omamoriCount -= decAmt

                        if count == 0:
                            return
                if card.canTransform():
                    self.transformableCount += count
                    self.cardTypeCounts[int(CardType.CURSE)] += count


            if type != CardType.ATTACK and type != CardType.SKILL and type != CardType.POWER and type != CardType.CURSE:
                False = assert()


            if gc.relics.has(RelicId.CERAMIC_FISH):
                gc.obtainGold(9 * count)

            for i in range(0, count):
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cards.push_back(card);
                self.cards.push_back(sts.Card(card))

        def obtainRaw(self, card):
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cards.push_back(card);
            self.cards.push_back(sts.Card(card))
            self.transformableCount += 1
            self.cardTypeCounts[int(card.getType())] += 1

            if (card.getType() == CardType.ATTACK) or card.getType() == CardType.SKILL or (card.getType() == CardType.POWER):
                self.transformableCount += 1
                self.cardTypeCounts[int(card.getType())] += 1
                if card.canUpgrade():
                    self.upgradeableCount += 1

            elif card.getType() == CardType.CURSE:
                if card.canTransform():
                    self.transformableCount += 1
                    self.cardTypeCounts[int(card.getType())] += 1


            if card.getType() != CardType.ATTACK and card.getType() != CardType.SKILL and card.getType() != CardType.POWER and card.getType() != CardType.CURSE:
                False = assert()

        def remove(self, gc, idx):
            c = self.cards.get(idx)

            if c.getType() == CardType.CURSE:
                if c.canTransform():
                    self.cardTypeCounts[int(CardType.CURSE)] -= 1
                    self.transformableCount -= 1
                if c.getId() == CardId.PARASITE:
                    gc.loseMaxHp(3)
                self.cards.remove(idx)
                return

            self.transformableCount -= 1
            self.cardTypeCounts[int(c.getType())] -= 1
            if c.canUpgrade():
                self.upgradeableCount -= 1

            if not self.anyCardBottled():
                self.cards.remove(idx)
                return

            # for erasing a card from the deck when there is a bottled card
            for i in range(0, 3):
                if idx == self.bottleIdxs[i]:
                    self.bottleIdxs[i] = -1
                    self.transformableCount += 1 # if was in a bottle (not counted as transformable), we need to change the transformable count backIdx

                elif idx < self.bottleIdxs[i]:
                    self.bottleIdxs[i] -= 1 # shift the bottleIdx to reflect shift in the cards list

            i = idx
            while i+1 < self.cards.size():
                self.cards.set(i, self.cards.get(i+1)) # shift cards to erase remove card
                i += 1
            self.cards.resize(self.cards.size()-1)

        def removeSelected(self, gc, selectList):
            removeIdx = [0 for _ in range(3)]
            for i, unusedItem in enumerate(selectList):
                removeIdx[i] = selectList.get(i).deckIdx
            std::sort(removeIdx, removeIdx+selectList.size())

            for i in range(selectList.size() - 1, -1, -1):
                self.remove(gc, selectList.get(i).deckIdx)

        def upgrade(self, idx):
            self.cards.get(idx).upgrade()
            self.upgradeableCount -= 1

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: void addMatchingToSelectList(fixed_list<SelectScreenCard, Deck::MAX_SIZE> &selectList, const CardPredicate &p) const
        def addMatchingToSelectList(self, selectList, p):
            for i, unusedItem in enumerate(self.cards):
                if p(self.cards.get(i)):
                    selectList.push_back(SelectScreenCard(self.cards.get(i), i))

        def bottleCard(self, idx, bottleType):
            self.bottleIdxs[int(bottleType)] = idx
            self.transformableCount -= 1

        def removeBottle(self, bottleType):
            self.bottleIdxs[int(bottleType)] = -1
            self.transformableCount += 1

// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        removeAllMatching(gc, p)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] fixed_list<int, MAX_SIZE> getUpgradeableCardIdxs() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: fixed_list<int, Deck::MAX_SIZE> getUpgradeableCardIdxs() const
        def getUpgradeableCardIdxs(self):
            ret = fixed_list()
            for i, unusedItem in enumerate(self.cards):
                if self.cards.get(i).canUpgrade():
                    ret.push_back(i)
            return fixed_list(ret)


# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int Deck::getCountMatching(const std::function<bool(const Card &)> &predicate, const int limit) const
def getCountMatching(predicate, limit):
    count = 0
    for card in cards:
        if predicate.invoke(card):
            count += 1
            if limit != -1 and count > limit:
                return count
    return count

def removeAllMatching(gc, p):
    #    int cumRemove[MAX_DECK_SIZE+1]; // OwO
    #    cumRemove[cards.size()] = 0
    #
    #    for (int i = cards.size()-1; i >= 0; --i) {
    #        cumRemove[i] = cumRemove[i+1] + (predicate(cards[i]) ? 1 : 0)
    #    }
    #
    #    int x = 0
    #    for (int i = 0; i < cards.size(); ++i) {
    #        bool addCurCard = cumRemove[i+1] == cumRemove[i]
    #        if (addCurCard) {
    #            cards[x++] = cards[i]
    #        }
    #    }
    #    cards.resize(x)

    for i in range(cards.size(), -1, -1):
        if p.invoke(cards[i]):
            remove(gc, i)

