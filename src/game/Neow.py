from sts import *

from enum import Enum

#
# Created by gamerpuppy on 6/24/2021.
#

#
# Created by gamerpuppy on 6/24/2021.
#



class sts: #this class replaces the original namespace 'sts'

    class Neow: #this class replaces the original namespace 'Neow'

        class CurrentActionSpace(Enum):
            CHOICE_LIST = 0
            MAP_FORK = 1
            MAP_BEGIN = 2
            COMBAT = 3
            REWARDS = 4
            SHOP = 5

        class Bonus(Enum):
            THREE_CARDS = 0
            ONE_RANDOM_RARE_CARD = 1
            REMOVE_CARD = 2
            UPGRADE_CARD = 3
            TRANSFORM_CARD = 4
            RANDOM_COLORLESS = 5

            THREE_SMALL_POTIONS = 6
            RANDOM_COMMON_RELIC = 7
            TEN_PERCENT_HP_BONUS = 8
            THREE_ENEMY_KILL = 9
            HUNDRED_GOLD = 10

            RANDOM_COLORLESS_2 = 11
            REMOVE_TWO = 12
            ONE_RARE_RELIC = 13
            THREE_RARE_CARDS = 14
            TWO_FIFTY_GOLD = 15
            TRANSFORM_TWO_CARDS = 16
            TWENTY_PERCENT_HP_BONUS = 17

            BOSS_RELIC = 18
            INVALID = 19

        BONUSSTRINGS = ["Choose a card to obtain.", "Obtain a random rare card.", "Remove a card.", "Upgrade a card.", "Transform a card.", "Choose a colorless card to obtain.", "Obtain three potions.", "Obtain a random common relic.", "Max Hp +10%.", "Obtain Neow's Lament.", "Obtain 100 gold.", "Choose a rare colorless card to obtain.", "Remove two cards.", "Obtain a random rare relic.", "Choose a rare card to obtain.", "Obtain 250 gold.", "Transform two cards in your cards.", "Max Hp +20%.", "Obtain a random boss relic.", "INVALID"]


        class Drawback(Enum):
            INVALID = 0
            NONE = 1
            TEN_PERCENT_HP_LOSS = 2
            NO_GOLD = 3
            CURSE = 4
            PERCENT_DAMAGE = 5
            LOSE_STARTER_RELIC = 6


        DRAWBACKSTRINGS = ["INVALID", "", "Max Hp -10%.", "Lose all gold.", "Obtain a curse.", "Take 30% Hp damage.", "Lose your starter relic."]


        class Option:

            def __init__(self):
                # instance fields found by C++ to Python Converter:
                self.r = 0
                self.d = 0


        # C++ TO PYTHON CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Python):
        myRewards = [getOptions_Bonus.RANDOM_COLORLESS_2, getOptions_Bonus.REMOVE_TWO, getOptions_Bonus.ONE_RARE_RELIC, getOptions_Bonus.THREE_RARE_CARDS, getOptions_Bonus.TWO_FIFTY_GOLD, getOptions_Bonus.TRANSFORM_TWO_CARDS]
        # C++ TO PYTHON CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Python):
        myRewards = [getOptions_Bonus.RANDOM_COLORLESS_2, getOptions_Bonus.REMOVE_TWO, getOptions_Bonus.ONE_RARE_RELIC, getOptions_Bonus.THREE_RARE_CARDS, getOptions_Bonus.TRANSFORM_TWO_CARDS, getOptions_Bonus.TWENTY_PERCENT_HP_BONUS]
        # C++ TO PYTHON CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Python):
        myRewards = [getOptions_Bonus.RANDOM_COLORLESS_2, getOptions_Bonus.ONE_RARE_RELIC, getOptions_Bonus.THREE_RARE_CARDS, getOptions_Bonus.TWO_FIFTY_GOLD, getOptions_Bonus.TRANSFORM_TWO_CARDS, getOptions_Bonus.TWENTY_PERCENT_HP_BONUS]

        @staticmethod
        def getOptions(r):
            rewards = []
            rewards[0].r = r.random(0, 5)
            rewards[0].d = sts.Neow.Drawback.NONE
            rewards[1].r = (6 + r.random(0, 4))
            rewards[1].d = sts.Neow.Drawback.NONE

            rewards[2].d = (2 + r.random(0, 3))
            if rewards[2].d == sts.Neow.Drawback.TEN_PERCENT_HP_LOSS:
                    # C++ TO PYTHON CONVERTER NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                    #                    static constexpr Bonus myRewards[]{ Bonus::RANDOM_COLORLESS_2, Bonus::REMOVE_TWO, Bonus::ONE_RARE_RELIC, Bonus::THREE_RARE_CARDS, Bonus::TWO_FIFTY_GOLD, Bonus::TRANSFORM_TWO_CARDS}
                    rewards[2].r = myRewards[r.random(0, 5)]

            elif rewards[2].d == sts.Neow.Drawback.NO_GOLD:
                    # C++ TO PYTHON CONVERTER NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                    #                    static constexpr Bonus myRewards[]{ Bonus::RANDOM_COLORLESS_2, Bonus::REMOVE_TWO, Bonus::ONE_RARE_RELIC, Bonus::THREE_RARE_CARDS, Bonus::TRANSFORM_TWO_CARDS, Bonus::TWENTY_PERCENT_HP_BONUS}
                    rewards[2].r = myRewards[r.random(0, 5)]

            elif rewards[2].d == sts.Neow.Drawback.CURSE:
                    # C++ TO PYTHON CONVERTER NOTE: This static local variable declaration (not allowed in Python) has been moved just prior to the method:
                    #                    static constexpr Bonus myRewards[]{ Bonus::RANDOM_COLORLESS_2, Bonus::ONE_RARE_RELIC, Bonus::THREE_RARE_CARDS, Bonus::TWO_FIFTY_GOLD, Bonus::TRANSFORM_TWO_CARDS, Bonus::TWENTY_PERCENT_HP_BONUS}
                    rewards[2].r = myRewards[r.random(0, 5)]

            elif rewards[2].d == sts.Neow.Drawback.PERCENT_DAMAGE:
                rewards[2].r = (11 + r.random(0, 6))



            rewards[3].r = getOptions_Bonus.BOSS_RELIC
            rewards[3].d = sts.Neow.Drawback.LOSE_STARTER_RELIC
            r.random(0, 0)

            return list(rewards)

        @staticmethod
        def getCardReward(rng, cc, rareOnly = False):
            reward = CardReward()

            for i in range(0, 3):
                rarity = sts.CardRarity.UNCOMMON if rng.randomBoolean(0.33) else sts.CardRarity.COMMON
                if rareOnly:
                    rarity = sts.CardRarity.RARE

                card = getRandomClassCardOfRarity(rng, cc, rarity)
                while True:
                    containsCard = False
                    x = 0
                    while x < i:
                        if reward[x].id == card.id:
                            containsCard = True
                            break
                        x += 1
                    if containsCard:
                        card = getRandomClassCardOfRarity(rng, cc, rarity)
                    else:
                        break
                reward.push_back(card)
            return CardReward(reward)

        @staticmethod
        def getColorlessCardReward(neowRng, cardRng, rareOnly = False):
            reward = CardReward()
            for i in range(0, 3):

                rarity = sts.CardRarity.UNCOMMON if neowRng.randomBoolean(0.33) else sts.CardRarity.COMMON
                if rareOnly:
                    rarity = sts.CardRarity.RARE
                elif rarity == sts.CardRarity.COMMON:
                    rarity = sts.CardRarity.UNCOMMON

                card = getRandomColorlessCardNeow(cardRng, rarity)
                while True:
                    containsCard = False
                    x = 0
                    while x < i:
                        if reward[x].id == card.id:
                            containsCard = True
                            break
                        x += 1
                    if containsCard:
                        card = getRandomColorlessCardNeow(cardRng, rarity)
                    else:
                        break
                reward.push_back(card)

            return CardReward(reward)



