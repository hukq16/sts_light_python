from sts import *

from enum import Enum
import math

#
# Created by gamerpuppy on 6/25/2021.
#

#
# Created by gamerpuppy on 6/24/2021.
#






class sts: #this class replaces the original namespace 'sts'

    class GameOutcome(Enum):
        PLAYER_LOSS = 0
        UNDECIDED = 1
        PLAYER_VICTORY = 2

    class RngReference(Enum):
        MISC_RNG = 0
        CARD_RNG = 1
        NEOW_RNG = 2

    class CardSelectScreenType(Enum):
        INVALID = 0
        TRANSFORM = 1
        TRANSFORM_UPGRADE = 2
        UPGRADE = 3
        REMOVE = 4
        DUPLICATE = 5
        OBTAIN = 6
        BOTTLE = 7
        BONFIRE_SPIRITS = 8

    class ScreenState(Enum):
        INVALID = 0
        EVENT_SCREEN = 1
        REWARDS = 2
        BOSS_RELIC_REWARDS = 3
        CARD_SELECT = 4
        MAP_SCREEN = 5
        TREASURE_ROOM = 6
        REST_ROOM = 7
        SHOP_ROOM = 8
        BATTLE = 9

    class SelectScreenCard:

        def _initialize_instance_fields(self):
            # instance fields found by C++ to Python Converter:
            self.card = Card()
            self.deckIdx = -1


# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        SelectScreenCard() = default
# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: SelectScreenCard(const Card &card) : card(card)
        def __init__(self, card):
            self._initialize_instance_fields()

            self.card = sts.Card(card)

# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: SelectScreenCard(const Card &card, int deckIdx) : card(card), deckIdx(deckIdx)
        def __init__(self, card, deckIdx):
            self._initialize_instance_fields()

            self.card = sts.Card(card)
            self.deckIdx = short(deckIdx)

    class ScreenStateInfo:

        def __init__(self):
            # instance fields found by C++ to Python Converter:
            self.encounter = 0
            self.transformRng = RngReference.CARD_RNG
            self.selectScreenType = CardSelectScreenType.INVALID
            self.toSelectCount = 0
            self.toSelectCards = fixed_list()
            self.haveSelectedCards = fixed_list()
            self.eventData = 0
            self.hpAmount0 = 0
            self.hpAmount1 = 0
            self.hpAmount2 = 0
            self.phase = 0
            self.rewards = [0 for _ in range(3)]
            self.upgradeOne = False
            self.cleanUpIsRemoveCard = False
            self.haveGold = False
            self.chestSize = 0
            self.tier = 0
            self.goldLoss = 0
            self.potionIdx = 0
            self.gold = 0
            self.cardIdx = 0
            self.relicIdx0 = 0
            self.relicIdx1 = 0
            self.skillCardDeckIdx = 0
            self.powerCardDeckIdx = 0
            self.attackCardDeckIdx = 0
            self.bossRelics = [0 for _ in range(3)]
            self.neowRewards = NeowOptions()
            self.rewardsContainer = Rewards()
            self.stolenGold = 0
            self.shop = Shop()


        # CardSelectScreen

        # Events


        # Dead Adventurer

        # Designer In-Spire

        # Treasure Room

        # World of Goop

        # We Meet Again Event

        # N'loth

        # Falling

        # Boss Room


        # from combats

        # Shop Room


# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class GameContext
    class GameContextAction:
        def invoke(self, UnnamedParameter):
            pass


# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class BattleContext
# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class SaveFile

    class GameContext:

        def _initialize_instance_fields(self):
            # instance fields found by C++ to Python Converter:
            self.noteForYourselfCard = Card(CardId.IRON_WAVE)
            self.skipBattles = False
            self.seed = 0
            self.aiRng = Random()
            self.cardRandomRng = Random()
            self.cardRng = Random()
            self.eventRng = Random()
            self.mathUtilRng = Random()
            self.merchantRng = Random()
            self.miscRng = Random()
            self.monsterHpRng = Random()
            self.monsterRng = Random()
            self.neowRng = Random()
            self.potionRng = Random()
            self.relicRng = Random()
            self.shuffleRng = Random()
            self.treasureRng = Random()
            self.eventList = []
            self.shrineList = []
            self.specialOneTimeEventList = []
            self.commonRelicPool = []
            self.uncommonRelicPool = []
            self.rareRelicPool = []
            self.shopRelicPool = []
            self.bossRelicPool = []
            self.colorlessCardPool = baseColorlessPool
            self.monsterListOffset = 0
            self.monsterList = fixed_list()
            self.eliteMonsterListOffset = 0
            self.eliteMonsterList = fixed_list()
            self.secondBoss = MonsterEncounter.INVALID
            self.outcome = GameOutcome.UNDECIDED
            self.screenState = ScreenState.INVALID
            self.info = ScreenStateInfo()
            self.lastRoom = Room.INVALID
            self.curEvent = Event.INVALID
            self.curRoom = Room.INVALID
            self.boss = MonsterEncounter.INVALID
            self.monsterChance = 0.1
            self.shopChance = 0.03
            self.treasureChance = 0.02
            self.potionChance = 0
            self.cardRarityFactor = 5
            self.shopRemoveCount = 0
            self.speedrunPace = False
            self.curMapNodeX = -1
            self.curMapNodeY = -1
            self.map = None
            self.act = 1
            self.ascension = 0
            self.floorNum = 0
            self.cc = 0
            self.curHp = 80
            self.maxHp = 80
            self.gold = 99
            self.potionCount = 0
            self.potionCapacity = 0
            self.potions = [None for _ in range(5)]
            self.relics = RelicContainer()
            self.deck = Deck()
            self.blueKey = False
            self.greenKey = False
            self.redKey = False
            self.regainControlAction = None

        SHRINE_CHANCE = 0.25


        DISABLECOLOSSEUM = True
        DISABLEMATCHANDKEEP = True
        DISABLEPRISMATICSHARD = True

        # ********* hidden from player *********


        # todo change these to fixed lists




        # ********* player information *********











# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        GameContext() = default
# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: GameContext(CharacterClass cc, ulong seed, int ascension) : seed(seed), neowRng(seed), treasureRng(seed), eventRng(seed), relicRng(seed), potionRng(seed), cardRng(seed), cardRandomRng(seed), merchantRng(seed), monsterRng(seed), shuffleRng(seed), miscRng(seed), mathUtilRng(seed-897897), cc(cc), map(new Map(Map::fromSeed(seed, ascension, 1, true))), ascension(ascension)
        def __init__(self, cc, seed, ascension):
            self._initialize_instance_fields()

            self.seed = seed
            self.neowRng = sts.Random(seed)
            self.treasureRng = sts.Random(seed)
            self.eventRng = sts.Random(seed)
            self.relicRng = sts.Random(seed)
            self.potionRng = sts.Random(seed)
            self.cardRng = sts.Random(seed)
            self.cardRandomRng = sts.Random(seed)
            self.merchantRng = sts.Random(seed)
            self.monsterRng = sts.Random(seed)
            self.shuffleRng = sts.Random(seed)
            self.miscRng = sts.Random(seed)
            self.mathUtilRng = sts.Random(seed-897897)
            self.cc = sts.CharacterClass(cc)
            self.map = Map(Map.fromSeed(seed, ascension, 1, True))
            self.ascension = ascension
            self.eventList.extend(EventPools.Act1.events)
            self.shrineList.extend(EventPools.Act1.shrines)
            if ascension < 15:
                self.specialOneTimeEventList.extend(EventPools.oneTimeEventsAsc0)
            else:
                self.specialOneTimeEventList.extend(EventPools.oneTimeEventsAsc15)

            self.generateMonsters()
            self.initRelics()
            self.initPlayer()

            self.potionCapacity = 3 if ascension < 11 else 2
            std::fill(self.potions.begin(), self.potions.end(), Potion.EMPTY_POTION_SLOT)

            self.curEvent = Event.NEOW
            self.info.neowRewards = Neow.getOptions(self.neowRng)
            self.screenState = ScreenState.EVENT_SCREEN

        def initFromSave(self, s):
            self.seed = s.seed

            self.outcome = GameOutcome.UNDECIDED
            self.ascension = int(s.ascension_level)
            self.act = s.act_num
            self.floorNum = s.floor_num
            self.curMapNodeX = s.room_x
            self.curMapNodeY = s.room_y

            self.cc = s.cc
            self.curHp = s.current_health
            self.maxHp = s.max_health
            self.gold = s.gold
            self.speedrunPace = s.play_time < (60 *13 + 20) # speedrun pace is below 13m20s

            self.treasureRng = Random(self.seed, s.treasure_seed_count)
            self.eventRng = Random(self.seed, s.event_seed_count)
            self.relicRng = Random(self.seed, s.relic_seed_count)
            self.potionRng = Random(self.seed, s.potion_seed_count)
            self.cardRng = Random(self.seed, s.card_seed_count)
            self.cardRandomRng = Random(self.seed, s.card_random_seed_count)
            self.merchantRng = Random(self.seed, s.merchant_seed_count)
            self.mathUtilRng = Random(self.seed, 0)
            self.merchantRng = Random(self.seed, s.merchant_seed_count) # arbitrary
            self.miscRng = Random(self.seed+self.floorNum)
            self.monsterRng = Random(self.seed, s.monster_seed_count)

            self.cardRarityFactor = s.card_random_seed_randomizer
            self.potionChance = s.potion_chance
            self.monsterChance = s.monsterChance
            self.shopChance = s.shopChance
            self.treasureChance = s.treasureChance

            if s.has_emerald_key:
                obtainKey.EMERALD_KEY
            if s.has_ruby_key:
                obtainKey.RUBY_KEY
            if s.has_sapphire_key:
                obtainKey.SAPPHIRE_KEY

            # this is a game bug, the shrine list is not stored in the save file
            self.shrineList.clear()
            if self.act == 1:
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
                self.shrineList.insert(self.shrineList.begin(), EventPools.Act1.shrines.begin(), EventPools.Act1.shrines.end())

            elif (self.act == 2) or (self.act == 3):
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
                self.shrineList.insert(self.shrineList.begin(), EventPools.Act2.shrines.begin(), EventPools.Act2.shrines.end())


# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.eventList.insert(self.eventList.begin(), s.event_list.begin(), s.event_list.end())
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.specialOneTimeEventList.insert(self.specialOneTimeEventList.begin(), s.one_time_event_list.begin(), s.one_time_event_list.end())

# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.commonRelicPool.insert(self.commonRelicPool.begin(), s.common_relics.begin(), s.common_relics.end())
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.uncommonRelicPool.insert(self.uncommonRelicPool.begin(), s.uncommon_relics.begin(), s.uncommon_relics.end())
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.rareRelicPool.insert(self.rareRelicPool.begin(), s.rare_relics.begin(), s.rare_relics.end())
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.shopRelicPool.insert(self.shopRelicPool.begin(), s.shop_relics.begin(), s.shop_relics.end())
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'insert' method in Python:
            self.bossRelicPool.insert(self.bossRelicPool.begin(), s.boss_relics.begin(), s.boss_relics.end())


            #    std::cout << "monsterListSize: " << s.monster_list.size() << std::endl
            #    std::cout << "eliteListSize: " << s.elite_monster_list.size() << std::endl

            self.boss = s.boss_list[0]
            if len(s.boss_list) > 1:
                self.secondBoss = s.boss_list[1]

            self.monsterListOffset = 0
            self.monsterList = fixed_list( [0] )
            for m in s.monster_list:
                if self.monsterList.size() == 16:
                    False = assert()
                self.monsterList.push_back(m)

            self.eliteMonsterListOffset = 0
            self.eliteMonsterList = fixed_list( [0] )
            for m in s.elite_monster_list:
                if self.eliteMonsterList.size() == 10:
                    False = assert()
                self.eliteMonsterList.push_back(m)

            encounter = 0

            if s.current_room == Save.RoomType.MONSTER_ROOM:
                self.curRoom = Room.MONSTER
                encounter = self.getMonsterForRoomCreation()

            elif s.current_room == Save.RoomType.MONSTER_ROOM_ELITE:
                self.curRoom = Room.ELITE
                encounter = self.getEliteForRoomCreation()

            elif s.current_room == Save.RoomType.MONSTER_ROOM_BOSS:
                self.curRoom = Room.BOSS
                encounter = self.boss

            else:
                std::cerr << "Only save files from the start of combat are supported right now. \n"
                False = assert() # other rooms not supported right now.

            self.deck.initFromSaveFile(s)

            self.initRelicsFromSave(s)

            self.potionCount = 0
            self.potionCapacity = 2 if self.ascension >= 11 else 3
            if self.relics.has(RelicId.POTION_BELT):
                self.potionCapacity += 2

            tempPotion = [0 for _ in range(6)]
            for i, unusedItem in enumerate(s.potions):
                p = s.potions[i]
                if p != Potion.EMPTY_POTION_SLOT:
                    self.potionCount += 1
                self.potions[i] = p

            self.map = Map(Map.fromSeed(self.seed, self.ascension, self.act, True))

# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#            this.regainControlAction = [](GameContext &gc)
            #            {
            #                gc.afterBattle()
            #            }
            self.enterBattle(encounter)

        def initRelicsFromSave(self, s):
            for i, unusedItem in enumerate(s.relics):
                r = s.relics[i]
                #        std::cout << getRelicName(r) << " " << s.relic_counters[i] << '\n'

                # todo lizard tail, and others
                relic = RelicInstance(r, s.relic_counters[i])
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: relics.add(relic);
                self.relics.add(sts.RelicInstance(relic))

        # const methods
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] const MapNode& getCurMapNode() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: const MapNode& getCurMapNode() const
        def getCurMapNode(self):
            return self.map.getNode(self.curMapNodeX, self.curMapNodeY)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int fractionMaxHp(float percent, HpType type=HpType::FLOOR) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int fractionMaxHp(float percent, HpType type =HpType::FLOOR) const
        def fractionMaxHp(self, percent, type = HpType.FLOOR):
            if type == HpType.ROUND:
                return int(round(float(self.maxHp) * percent))

            elif type == HpType.FLOOR:
                return int((float(self.maxHp) * percent))

            else:
                return int(math.ceil(float(self.maxHp) * percent))

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool hasRelic(RelicId r) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool hasRelic(RelicId r) const
        def hasRelic(self, r):
            return self.relics.has(r)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool hasKey(Key key) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool hasKey(Key key) const
        def hasKey(self, key):
            if key == Key.EMERALD_KEY:
                return self.greenKey

            elif key == Key.SAPPHIRE_KEY:
                return self.blueKey

            elif key == Key.RUBY_KEY:
                return self.redKey

            else:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                False = assert()
