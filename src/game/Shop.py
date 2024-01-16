from sts import *

import math

#
# Created by gamerpuppy on 7/11/2021.
#

#
# Created by gamerpuppy on 7/11/2021.
#




class sts: #this class replaces the original namespace 'sts'

# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class GameContext

    class Shop:

        def __init__(self):
            # instance fields found by C++ to Python Converter:
            self.prices = [0 for _ in range(13)]
            self.removeCost = 0
            self.cards = [Card() for _ in range(7)]
            self.potions = [0 for _ in range(3)]
            self.relics = [0 for _ in range(3)]


        REMOVE_PRICE_INCREASE = 25
        BASE_REMOVE_PRICE = 75
        SMILING_MASK_PRICE = 50
        COURIER_FACTOR = 0.80
        MEMBERSHIP_CARD_FACTOR = 0.50

        def setup(self, gc):
            self.setupCards(gc)
            self.setupRelics(gc)
            self.setupPotions(gc)

            if gc.ascension >= 16:
                self.applyDiscount(0.80)
            if gc.hasRelic(RelicId.THE_COURIER):
                self.applyDiscount(0.80)
            if gc.hasRelic(RelicId.MEMBERSHIP_CARD):
                self.applyDiscount(0.50)
            self.removeCost = sts.Shop.getRemoveCost(gc)

        def setupCards(self, gc):
            rarities = [0 for _ in range(5)]

            rarities[0] = sts.Shop.rollCardRarityShop(gc.cardRng, gc.cardRarityFactor)
            self.cards[0] = getRandomClassCardOfTypeAndRarity(gc.cardRng, gc.cc, CardType.ATTACK, rarities[0])
            sts.Shop.assignRandomCardExcluding(gc, CardType.ATTACK, self.cards[0].id, self.cards[1], rarities[1])

            rarities[2] = sts.Shop.rollCardRarityShop(gc.cardRng, gc.cardRarityFactor)
            self.cards[2] = getRandomClassCardOfTypeAndRarity(gc.cardRng, gc.cc, CardType.SKILL, rarities[2])
            sts.Shop.assignRandomCardExcluding(gc, CardType.SKILL, self.cards[2].id, self.cards[3], rarities[3])

            rarities[4] = sts.Shop.rollCardRarityShop(gc.cardRng, gc.cardRarityFactor)
            rarities[4] = CardRarity.UNCOMMON if rarities[4] == CardRarity.COMMON else rarities[4]
            self.cards[4] = getRandomClassCardOfTypeAndRarity(gc.cardRng, gc.cc, CardType.POWER, rarities[4])

            self.cards[5] = getColorlessCardFromPool(gc.cardRng, CardRarity.UNCOMMON)
            self.cards[6] = getColorlessCardFromPool(gc.cardRng, CardRarity.RARE)

            for i in range(0, 5):

                tmpPrice = cardRarityPrices[int(rarities[i])] * gc.merchantRng.random(0.9, 1.1)
                self.prices[i] = int(tmpPrice)

            self.prices[5] = cardRarityPrices[int(CardRarity.UNCOMMON)] * gc.merchantRng.random(0.9, 1.1) * 1.2
            self.prices[6] = cardRarityPrices[int(CardRarity.RARE)] * gc.merchantRng.random(0.9, 1.1) * 1.2

            saleIdx = gc.merchantRng.random(4)
            self.prices[saleIdx] = math.trunc(self.prices[saleIdx] / float(2))

        def setupRelics(self, gc):
            self.relics[0] = gc.returnRandomRelic(sts.Shop.rollRelicTier(gc.merchantRng), True, False)
            self.relicPrice(0) = round(getRelicBasePrice(self.relics[0]) * gc.merchantRng.random(0.95, 1.05))

            self.relics[1] = gc.returnRandomRelic(sts.Shop.rollRelicTier(gc.merchantRng), True, False)
            self.relicPrice(1) = round(getRelicBasePrice(self.relics[1]) * gc.merchantRng.random(0.95, 1.05))

            self.relics[2] = gc.returnRandomRelic(RelicTier.SHOP, True, False)
            self.relicPrice(2) = round(relicTierPrices[int(RelicTier.SHOP)] * gc.merchantRng.random(0.95, 1.05))

        def setupPotions(self, gc):
            for i in range(0, 3):
                self.potions[i] = returnRandomPotion(gc.potionRng, gc.cc)
                rarity = potionRarities[int(self.potions[i])]
                basePrice = potionRarityPrices[int(rarity)]
                self.potionPrice(i) = round(basePrice * gc.merchantRng.random(0.95, 1.05))

        def applyDiscount(self, factor):
            for price in self.prices:
                price = int(round(factor* float(price)))

        def buyCard(self, gc, idx):
            gc.deck.obtain(gc, self.cards[idx], 1)
            gc.loseGold(self.cardPrice(idx), True)

            if gc.hasRelic(RelicId.THE_COURIER):
                if idx >= 5:
                    # colorless card
                    rarity = CardRarity.RARE if gc.merchantRng.random() < COLORLESS_RARE_CHANCE else CardRarity.UNCOMMON
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards[idx] = gc.previewObtainCard(getColorlessCardFromPool(gc.cardRng, rarity));
                    self.cards[idx].copy_from(gc.previewObtainCard(getColorlessCardFromPool(gc.cardRng, rarity)))
                    self.cardPrice(idx) = sts.Shop.getNewCardPrice(gc, rarity, True)
                else:
                    rarity = gc.rollCardRarity(Room.SHOP)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards[idx] = gc.previewObtainCard(getRandomClassCardOfRarity(gc.mathUtilRng, gc.cc, rarity));
                    self.cards[idx].copy_from(gc.previewObtainCard(getRandomClassCardOfRarity(gc.mathUtilRng, gc.cc, rarity)))
                    self.cardPrice(idx) = sts.Shop.getNewCardPrice(gc, rarity, False)

            else:
                self.cardPrice(idx) = -1

        def buyRelic(self, gc, idx):
            r = self.relics[idx]

            openedScreen = gc.obtainRelic(r)
            if openedScreen:
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                gc.regainControlAction = [](GameContext &gc)
                #                {
                #                    gc.screenState = ScreenState::SHOP_ROOM
                #                    gc.regainControlAction = [] (auto &gc)
                #                    {
                #                        gc.screenState = ScreenState::MAP_SCREEN
                #                    }
                #                }

            gc.loseGold(self.relicPrice(idx), True)

            if r == RelicId.MEMBERSHIP_CARD:
                self.applyDiscount(sts.Shop.MEMBERSHIP_CARD_FACTOR)
                self.removeCost = int(round(float(self.removeCost) * sts.Shop.MEMBERSHIP_CARD_FACTOR))

            if gc.hasRelic(RelicId.THE_COURIER):
                self.relics[idx] = gc.returnRandomRelic(sts.Shop.rollRelicTier(gc.merchantRng), True, False)
                sts.Shop.getNewPrice(gc, getRelicBasePrice(self.relics[idx]))
            else:
                self.relicPrice(idx) = -1

            if isEggRelic(self.relics[idx]):
                for c in self.cards:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: c = gc.previewObtainCard(c);
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
                    c.copy_from(gc.previewObtainCard(sts.Card(c)))

        def buyPotion(self, gc, idx):
            #    if (gc.hasRelic(RelicId::SOZU)) { // just dont call this with sozu or without enough slots
            #        return
            #    }
            gc.obtainPotion(self.potions[idx])
            gc.loseGold(self.potionPrice(idx), True)
            if gc.hasRelic(RelicId.THE_COURIER):
                self.potions[idx] = returnRandomPotion(gc.potionRng, gc.cc)
                self.potionPrice(idx) = sts.Shop.getNewPrice(gc, getPotionBaseCost(self.potions[idx]))
            else:
                self.potionPrice(idx) = -1

        def buyCardRemove(self, gc):
            gc.loseGold(self.removeCost, True)
            self.removeCost = -1
            gc.shopRemoveCount += 1

# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#            gc.regainControlAction = [:=](GameContext &g)
            #            {
            #                g.screenState = ScreenState::SHOP_ROOM
            #                g.regainControlAction = gc.regainControlAction
            #            }

            gc.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

# C++ TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def cardPrice(self, idx):
            return self.prices[idx]

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int cardPrice(int idx) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int cardPrice(int idx) const
# C++ TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def cardPrice(self, idx):
            return self.prices[idx]

# C++ TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def relicPrice(self, idx):
            return self.prices[7+idx]

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int relicPrice(int idx) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int relicPrice(int idx) const
# C++ TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def relicPrice(self, idx):
            return self.prices[7+idx]

# C++ TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def potionPrice(self, idx):
            return self.prices[10+idx]

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int potionPrice(int idx) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int potionPrice(int idx) const
# C++ TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def potionPrice(self, idx):
            return self.prices[10+idx]

        # C++ TO PYTHON CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Python):
        BASE_RARE_CHANCE = 9
        # C++ TO PYTHON CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Python):
        BASE_UNCOMMON_CHANCE = 37

        @staticmethod
        def rollCardRarityShop(cardRng, cardRarityAdjustment):
            # C++ TO PYTHON CONVERTER NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
            #            static constexpr int BASE_RARE_CHANCE = 9
            # C++ TO PYTHON CONVERTER NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
            #            static constexpr int BASE_UNCOMMON_CHANCE = 37

            roll = cardRng.random(99)
            roll += cardRarityAdjustment

            if roll < BASE_RARE_CHANCE:
                return CardRarity.RARE

            elif roll >= BASE_RARE_CHANCE + BASE_UNCOMMON_CHANCE:
                return CardRarity.COMMON

            else:
                return CardRarity.UNCOMMON

        @staticmethod
        def getNewCardPrice(gc, rarity, colorless):
            price = float((cardRarityPrices[int(rarity)] * gc.merchantRng.random(0.9, 1.1)))
            if colorless:
                price *= 1.2
            if gc.hasRelic(RelicId.THE_COURIER):
                price *= 0.8
            if gc.hasRelic(RelicId.THE_COURIER):
                price *= 0.5
            return int(price)

        @staticmethod
        def getNewPrice(gc, basePrice):
            basePrice = int(round(gc.merchantRng.random(0.95, 1.05)))
            if gc.hasRelic(RelicId.THE_COURIER):
                round(basePrice * sts.Shop.COURIER_FACTOR)
            if gc.hasRelic(RelicId.MEMBERSHIP_CARD):
                round(basePrice * sts.Shop.MEMBERSHIP_CARD_FACTOR)
            return basePrice

        @staticmethod
        def getRemoveCost(gc):
            cost = 0
            if gc.hasRelic(RelicId.SMILING_MASK):
                cost = sts.Shop.SMILING_MASK_PRICE
            else:
                cost = sts.Shop.BASE_REMOVE_PRICE+(sts.Shop.REMOVE_PRICE_INCREASE *gc.shopRemoveCount)

            if gc.hasRelic(RelicId.THE_COURIER) and gc.hasRelic(RelicId.MEMBERSHIP_CARD):
                cost = round(float(cost) * sts.Shop.COURIER_FACTOR * sts.Shop.MEMBERSHIP_CARD_FACTOR)

            elif gc.hasRelic(RelicId.THE_COURIER):
                cost = round(float(cost) * sts.Shop.COURIER_FACTOR)

            elif gc.hasRelic(RelicId.MEMBERSHIP_CARD):
                cost = round(float(cost) * sts.Shop.MEMBERSHIP_CARD_FACTOR)
            return cost

        @staticmethod
        def rollRelicTier(merchantRng):
            roll = merchantRng.random(99)
            if roll < 48:
                return RelicTier.COMMON
            elif roll < 82:
                return RelicTier.UNCOMMON
            else:
                return RelicTier.RARE

        @staticmethod
        def assignRandomCardExcluding(gc, type, excludeId, outCard, outRarity):
            id = 0
            loop_condition = True
            while loop_condition:
                outRarity.arg_value = sts.Shop.rollCardRarityShop(gc.cardRng, gc.cardRarityFactor)
                id = getRandomClassCardOfTypeAndRarity(gc.cardRng, gc.cc, type, outRarity.arg_value)
                loop_condition = id == excludeId

            outCard.arg_value = gc.previewObtainCard(id)