##endif
                return assert(False)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool hasLessThanTwoCampfireRelics() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool hasLessThanTwoCampfireRelics() const
        def hasLessThanTwoCampfireRelics(self):
            count = 0
            if self.hasRelic(RelicId.GIRYA):
                count += 1
            if self.hasRelic(RelicId.PEACE_PIPE):
                count += 1
            if self.hasRelic(RelicId.SHOVEL):
                count += 1
            return count < 2

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool relicCanSpawn(RelicId relic, bool shopRoom) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool relicCanSpawn(RelicId relic, bool shopRoom) const
        def relicCanSpawn(self, relic, shopRoom):

            if relic == RelicId.BOTTLED_FLAME:
                return self.deck.getCountMatching(lambda c : c.getType() == CardType.ATTACK and c.getRarity() != CardRarity.BASIC, 1) != 0

            elif relic == RelicId.BOTTLED_LIGHTNING:
                return self.deck.getCountMatching(lambda c : c.getType() == CardType.SKILL and c.getRarity() != CardRarity.BASIC, 1) != 0

            elif relic == RelicId.BOTTLED_TORNADO:
                return self.deck.getCountMatching(lambda c : c.getType() == CardType.POWER, 1) != 0

            elif relic == RelicId.BLACK_BLOOD:
                return self.relics.has(RelicId.BURNING_BLOOD)

            elif relic == RelicId.FROZEN_CORE:
                return self.hasRelic(RelicId.CRACKED_CORE)

            elif relic == RelicId.BURNING_BLOOD:
                return self.hasRelic(RelicId.BURNING_BLOOD)

            elif relic == RelicId.RING_OF_THE_SERPENT:
                return self.hasRelic(RelicId.RING_OF_THE_SNAKE)

            elif relic == RelicId.HOLY_WATER:
                return self.hasRelic(RelicId.PURE_WATER)

            elif relic == RelicId.TINY_CHEST:
                return self.floorNum <= 35

            elif (relic == RelicId.WING_BOOTS) or (relic == RelicId.MATRYOSHKA):
                return self.floorNum <= 40

            elif (relic == RelicId.GIRYA) or (relic == RelicId.PEACE_PIPE) or (relic == RelicId.SHOVEL):
                return self.floorNum < 48 and self.hasLessThanTwoCampfireRelics()

            elif (relic == RelicId.MAW_BANK) or (relic == RelicId.OLD_COIN) or (relic == RelicId.SMILING_MASK):
                return self.floorNum <= 48 and not shopRoom

            elif (relic == RelicId.ANCIENT_TEA_SET) or (relic == RelicId.CERAMIC_FISH) or (relic == RelicId.DARKSTONE_PERIAPT) or (relic == RelicId.DREAM_CATCHER) or (relic == RelicId.FROZEN_EGG) or (relic == RelicId.JUZU_BRACELET) or (relic == RelicId.MEAL_TICKET) or (relic == RelicId.MEAT_ON_THE_BONE) or (relic == RelicId.MOLTEN_EGG) or (relic == RelicId.OMAMORI) or (relic == RelicId.POTION_BELT) or (relic == RelicId.PRAYER_WHEEL) or (relic == RelicId.QUESTION_CARD) or (relic == RelicId.REGAL_PILLOW) or (relic == RelicId.SINGING_BOWL) or (relic == RelicId.THE_COURIER) or (relic == RelicId.TOXIC_EGG):
                return self.floorNum <= 48

            elif relic == RelicId.PRESERVED_INSECT:
                return self.floorNum <= 52

            else:
                return True

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool canAddOneTimeEvent(Event shrine) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool canAddOneTimeEvent(Event shrine) const
        def canAddOneTimeEvent(self, shrine):
            if shrine == Event.THE_DIVINE_FOUNTAIN:
                return self.deck.hasCurse()

            elif shrine == Event.DESIGNER_IN_SPIRE:
                return (self.act == 2 or self.act == 3) and self.gold >= 75

            elif shrine == Event.DUPLICATOR:
                return self.act == 2 or self.act == 3

            elif shrine == Event.FACE_TRADER:
                return self.act == 1 or self.act == 2

            elif shrine == Event.KNOWING_SKULL:
                return self.act == 2 and self.curHp > 12

            elif shrine == Event.NLOTH:
                return self.act == 2 and self.relics.size() >= 2

            elif shrine == Event.THE_JOUST:
                return self.act == 2 and self.gold >= 50

            elif shrine == Event.THE_WOMAN_IN_BLUE:
                return self.gold >= 50

            elif shrine == Event.SECRET_PORTAL:
                return self.act == 3 and not self.speedrunPace

            else:
                return True

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool canAddEvent(Event event) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool canAddEvent(Event event) const
        def canAddEvent(self, event):
            if (event == Event.DEAD_ADVENTURER) or (event == Event.HYPNOTIZING_COLORED_MUSHROOMS):
                return self.floorNum > 6

            elif event == Event.THE_MOAI_HEAD:
                    playerAtLessHalf = self.curHp <= math.trunc(self.maxHp / float(2))
                    return playerAtLessHalf or self.hasRelic(RelicId.GOLDEN_IDOL)

            elif event == Event.THE_CLERIC:
                return self.gold >= 35

            elif event == Event.OLD_BEGGAR:
                return self.gold >= 75

            elif event == Event.COLOSSEUM:
                return self.curMapNodeY > 7 and not sts.GameContext.DISABLECOLOSSEUM

            else:
                return True

        # initialization
        def initRelics(self):

            if self.cc == CharacterClass.IRONCLAD:
                self.commonRelicPool.extend(Ironclad.COMMONRELICPOOL)
                self.uncommonRelicPool.extend(Ironclad.UNCOMMONRELICPOOL)
                self.rareRelicPool.extend(Ironclad.RARERELICPOOL)
                self.shopRelicPool.extend(Ironclad.SHOPRELICPOOL)
                self.bossRelicPool.extend(Ironclad.BOSSRELICPOOL)

            elif self.cc == CharacterClass.SILENT:
                self.commonRelicPool.extend(Silent.COMMONRELICPOOL)
                self.uncommonRelicPool.extend(Silent.UNCOMMONRELICPOOL)
                self.rareRelicPool.extend(Silent.RARERELICPOOL)
                self.shopRelicPool.extend(Silent.SHOPRELICPOOL)
                self.bossRelicPool.extend(Silent.BOSSRELICPOOL)

            elif self.cc == CharacterClass.DEFECT:
                self.commonRelicPool.extend(Defect.COMMONRELICPOOL)
                self.uncommonRelicPool.extend(Defect.UNCOMMONRELICPOOL)
                self.rareRelicPool.extend(Defect.RARERELICPOOL)
                self.shopRelicPool.extend(Defect.SHOPRELICPOOL)
                self.bossRelicPool.extend(Defect.BOSSRELICPOOL)

            elif self.cc == CharacterClass.WATCHER:
                self.commonRelicPool.extend(Watcher.COMMONRELICPOOL)
                self.uncommonRelicPool.extend(Watcher.UNCOMMONRELICPOOL)
                self.rareRelicPool.extend(Watcher.RARERELICPOOL)
                self.shopRelicPool.extend(Watcher.SHOPRELICPOOL)
                self.bossRelicPool.extend(Watcher.BOSSRELICPOOL)


            java.Collections.shuffle(self.commonRelicPool.begin(), self.commonRelicPool.end(), java.Random(self.relicRng.nextLong()))
            java.Collections.shuffle(self.uncommonRelicPool.begin(), self.uncommonRelicPool.end(), java.Random(self.relicRng.nextLong()))
            java.Collections.shuffle(self.rareRelicPool.begin(), self.rareRelicPool.end(), java.Random(self.relicRng.nextLong()))
            java.Collections.shuffle(self.shopRelicPool.begin(), self.shopRelicPool.end(), java.Random(self.relicRng.nextLong()))
            java.Collections.shuffle(self.bossRelicPool.begin(), self.bossRelicPool.end(), java.Random(self.relicRng.nextLong()))


        def initPlayer(self):

            if self.ascension >= 10:
                self.deck.obtain(self, CardId.ASCENDERS_BANE)

            if self.cc == CharacterClass.IRONCLAD:
                self.maxHp = 80 if self.ascension < 14 else 75
                self.obtainRelic(RelicId.BURNING_BLOOD)
                self.deck.obtain(self, CardId.STRIKE_RED, 5)
                self.deck.obtain(self, CardId.DEFEND_RED, 4)
                self.deck.obtain(self, CardId.BASH)

            elif self.cc == CharacterClass.SILENT:
                self.maxHp = 70 if self.ascension < 14 else 66
                self.obtainRelic(RelicId.RING_OF_THE_SNAKE)
                self.deck.obtain(self, CardId.STRIKE_GREEN, 5)
                self.deck.obtain(self, CardId.DEFEND_GREEN, 5)
                self.deck.obtain(self, CardId.SURVIVOR)
                self.deck.obtain(self, CardId.NEUTRALIZE)

            elif self.cc == CharacterClass.DEFECT:
                self.maxHp = 75 if self.ascension < 14 else 71
                self.obtainRelic(RelicId.CRACKED_CORE)
                self.deck.obtain(self, CardId.STRIKE_BLUE, 4)
                self.deck.obtain(self, CardId.DEFEND_BLUE, 4)
                self.deck.obtain(self, CardId.ZAP)
                self.deck.obtain(self, CardId.DUALCAST)

            elif self.cc == CharacterClass.WATCHER:
                self.maxHp = 72 if self.ascension < 14 else 68
                self.obtainRelic(RelicId.PURE_WATER)
                self.deck.obtain(self, CardId.STRIKE_PURPLE, 4)
                self.deck.obtain(self, CardId.DEFEND_PURPLE, 4)
                self.deck.obtain(self, CardId.ERUPTION)
                self.deck.obtain(self, CardId.VIGILANCE)

            self.curHp = self.maxHp if self.ascension < 6 else round(float(self.maxHp) * 0.9)

        def generateMonsters(self):
            self.generateWeakMonsters()
            self.generateStrongMonsters()
            self.generateElites()
            self.generateBoss()

        def generateWeakMonsters(self):
            self.populateMonsterList(MonsterEncounterPool.WEAKENEMIES[self.act-1], MonsterEncounterPool.WEAKWEIGHTS[self.act - 1], MonsterEncounterPool.weakCount[self.act - 1],3 if self.act == 1 else 2)

        def generateStrongMonsters(self):
            self.populateFirstStrongEnemy(MonsterEncounterPool.STRONGENEMIES[self.act-1], MonsterEncounterPool.STRONGWEIGHTS[self.act-1], MonsterEncounterPool.strongCount[self.act-1])

            self.populateMonsterList(MonsterEncounterPool.STRONGENEMIES[self.act-1], MonsterEncounterPool.STRONGWEIGHTS[self.act-1], MonsterEncounterPool.strongCount[self.act-1], 12)

        def generateElites(self):
            for i in range(0, 10):
                if self.eliteMonsterList.empty():
                    self.eliteMonsterList.push_back(MonsterEncounterPool.elites[self.act-1][Globals.rollElite(self.monsterRng)])
                else:
                    toAdd = MonsterEncounterPool.elites[self.act-1][Globals.rollElite(self.monsterRng)]
                    if toAdd != self.eliteMonsterList.back():
                        self.eliteMonsterList.push_back(toAdd)
                    else:
                        i -= 1

        def generateBoss(self):
            bosses = [[ ME.THE_GUARDIAN, ME.HEXAGHOST, ME.SLIME_BOSS ], [ ME.AUTOMATON, ME.COLLECTOR, ME.CHAMP ], [ ME.AWAKENED_ONE, ME.TIME_EATER, ME.DONU_AND_DECA ]]

            indices = [0, 1, 2]

            java.Collections.shuffle(indices, indices+3, java.Random(self.monsterRng.randomLong()))

            self.boss = bosses[self.act-1][indices[0]]
            if self.act == 3 and self.ascension >= 20:
                self.secondBoss = bosses[self.act-1][indices[1]]

        def populateMonsterList(self, monsters, weights, monstersSize, numMonsters):
            for i in range(0, numMonsters):
                if self.monsterList.empty():
                    idx = Globals.rollWeightedIdx(self.monsterRng.random(), weights, monstersSize)
                    self.monsterList.push_back(monsters[idx])

                else:
                    idx = Globals.rollWeightedIdx(self.monsterRng.random(), weights, monstersSize)
                    toAdd = monsters[idx]

                    if toAdd != self.monsterList.back() and (self.monsterList.size() < 2 or toAdd != self.monsterList.get(self.monsterList.size()-2)):
                        self.monsterList.push_back(toAdd)

                    else:
                        i -= 1

        def populateFirstStrongEnemy(self, monsters, weights, monstersSize):
            lastMonster = self.monsterList.back()
            while True:
                idx = Globals.rollWeightedIdx(self.monsterRng.random(), weights, monstersSize)
                toAdd = monsters[idx]


                if (toAdd == MonsterEncounter.LARGE_SLIME) or (toAdd == MonsterEncounter.LOTS_OF_SLIMES):
                    if lastMonster == MonsterEncounter.SMALL_SLIMES:
                        continue

                elif toAdd == MonsterEncounter.THREE_LOUSE:
                    if lastMonster == MonsterEncounter.TWO_LOUSE:
                        continue

                elif toAdd == MonsterEncounter.CHOSEN_AND_BYRDS:
                    pass
                elif toAdd == MonsterEncounter.SENTRY_AND_SPHERE:
                    pass
                elif toAdd == MonsterEncounter.SNAKE_PLANT:
                    pass
                elif toAdd == MonsterEncounter.SNECKO:
                    pass
                elif toAdd == MonsterEncounter.CENTURION_AND_HEALER:
                    pass
                elif toAdd == MonsterEncounter.CULTIST_AND_CHOSEN:
                    pass
                elif toAdd == MonsterEncounter.THREE_CULTIST:
                    pass
                elif toAdd == MonsterEncounter.SHELLED_PARASITE_AND_FUNGI:
                    pass
                elif toAdd == MonsterEncounter.SPIRE_GROWTH:
                    pass
                elif toAdd == MonsterEncounter.TRANSIENT:
                    pass
                elif toAdd == MonsterEncounter.FOUR_SHAPES:
                    pass
                elif toAdd == MonsterEncounter.MAW:
                    pass
                elif toAdd == MonsterEncounter.SPHERE_AND_TWO_SHAPES:
                    pass
                elif toAdd == MonsterEncounter.JAW_WORM_HORDE:
                    pass
                elif toAdd == MonsterEncounter.WRITHING_MASS:
                    pass


                self.monsterList.push_back(toAdd)
                return

        # room setup
        def transitionToAct(self, targetAct):
            self.act = targetAct

            if self.cardRng.counter < 250:
                self.cardRng.setCounter(250)
            elif self.cardRng.counter < 500:
                self.cardRng.setCounter(500)
            elif self.cardRng.counter < 750:
                self.cardRng.setCounter(750)

            self.curMapNodeX = -1
            self.curMapNodeY = -1
            if targetAct == 2 or targetAct == 3:
                self.map = Map.fromSeed(self.seed, self.ascension, targetAct, (not hasKey.EMERALD_KEY))
            elif targetAct == 4:
                self.map = Map.act4Map()

            self.colorlessCardPool = baseColorlessPool
            if self.ascension >= 5:
                self.playerHeal(int(round(float((self.maxHp-self.curHp))*0.75)))
            else:
                self.playerHeal(self.maxHp)

            self.monsterListOffset = 0
            self.monsterList.clear()
            self.eliteMonsterListOffset = 0
            self.eliteMonsterList.clear()

            if targetAct == 4:
                self.boss = MonsterEncounter.THE_HEART
                self.eliteMonsterList.push_back(MonsterEncounter.SHIELD_AND_SPEAR)

            else:
                self.generateMonsters()

            self.monsterChance = 0.1
            self.shopChance = 0.03
            self.treasureChance = 0.02
            self.potionChance = 0

            self.eventList.clear()
            self.shrineList.clear()
            if targetAct == 2:
                self.eventList.extend(EventPools.Act2.events)
                self.shrineList.extend(EventPools.Act2.shrines)

            elif targetAct == 3:
                self.eventList.extend(EventPools.Act3.events)
                self.shrineList.extend(EventPools.Act3.shrines)

            self.screenState = ScreenState.MAP_SCREEN

        def transitionToMapNode(self, mapNodeX):
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: lastRoom = curRoom;
            self.lastRoom.copy_from(self.curRoom)
            self.curMapNodeX = mapNodeX
            self.floorNum += 1
            self.curMapNodeY += 1

            r = Random(self.seed + self.floorNum)
            self.miscRng = r
            self.shuffleRng = r
            self.cardRandomRng = r

# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
# C++ TO PYTHON CONVERTER NOTE: 'auto' variable declarations are not supported in Python:
# ORIGINAL LINE: regainControlAction = [](auto &gs)
#            this.regainControlAction = [](gs)
            #            {
            #                gs.screenState = ScreenState::MAP_SCREEN
            #            }

            if self.curMapNodeY == 15:
                self.curRoom = Room.BOSS
            else:
                self.curRoom = self.map.getNode(self.curMapNodeX, self.curMapNodeY).room
            self.relicsOnEnterRoom(Room(self.curRoom))

            self.curEvent = Event.INVALID
            if self.curRoom is Room.EVENT:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: curRoom = getEventRoomOutcomeHelper(lastRoom == Room::SHOP);
                self.curRoom.copy_from(self.getEventRoomOutcomeHelper(self.lastRoom is Room.SHOP))
                if self.curRoom is Room.EVENT:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: curEvent = generateEvent(eventRng);
                    self.curEvent = self.generateEvent(sts.Random(self.eventRng))

                elif (self.curRoom is Room.SHOP) or (self.curRoom is Room.MONSTER) or (self.curRoom is Room.TREASURE):
                    pass

                else:
                    False = assert()

            if self.curRoom is Room.EVENT:
                    self.setupEvent()

            elif self.curRoom is Room.BOSS:
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                    this.regainControlAction = [](GameContext &gc)
                    #                    {
                    #                        gc.afterBattle()
                    #                    }
                    self.enterBattle(self.boss)

            elif self.curRoom is Room.ELITE:
                    encounter = self.getEliteForRoomCreation()
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                    this.regainControlAction = [](GameContext &gc)
                    #                    {
                    #                        gc.afterBattle()
                    #                    }
                    self.enterBattle(encounter)

            elif self.curRoom is Room.MONSTER:
                    encounter = self.getMonsterForRoomCreation()
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                    this.regainControlAction = [](GameContext &gc)
                    #                    {
                    #                        gc.afterBattle()
                    #                    }
                    self.enterBattle(encounter)

            elif self.curRoom is Room.REST:
                    self.screenState = ScreenState.REST_ROOM

            elif self.curRoom is Room.SHOP:
                    self.screenState = ScreenState.SHOP_ROOM
                    self.info.shop.setup(self)

            elif self.curRoom is Room.TREASURE:
                    self.setupTreasureRoom()

            else:
                False = assert()


        def setupEvent(self):
            self.screenState = ScreenState.EVENT_SCREEN
            unfavorable = self.ascension >= 15

            if self.curEvent == Event.BIG_FISH:
                self.info.hpAmount0 = self.fractionMaxHp(1/3.0, HpType.FLOOR)

            elif self.curEvent == Event.BONFIRE_SPIRITS:
                self.openCardSelectScreen(CardSelectScreenType.BONFIRE_SPIRITS, 1)

            elif self.curEvent == Event.CURSED_TOME:
                self.info.eventData = 0

            elif self.curEvent == Event.DEAD_ADVENTURER:
                    self.info.phase = 0
                    self.info.rewards = [0, 1, 2]
                    java.Collections.shuffle(self.info.rewards.begin(), self.info.rewards.end(), self.miscRng.randomLong())

                    encounters = [ME.THREE_SENTRIES, ME.GREMLIN_NOB, ME.LAGAVULIN_EVENT]
                    self.info.encounter = encounters[self.miscRng.random(2)]

            elif self.curEvent == Event.DESIGNER_IN_SPIRE:
                self.info.upgradeOne = self.miscRng.randomBoolean()
                self.info.cleanUpIsRemoveCard = self.miscRng.randomBoolean()

            elif self.curEvent == Event.FACE_TRADER:
                self.info.hpAmount0 = max(1, self.fractionMaxHp(.10, HpType.FLOOR))

            elif self.curEvent == Event.FALLING:
                    counts = [0 for _ in range(3)]
                    for c in self.deck.cards:
                        counts[int(c.getType())] += 1

                    attacksIdx = self.miscRng.random(counts[0] - 1) if counts[0] > 0 else -1
                    skillsIdx = self.miscRng.random(counts[1] - 1) if counts[1] > 0 else -1
                    powersIdx = self.miscRng.random(counts[2] - 1) if counts[2] > 0 else -1

                    attackCount = 0
                    skillCount = 0
                    powerCount = 0

                    self.info.attackCardDeckIdx = -1
                    self.info.skillCardDeckIdx = -1
                    self.info.powerCardDeckIdx = -1

                    for i, unusedItem in enumerate(self.deck.cards):
                        if self.deck.cards.get(i).getType() == CardType.ATTACK:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (attackCount++ == attacksIdx)
                            if attackCount == attacksIdx:
                                attackCount += 1
                                self.info.attackCardDeckIdx = i
                            else:
                                attackCount += 1

                        elif self.deck.cards.get(i).getType() == CardType.SKILL:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (skillCount++ == skillsIdx)
                            if skillCount == skillsIdx:
                                skillCount += 1
                                self.info.skillCardDeckIdx = i
                            else:
                                skillCount += 1

                        elif self.deck.cards.get(i).getType() == CardType.POWER:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (powerCount++ == powersIdx)
                            if powerCount == powersIdx:
                                powerCount += 1
                                self.info.powerCardDeckIdx = i
                            else:
                                powerCount += 1


            elif self.curEvent == Event.FORGOTTEN_ALTAR:
                self.info.hpAmount0 = self.fractionMaxHp(0.35 if unfavorable else 0.25, HpType.ROUND)

            elif self.curEvent == Event.GHOSTS:
                self.info.hpAmount0 = min(self.maxHp-1, self.fractionMaxHp(0.5, HpType.CEIL))

            elif self.curEvent == Event.GOLDEN_IDOL:
                self.info.hpAmount0 = self.fractionMaxHp(0.35 if unfavorable else 0.25)
                self.info.hpAmount1 = self.fractionMaxHp(0.10 if unfavorable else 0.08)

            elif self.curEvent == Event.KNOWING_SKULL:
                self.info.hpAmount0 = 6
                self.info.hpAmount1 = 6
                self.info.hpAmount2 = 6

            elif self.curEvent == Event.LAB:
                    pReward = [0 for _ in range(3)]
                    pCount = 2
                    pReward[0] = getRandomPotion(self.potionRng, self.cc)
                    pReward[1] = getRandomPotion(self.potionRng, self.cc)
                    if not unfavorable:
                        pReward[2] = getRandomPotion(self.potionRng, self.cc)
                        pCount += 1
                    self.openCombatRewardScreen(Rewards(pReward, pCount))

            elif self.curEvent == Event.MATCH_AND_KEEP:
                    if sts.GameContext.DISABLEMATCHANDKEEP:
                        self.regainControl()

                    self.info.toSelectCards.clear()

                    cards = [Card() for _ in range(6)]
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards[0] = previewObtainCard(getRandomClassCardOfRarity(cardRng, cc, CardRarity::RARE));
                    cards[0].copy_from(self.previewObtainCard(getRandomClassCardOfRarity(self.cardRng, self.cc, CardRarity.RARE)))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards[1] = previewObtainCard(getRandomClassCardOfRarity(cardRng, cc, CardRarity::UNCOMMON));
                    cards[1].copy_from(self.previewObtainCard(getRandomClassCardOfRarity(self.cardRng, self.cc, CardRarity.UNCOMMON)))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards[2] = previewObtainCard(getRandomClassCardOfRarity(cardRng, cc, CardRarity::COMMON));
                    cards[2].copy_from(self.previewObtainCard(getRandomClassCardOfRarity(self.cardRng, self.cc, CardRarity.COMMON)))
                    if unfavorable:
                        cards[3] = getRandomCurse(self.cardRng)
                    else:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards[3] = previewObtainCard(returnColorlessCard(CardRarity::UNCOMMON));
                        cards[3].copy_from(self.previewObtainCard(self.returnColorlessCard(CardRarity.UNCOMMON)))
                    cards[4] = getRandomCurse(self.cardRng)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards[5] = previewObtainCard(getStartCardForEvent(cc));
                    cards[5].copy_from(self.previewObtainCard(getStartCardForEvent(self.cc)))

                    indices = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
                    java.Collections.shuffle(indices, indices+12, java.Random(self.miscRng.randomLong()))

                    self.info.toSelectCards.resize(12)
                    for i in range(0, 12):
                        cardIdx = indices[i]
                        gridX = math.fmod(i, 4)
                        gridY = math.fmod(i, 3)
                        selectIdx = gridY *4 + gridX
                        self.info.toSelectCards.set(selectIdx, {cards[cardIdx], -1})

                    self.info.eventData = 5 # attempts remaining

            elif self.curEvent == Event.NLOTH:
                    relicIdxs = [0 for _ in range(200)] # should be large enough
                    for i, unusedItem in enumerate(self.relics):
                        relicIdxs[i] = i
                    java.Collections.shuffle(relicIdxs, relicIdxs+self.relics.size(), java.Random(self.miscRng.randomLong()))
                    self.info.relicIdx0 = relicIdxs[0]
                    self.info.relicIdx1 = relicIdxs[1]

            elif self.curEvent == Event.SHINING_LIGHT:
                self.info.hpAmount0 = self.fractionMaxHp(0.30 if unfavorable else 0.20, HpType.ROUND)

            elif self.curEvent == Event.THE_CLERIC:
                self.info.hpAmount0 = self.fractionMaxHp(0.25)

            elif self.curEvent == Event.THE_LIBRARY:
                self.info.hpAmount0 = self.fractionMaxHp(0.20 if unfavorable else 0.33, HpType.ROUND)

            elif self.curEvent == Event.THE_MOAI_HEAD:
                self.info.hpAmount0 = self.fractionMaxHp(0.18 if unfavorable else 0.125, HpType.ROUND)

            elif self.curEvent == Event.THE_WOMAN_IN_BLUE:
                self.info.hpAmount0 = self.fractionMaxHp(0.05, HpType.CEIL)

            elif self.curEvent == Event.VAMPIRES:
                self.info.hpAmount0 = min(self.maxHp-1, self.fractionMaxHp(0.3, HpType.CEIL))

            elif self.curEvent == Event.WE_MEET_AGAIN:
                    self.info.potionIdx = self.getRandomPlayerPotionIdx()
                    if self.gold < 50:
                        self.info.gold = -1
                    else:
                        self.info.gold = self.miscRng.random(50, min(150, self.gold))
                    self.info.cardIdx = self.getRandomPlayerNonBasicCardIdx()

            elif self.curEvent == Event.WINDING_HALLS:
                self.info.hpAmount0 = self.fractionMaxHp(0.18 if unfavorable else 0.125, HpType.ROUND) # curHp loss
                self.info.hpAmount1 = self.fractionMaxHp(0.2 if unfavorable else 0.25, HpType.ROUND) # heal amount
                self.info.hpAmount2 = self.fractionMaxHp(0.05, HpType.ROUND) # maxHp loss

            elif self.curEvent == Event.WORLD_OF_GOOP:
                if unfavorable:
                    self.info.goldLoss = min(self.gold, self.miscRng.random(35, 75))
                else:
                    self.info.goldLoss = min(self.gold, self.miscRng.random(20, 50))


        def setupTreasureRoom(self):
            self.screenState = ScreenState.TREASURE_ROOM
            self.info.chestSize = getRandomChestSize(self.treasureRng)

            roll = self.treasureRng.random(99)
            self.info.haveGold = roll < chestGoldChances[int(self.info.chestSize)]

            tierChances = chestRelicTierChances[int(self.info.chestSize)]
            commonChance = tierChances[int(RelicTier.COMMON)]
            uncommonChance = tierChances[int(RelicTier.UNCOMMON)]
            if roll < commonChance:
                self.info.tier = RelicTier.COMMON
            elif roll < commonChance + uncommonChance:
                self.info.tier = RelicTier.UNCOMMON
            else:
                self.info.tier = RelicTier.RARE

        def enterBossTreasureRoom(self):
            self.floorNum += 1
            r = Random(self.seed+self.floorNum)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: miscRng = r;
            self.miscRng.copy_from(r)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: shuffleRng = r;
            self.shuffleRng.copy_from(r)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cardRandomRng = r;
            self.cardRandomRng.copy_from(r)

            self.relicsOnEnterRoom(Room.BOSS_TREASURE)

            self.curRoom = Room.BOSS_TREASURE
            self.screenState = ScreenState.BOSS_RELIC_REWARDS

            for i in range(0, 3):
                self.info.bossRelics[i] = self.returnRandomRelic(RelicTier.BOSS)

# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#            this.regainControlAction = [:=](GameContext &gc)
            #            {
            #                gc.transitionToAct(act+1)
            #            }

        def enterAct3VictoryRoom(self):
            self.floorNum += 1
            self.relicsOnEnterRoom(Room.BOSS_TREASURE)

            if hasKey.SAPPHIRE_KEY and hasKey.EMERALD_KEY and hasKey.RUBY_KEY:
                self.transitionToAct(4)
            else:
                self.outcome = GameOutcome.PLAYER_VICTORY

        def enterBattle(self, encounter):
            self.screenState = ScreenState.BATTLE
            self.info.encounter = encounter
            if self.skipBattles:
                self.afterBattle()

        def afterBattle(self):
            if self.hasRelic(RelicId.FACE_OF_CLERIC):
                self.playerIncreaseMaxHp(1)

            if self.curRoom is Room.MONSTER:
                    self.regainControlAction = returnToMapAction
                    reward = self.createCombatReward()
                    if self.info.stolenGold != 0:
                        reward.addGold(self.info.stolenGold)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: openCombatRewardScreen(reward);
                    self.openCombatRewardScreen(sts.Rewards(reward))

            elif self.curRoom is Room.ELITE:
                self.regainControlAction = returnToMapAction
                self.openCombatRewardScreen(self.createEliteCombatReward())

            elif self.curRoom is Room.BOSS:
                if self.act == 1 or self.act == 2:
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                    this.regainControlAction = [:=](GameContext &gc)
                    #                        {
                    #                            gc.enterBossTreasureRoom()
                    #                        }
                    self.openCombatRewardScreen(self.createBossCombatReward())

                elif self.act == 3:

                    if self.ascension >= 20 and self.info.encounter == self.boss:
                        # go to second boss
                        self.floorNum += 1
                        r = Random(self.seed + self.floorNum)
                        self.miscRng = r
                        self.shuffleRng = r
                        self.cardRandomRng = r
                        self.relicsOnEnterRoom(Room(self.curRoom))

# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                        this.regainControlAction = [](GameContext &gc)
                        #                            {
                        #                                gc.afterBattle()
                        #                            }
                        self.enterBattle(self.secondBoss)

                    else:
                        # go to next act
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                        this.regainControlAction = [](GameContext &gc)
                        #                            {
                        #                                gc.transitionToAct(gc.act + 1)
                        #                            }
                        self.enterAct3VictoryRoom()

                elif self.act == 4:
                    self.outcome = GameOutcome.PLAYER_VICTORY


            elif self.curRoom is Room.EVENT:
                if self.curEvent == Event.MYSTERIOUS_SPHERE:
                    reward = Rewards()
                    reward.addGold(self.info.gold)
                    reward.addRelic(self.info.bossRelics[0])
                    self.addPotionRewards(reward)
                    reward.addCardReward(self.createCardReward(Room.EVENT))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: openCombatRewardScreen(reward);
                    self.openCombatRewardScreen(sts.Rewards(reward))
                    self.regainControlAction = returnToMapAction
                else:
                    self.regainControl()

            else:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                False = assert()
##endif

        # actions
        def obtainCard(self, c, count = 1):
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: deck.obtain(*this, c, count);
            self.deck.obtain(self, sts.Card(c), count)

        def obtainGold(self, amount):
            if self.relics.has(R.ECTOPLASM):
                return

            self.gold += amount
            if self.relics.has(R.BLOODY_IDOL):
                self.playerHeal(5)

        def obtainKey(self, key):
            if key == Key.EMERALD_KEY:
                self.greenKey = True

            elif key == Key.SAPPHIRE_KEY:
                self.blueKey = True

            elif key == Key.RUBY_KEY:
                self.redKey = True

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                False = assert()
##endif

        def obtainPotion(self, p):
            if self.relics.has(RelicId.SOZU) or self.potionCount == self.potionCapacity:
                return

            i = 0
            while i < self.potionCapacity:
                if self.potions[i] == Potion.EMPTY_POTION_SLOT:
                    self.potions[i] = p
                    self.potionCount += 1
                    return
                i += 1

            # todo, just ignoring if there is not enough space for now
            ##ifdef sts_asserts
            #    assert(false)
            ##endif


        # relics with screens will call regainControl() after obtaining a relic with a screen
        def obtainRelic(self, r):
            #    std::cout << "obtained relic: " << relicNames[static_cast<int>(r)] << std::endl
            #    std::cout << *this << std::endl

            if self.relics.has(r):
                return False

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert not self.relics.has(r)
##endif

            self.relics.setHasRelic(r, True)

            relicData = 0
            opensScreen = False


            if r == RelicId.ASTROLABE:
                    self.info.toSelectCards.clear()
                    self.deck.addMatchingToSelectList(self.info.toSelectCards, lambda c : c.canTransform())

                    if self.info.toSelectCards.empty():
                        break # if we have no cards at all

                    self.openCardSelectScreen(CardSelectScreenType.TRANSFORM_UPGRADE, min(self.info.toSelectCards.size(), 3), False)
                    opensScreen = True

            elif r == RelicId.BLACK_BLOOD:
                    if self.hasRelic(RelicId.BURNING_BLOOD):
                        self.relics.remove(RelicId.BURNING_BLOOD)

            elif r == RelicId.BOTTLED_FLAME:
                    opensScreen = Globals.obtainBottleHelper(self, CardType.ATTACK)

            elif r == RelicId.BOTTLED_LIGHTNING:
                    opensScreen = Globals.obtainBottleHelper(self, CardType.SKILL)

            elif r == RelicId.BOTTLED_TORNADO:
                    opensScreen = Globals.obtainBottleHelper(self, CardType.POWER)

            elif r == RelicId.CAULDRON:
                    pReward = [0 for _ in range(5)]
                    for i in range(0, 5):
                        pReward[i] = getRandomPotion(self.potionRng, self.cc)
                    self.openCombatRewardScreen(Rewards(pReward, 5))
                    opensScreen = True

            elif r == RelicId.CALLING_BELL:
                    self.deck.obtain(self, CardId.CURSE_OF_THE_BELL)
                    reward = Rewards()
                    reward.addRelic(self.returnRandomScreenlessRelic(RelicTier.COMMON))
                    reward.addRelic(self.returnRandomScreenlessRelic(RelicTier.UNCOMMON))
                    reward.addRelic(self.returnRandomScreenlessRelic(RelicTier.RARE))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: openCombatRewardScreen(reward);
                    self.openCombatRewardScreen(sts.Rewards(reward))
                    opensScreen = True

            elif r == RelicId.LEES_WAFFLE:
                    self.playerIncreaseMaxHp(7)
                    self.playerHeal(self.maxHp)

            elif r == RelicId.NEOWS_LAMENT:
                    relicData = 3

            elif r == RelicId.MANGO:
                    self.playerIncreaseMaxHp(14)

            elif r == RelicId.MAW_BANK:
                    relicData = 1

            elif r == RelicId.OMAMORI:
                    relicData = 2

            elif r == RelicId.PANDORAS_BOX:
                    transformCount = 0
                    for i in range(self.deck.size()-1, -1, -1):
                        if self.deck.cards.get(i).isStarterStrikeOrDefend():
                            self.deck.remove(self, i)
                            transformCount += 1

                    toObtain = [0 for _ in range(15)] # 15 is more strikes/defends then we can ever have right?

                    for i in range(0, transformCount):
                        toObtain[i] = getTrulyRandomCard(self.cardRandomRng, self.cc)

                    for i in range(transformCount-1, -1, -1):
                        self.deck.obtain(self, toObtain[i])

            elif r == RelicId.PEAR:
                self.playerIncreaseMaxHp(10)

            elif r == RelicId.PRISMATIC_SHARD:
                    # todo if not defect: masterMaxOrbs = 1

            elif r == RelicId.POTION_BELT:
                    self.potionCapacity += 2
                    self.potions[self.potionCapacity-1] = Potion.EMPTY_POTION_SLOT
                    self.potions[self.potionCapacity-2] = Potion.EMPTY_POTION_SLOT

            elif r == RelicId.STRAWBERRY:
                    self.playerIncreaseMaxHp(7)

            elif r == RelicId.TINY_HOUSE:
                    self.relics.relics.append(RelicInstance(r, 0))
                    upgradeCards = self.deck.getUpgradeableCardIdxs()
                    java.Collections.shuffle(upgradeCards.begin(), upgradeCards.end(), java.Random(self.miscRng.nextLong()))

                    if not upgradeCards.empty():
                        self.deck.upgrade(upgradeCards.get(0))

                    self.playerIncreaseMaxHp(5)
                    reward = Rewards()
                    reward.addGold(50)
                    reward.addPotion(getRandomPotion(self.miscRng, self.cc))
                    reward.addCardReward(self.createCardReward(Room(self.curRoom)))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: openCombatRewardScreen(reward);
                    self.openCombatRewardScreen(sts.Rewards(reward))
                    opensScreen = True

            elif r == RelicId.WAR_PAINT:
                Globals.upgradeRandomCardsMatching(self, CardType.SKILL)

            elif r == RelicId.WHETSTONE:
                Globals.upgradeRandomCardsMatching(self, CardType.ATTACK)


            self.relics.relics.append(RelicInstance(r, relicData))
            return opensScreen

        def returnRandomRelic(self, tier, shopRoom = False, fromFront = True):
            retVal = RelicId.INVALID
            vec = None


            if tier == RelicTier.COMMON:
                if not self.commonRelicPool != 0:
                    retVal = self.returnRandomRelic(RelicTier.UNCOMMON, shopRoom)
                else:
                    vec = self.commonRelicPool

            elif tier == RelicTier.UNCOMMON:
                if not self.uncommonRelicPool != 0:
                    retVal = self.returnRandomRelic(RelicTier.RARE, shopRoom)
                else:
                    vec = self.uncommonRelicPool

            elif tier == RelicTier.RARE:
                if not self.rareRelicPool != 0:
                    retVal = RelicId.CIRCLET
                else:
                    vec = self.rareRelicPool

            elif tier == RelicTier.SHOP:
                if not self.shopRelicPool != 0:
                    retVal = self.returnRandomRelic(RelicTier.UNCOMMON, shopRoom)
                else:
                    vec = self.shopRelicPool

            elif tier == RelicTier.BOSS:
                if not self.bossRelicPool != 0:
                    retVal = RelicId.RED_CIRCLET
                else:
                    vec = self.bossRelicPool


            if fromFront:
                retVal = vec[0]
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'erase' method in Python:
                vec.erase(vec.begin())
            else:
                retVal = vec[len(vec) - 1]
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'erase' method in Python:
                vec.erase(vec.end()-1)

            canSpawn = self.relicCanSpawn(retVal, shopRoom)
            if canSpawn:
                return retVal
            else:
                return self.returnRandomRelic(tier, shopRoom, False)

        def returnNonCampfireRelic(self, tier, shopRoom = False):
            relic = 0
            loop_condition = True
            while loop_condition:
                relic = self.returnRandomRelic(tier, shopRoom)
                loop_condition = Globals.isCampfireRelic(relic)
            return relic

        def returnRandomScreenlessRelic(self, tier, shopRoom = False):
            r = 0
            loop_condition = True
            while loop_condition:
                r = self.returnRandomRelic(tier, shopRoom)
                loop_condition = r == RelicId.BOTTLED_FLAME or r == RelicId.BOTTLED_LIGHTNING or r == RelicId.BOTTLED_TORNADO or r == RelicId.WHETSTONE

            return r

        def previewObtainCard(self, card):
            if card.getType() == CardType.ATTACK:
                if self.hasRelic(RelicId.MOLTEN_EGG):
                    card.upgrade()

            elif card.getType() == CardType.SKILL:
                if self.hasRelic(RelicId.TOXIC_EGG):
                    card.upgrade()

            elif card.getType() == CardType.POWER:
                if self.hasRelic(RelicId.FROZEN_EGG):
                    card.upgrade()

# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: return card;
            return sts.Card(card)

        def relicsOnEnterRoom(self, room):
            if self.hasRelic(RelicId.MAW_BANK) and self.relics.getRelicValue(RelicId.MAW_BANK) != 0:
                self.obtainGold(12)

            if room is Room.REST:
                if self.hasRelic(RelicId.ETERNAL_FEATHER):
                    self.playerHeal(math.trunc(self.deck.size() / float(5 * 3)))

            elif room is Room.EVENT:
                if self.hasRelic(RelicId.SSSERPENT_HEAD):
                    self.obtainGold(50)


        def rollCardRarity(self, room):
            roll = self.cardRng.random(99) + self.cardRarityFactor

            if room is Room.BOSS:
                return CardRarity.RARE

            rareChance = (10 if room is Room.ELITE else 3)
            uncommonChance = (40 if room is Room.ELITE else 37)

            if room is not Room.REST and self.hasRelic(RelicId.NLOTHS_GIFT):
                rareChance = rareChance * 3

            if roll < rareChance:
                return CardRarity.RARE

            elif roll < rareChance + uncommonChance:
                return CardRarity.UNCOMMON

            else:
                return CardRarity.COMMON

        def returnTrulyRandomCardFromAvailable(self, rng, exclude):
            color = getCardColor(exclude)
            if color == CardColor.COLORLESS:
                    idx = rng.random(int((len(self.colorlessCardPool)-2)))
                    if self.colorlessCardPool[idx] == exclude:
                        return self.colorlessCardPool[idx + 1]
                    else:
                        return self.colorlessCardPool[idx]

            elif color == CardColor.CURSE:
                    return getRandomCurse(self.cardRng)

            else:
                    pool = TransformCardPool.getPoolForClass(self.cc)
                    poolSize = TransformCardPool.getPoolSizeForClass(self.cc)

                    excludeInPool = cardRarities[int(exclude)] != CardRarity.BASIC and self.cc is color

                    if excludeInPool:
                        idx = rng.random(poolSize-2)
                        if pool[idx] == exclude:
                            return pool[idx+1]
                        else:
                            return pool[idx]
                    else:
                        return pool[rng.random(poolSize-1)]

        def getTransformedCard(self, rng, exclude, autoUpgrade = False):
            color = getCardColor(exclude)

            if color == CardColor.CURSE:
                return getRandomCurse(rng, exclude)
            elif color == CardColor.COLORLESS:
                return returnTrulyRandomColorlessCardFromAvailable(rng, exclude)

            transformCard = self.returnTrulyRandomCardFromAvailable(rng, exclude)
            return Card(transformCard,1 if autoUpgrade else 0)

        def returnColorlessCard(self, rarity):
            java.Collections.shuffle(self.colorlessCardPool.begin(), self.colorlessCardPool.end(), java.Random(self.shuffleRng.randomLong()))
            for c in self.colorlessCardPool:
                if getCardRarity(c) == rarity:
                    return c
            return CardId.SWIFT_STRIKE

        def getRandomPlayerPotionIdx(self):
            if self.potionCount <= 0:
                return -1

            potionIdxs = fixed_list()
            i = 0
            while i < self.potionCapacity:
                if self.potions[i] != Potion.EMPTY_POTION_SLOT:
                    potionIdxs.push_back(i)
                i += 1
            java.Collections.shuffle(potionIdxs.begin(), potionIdxs.end(), java.Random(self.miscRng.nextLong()))
            return potionIdxs.get(0)

        def getRandomPlayerNonBasicCardIdx(self):
            cardIdxs = fixed_list()

            for i, unusedItem in enumerate(self.deck.cards):
                c = self.deck.cards.get(i)
                if c.getRarity() != CardRarity.BASIC and c.getType() != CardType.CURSE:
                    cardIdxs.push_back(i)

            if cardIdxs.empty():
                return -1

            java.Collections.shuffle(cardIdxs.begin(), cardIdxs.end(), java.Random(self.miscRng.randomLong()))

            retIdx = cardIdxs.get(0)
            for i in range(0, retIdx):
                if self.deck.cards.get(i) == self.deck.cards.get(retIdx):
                    return i
            return retIdx

        def getMonsterForRoomCreation(self):
            if self.monsterListOffset == self.monsterList.size():
                # the number generated here won't be accurate but it should not matter
                # monster list is empty
                self.monsterListOffset = 0
                self.monsterList.clear()
                self.generateStrongMonsters() # game generates 12
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: return monsterList[monsterListOffset++];
            temp_var = self.monsterList.get(self.monsterListOffset)
            self.monsterListOffset += 1
            return temp_var

        def getEliteForRoomCreation(self):
            if self.eliteMonsterListOffset == self.eliteMonsterList.size():
                # the number generated here won't be accurate but it should not matter
                # monster list is empty
                self.eliteMonsterListOffset = 0
                self.eliteMonsterList.clear()
                self.generateElites() # game generates 10
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: return eliteMonsterList[eliteMonsterListOffset++];
            temp_var = self.eliteMonsterList.get(self.eliteMonsterListOffset)
            self.eliteMonsterListOffset += 1
            return temp_var

        def addPotionRewards(self, r):
            # assume if in a monsters room, they didnt escape
            chance = 40 + self.potionChance

            if self.hasRelic(RelicId.WHITE_BEAST_STATUE):
                chance = 100

            rewardsSize = r.potionCount + r.relicCount + r.goldRewardCount + r.cardRewardCount
            if rewardsSize >= 4:
                chance = 0

            if self.potionRng.random(99) >= chance:
                self.potionChance += 10

            else:
                r.addPotion(returnRandomPotion(self.potionRng, self.cc))
                self.potionChance -= 10

        def createCardReward(self, room):
            numCards = 3
            if self.relics.has(RelicId.QUESTION_CARD):
                numCards += 1
            if self.relics.has(RelicId.BUSTED_CROWN):
                numCards -= 2

            cards = [0 for _ in range(4)]
            rewardRarities = [0 for _ in range(4)]

            for i in range(0, numCards):
                rarity = self.rollCardRarity(Room(room))

                rewardRarities[i] = rarity
                if rarity == CardRarity.COMMON:
                    self.cardRarityFactor = max(self.cardRarityFactor - 1, -40)

                elif rarity == CardRarity.RARE:
                    self.cardRarityFactor = 5


                id = 0
                hasDuplicate = True
                while hasDuplicate:

                    if self.hasRelic(RelicId.PRISMATIC_SHARD) and not sts.GameContext.DISABLEPRISMATICSHARD:
                        id = getAnyColorCard(self.cardRng, rarity)
                    else:
                        id = getRandomClassCardOfRarity(self.cardRng, self.cc, rarity)

                    hasDuplicate = False
                    x = 0
                    while x < i:
                        if cards[x] == id:
                            hasDuplicate = True
                            break
                        x += 1
                cards[i] = id

            cardUpgradedChance = getUpgradedCardChance(self.act, self.ascension)

            reward = CardReward()
            for i in range(0, numCards):
                if rewardRarities[i] != CardRarity.RARE and self.cardRng.randomBoolean(cardUpgradedChance):
                    reward.push_back(Card(cards[i],1 if True else 0))
                else:
                    reward.push_back(self.previewObtainCard(cards[i]))
            return CardReward(reward)

        def createColorlessCardReward(self):
            numCards = 3
            if self.hasRelic(RelicId.QUESTION_CARD):
                numCards += 1
            if self.hasRelic(RelicId.BUSTED_CROWN):
                numCards -= 2

            reward = CardReward()
            reward.resize(numCards)

            for i in range(0, numCards):
                rarity = CardRarity.RARE if self.cardRng.randomBoolean(COLORLESS_RARE_CHANCE) else CardRarity.UNCOMMON
                if rarity == CardRarity.COMMON:
                    self.cardRarityFactor = max(self.cardRarityFactor - 1, -40)

                elif rarity == CardRarity.RARE:
                    self.cardRarityFactor = 5


                id = 0
                hasDuplicate = True
                while hasDuplicate:
                    id = getColorlessCardFromPool(self.cardRng, rarity)

                    hasDuplicate = False
                    x = 0
                    while x < i:
                        if reward[x].id == id:
                            hasDuplicate = True
                            break
                        x += 1
                reward[i] = self.previewObtainCard(id)
            return CardReward(reward)

        def createCombatReward(self):
            reward = Rewards()
            goldAmt = self.treasureRng.random(10, 20)
            if self.hasRelic(RelicId.GOLDEN_IDOL):
                goldAmt += round(float(goldAmt) * 0.25)
            reward.addGold(goldAmt)
            self.addPotionRewards(reward)
            reward.addCardReward(self.createCardReward(Room.MONSTER)) # TODO Prayer wheel
            if self.hasRelic(RelicId.PRAYER_WHEEL):
                reward.addCardReward(self.createCardReward(Room.MONSTER))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: return reward;
            return sts.Rewards(reward)

        def createEliteCombatReward(self):
            reward = Rewards()

            goldAmt = self.treasureRng.random(25, 35)
            if self.hasRelic(RelicId.GOLDEN_IDOL):
                goldAmt += round(float(goldAmt) * 0.25)
            reward.addGold(goldAmt)

            reward.addRelic(self.returnRandomRelic(returnRandomRelicTierElite(self.relicRng)))
            if self.hasRelic(RelicId.BLACK_STAR):
                reward.addRelic(self.returnNonCampfireRelic(returnRandomRelicTierElite(self.relicRng)))
            reward.emeraldKey = self.map.burningEliteX == self.curMapNodeX and self.map.burningEliteY == self.curMapNodeY
            self.addPotionRewards(reward)
            reward.addCardReward(self.createCardReward(Room.ELITE))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: return reward;
            return sts.Rewards(reward)

        def createBossCombatReward(self):
            reward = Rewards()
            # room == BOSS
            goldAmt = 100 + self.miscRng.random(-5, 5)
            if self.ascension >= 13:
                goldAmt = int(round(float(goldAmt) * 0.75))
            if self.hasRelic(RelicId.GOLDEN_IDOL):
                goldAmt += round(float(goldAmt) * 0.25)
            reward.addGold(goldAmt)
            if self.act < 3:
                self.addPotionRewards(reward)
                reward.addCardReward(self.createCardReward(Room.BOSS))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: return reward;
            return sts.Rewards(reward)

        def getShrine(self, eventRngCopy):
            tempLength = 0
            tempShrines = [0 for _ in range(20)]

            for shrine in self.shrineList:
                if shrine != Event.MATCH_AND_KEEP or not sts.GameContext.DISABLEMATCHANDKEEP:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: tempShrines[tempLength++] = shrine;
                    tempShrines[tempLength] = shrine
                    tempLength += 1

            for event in self.specialOneTimeEventList:
                if self.canAddOneTimeEvent(event):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: tempShrines[tempLength++] = event;
                    tempShrines[tempLength] = event
                    tempLength += 1

            idx = eventRngCopy.random(tempLength-1)
            shrine = tempShrines[idx]
            didRemove = False
            for it in self.shrineList:
                if it is shrine:
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'erase' method in Python:
                    self.shrineList.erase(it)
                    didRemove = True
                    break
            for it in self.specialOneTimeEventList:
                if it is shrine:
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'erase' method in Python:
                    self.specialOneTimeEventList.erase(it)
                    didRemove = True
                    break
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            didRemove = assert()
##endif
            return shrine

        def getEvent(self, eventRngCopy):
            tempLength = 0
            tempEvents = [0 for _ in range(14)]

            for event in self.eventList:
                if self.canAddEvent(event):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: tempEvents[tempLength++] = event;
                    tempEvents[tempLength] = event
                    tempLength += 1

            if tempLength == 0:
                return self.getShrine(self.eventRng)

            idx = eventRngCopy.random(tempLength-1)
            event = tempEvents[idx]

            eventListPos = std::find(self.eventList.begin(), self.eventList.end(), event)
# C++ TO PYTHON CONVERTER TASK: There is no direct equivalent to the STL vector 'erase' method in Python:
            self.eventList.erase(eventListPos)
            return tempEvents[idx]

        def generateEvent(self, eventRngCopy):
            if eventRngCopy.random(1.0) < sts.GameContext.SHRINE_CHANCE:
                if not self.shrineList and not self.specialOneTimeEventList:
                    if not self.eventList:
                        return sts.Event.INVALID
                    else:
                        return self.getEvent(eventRngCopy)

                else:
                    return self.getShrine(eventRngCopy)
            else:
                return self.getEvent(eventRngCopy)

        def getEventRoomOutcomeHelper(self, lastRoomWasShop):
            roll = self.eventRng.random()
            choice = Room.NONE

            if self.hasRelic(RelicId.TINY_CHEST):
                value = self.relics.getRelicValueRef(RelicId.TINY_CHEST)
                if value == 3:
                    value = 0
                    choice = sts.Room.TREASURE
                else:
                    value += 1

            if choice is not sts.Room.TREASURE:
                monsterSize = int((self.monsterChance * 100))
                shopSize = (0 if lastRoomWasShop else int((self.shopChance * 100))) + monsterSize
                treasureSize = int((self.treasureChance * 100)) + shopSize

                idx = int((roll * 100))

                if idx < monsterSize:
                    choice = Room.MONSTER
                elif idx < shopSize:
                    choice = Room.SHOP
                elif idx < treasureSize:
                    choice = Room.TREASURE
                else:
                    choice = Room.EVENT

            if choice is Room.MONSTER:
                if self.hasRelic(RelicId.JUZU_BRACELET):
                    choice = Room.EVENT
                self.monsterChance = 0.1
            else:
                self.monsterChance += 0.1

            if choice is Room.SHOP:
                self.shopChance = 0.03
            else:
                self.shopChance += 0.03

            if choice is Room.TREASURE:
                self.treasureChance = 0.02
            else:
                self.treasureChance += 0.02

            return Room(choice)

        # actions
        def damagePlayer(self, amount):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert amount > 0
##endif
            if amount <= 5 and self.relics.has(RelicId.TORII):
                amount = 1
            self.playerLoseHp(amount)

        def playerLoseHp(self, amount):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert amount > 0
##endif

            if self.hasRelic(RelicId.TUNGSTEN_ROD):
                amount -= 1
            self.curHp -= amount

            if self.curHp <= 0:
                self.curHp = 0
                self.playerOnDie()

        def playerOnDie(self):
            if self.hasRelic(RelicId.MARK_OF_THE_BLOOM):
                self.outcome = GameOutcome.PLAYER_LOSS
                return

            hasBark = self.relics.has(RelicId.SACRED_BARK)
            it = std::find(self.potions.begin(), self.potions.end(), Potion.FAIRY_POTION)
            if it is not self.potions.end():
                *it = Potion.EMPTY_POTION_SLOT
                self.potionCount -= 1
                self.curHp = max(1, int((0.6 if hasBark else 0.3 * float(self.maxHp))))
                return

            if self.hasRelic(RelicId.LIZARD_TAIL):
                lizardValue = self.relics.getRelicValueRef(RelicId.LIZARD_TAIL)
                if lizardValue != 0:
                    lizardValue = 0
                    self.curHp = max(1, math.trunc(self.maxHp / float(2)))
                    return

            self.outcome = GameOutcome.PLAYER_LOSS

        def playerHeal(self, amount):
            if self.hasRelic(RelicId.MARK_OF_THE_BLOOM):
                return
            self.curHp = min(self.curHp + amount, self.maxHp)

        def playerIncreaseMaxHp(self, amount):
            self.maxHp += amount
            self.playerHeal(amount)

        def loseGold(self, amount, inShop = False):
            if inShop and self.relics.has(RelicId.MAW_BANK):
                self.relics.getRelicValueRef(RelicId.MAW_BANK) = 0
            self.gold = max(0, self.gold-amount)

        def loseMaxHp(self, amount):
            self.maxHp -= amount
            self.curHp = min(self.curHp, self.maxHp)


        def drinkPotion(self, p):
            if p == Potion.BLOOD_POTION:
                self.playerHeal(self.fractionMaxHp(0.40 if self.hasRelic(RelicId.SACRED_BARK) else 0.20))

            elif p == Potion.ENTROPIC_BREW:
                    randPotions = [0 for _ in range(5)]
                    i = 0
                    while i < self.potionCapacity:
                        randPotions[i] = returnRandomPotion(self.potionRng, self.cc)
                        if self.potions[i] == Potion.EMPTY_POTION_SLOT:
                            self.potions[i] = randPotions[i]
                        i += 1
                    self.potionCount = self.potionCapacity

            elif p == Potion.FRUIT_JUICE:
                self.playerIncreaseMaxHp(10 if self.hasRelic(RelicId.SACRED_BARK) else 5)


            if p != Potion.BLOOD_POTION and p != Potion.ENTROPIC_BREW and p != Potion.FRUIT_JUICE:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                False = assert()
##endif

        def drinkPotionAtIdx(self, idx):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert not(self.curEvent == Event.WE_MEET_AGAIN and self.screenState == ScreenState.EVENT_SCREEN)
            potions = Potion.EMPTY_POTION_SLOT
            potions = Potion.INVALID
##endif
            p = potions[idx]
            self.discardPotionAtIdx(idx)
            self.drinkPotion(p)

        def discardPotionAtIdx(self, idx):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert not(self.curEvent == Event.WE_MEET_AGAIN and self.screenState == ScreenState.EVENT_SCREEN)
            potions = Potion.EMPTY_POTION_SLOT
            potions = Potion.INVALID
##endif
            potions[idx] = Potion.EMPTY_POTION_SLOT
            self.potionCount -= 1


        def openTreasureRoomChest(self):
            reward = Rewards()

            if self.hasRelic(RelicId.MATRYOSHKA) and self.relics.getRelicValue(RelicId.MATRYOSHKA) > 0:
                matryoshkaTier = getMatryoshkaRelicTier(self.relicRng)
                relic = self.returnRandomRelic(auto(matryoshkaTier), False)
                reward.addRelic(relic)
                self.relics.getRelicValueRef(RelicId.MATRYOSHKA) -= 1

            if self.hasRelic(RelicId.CURSED_KEY):
                self.deck.obtain(self, getRandomCurse(self.cardRng))

            if self.info.haveGold:
                amount = chestGoldAmounts[int(self.info.chestSize)]
                amount = round(self.treasureRng.random(amount *0.9, amount *1.1))
                reward.addGold(amount)

            relic = self.returnRandomRelic(self.info.tier, False)
            if self.hasRelic(RelicId.NLOTHS_HUNGRY_FACE) and self.relics.getRelicValue(RelicId.NLOTHS_HUNGRY_FACE) > 0:
                self.relics.getRelicValueRef(RelicId.NLOTHS_HUNGRY_FACE) -= 1
            else:
                reward.addRelic(relic)

            if not hasKey.SAPPHIRE_KEY:
                reward.sapphireKey = True

# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: openCombatRewardScreen(reward);
            self.openCombatRewardScreen(sts.Rewards(reward))

        def selectScreenTransform(self):
            rng = None
            if self.info.transformRng == RngReference.MISC_RNG:
                rng = self.miscRng
            elif self.info.transformRng == RngReference.CARD_RNG:
                rng = self.cardRng
            elif self.info.transformRng == RngReference.NEOW_RNG:
                rng = self.neowRng
            else:
                False = assert()

            self.deck.removeSelected(self, self.info.haveSelectedCards)
            for c in self.info.haveSelectedCards:
                transformCard = self.getTransformedCard(rng, c.card.id)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: deck.obtain(*this, transformCard);
                self.deck.obtain(self, sts.Card(transformCard))
            self.info.transformRng = RngReference.CARD_RNG

        def openCombatRewardScreen(self, reward):
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: info.rewardsContainer = reward;
            self.info.rewardsContainer.copy_from(reward)
            self.screenState = ScreenState.REWARDS

        def openCardSelectScreen(self, type, selectCount, initSelectCards = True):
            self.screenState = ScreenState.CARD_SELECT
            self.info.selectScreenType = type
            self.info.toSelectCount = selectCount
            self.info.haveSelectedCards.clear()

            if initSelectCards:
                self.info.toSelectCards.clear()

                if type == CardSelectScreenType.DUPLICATE:
                    for i, unusedItem in enumerate(self.deck):
                        self.info.toSelectCards.push_back(SelectScreenCard(self.deck.cards.get(i), i))


                elif (type == CardSelectScreenType.REMOVE) or (type == CardSelectScreenType.BONFIRE_SPIRITS) or (type == CardSelectScreenType.TRANSFORM):
                    for i, unusedItem in enumerate(self.deck):
                        c = self.deck.cards.get(i)
                        if c.canTransform() and not self.deck.isCardBottled(i):
                            self.info.toSelectCards.push_back(SelectScreenCard(c, i))

                elif type == CardSelectScreenType.UPGRADE:
                    self.deck.addMatchingToSelectList(self.info.toSelectCards, lambda c : c.canUpgrade())

                elif type == CardSelectScreenType.TRANSFORM_UPGRADE:
                    self.deck.addMatchingToSelectList(self.info.toSelectCards, lambda c : c.canTransform())


        # interface methods
        def chooseNeowOption(self, o):

            if o.d == Neow.Drawback.TEN_PERCENT_HP_LOSS:
                self.maxHp = int((0.9 * float(self.maxHp)))
                self.curHp = min(self.curHp, self.maxHp)

            elif o.d == Neow.Drawback.NO_GOLD:
                self.gold = 0

            elif o.d == Neow.Drawback.PERCENT_DAMAGE:
                self.curHp = math.trunc(self.curHp / float(10 * 7))

            elif o.d == Neow.Drawback.LOSE_STARTER_RELIC:
                self.relics.remove(getStarterRelicForClass(self.cc))


            if o.d == Neow.Drawback.CURSE:
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
# C++ TO PYTHON CONVERTER NOTE: 'auto' variable declarations are not supported in Python:
# ORIGINAL LINE: regainControlAction = [](auto &gc)
#                this.regainControlAction = [](gc)
                #                {
                #                    int roll = gc.cardRng.random(static_cast<int>(9))
                #                    gc.deck.obtain(gc, curseCardPool[roll])
                #                    gc.screenState = ScreenState::MAP_SCREEN
                #                    gc.regainControlAction = returnToMapAction
                #                }
            else:
                self.regainControlAction = returnToMapAction

            if o.r == Neow.Bonus.THREE_CARDS:
                self.regainControlAction.invoke(self) # hack because curse is received first
                self.regainControlAction = returnToMapAction
                self.openCombatRewardScreen(Neow.getCardReward(self.neowRng, self.cc, False))

            elif o.r == Neow.Bonus.ONE_RANDOM_RARE_CARD:
                    idx = self.neowRng.random(RarityCardPool.getPoolSize(self.cc, CardRarity.RARE) - 1)
                    self.deck.obtain(self, RarityCardPool.getCardFromPool(self.cc, CardRarity.RARE, idx), 1)
                    self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.REMOVE_CARD:
                self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

            elif o.r == Neow.Bonus.UPGRADE_CARD:
                self.openCardSelectScreen(CardSelectScreenType.UPGRADE, 1)

            elif o.r == Neow.Bonus.TRANSFORM_CARD:
                self.info.transformRng = RngReference.NEOW_RNG
                self.openCardSelectScreen(CardSelectScreenType.TRANSFORM, 1)

            elif o.r == Neow.Bonus.RANDOM_COLORLESS:
                self.regainControlAction.invoke(self) # hack because curse is received first
                self.regainControlAction = returnToMapAction
                self.openCombatRewardScreen(Neow.getColorlessCardReward(self.neowRng, self.cardRng, False))

            elif o.r == Neow.Bonus.THREE_SMALL_POTIONS:
                    self.createCardReward(Room.EVENT)
                    potions = [0 for _ in range(3)]
                    for i in range(0, 3):
                        potions[i] = getRandomPotion(self.potionRng, self.cc)
                    self.openCombatRewardScreen(Rewards(potions, 3))

            elif o.r == Neow.Bonus.RANDOM_COMMON_RELIC:
                self.obtainRelic(self.returnRandomRelic(RelicTier.COMMON, False, True))
                self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.TEN_PERCENT_HP_BONUS:
                self.maxHp += int((float(self.maxHp) * 0.1))
                self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.THREE_ENEMY_KILL:
                self.obtainRelic(RelicId.NEOWS_LAMENT)
                self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.HUNDRED_GOLD:
                self.obtainGold(100)
                self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.RANDOM_COLORLESS_2:
                self.regainControlAction.invoke(self) # hack because curse is received first
                self.regainControlAction = returnToMapAction
                self.openCombatRewardScreen(Neow.getColorlessCardReward(self.neowRng, self.cardRng, True))

            elif o.r == Neow.Bonus.REMOVE_TWO:
                self.openCardSelectScreen(CardSelectScreenType.REMOVE, 2)

            elif o.r == Neow.Bonus.ONE_RARE_RELIC:
                self.obtainRelic(self.returnRandomRelic(RelicTier.RARE, False, True))
                self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.THREE_RARE_CARDS:
                self.regainControlAction.invoke(self) # hack because curse is received first
                self.regainControlAction = returnToMapAction
                self.openCombatRewardScreen(Neow.getCardReward(self.neowRng, self.cc, True))

            elif o.r == Neow.Bonus.TWO_FIFTY_GOLD:
                self.obtainGold(250)
                self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.TRANSFORM_TWO_CARDS:
                self.info.transformRng = RngReference.NEOW_RNG
                self.openCardSelectScreen(CardSelectScreenType.TRANSFORM, 2)
                    roll = self.cardRng.random(int(9))
                    self.deck.obtain(self, curseCardPool[roll])
                self.regainControlAction = returnToMapAction

            elif o.r == Neow.Bonus.TWENTY_PERCENT_HP_BONUS:
                self.maxHp += int((float(self.maxHp) * 0.2))
                self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.BOSS_RELIC:
                    openedScreen = self.obtainRelic(self.returnRandomRelic(RelicTier.BOSS, False, True))
                    if not openedScreen:
                        self.regainControlAction.invoke(self)

            elif o.r == Neow.Bonus.INVALID:
                False = assert()


        def chooseBossRelic(self, idx):
            if idx >= 0 and idx < 3:
                screenUp = self.obtainRelic(self.info.bossRelics[idx])
                if not screenUp:
                    self.regainControl()
            elif idx == 3:
                self.regainControl()

        def chooseEventOption(self, idx):
            #    regainControlAction = [](auto &gs) {
            #        gs.screenState = ScreenState::MAP_SCREEN
            #        gs.regainControlAction = nullptr
            #    }
            unfavorable = self.ascension >= 15

            if self.curEvent == Event.NEOW:
                self.chooseNeowOption(self.info.neowRewards[idx])

            elif self.curEvent == Event.OMINOUS_FORGE:
                    if idx == 0:
                        self.openCardSelectScreen(CardSelectScreenType.UPGRADE, 1)

                    elif idx == 1:
                        self.deck.obtain(self, CardId.PAIN)
                        self.obtainRelic(RelicId.WARPED_TONGS)
                        self.regainControl()

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.PLEADING_VAGRANT:
                    if idx == 0:
                            self.loseGold(85)
                            r = self.returnRandomScreenlessRelic(returnRandomRelicTier(self.relicRng, self.act), False)
                            self.obtainRelic(r)
                            self.regainControl()

                    elif idx == 1:
                            r = self.returnRandomScreenlessRelic(returnRandomRelicTier(self.relicRng, self.act), False)
                            self.obtainRelic(r)
                            self.deck.obtain(self, CardId.SHAME)
                            self.regainControl()

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.ANCIENT_WRITING:
                    if idx == 0:
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

                    elif idx == 1:
                        self.deck.upgradeStrikesAndDefends()
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.OLD_BEGGAR:
                    if idx == 0:
                        self.loseGold(75)
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.BIG_FISH:
                    if idx == 0:
                            self.playerHeal(self.fractionMaxHp(1 / 3.0))
                            self.regainControl()

                    elif idx == 1:
                            self.playerIncreaseMaxHp(5)
                            self.regainControl()

                    elif idx == 2:
                            r = self.returnRandomScreenlessRelic(returnRandomRelicTier(self.relicRng, self.act))
                            self.obtainRelic(r)
                            self.deck.obtain(self, CardId.REGRET)
                            self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.COLOSSEUM: # todo
                self.regainControl()

            elif self.curEvent == Event.CURSED_TOME:
# C++ TO PYTHON CONVERTER TASK: Python does not have an equivalent to references to value types:
# ORIGINAL LINE: int &phase = info.eventData;
                    phase = self.info.eventData
                    if idx == 0:
                        phase += 1

                    elif idx == 1:
                        self.regainControl()

                    elif (idx == 2) or (idx == 3) or (idx == 4):
                        self.playerLoseHp(phase)
                        phase += 1

                    elif idx == 5:
                            self.playerLoseHp(15 if unfavorable else 10)
                            res = self.miscRng.random(2)
                            book = RelicId.NECRONOMICON if res == 0 else (RelicId.ENCHIRIDION if res == 1 else RelicId.NILRYS_CODEX)

                            reward = Rewards()
                            reward.addRelic(book)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: openCombatRewardScreen(reward);
                            self.openCombatRewardScreen(sts.Rewards(reward))

                    elif idx == 6:
                            self.playerLoseHp(3)
                            self.regainControl()


            elif self.curEvent == Event.DEAD_ADVENTURER:
                    if idx == 0:
                        encounterChance = self.info.phase * 25 + (35 if unfavorable else 25)
                        didEncounter = self.miscRng.random(99) < encounterChance

                        if didEncounter:
                            goldAmt = self.miscRng.random(25, 35)
                            addRelic = False
                            combatRewardRelic = 0

                            for i in range(self.info.phase, 3):
                                if self.info.rewards[i] == 0:
                                    goldAmt += 30
                                elif self.info.rewards[i] == 2:
                                    addRelic = True
                                    combatRewardRelic = self.returnRandomRelic(returnRandomRelicTier(self.relicRng, 1))

# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                            this.regainControlAction = [:=](GameContext &gc)
                            #                            {
                            #                                Rewards reward
                            #                                reward.addGold(goldAmt)
                            #                                if (addRelic)
                            #                                {
                            #                                    reward.addRelic(combatRewardRelic)
                            #                                }
                            #                                reward.addCardReward(createCardReward(Room::EVENT))
                            #                                addPotionRewards(reward)
                            #                                gc.openCombatRewardScreen(reward)
                            #                                gc.regainControlAction = returnToMapAction
                            #                            }
                            self.enterBattle(self.info.encounter)

                        else:
                            reward = self.info.rewards[self.info.phase]
                            if reward == 0:
                                # GOLD
                                self.obtainGold(30)

                            elif reward == 2:
                                # RELIC
                                relic = self.returnRandomScreenlessRelic(returnRandomRelicTier(self.relicRng, 1))
                                self.obtainRelic(relic)

                            self.info.phase += 1

                    elif idx == 1:
                        self.regainControl()

                    else:
                        std::cerr << idx << " " << self << std::endl
                        False = assert()

            elif self.curEvent == Event.DESIGNER_IN_SPIRE:
                    if idx == 0:
                        self.loseGold(50 if unfavorable else 40)
                        self.openCardSelectScreen(CardSelectScreenType.UPGRADE, 1)

                    elif idx == 1:
                        self.deck.upgradeRandomCards(self.miscRng, 2)
                        self.regainControl()

                    elif idx == 2:
                        self.loseGold(75 if unfavorable else 60)
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

                    elif idx == 3:
                        self.loseGold(75 if unfavorable else 60)
                        self.deck.transformRandomCards(self.miscRng, 2) # TODO
                        self.regainControl()

                    elif (idx == 3) or (idx == 4):
                        self.loseGold(110 if unfavorable else 90)
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                        this.regainControlAction = [:=](GameContext &gc)
                        #                            {
                        #                                gc.deck.upgradeRandomCards(miscRng, 1)
                        #                                returnToMapAction(gc)
                        #                            }
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

                    elif (idx == 3) or (idx == 4) or (idx == 5):
                        self.playerLoseHp(5 if unfavorable else 3)
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.AUGMENTER:
                    if idx == 0:
                        self.deck.obtain(self, CardId.JAX)
                        self.regainControl()

                    elif idx == 1:
                        self.info.transformRng = RngReference.MISC_RNG
                        self.openCardSelectScreen(CardSelectScreenType.TRANSFORM, 2)

                    elif idx == 2:
                        self.obtainRelic(RelicId.MUTAGENIC_STRENGTH)
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.DUPLICATOR:
                    if idx == 0:
                        self.openCardSelectScreen(CardSelectScreenType.DUPLICATE, 1)

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.FACE_TRADER:
                    if idx == 0:
                        self.obtainGold(50 if unfavorable else 75)
                        self.damagePlayer(max(self.fractionMaxHp(.10), 1))
                        self.regainControl()

                    elif idx == 1:
                        self.obtainRelic(getRandomFace(self.relics, self.miscRng))
                        self.regainControl()

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.FALLING:
                    if idx == 0:
                        # Warn!! replace might go around future obtainRelic logic
                        self.deck.remove(self, self.info.skillCardDeckIdx)
                        self.regainControl()

                    elif idx == 1:
                        self.deck.remove(self, self.info.powerCardDeckIdx)
                        self.regainControl()

                    elif idx == 2:
                        self.deck.remove(self, self.info.attackCardDeckIdx)
                        self.regainControl()

                    elif idx == 3:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.FORGOTTEN_ALTAR:
                    if idx == 0:
                        # Warn!! replace might go around future obtainRelic logic
                        self.relics.replaceRelic(RelicId.GOLDEN_IDOL, RelicId.BLOODY_IDOL)
                        self.regainControl()

                    elif idx == 1:
                        self.playerIncreaseMaxHp(5)
                        self.playerLoseHp(self.info.hpAmount0)
                        self.regainControl()

                    elif idx == 2:
                        self.deck.obtain(self, CardId.DECAY)
                        self.regainControl()

                    else:
                        False = assert()


            elif self.curEvent == Event.THE_DIVINE_FOUNTAIN:
                    if idx == 0:
                        for i in range(self.deck.size()-1, -1, -1):
                            if self.deck.cards.get(i).getType() == CardType.CURSE and self.deck.cards.get(i).canTransform():
                                self.deck.remove(self, i)
                        self.regainControl()

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.GHOSTS:
                    if idx == 0:
                        self.loseMaxHp(self.info.hpAmount0)
                        self.deck.obtain(self, CardId.APPARITION,3 if unfavorable else 5)
                        self.regainControl()

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.GOLDEN_IDOL:
                    if idx == 0:
                        self.obtainRelic(RelicId.GOLDEN_IDOL)

                    elif idx == 1:
                        self.regainControl()

                    elif idx == 2:
                        self.obtainCard(CardId.INJURY)
                        self.regainControl()

                    elif idx == 3:
                        self.damagePlayer(self.info.hpAmount0)
                        self.regainControl()

                    elif idx == 4:
                        self.loseMaxHp(self.info.hpAmount1)
                        self.regainControl()


            elif (self.curEvent == Event.GOLDEN_IDOL) or (self.curEvent == Event.GOLDEN_SHRINE):
                    if idx == 0:
                        self.obtainGold(50 if unfavorable else 100)
                        self.regainControl()

                    elif idx == 1:
                        self.obtainGold(275)
                        self.deck.obtain(self, CardId.REGRET)
                        self.regainControl()

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.WING_STATUE:
                    if idx == 0:
                        self.damagePlayer(7)
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

                    elif idx == 1:
                        self.obtainGold(self.miscRng.random(50, 80))
                        self.regainControl()

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.KNOWING_SKULL:
                    if idx == 0:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: playerLoseHp(info.hpAmount0++);
                        self.playerLoseHp(self.info.hpAmount0)
                        self.info.hpAmount0 += 1
                        self.obtainGold(90)

                    elif idx == 1:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: playerLoseHp(info.hpAmount1++);
                        self.playerLoseHp(self.info.hpAmount1)
                        self.info.hpAmount1 += 1
                        self.deck.obtain(self, self.returnColorlessCard(CardRarity.UNCOMMON))

                    elif idx == 2:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: playerLoseHp(info.hpAmount2++);
                        self.playerLoseHp(self.info.hpAmount2)
                        self.info.hpAmount2 += 1
                        self.obtainPotion(getRandomPotion(self.potionRng, self.cc))

                    elif idx == 3:
                        self.playerLoseHp(6)
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.LAB:
                # no actions to take
                False = assert()

            elif self.curEvent == Event.THE_SSSSSERPENT:
                    if idx == 0:
                        self.obtainGold(150 if unfavorable else 175)
                        self.deck.obtain(self, CardId.DOUBT)
                        self.regainControl()

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.LIVING_WALL:
                    if idx == 0:
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)
                    elif idx == 1:
                        self.info.transformRng = RngReference.MISC_RNG
                        self.openCardSelectScreen(CardSelectScreenType.TRANSFORM, 1)
                    elif idx == 2:
                        self.openCardSelectScreen(CardSelectScreenType.UPGRADE, 1)

                    else:
                        False = assert()

            elif self.curEvent == Event.MASKED_BANDITS:
                    if idx == 0:
                        self.loseGold(self.gold)
                        self.regainControl()

                    elif idx == 1:
                        goldAmt = self.miscRng.random(25, 35)
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
# C++ TO PYTHON CONVERTER NOTE: 'auto' variable declarations are not supported in Python:
# ORIGINAL LINE: regainControlAction = [goldAmt](auto &gc)
#                        this.regainControlAction = [goldAmt](gc)
                        #                        {
                        #                            Rewards reward
                        #                            reward.addGold(goldAmt)
                        #                            reward.addRelic(RelicId::RED_MASK)
                        #                            reward.addCardReward(gc.createCardReward(Room::EVENT))
                        #                            gc.openCombatRewardScreen(reward)
                        #                            gc.regainControlAction = returnToMapAction
                        #                        }
                        self.enterBattle(MonsterEncounter.MASKED_BANDITS_EVENT)

                    else:
                        False = assert()

            elif self.curEvent == Event.MATCH_AND_KEEP:
                # handled elsewhere
                False = assert()

            elif self.curEvent == Event.MINDBLOOM:
                    if idx == 0:
                            bosses = [(int)MonsterEncounter.THE_GUARDIAN, MonsterEncounter.HEXAGHOST, (int)MonsterEncounter.SLIME_BOSS]
                            java.Collections.shuffle(bosses, bosses+3, java.Random(self.miscRng.randomLong()))

                            goldAmt = 25 if unfavorable else 50
                            rareRelic = self.returnRandomRelic(RelicTier.RARE)
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                            this.regainControlAction = [:=](GameContext &gc)
                            #                            {
                            #                                Rewards reward
                            #                                reward.addGold(goldAmt)
                            #                                reward.addRelic(rareRelic)
                            #                                addPotionRewards(reward)
                            #                                reward.addCardReward(gc.createCardReward(Room::EVENT))
                            #                                gc.openCombatRewardScreen(reward)
                            #                                gc.regainControlAction = returnToMapAction
                            #                            }
                            self.enterBattle(bosses[0])

                    elif idx == 1:
                        for i, unusedItem in enumerate(self.deck.cards):
                            if self.deck.cards.get(i).canUpgrade():
                                self.deck.upgrade(i)

                        self.obtainRelic(RelicId.MARK_OF_THE_BLOOM)
                        self.regainControl()

                    elif idx == 2:
                        self.obtainGold(999)
                        self.deck.obtain(self, CardId.NORMALITY, 2)
                        self.regainControl()

                    elif idx == 3:
                        self.playerHeal(self.maxHp)
                        self.deck.obtain(self, CardId.DOUBT)
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.HYPNOTIZING_COLORED_MUSHROOMS:
                    if idx == 0:
                        goldAmt = self.miscRng.random(20, 30)
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                        this.regainControlAction = [:=](GameContext &gc)
                        #                        {
                        #                            Rewards reward
                        #                            reward.addGold(goldAmt)
                        #                            reward.addRelic(RelicId::ODD_MUSHROOM)
                        #                            addPotionRewards(reward)
                        #                            reward.addCardReward(createCardReward(Room::EVENT))
                        #                            gc.openCombatRewardScreen(reward)
                        #                            gc.regainControlAction = returnToMapAction
                        #                        }
                        self.enterBattle(MonsterEncounter.MUSHROOMS_EVENT)

                    elif idx == 1:
                        self.obtainGold(50 if unfavorable else 99)
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.MYSTERIOUS_SPHERE:
                    if idx == 0:
                        goldAmt = self.miscRng.random(45, 55)
                        rareRelic = self.returnRandomScreenlessRelic(RelicTier.RARE)
                        self.info.bossRelics[0] = rareRelic
                        self.info.gold = goldAmt
# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
#                        this.regainControlAction = [:=](GameContext &gc)
                        #                        {
                        #                            gc.afterBattle()
                        #                        }
                        self.enterBattle(MonsterEncounter.MYSTERIOUS_SPHERE_EVENT)

                    elif idx == 1:
                        self.obtainGold(50 if unfavorable else 99)
                        self.regainControl()

                    else:
                        False = assert()


            elif self.curEvent == Event.THE_NEST:
                    if idx == 0:
                        self.obtainGold(50 if unfavorable else 99)
                        self.regainControl()

                    elif idx == 1:
                        self.damagePlayer(6)
                        self.deck.obtain(self, CardId.RITUAL_DAGGER)
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.NLOTH:
                    if idx == 0:
                        self.relics.remove(self.relics.relics[self.info.relicIdx0].id) # maybe add a removeAtIdx method?
                        self.obtainRelic(RelicId.NLOTHS_GIFT)
                        self.regainControl()

                    elif idx == 1:
                        self.relics.remove(self.relics.relics[self.info.relicIdx1].id) # maybe add a removeAtIdx method?
                        self.obtainRelic(RelicId.NLOTHS_GIFT)
                        self.regainControl()

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.NOTE_FOR_YOURSELF:
                if idx == 0:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: deck.obtain(*this, noteForYourselfCard);
                    self.deck.obtain(self, sts.Card(self.noteForYourselfCard))
                    self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)
                elif idx == 1:
                    self.regainControl()
                else:
                    False = assert()

            elif self.curEvent == Event.PURIFIER:
                    if idx == 0:
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.SCRAP_OOZE:
                if idx == 0:
                    self.damagePlayer(5 if unfavorable else 3)
                    roll = self.miscRng.random(99)
                    relicChance = self.info.eventData *10 + 25
                    if roll >= 99 - relicChance:
                        relic = self.returnRandomScreenlessRelic(returnRandomRelicTier(self.relicRng, 1))
                        self.obtainRelic(relic)
                        self.regainControl()
                    else:
                        self.info.eventData += 1

                elif idx == 1:
                    self.regainControl()

                else:
                    False = assert()

            elif self.curEvent == Event.SECRET_PORTAL:
                    if idx == 0:
                        self.curMapNodeY = 14
                        self.transitionToMapNode(0)

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.SENSORY_STONE:
                    if idx < 0 or idx > 3:
                        False = assert()

                    if idx == 1:
                        self.playerLoseHp(5)
                    elif idx == 2:
                        self.playerLoseHp(10)

                    reward = Rewards()
                    for i in range(0, idx + 1):
                        reward.addCardReward(self.createColorlessCardReward())
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: openCombatRewardScreen(reward);
                    self.openCombatRewardScreen(sts.Rewards(reward))

            elif self.curEvent == Event.SHINING_LIGHT:
                    if idx == 0:
                        self.damagePlayer(self.info.hpAmount0)
                        list = self.deck.getUpgradeableCardIdxs()
                        java.Collections.shuffle(list.begin(), list.end(), java.Random(self.miscRng.randomLong()))
                        if not list.empty():
                            if list.size() == 1:
                                self.deck.upgrade(list.get(0))
                            else:
                                self.deck.upgrade(list.get(0))
                                self.deck.upgrade(list.get(1))
                        self.regainControl()

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.THE_CLERIC:
                    if idx == 0:
                        self.loseGold(35)
                        self.playerHeal(self.info.hpAmount0)
                        self.regainControl()

                    elif idx == 1:
                        self.loseGold(75 if unfavorable else 50)
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.THE_JOUST:
                    ownerWins = self.miscRng.randomBoolean(0.3)
                    self.loseGold(50)
                    if idx == 0:
                        if not ownerWins:
                            self.obtainGold(100)

                    elif idx == 1:
                        if ownerWins:
                            self.obtainGold(250)

                    else:
                        False = assert()
                    self.regainControl()

            elif self.curEvent == Event.THE_LIBRARY:
                    if idx == 0:
                        std::bitset<384> selectedBits
                        self.info.toSelectCards.clear()
                        self.info.toSelectCards.resize(20)
                        # cards are added in displayed in reverse order that they are generated
                        for i in range(19, -1, -1):
                            id = 0
                            loop_condition = True
                            while loop_condition:
                                id = getRandomClassCardOfRarity(self.cardRng, self.cc, self.rollCardRarity(Room.EVENT))
                                loop_condition = selectedBits.test(int(id))
                            selectedBits.set(int(id))
                            self.info.toSelectCards.set(i, self.previewObtainCard(id))
                        self.openCardSelectScreen(CardSelectScreenType.OBTAIN, 1, False)

                    elif idx == 1:
                        self.playerHeal(self.info.hpAmount0)
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.THE_MAUSOLEUM:
                    if idx == 0:
                        result = self.miscRng.randomBoolean()
                        if result is not None or unfavorable:
                            self.deck.obtain(self, CardId.WRITHE)
                        self.regainControl()

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.THE_MOAI_HEAD:
                    if idx == 0:
                        self.loseMaxHp(self.fractionMaxHp(0.18 if unfavorable else 0.125, HpType.ROUND))
                        if self.maxHp < 1:
                            self.maxHp = 1
                        if self.curHp <= 0 and self.hasRelic(RelicId.MARK_OF_THE_BLOOM):
                            self.outcome = GameOutcome.PLAYER_LOSS
                        self.playerHeal(self.maxHp)
                        self.regainControl()


                    elif idx == 1:
                        self.obtainGold(333)
                        self.relics.remove(RelicId.GOLDEN_IDOL)
                        self.regainControl()

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.THE_WOMAN_IN_BLUE:
                    pArr = [0 for _ in range(3)]
                    if idx == 0:
                            pArr[0] = getRandomPotion(self.potionRng, self.cc)
                            self.openCombatRewardScreen(Rewards(pArr, 1))
                    elif idx == 1:
                            pArr[0] = getRandomPotion(self.potionRng, self.cc)
                            pArr[1] = getRandomPotion(self.potionRng, self.cc)
                            self.openCombatRewardScreen(Rewards(pArr, 2))
                    elif idx == 2:
                            pArr[0] = getRandomPotion(self.potionRng, self.cc)
                            pArr[1] = getRandomPotion(self.potionRng, self.cc)
                            pArr[2] = getRandomPotion(self.potionRng, self.cc)
                            self.openCombatRewardScreen(Rewards(pArr, 3))
                    elif idx == 3:
                            if unfavorable:
                                hpLoss = math.ceil(float(self.maxHp) * 0.05)
                                self.playerLoseHp(hpLoss)
                                self.regainControl()
                            else:
                                self.regainControl()

            elif self.curEvent == Event.TOMB_OF_LORD_RED_MASK:
                    if idx == 0:
                            self.obtainGold(222)
                            self.regainControl()
                    elif idx == 1:
                            self.loseGold(self.gold)
                            self.obtainRelic(RelicId.RED_MASK)
                            self.regainControl()
                    elif idx == 2:
                            self.regainControl()
                    else:
                        False = assert()


            elif self.curEvent == Event.TRANSMORGRIFIER:
                    if idx == 0:
                        self.info.transformRng = RngReference.MISC_RNG
                        self.openCardSelectScreen(CardSelectScreenType.TRANSFORM, 1)

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.UPGRADE_SHRINE:
                    if idx == 0:
                        self.openCardSelectScreen(CardSelectScreenType.UPGRADE, 1)

                    elif idx == 1:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.VAMPIRES:
                    if idx == 0:
                        self.relics.remove(RelicId.BLOOD_VIAL)
                    elif idx == 1:
                        maxHpLoss = min(self.maxHp-1, self.fractionMaxHp(0.3, HpType.CEIL))
                        self.loseMaxHp(maxHpLoss)

                    if idx == 0 or idx == 1:
                        self.deck.removeAllMatching(self, lambda card : card.isStarterStrike())
                        self.deck.obtain(self, CardId.BITE, 5)
                        self.regainControl()

                    elif idx == 2:
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.WE_MEET_AGAIN:
                    if idx == 3:
                        self.regainControl()
                        break

                    if idx == 0:
                        self.potions[self.info.potionIdx] = Potion.EMPTY_POTION_SLOT
                        self.potionCount -= 1 # doing this instead of calling discardPotion because drinkPotionAtIdx/discardPotionAtIdx is not allowed during this event

                    elif idx == 1:
                        self.loseGold(self.info.gold)

                    elif idx == 2:
                        self.deck.remove(self, self.info.cardIdx)

                    else:
                        False = assert()

                    r = self.returnRandomScreenlessRelic(returnRandomRelicTier(self.relicRng, self.act))
                    self.obtainRelic(r)
                    self.regainControl()


            elif self.curEvent == Event.WHEEL_OF_CHANGE:
                    if idx != 0:
                        False = assert()
                    result = self.miscRng.random(5)
                    if result == 0:
                        self.obtainGold(self.act * 100)
                        self.regainControl()

                    elif result == 1:
                        self.openCombatRewardScreen(self.returnRandomScreenlessRelic(returnRandomRelicTier(self.relicRng, self.act)))

                    elif result == 2:
                        self.playerHeal(self.maxHp)
                        self.regainControl()

                    elif result == 3:
                        self.deck.obtain(self, CardId.DECAY)
                        self.regainControl()

                    elif result == 4:
                        self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)

                    else:
                        hpLoss = self.fractionMaxHp(0.15 if unfavorable else 0.10)
                        self.playerLoseHp(hpLoss)
                        self.regainControl()

            elif self.curEvent == Event.WINDING_HALLS:
                    if idx == 0:
                        self.playerLoseHp(self.info.hpAmount0)
                        self.deck.obtain(self, CardId.MADNESS, 2)
                        self.regainControl()

                    elif idx == 1:
                        self.playerHeal(self.info.hpAmount1)
                        self.deck.obtain(self, CardId.WRITHE)
                        self.regainControl()

                    elif idx == 2:
                        self.loseMaxHp(self.info.hpAmount2)
                        self.regainControl()

                    else:
                        False = assert()

            elif self.curEvent == Event.WORLD_OF_GOOP:
                    if idx == 0:
                        self.damagePlayer(11)
                        self.obtainGold(75)
                        self.regainControl()

                    elif idx == 1:
                        self.loseGold(self.info.goldLoss)
                        self.regainControl()

                    else:
                        False = assert()


            if curEvent != Event.NEOW and curEvent != Event.OMINOUS_FORGE and curEvent != Event.PLEADING_VAGRANT and curEvent != Event.ANCIENT_WRITING and curEvent != Event.OLD_BEGGAR and curEvent != Event.BIG_FISH and curEvent != Event.COLOSSEUM and curEvent != Event.CURSED_TOME and curEvent != Event.DEAD_ADVENTURER and curEvent != Event.DESIGNER_IN_SPIRE and curEvent != Event.AUGMENTER and curEvent != Event.DUPLICATOR and curEvent != Event.FACE_TRADER and curEvent != Event.FALLING and curEvent != Event.FORGOTTEN_ALTAR and curEvent != Event.THE_DIVINE_FOUNTAIN and curEvent != Event.GHOSTS and curEvent != Event.GOLDEN_IDOL and curEvent != Event.GOLDEN_SHRINE and curEvent != Event.WING_STATUE and curEvent != Event.KNOWING_SKULL and curEvent != Event.LAB and curEvent != Event.THE_SSSSSERPENT and curEvent != Event.LIVING_WALL and curEvent != Event.MASKED_BANDITS and curEvent != Event.MATCH_AND_KEEP and curEvent != Event.MINDBLOOM and curEvent != Event.HYPNOTIZING_COLORED_MUSHROOMS and curEvent != Event.MYSTERIOUS_SPHERE and curEvent != Event.THE_NEST and curEvent != Event.NLOTH and curEvent != Event.NOTE_FOR_YOURSELF and curEvent != Event.PURIFIER and curEvent != Event.SCRAP_OOZE and curEvent != Event.SECRET_PORTAL and curEvent != Event.SENSORY_STONE and curEvent != Event.SHINING_LIGHT and curEvent != Event.THE_CLERIC and curEvent != Event.THE_JOUST and curEvent != Event.THE_LIBRARY and curEvent != Event.THE_MAUSOLEUM and curEvent != Event.THE_MOAI_HEAD and curEvent != Event.THE_WOMAN_IN_BLUE and curEvent != Event.TOMB_OF_LORD_RED_MASK and curEvent != Event.TRANSMORGRIFIER and curEvent != Event.UPGRADE_SHRINE and curEvent != Event.VAMPIRES and curEvent != Event.WE_MEET_AGAIN and curEvent != Event.WHEEL_OF_CHANGE and curEvent != Event.WINDING_HALLS and curEvent != Event.WORLD_OF_GOOP:
                False = assert()

        def chooseSelectCardScreenOption(self, idx):
            isLastCard = self.info.haveSelectedCards.size() + 1 == self.info.toSelectCount
            self.info.haveSelectedCards.push_back(self.info.toSelectCards.get(idx))
            self.info.toSelectCards.remove(idx)

            if not isLastCard:
                return

            if self.info.selectScreenType == CardSelectScreenType.TRANSFORM:
                self.selectScreenTransform()
                self.regainControl()

            elif self.info.selectScreenType == CardSelectScreenType.UPGRADE:
                for c in self.info.haveSelectedCards:
                    self.deck.upgrade(c.deckIdx)
                self.regainControl()

            elif self.info.selectScreenType == CardSelectScreenType.REMOVE:
                    self.deck.removeSelected(self, self.info.haveSelectedCards)
                    self.regainControl()

            elif (self.info.selectScreenType == CardSelectScreenType.DUPLICATE) or (self.info.selectScreenType == CardSelectScreenType.OBTAIN):
                for c in self.info.haveSelectedCards:
                    self.deck.obtain(self, c.card, 1)
                self.regainControl()

            elif self.info.selectScreenType == CardSelectScreenType.BOTTLE:
                    selected = self.info.haveSelectedCards.get(0)
                    self.deck.bottleCard(selected.deckIdx, selected.card.getType())
                    self.regainControl()

            elif self.info.selectScreenType == CardSelectScreenType.TRANSFORM_UPGRADE:
                    self.deck.removeSelected(self, self.info.haveSelectedCards)
                    for i, unusedItem in enumerate(self.info.haveSelectedCards):
                        id = self.info.haveSelectedCards.get(i).card.id
                        self.deck.obtain(self, self.getTransformedCard(self.miscRng, auto(id), True))
                    self.regainControl()

            elif self.info.selectScreenType == CardSelectScreenType.BONFIRE_SPIRITS:
                    c = self.info.haveSelectedCards.get(0)
                    if c.card.getRarity() == CardRarity.CURSE:
                        self.obtainRelic(RelicId.SPIRIT_POOP)

                    elif c.card.getRarity() == CardRarity.BASIC:
                        pass

                    elif (c.card.getRarity() == CardRarity.COMMON) or c.card.getRarity() == CardRarity.SPECIAL:
                        self.playerHeal(5)

                    elif c.card.getRarity() == CardRarity.UNCOMMON:
                        self.playerHeal(10)

                    elif c.card.getRarity() == CardRarity.RARE:
                        self.playerIncreaseMaxHp(10)
                        self.playerHeal(self.maxHp)

                    else:
                        False = assert()
                    self.deck.remove(self, c.deckIdx)
                    self.screenState = ScreenState.MAP_SCREEN


            else:
                False = assert()


        def chooseCampfireOption(self, idx):
            if idx == 0:
                    healAmt = self.fractionMaxHp(0.30) + (15 if self.hasRelic(RelicId.REGAL_PILLOW) else 0)
                    self.playerHeal(healAmt)
                    if self.hasRelic(RelicId.DREAM_CATCHER):
                        self.openCombatRewardScreen(self.createCardReward(Room.REST))
                    else:
                        self.regainControl()

            elif idx == 1:
                    self.openCardSelectScreen(CardSelectScreenType.UPGRADE, 1)

            elif idx == 2:
                    obtainKey.RUBY_KEY
                    self.regainControl()

            elif idx == 3:
                    self.relics.getRelicValueRef(RelicId.GIRYA) += 1
                    self.regainControl()

            elif idx == 4:
                    self.openCardSelectScreen(CardSelectScreenType.REMOVE, 1)
                    self.regainControl()

            elif idx == 5:
                    r = self.returnRandomRelic(returnRandomRelicTier(self.relicRng, self.act))
                    self.openCombatRewardScreen(Rewards(r))

            elif idx == 6:
                    self.regainControl()

            else:
                False = assert()

        def chooseMatchAndKeepCards(self, idx1, idx2):
            if idx1 < 0 or idx1 >= 12 or self.info.toSelectCards.get(idx1).card.id == CardId.INVALID or idx2 == idx1 or idx2 < 0 or idx2 >= 12 or self.info.toSelectCards.get(idx2).card.id == CardId.INVALID:
                False = assert()

            s1 = self.info.toSelectCards.get(idx1).card
            s2 = self.info.toSelectCards.get(idx2).card

            if s1.id == s2.id:
                self.deck.obtain(self, auto(s1), 1)
                self.info.toSelectCards.get(idx1).deckIdx = 0
                self.info.toSelectCards.get(idx2).deckIdx = 0
            else:
                self.info.toSelectCards.get(idx1).deckIdx = 1
                self.info.toSelectCards.get(idx2).deckIdx = 1

            self.info.eventData -= 1
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (--info.eventData == 0)
            if self.info.eventData == 0:
                self.info.toSelectCards.clear()
                self.info.eventData = 0
                self.regainControl()

        def chooseTreasureRoomOption(self, openChest):
            if openChest:
                self.openTreasureRoomChest()
            else:
                self.regainControl()

        def regainControl(self):
            if self.regainControlAction is None:
                std::cerr << "regain control lambda was null" << "\n"
                #        assert(false)
            self.regainControlAction.invoke(self)



# C++ TO PYTHON CONVERTER TASK: Only expression lambdas are converted by C++ to Python Converter:
# C++ TO PYTHON CONVERTER TASK: The following statement was not recognized, possibly due to an unrecognized macro:
#const GameContextAction returnToMapAction = [](auto &gs)