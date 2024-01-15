from sts import *

from enum import Enum
import math

#
# Created by gamerpuppy on 7/4/2021.
#

#
# Created by gamerpuppy on 7/4/2021.
#






class sts: #this class replaces the original namespace 'sts'



    class Outcome(Enum):
        UNDECIDED = 0
        PLAYER_VICTORY = 1
        PLAYER_LOSS = 2

    battleOutcomeStrings = ["UNDECIDED", "PLAYER_VICTORY", "PLAYER_LOSS"]

# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class GameContext

# C++ TO PYTHON CONVERTER NOTE: 'extern' variable declarations are not required in Python:
#    extern thread_local BattleContext *g_debug_bc

    class BattleContext:

        def _initialize_instance_fields(self):
            # instance fields found by C++ to Python Converter:
            self.haveUsedDiscoveryAction = False
            self.undefinedBehaviorEvoked = False
            self.seed = 0
            self.floorNum = 0
            self.encounter = MonsterEncounter.INVALID
            self.loopCount = 0
            self.energyWasted = 0
            self.cardsDrawn = 0
            self.aiRng = Random()
            self.cardRandomRng = Random()
            self.miscRng = Random()
            self.monsterHpRng = Random()
            self.potionRng = Random()
            self.shuffleRng = Random()
            self.ascension = 0
            self.outcome = Outcome.UNDECIDED
            self.inputState = InputState.EXECUTING_ACTIONS
            self.cardSelectInfo = CardSelectInfo()
            self.monsterTurnIdx = 6
            self.isBattleOver = False
            self.endTurnQueued = False
            self.turnHasEnded = False
            self.skipMonsterTurn = False
            self.cardQueue = CardQueue()
            self.potionCount = 0
            self.potionCapacity = 3
            self.potions = [None for _ in range(5)]
            self.turn = 0
            self.player = Player()
            self.monsters = MonsterGroup()
            self.cards = CardManager()
            self.curCardQueueItem = CardQueueItem()


        # begin for debugging purposes
        sum = 0 # for preventing optimization in benchmarks
        # end for debugging purposes





# C++ TO PYTHON CONVERTER TASK: The following line could not be converted:
        ActionQueue<50> actionQueue;




# C++ TO PYTHON CONVERTER TASK: The following line could not be converted:
        std::bitset<32> miscBits;

# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        BattleContext() = default
# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        BattleContext(const BattleContext &rhs) = default

        # ****************************************


        # assume all bc fields have just been initialized by in class member initializers
# C++ TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def init(self, gc):
            self.init(gc, gc.info.encounter)

# C++ TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def init(self, gc, encounterToInit):
            self.undefinedBehaviorEvoked = False
            self.haveUsedDiscoveryAction = False
            self.seed = gc.seed
            self.floorNum = gc.floorNum
            self.encounter = encounterToInit

            startRandom = Random(gc.seed+gc.floorNum)
            self.aiRng = startRandom
            self.monsterHpRng = startRandom
            self.shuffleRng = startRandom
            self.cardRandomRng = startRandom
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: miscRng = gc.miscRng;
            self.miscRng.copy_from(gc.miscRng)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: potionRng = gc.potionRng;
            self.potionRng.copy_from(gc.potionRng)

            self.ascension = gc.ascension
            self.outcome = Outcome.UNDECIDED
            self.inputState = InputState.EXECUTING_ACTIONS
            miscBits.reset()

            self.monsterTurnIdx = 6
            self.skipMonsterTurn = False
            self.turnHasEnded = False
            self.isBattleOver = False

            actionQueue.clear()
            self.cardQueue.clear()

            self.potionCount = gc.potionCount
            self.potionCapacity = gc.potionCapacity
            self.potions = list(gc.potions)

            self.player.curHp = gc.curHp
            self.player.maxHp = gc.maxHp
            self.player.gold = gc.gold

            self.monsters.init(self, encounterToInit)
            if gc.map.burningEliteX == gc.curMapNodeX and gc.map.burningEliteY == gc.curMapNodeY:
                self.monsters.applyEmeraldEliteBuff(self, gc.map.burningEliteBuff, gc.act)

            self.player.cardDrawPerTurn = 5
            if gc.hasRelic(R.SNECKO_EYE):
                self.player.cardDrawPerTurn += 2
            if gc.relics.has(R.RING_OF_THE_SERPENT):
                self.player.cardDrawPerTurn += 1
            #addToBot(Actions::DrawCards(player.cardDrawPerTurn))

            self.cards.init(gc, self)

            self.initRelics(gc)
            self.player.energy += self.player.energyPerTurn

            self.executeActions()


        # this doesnt apply powers in order, so if that matters in the future all relics will have to be sorted
        def initRelics(self, gc):
            self.player.relicBits0 = gc.relics.relicBits0
            self.player.relicBits1 = gc.relics.relicBits1

            atBattleStartPreDraw = fixed_list()
            atBattleStart = fixed_list()
            atTurnStartPostDraw = fixed_list()

            room = gc.curRoom

            p = self.player

            for r in gc.relics.relics:

                if (r.id == R.HOLY_WATER) or r.id == R.NINJA_SCROLL or (r.id == R.PURE_WATER) or (r.id == R.TOOLBOX):
                    atBattleStartPreDraw.push_back(r.id)

                elif (r.id == R.BAG_OF_MARBLES) or (r.id == R.BAG_OF_PREPARATION) or (r.id == R.CLOCKWORK_SOUVENIR) or (r.id == R.GREMLIN_VISAGE) or (r.id == R.RED_MASK) or (r.id == R.RING_OF_THE_SNAKE) or r.id == R.TWISTED_FUNNEL:
                    atBattleStart.push_back(r.id)

                elif r.id == R.MARK_OF_PAIN:
                    p.energyPerTurn += 1
                    atBattleStart.push_back(r.id)

                elif (r.id == R.GAMBLING_CHIP) or (r.id == R.WARPED_TONGS):
                    atTurnStartPostDraw.push_back(r.id)

                elif r.id == R.AKABEKO:
                    p.buff(8)

                elif r.id == R.BRIMSTONE:
                    p.buff(2)
                    i = 0
                    while i < self.monsters.monsterCount:
                        m = self.monsters.arr[i]
                        if m.isTargetable():
                            m.buff(1)
                        i += 1

                elif r.id == R.ECTOPLASM:
                    p.energyPerTurn += 1

                elif r.id == R.ENCHIRIDION:
                        cardId = getTrulyRandomCardInCombat(self.cardRandomRng, p.cc, CardType.POWER)
                        c = CardInstance(cardId)
                        c.setCostForTurn(0)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: addToBot(Actions::MakeTempCardInHand(c));
                        self.addToBot(Actions.MakeTempCardInHand(sts.CardInstance(c)))

                elif r.id == R.HAPPY_FLOWER:
                    self.player.happyFlowerCounter = r.data + 1
                    if self.player.happyFlowerCounter == 3:
                        self.player.energy += 1
                        self.player.happyFlowerCounter = 0

                elif r.id == R.INCENSE_BURNER:
                    p.incenseBurnerCounter = r.data
                    p.incenseBurnerCounter += 1
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (++p.incenseBurnerCounter == 6)
                    if p.incenseBurnerCounter == 6:
                        p.incenseBurnerCounter = 0
                        p.buff(1)

                elif r.id == R.INK_BOTTLE:
                    p.inkBottleCounter = r.data

                elif r.id == R.INSERTER:
                    if r.data != 0:
                        p.inserterCounter = 0
                        p.increaseOrbSlots(1)
                    else:
                        p.inserterCounter = 1

                elif r.id == R.LIZARD_TAIL:
                    p.setHasRelic<R.LIZARD_TAIL>(r.data)

                elif r.id == R.NUNCHAKU:
                    p.nunchakuCounter = r.data

                elif r.id == R.OMAMORI:
                    p.setHasRelic(r.data)

                elif r.id == R.PEN_NIB:
                    if r.data == 9:
                        p.buff(1)
                        p.penNibCounter = -1
                    else:
                        p.penNibCounter = r.data

                elif r.id == R.PHILOSOPHERS_STONE:
                    i = 0
                    while i < self.monsters.monsterCount:
                        m = self.monsters.arr[i]
                        m.buff(1)
                        i += 1
                    p.energyPerTurn += 1

                elif r.id == R.RUNIC_DOME:
                    p.energyPerTurn += 1

                elif r.id == R.SNECKO_EYE:
                    p.debuff(1)

                elif r.id == R.SOZU:
                    p.energyPerTurn += 1

                elif r.id == R.SUNDIAL:
                    p.sundialCounter = r.data

                elif r.id == R.VELVET_CHOKER:
                    p.energyPerTurn += 1

                elif r.id == R.ANCHOR:
                    p.block += 10

                elif r.id == R.ANCIENT_TEA_SET:
                    if gc.lastRoom is Room.REST:
                        p.gainEnergy(2)

                elif r.id == R.BLOOD_VIAL:
                    p.heal(2) # todo not correct

                elif r.id == R.BRONZE_SCALES:
                    p.buff(3)

                elif r.id == R.BUSTED_CROWN:
                    p.energyPerTurn += 1

                elif r.id == R.COFFEE_DRIPPER:
                    p.energyPerTurn += 1

                elif r.id == R.CRACKED_CORE:
                    p.channelOrb.LIGHTNING

                elif r.id == R.CURSED_KEY:
                    p.energyPerTurn += 1

                elif r.id == R.DAMARU:
                    p.buff(1)

                elif r.id == R.DATA_DISK:
                    p.buff(1)

                elif r.id == R.DU_VU_DOLL:
                    p.buff(r.data)

                elif r.id == R.FOSSILIZED_HELIX:
                    p.buff(1)

                elif r.id == R.FUSION_HAMMER:
                    p.energyPerTurn += 1

                elif r.id == R.GIRYA:
                    p.buff(r.data)

                elif r.id == R.LANTERN:
                    p.gainEnergy(1)

                elif r.id == R.MUTAGENIC_STRENGTH: # this appears to be applied before clockwork if it was acquired first
                    p.buff(3)
                    p.debuff(3)

                elif r.id == R.NEOWS_LAMENT: # remember to decrement somewhere else
                    if r.data > 0:
                        i = 0
                        while i < self.monsters.monsterCount:
                            m = self.monsters.arr[i]
                            m.curHp = 1
                            i += 1

                elif r.id == R.NUCLEAR_BATTERY:
                    p.channelOrb.FUSION

                elif r.id == R.ODDLY_SMOOTH_STONE:
                    p.buff(1)

                elif r.id == R.PANTOGRAPH:
                    if room is Room.BOSS:
                        p.heal(25)

                elif r.id == R.PRESERVED_INSECT:
                    if room is Room.ELITE:
                        i = 0
                        while i < self.monsters.monsterCount:
                            m = self.monsters.arr[i]
                            m.curHp = int((m.maxHp * .75))
                            i += 1

                elif r.id == R.RING_OF_THE_SERPENT:
                    # now handled in battlecontext init
                    #                p.cardDrawPerTurn++
                    pass

                elif r.id == R.RUNIC_CAPACITOR:
                    p.increaseOrbSlots(3)

                elif r.id == R.SLAVERS_COLLAR:
                    if room is Room.ELITE or room is Room.BOSS:
                        p.energyPerTurn += 1

                elif r.id == R.SLING_OF_COURAGE:
                    if room is Room.ELITE:
                        p.buff(2)

                elif r.id == R.SYMBIOTIC_VIRUS:
                    p.channelOrb.DARK

                elif r.id == R.TEARDROP_LOCKET:
                    p.changeStance()

                elif r.id == R.THREAD_AND_NEEDLE:
                    p.buff(4)

                elif r.id == R.VAJRA:
                    p.buff(1)


            # todo maybe move this to proper place -nvm drawCards is added below this
            for r in atBattleStartPreDraw:
                if r is R.HOLY_WATER:
                    self.addToBot(Actions.MakeTempCardInHand(CardId.MIRACLE, False, 3))

                elif r == R.NINJA_SCROLL:
                    self.addToBot(Actions.MakeTempCardInHand(CardId.SHIV, False, 3))

                elif r is R.PURE_WATER:
                    self.addToBot(Actions.MakeTempCardInHand(CardId.MIRACLE, False, 1))

                elif r is R.TOOLBOX:
                    self.addToBot(Actions.ToolboxAction())


            self.addToBot(Actions.DrawCards(int8_t(p.cardDrawPerTurn)))

            for r in atBattleStart:
                if r is R.BAG_OF_MARBLES:
                    self.addToBot(Actions.DebuffAllEnemy(1, False))

                elif r is R.BAG_OF_PREPARATION:
                    self.addToBot(Actions.DrawCards(2))

                elif r is R.CLOCKWORK_SOUVENIR:
                    self.addToBot(Actions.BuffPlayer(1))

                elif r is R.GREMLIN_VISAGE:
                    p.debuff(1)

                elif r is R.MARK_OF_PAIN:
                    self.addToBot(Actions.MakeTempCardInDrawPile(CardInstance(CardId.WOUND), 2, True))

                elif r is R.RED_MASK:
                    self.addToBot(Actions.DebuffAllEnemy(1))

                elif r is R.RING_OF_THE_SNAKE:
                    self.addToBot(Actions.DrawCards(2))

                elif r == R.TWISTED_FUNNEL:
                    self.addToBot(Actions.DebuffAllEnemy(4))


            if gc.hasRelic(R.MERCURY_HOURGLASS):
                self.addToBot(Actions.DamageAllEnemy(3))

            if gc.hasRelic(R.RED_SKULL) and gc.curHp <= math.trunc(gc.maxHp / float(2)):
                p.buff(3)

            for r in atTurnStartPostDraw:
                if r is R.GAMBLING_CHIP:
                    self.addToBot(Actions.GambleAction())

                elif r is R.WARPED_TONGS:
                    self.addToBot(Actions.UpgradeRandomCardAction())


            # ** OnStartOfTurn ** ORBS todo
            #RelicCables -> OnStartOfTurn again for orb 0

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: void exitBattle(GameContext &g) const
        def exitBattle(self, g):
            # do this first so that darkstone periapt is overridden by curHp and maxHp are set afterwards
            m = self.monsters.arr[0]
            if m.id == MonsterId.WRITHING_MASS and m.miscInfo != 0:
                if self.player.hasRelic():
                    g.relics.getRelicValueRef(RelicId.OMAMORI) -= 1
                else:
                    g.deck.obtain(g, CardId.PARASITE)


            g.potionCount = self.potionCount
            g.potions = list(self.potions)

            # not sure its really necessary to sync these every time, (i believe colosseum is the only time two battles occur on the same floor)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: g.aiRng = aiRng;
            g.aiRng.copy_from(self.aiRng)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: g.cardRandomRng = cardRandomRng;
            g.cardRandomRng.copy_from(self.cardRandomRng)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: g.miscRng = miscRng;
            g.miscRng.copy_from(self.miscRng)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: g.monsterHpRng = monsterHpRng;
            g.monsterHpRng.copy_from(self.monsterHpRng)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: g.potionRng = potionRng;
            g.potionRng.copy_from(self.potionRng)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: g.shuffleRng = shuffleRng;
            g.shuffleRng.copy_from(self.shuffleRng)

            g.curHp = self.player.curHp
            g.maxHp = self.player.maxHp
            g.gold = self.player.gold


            # todo lesson learned bitset

            # relic counters
            self.updateRelicsOnExit(g)

            # cards
            self.updateCardsOnExit(g.deck)

            g.info.stolenGold = 0
            if self.requiresStolenGoldCheck():
                i = 0
                while i < self.monsters.monsterCount:
                    m = self.monsters.arr[i]

                    canHaveStolenGold = m.id == MonsterId.LOOTER or m.id == MonsterId.MUGGER
                    escaped = m.curHp > 0 and (m.moveHistory[0] is MMID.LOOTER_ESCAPE or m.moveHistory[0] is MMID.MUGGER_ESCAPE)

                    if canHaveStolenGold and not escaped:
                        g.info.stolenGold += m.miscInfo
                    i += 1

            if self.outcome == Outcome.PLAYER_LOSS:
                g.outcome = GameOutcome.PLAYER_LOSS
            else:
                # player victory
                g.regainControl()

            BattleContext.sum += g.curHp + g.maxHp + g.gold + g.act + g.ascension + g.floorNum + self.potionRng.counter + self.cardRandomRng.counter

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: void updateRelicsOnExit(GameContext &g) const
        def updateRelicsOnExit(self, g):
            for r in g.relics.relics:
                if r.id == RelicId.HAPPY_FLOWER:
                    r.data = self.player.happyFlowerCounter

                elif r.id == RelicId.INCENSE_BURNER:
                    r.data = self.player.incenseBurnerCounter

                elif r.id == RelicId.INK_BOTTLE:
                    r.data = self.player.inkBottleCounter

                elif r.id == RelicId.INSERTER:
                    r.data = self.player.inserterCounter

                elif r.id == RelicId.NEOWS_LAMENT:
                    r.data -= 1

                elif r.id == RelicId.NUNCHAKU:
                    r.data = self.player.nunchakuCounter

                elif r.id == RelicId.PEN_NIB:
                    # possible bug
                    if self.player.penNibCounter == -1:
                        r.data = 9
                    else:
                        r.data = self.player.penNibCounter

                elif r.id == RelicId.SUNDIAL:
                    r.data = self.player.sundialCounter

                elif r.id == RelicId.LIZARD_TAIL:
                    if (not self.player.hasRelic)<R.LIZARD_TAIL>():
                        r.data = 0

                elif r.id == RelicId.BURNING_BLOOD:
                    if self.outcome == Outcome.PLAYER_VICTORY:
                        g.playerHeal(6)

                elif r.id == RelicId.BLACK_BLOOD:
                    if self.outcome == Outcome.PLAYER_VICTORY:
                        g.playerHeal(12)



# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: void updateCardsOnExit(Deck &deck) const
        def updateCardsOnExit(self, deck):
            for c in self.cards.drawPile:
                Globals.cardOnExit(c, deck)

            for c in self.cards.discardPile:
                Globals.cardOnExit(c, deck)

            for c in self.cards.exhaustPile:
                Globals.cardOnExit(c, deck)

            i = 0
            while i < self.cards.cardsInHand:
                Globals.cardOnExit(self.cards.hand[i], deck)
                i += 1

            #    if (curCardQueueItem)


        # ****************************************

        def setRequiresStolenGoldCheck(self, value):
            miscBits.set(0, value)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool requiresStolenGoldCheck() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool requiresStolenGoldCheck() const
        def requiresStolenGoldCheck(self):
            return miscBits.test(0)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getMonsterTurnNumber() const; // returns 1 for first turn, 2 for second, etc.
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getMonsterTurnNumber() const
        def getMonsterTurnNumber(self):
            return self.turn+1 # todo;

        # ****************************************

        def executeActions(self):
            # todo find a place for checking where card queue is empty and player doesn't have control for calling onEndingTurn
            sts.BattleContext.sum += 1
            g_debug_bc = self

            while True:
                self.loopCount += 1
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (++loopCount > 100000 || monsters.monstersAlive < 0 || turn > 500)
                if self.loopCount > 100000 or self.monsters.monstersAlive < 0 or self.turn > 500:
                    # something went wrong
                    if self.turn > 500:
                        self.outcome = Outcome.PLAYER_LOSS
                        break

                    std::cerr << self.seed << std::endl
                    print(self, end = '')
                    print()
                    False = assert()

                if self.inputState != InputState.EXECUTING_ACTIONS:
                    break

                if self.outcome == Outcome.PLAYER_LOSS:
                    break

                if not actionQueue.isEmpty():
                    # do a action
                    a = std::move(actionQueue.popFront())
                    a(self)
                    continue

                if self.outcome != Outcome.UNDECIDED:
                    break

                if not self.cardQueue.isEmpty():
                    # play a card queue item
                    item = self.cardQueue.popFront()
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: playCardQueueItem(item);
                    self.playCardQueueItem(sts.CardQueueItem(item))
                    continue

                # can't win check
                if self.cards.cardsInHand + self.cards.discardPile.size() + self.cards.drawPile.size() == 0:
                    hasDamageWithoutCards = self.player.hasStatus() or self.player.hasStatus() or self.player.bomb1 is not None or self.player.bomb2 is not None or self.player.bomb3 is not None

                    if (not hasDamageWithoutCards) and self.monsters.arr[0].id != MonsterId.TRANSIENT:
                        self.outcome = Outcome.PLAYER_LOSS
                        break

                if self.outcome != Outcome.UNDECIDED:
                    break

                if self.monsterTurnIdx < self.monsters.monsterCount:
                    # do a monster turn
                    self.monsters.doMonsterTurn(self)
                    continue
                self.monsters.skipTurn.reset()

                if self.outcome != Outcome.UNDECIDED:
                    break

                if self.turnHasEnded:
                    # after all monster turns
                    self.afterMonsterTurns()
                    continue


                if self.endTurnQueued:
                    self.endTurnQueued = False
                    self.onTurnEnding()
                    continue


                if self.player.hasRelic():
                    # turn cannot have ended here
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                    assert not self.endTurnQueued
                    assert actionQueue.isEmpty()
                    assert self.cardQueue.isEmpty()
##endif

                    if self.cards.cardsInHand == 0:
                        self.drawCards(1)

                self.setState(InputState.PLAYER_NORMAL)
                break

        def playCardQueueItem(self, playItem):
            # if c is null callEndOfTurnActions()
            # if cardQueueSize is 1 and carditem is endTurnAutoplay diable unceasing top

# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: curCardQueueItem = playItem;
            self.curCardQueueItem.copy_from(playItem)
            item = self.curCardQueueItem
            c = item.card

            if item.isEndTurn:
                # the game removes this card from limbo - don't think necessary
                self.callEndOfTurnActions()
                return


            # if cardQueueItem random target, assign a target
            if item.randomTarget:
                item.target = self.monsters.getRandomMonsterIdx(self.cardRandomRng)

            #    bool canPlayCard = false; // not really sure what this is used for
            canUseCard = item.purgeOnUse or (item.triggerOnUse and c.canUse(self, item.target, item.autoplay) and ((not c.requiresTarget()) or self.monsters.arr[item.target].isTargetable()))
            if canUseCard:
                #        canPlayCard = true; // what is this for......

                if c.isFreeToPlay(self):
                    c.freeToPlayOnce = True

                if c.requiresTarget():
                    self.player.lastTargetedMonster = sbyte(item.target)

                if (not c.requiresTarget()) or self.monsters.arr[item.target].isTargetable():
                    self.useCard()


            if not item.triggerOnUse:
                self.useNoTriggerCard() # for burn, decay, doubt, regret and shame,

        def useCard(self):
            item = self.curCardQueueItem
            c = item.card

            item.exhaustOnUse |= c.doesExhaust()
            self.player.cardsPlayedThisTurn += 1

            if c.getType() == CardType.ATTACK:
                self.useAttackCard()
                self.onUseAttackCard()

            elif c.getType() == CardType.SKILL:
                self.useSkillCard()
                self.onUseSkillCard()
                if self.player.hasStatus():
                    item.exhaustOnUse = True

            elif c.getType() == CardType.POWER:
                self.usePowerCard()
                self.onUsePowerCard()

            elif (c.getType() == CardType.STATUS) or (c.getType() == CardType.CURSE):
                self.onUseStatusOrCurseCard()

                # unreachable

            self.addToBot(Actions.OnAfterCardUsed())
            self.triggerOnOtherCardPlayed(c)

            if not item.purgeOnUse:
                self.cards.removeFromHandById(ushort(c.uniqueId))
                if c.costForTurn > 0 and (not c.isFreeToPlay(self)) and (not item.autoplay) and not(self.player.hasStatus() and c.getType() == CardType.SKILL):
                    self.player.useEnergy(c.costForTurn)

        def useNoTriggerCard(self):
            item = self.curCardQueueItem
            c = item.card

            if c.id == CardId.BURN:
                self.addToTop(Actions.DamagePlayer(4 if c.isUpgraded() else 2, True))

            elif c.id == CardId.DECAY:
                self.addToTop(Actions.DamagePlayer(2, True))

            elif c.id == CardId.DOUBT:
                self.player.debuff(1, True)

            elif c.id == CardId.REGRET:
                self.addToTop(Actions.PlayerLoseHp(item.regretCardCount, True))

            elif c.id == CardId.SHAME:
                # todo this is fixed just test -> this and doubt are bugged if you are already weak i think. because the apply power action does not create a new power and justapplied is not set to true
                self.player.debuff<PlayerStatus.FRAIL>(1, True)


                # this can actually be called on any card now because of time warp power

                ##ifdef sts_asserts
                #            assert(false)
                ##endif // sts_asserts

            self.cards.removeFromHandById(ushort(c.uniqueId))
            self.addToBot(Actions.DiscardNoTriggerCard()) # todo what if havoc plays one of these

        def useAttackCard(self):
            item = self.curCardQueueItem
            c = item.card

            t = item.target
            up = c.isUpgraded()

            # todo test vigor with multi attacks and necro/double tap
            if (c.getId() == CardId.STRIKE_RED) or (c.getId() == CardId.STRIKE_BLUE) or (c.getId() == CardId.STRIKE_GREEN) or (c.getId() == CardId.STRIKE_PURPLE):
                    self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,9 if up else 6)))

            elif c.getId() == CardId.ANGER:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,8 if up else 6)))
                self.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.ANGER, up), 1))

            elif c.getId() == CardId.BASH:
                # technically calculate attack damage is called first, keep note if we optimize addToBot later
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,10 if up else 8)))
                self.addToBot(Actions.DebuffEnemy(t,3 if up else 2, False))

            elif c.getId() == CardId.BITE:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,8 if up else 7)))
                self.addToBot(Actions.HealPlayer(3 if up else 2))

            elif c.getId() == CardId.BODY_SLAM:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t, self.player.block)))

            elif c.getId() == CardId.BLOOD_FOR_BLOOD:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,22 if up else 18)))

            elif c.getId() == CardId.BLUDGEON:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,42 if up else 32)))

            elif c.getId() == CardId.CARNAGE:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,28 if up else 20)))

            elif c.getId() == CardId.CLASH:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,18 if up else 14)))

            elif c.getId() == CardId.CLEAVE:
                    baseDamage = (11 if up else 8) + self.player.getStatus()
                    self.addToBot(Actions.AttackAllEnemy(baseDamage))

            elif c.getId() == CardId.CLOTHESLINE:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,14 if up else 12)))
                self.addToBot(Actions.DebuffEnemy(t,3 if up else 2, False))

            elif c.getId() == CardId.DRAMATIC_ENTRANCE:
                    baseDamage = (12 if up else 8) + self.player.getStatus()
                    self.addToBot(Actions.AttackAllEnemy(baseDamage))

            elif c.getId() == CardId.DROPKICK:
                self.addToBot(Actions.DropkickAction(t))

            elif c.getId() == CardId.FEED:
                self.addToBot(Actions.FeedAction(t, self.calculateCardDamage(c, t,12 if up else 10), up))

            elif c.getId() == CardId.FIEND_FIRE:
                self.addToBot(Actions.FiendFireAction(t, self.calculateCardDamage(c, t,10 if up else 7)))

            elif c.getId() == CardId.FLASH_OF_STEEL:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,6 if up else 3)))
                self.addToBot(Actions.DrawCards(1))

            elif c.getId() == CardId.HAND_OF_GREED:
                self.addToBot(Actions.HandOfGreedAction(t, self.calculateCardDamage(c, t,25 if up else 20), up))

            elif c.getId() == CardId.HEADBUTT:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,12 if up else 9)))
                self.addToBot(Actions.HeadbuttAction())

            elif c.getId() == CardId.HEAVY_BLADE:
                    dmg1 = 14 + ((4 if up else 2) * self.player.getStatus())
                    dmg2 = self.calculateCardDamage(c, t, dmg1)
                    self.addToBot(Actions.AttackEnemy(t, dmg2))

            elif c.getId() == CardId.HEMOKINESIS:
                #  attack enemy should recalculate damage, because we can lose hp and therefore gain strength before the dmg, need to test
                # actually no i dont think that is true ^^
                self.addToBot(Actions.PlayerLoseHp(2, True))
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,20 if up else 15)))

            elif c.getId() == CardId.IMMOLATE:
                    baseDamage = (28 if up else 21) + self.player.getStatus()
                    self.addToBot(Actions.AttackAllEnemy(baseDamage))
                    self.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.BURN), 1))

            elif c.getId() == CardId.IRON_WAVE:
                    self.addToBot(Actions.GainBlock(self.calculateCardBlock(self.calculateCardBlock(7 if up else 5))))
                    self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,7 if up else 5)))

            elif c.getId() == CardId.MIND_BLAST:
                    damage = self.calculateCardDamage(c, t, int(self.cards.drawPile.size()))
                    self.addToBot(Actions.AttackEnemy(t, damage))

            elif c.getId() == CardId.PERFECTED_STRIKE:
                    # hack because we calculate strikeCount while non purge cards are still in hand.
                    strikeDmg = self.cards.strikeCount * (3 if up else 2)
                    baseDamage = 6 + strikeDmg
                    self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t, baseDamage)))

            elif c.getId() == CardId.POMMEL_STRIKE:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,10 if up else 9)))
                self.addToBot(Actions.DrawCards(2 if up else 1))

            elif c.getId() == CardId.PUMMEL:
                    attackCount = 5 if up else 4
                    damage = self.calculateCardDamage(c, t, 2)
                    for i in range(0, attackCount):
                        self.addToBot(Actions.AttackEnemy(t, damage))

            elif c.getId() == CardId.RAMPAGE:
                    damage = self.calculateCardDamage(c, t, 8+c.specialData)
                    self.addToBot(Actions.AttackEnemy(t, damage))

                    if item.purgeOnUse:
                        self.cards.findAndUpgradeSpecialData(c.uniqueId,8 if up else 5)
                    c.specialData += short(8 if up else 5)


            elif c.getId() == CardId.REAPER:
                    baseDamage = (5 if up else 4) + self.player.getStatus()
                    self.addToBot(Actions.ReaperAction(baseDamage))

            elif c.getId() == CardId.RECKLESS_CHARGE:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,10 if up else 7)))
                self.addToBot(Actions.MakeTempCardInDrawPile(CardInstance(CardId.DAZED), 1, True))

            elif c.getId() == CardId.RITUAL_DAGGER:
                self.addToBot(Actions.RitualDaggerAction(t, self.calculateCardDamage(c, t, c.specialData)))

            elif c.getId() == CardId.SEARING_BLOW:
                    n = c.getUpgradeCount()
                    baseDmg = math.trunc(n * (n+7) / float(2)) + 12
                    self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t, baseDmg)))

            elif c.getId() == CardId.SEVER_SOUL: # another example of damage being calculated after an action, maybe need a new action to calculate damage later...
                self.addToBot(Actions.SeverSoulExhaustAction())
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,22 if up else 16)))

            elif c.getId() == CardId.SWIFT_STRIKE:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,10 if up else 7)))

            elif c.getId() == CardId.SWORD_BOOMERANG:
                i = 0
                while i < (4 if up else 3):
                    self.addToBot(Actions.SwordBoomerangAction(3+self.player.getStatus())) # vigor is removed afterwards so this is a necessary (maybe not 100% accurate) hack
                    i += 1

            elif c.getId() == CardId.THUNDERCLAP:
                    baseDamage = (7 if up else 4) + self.player.getStatus()
                    self.addToBot(Actions.AttackAllEnemy(baseDamage))
                    self.addToBot(Actions.DebuffAllEnemy(1, False))

            elif c.getId() == CardId.TWIN_STRIKE:
                    dmg = self.calculateCardDamage(c, t,7 if up else 5)
                    self.addToBot(Actions.AttackEnemy(t, dmg))
                    self.addToBot(Actions.AttackEnemy(t, dmg))

            elif c.getId() == CardId.UPPERCUT:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t, 13)))
                self.addToBot(Actions.DebuffEnemy(t,2 if up else 1, False))
                self.addToBot(Actions.DebuffEnemy(t,2 if up else 1, False))

            elif c.getId() == CardId.WHIRLWIND:
                    if item.ignoreEnergyTotal == 0 and self.player.energy < item.energyOnUse:
                        item.energyOnUse = self.player.energy
                    baseDamage = (8 if up else 5) + self.player.getStatus()
                    self.addToBot(Actions.WhirlwindAction(baseDamage, item.energyOnUse, not(item.freeToPlay or c.freeToPlayOnce)))

            elif c.getId() == CardId.WILD_STRIKE:
                self.addToBot(Actions.AttackEnemy(t, self.calculateCardDamage(c, t,17 if up else 12)))
                self.addToBot(Actions.MakeTempCardInDrawPile(CardInstance(CardId.WOUND), 1, True))


            else:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                std::cerr << "attempted to use unimplemented card: " << c.getName() << std::endl
                False = assert()
##endif


        # todo a lot of things can be done immediately
        def useSkillCard(self):
            item = self.curCardQueueItem
            c = item.card
            t = item.target
            up = c.isUpgraded()

            if (c.getId() == CardId.DEFEND_RED) or (c.getId() == CardId.DEFEND_BLUE) or (c.getId() == CardId.DEFEND_GREEN) or (c.getId() == CardId.DEFEND_PURPLE):
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(8 if up else 5)))

            elif c.getId() == CardId.ARMAMENTS:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(5)))
                if up:
                    self.addToBot(Actions.UpgradeAllCardsInHand())
                else:
                    self.addToBot(Actions.ArmamentsAction())

            elif c.getId() == CardId.APOTHEOSIS:
                self.addToBot(Actions.ApotheosisAction())

            elif c.getId() == CardId.APPARITION:
                self.addToBot(Actions.BuffPlayer(1))

            elif c.getId() == CardId.BANDAGE_UP:
                self.addToBot(Actions.HealPlayer(6 if up else 4))

            elif c.getId() == CardId.BATTLE_TRANCE:
                self.addToBot(Actions.DrawCards(4 if up else 3))
                self.addToBot(Actions.DebuffPlayer())

            elif c.getId() == CardId.BLIND:
                if up:
                    self.addToBot(Actions.DebuffAllEnemy(2, False))
                else:
                    self.addToBot(Actions.DebuffEnemy(t, 2, False))

            elif c.getId() == CardId.BLOODLETTING:
                self.addToBot(Actions.PlayerLoseHp(3, True))
                self.addToBot(Actions.GainEnergy(3 if up else 2))

            elif c.getId() == CardId.BURNING_PACT:
                self.addToBot(Actions.ChooseExhaustOne())
                self.addToBot(Actions.DrawCards(3 if up else 2))

            elif c.getId() == CardId.CHRYSALIS:
                self.addToBot(Actions.PutRandomCardsInDrawPile(CardType.SKILL,5 if up else 3))

            elif c.getId() == CardId.DARK_SHACKLES:
                self.addToBot(Actions.DebuffEnemy(t,15 if up else 9))
                if self.monsters.arr[t].hasStatus():
                    self.addToBot(Actions.BuffEnemy(t,15 if up else 9))

            elif c.getId() == CardId.DEEP_BREATH:
                if not self.cards.discardPile.empty():
                    self.onShuffle()
                    self.addToBot(Actions.EmptyDeckShuffle())
                    self.addToBot(Actions.ShuffleDrawPile())
                self.addToBot(Actions.DrawCards(2 if up else 1))

            elif c.getId() == CardId.DISARM:
                self.addToBot(Actions.DebuffEnemy(t, -2, False))

            elif c.getId() == CardId.DISCOVERY:
                self.undefinedBehaviorEvoked = True
                self.addToBot(Actions.DiscoveryAction(CardType.INVALID, 1))

            elif c.getId() == CardId.DOUBLE_TAP:
                self.addToBot(Actions.BuffPlayer(2 if up else 1))

            elif c.getId() == CardId.DUAL_WIELD:
                self.addToBot(Actions.DualWieldAction(2 if up else 1))

            elif c.getId() == CardId.ENLIGHTENMENT:
                self.addToBot(Actions.EnlightenmentAction(up))

            elif c.getId() == CardId.ENTRENCH:
                self.addToBot(Actions.EntrenchAction())

            elif c.getId() == CardId.EXHUME:
                self.addToBot(Actions.ExhumeAction())

            elif c.getId() == CardId.FINESSE:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(4 if up else 2)))
                self.addToBot(Actions.DrawCards(1))

            elif c.getId() == CardId.FORETHOUGHT:
                self.addToBot(Actions.ForethoughtAction(up))

            elif c.getId() == CardId.FLAME_BARRIER:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(16 if up else 12)))
                self.addToBot(Actions.BuffPlayer(6 if up else 4))

            elif c.getId() == CardId.FLEX:
                self.addToBot(Actions.BuffPlayer(4 if up else 2))
                self.addToBot(Actions.DebuffPlayer(4 if up else 2))

            elif c.getId() == CardId.GHOSTLY_ARMOR:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(13 if up else 10)))

            elif c.getId() == CardId.GOOD_INSTINCTS:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(9 if up else 6)))

            elif c.getId() == CardId.HAVOC:
                self.addToBot(Actions.PlayTopCard(self.monsters.getRandomMonsterIdx(self.cardRandomRng, True), True))

            elif c.getId() == CardId.IMPATIENCE:
                    hasAttack = False
                    i = 0
                    while i < self.cards.cardsInHand:
                        if self.cards.hand[i].getType() == CardType.ATTACK:
                            hasAttack = False
                            break
                        i += 1
                    if not hasAttack:
                        self.addToBot(Actions.DrawCards(3 if up else 2))

            elif c.getId() == CardId.IMPERVIOUS:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(40 if up else 30)))

            elif c.getId() == CardId.INFERNAL_BLADE:
                self.addToBot(Actions.InfernalBladeAction())

            elif c.getId() == CardId.INTIMIDATE:
                self.addToBot(Actions.DebuffAllEnemy(2 if up else 1, False)) # game justs adds one for each enemy in order

            elif c.getId() == CardId.JACK_OF_ALL_TRADES: # the game decides the random cards here and adds maketempcardtobot
                self.addToBot(Actions.JackOfAllTradesAction(up))

            elif c.getId() == CardId.JAX:
                self.addToBot(Actions.PlayerLoseHp(3, True))
                self.addToBot(Actions.BuffPlayer(3 if up else 2))

            elif c.getId() == CardId.LIMIT_BREAK:
                self.addToBot(Actions.LimitBreakAction())

            elif c.getId() == CardId.MADNESS:
                self.addToBot(Actions.MadnessAction())

            elif c.getId() == CardId.MASTER_OF_STRATEGY:
                self.addToBot(Actions.DrawCards(4 if up else 3))

            elif c.getId() == CardId.METAMORPHOSIS:
                self.addToBot(Actions.PutRandomCardsInDrawPile(CardType.ATTACK,5 if up else 3))

            elif c.getId() == CardId.OFFERING:
                self.addToBot(Actions.PlayerLoseHp(6, True))
                self.addToBot(Actions.GainEnergy(2))
                self.addToBot(Actions.DrawCards(5 if up else 3))

            elif c.getId() == CardId.PANACEA:
                self.addToBot(Actions.BuffPlayer(2 if up else 1))

            elif c.getId() == CardId.PANIC_BUTTON:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(40 if up else 30)))
                self.addToBot(Actions.DebuffPlayer(2))

            elif c.getId() == CardId.POWER_THROUGH:
                self.addToBot(Actions.MakeTempCardInHand(CardId.WOUND, False, 2))
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(20 if up else 15)))

            elif c.getId() == CardId.PURITY:
                self.addToBot(Actions.ExhaustMany(5 if up else 3))

            elif c.getId() == CardId.RAGE:
                self.addToBot(Actions.BuffPlayer(5 if up else 3))

            elif c.getId() == CardId.SECRET_TECHNIQUE:
                self.addToBot(Actions.DrawToHandAction(CardSelectTask.SECRET_TECHNIQUE, CardType.SKILL))

            elif c.getId() == CardId.SECRET_WEAPON:
                self.addToBot(Actions.DrawToHandAction(CardSelectTask.SECRET_WEAPON, CardType.ATTACK))

            elif c.getId() == CardId.SECOND_WIND:
                self.addToBot(Actions.SecondWindAction(self.calculateCardBlock(7 if up else 5)))

            elif c.getId() == CardId.SEEING_RED:
                self.addToBot(Actions.GainEnergy(2))

            elif c.getId() == CardId.SENTINEL:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(8 if up else 5)))

            elif c.getId() == CardId.SHOCKWAVE:
                self.addToBot(Actions.DebuffAllEnemy(5 if up else 3, False))
                self.addToBot(Actions.DebuffAllEnemy(5 if up else 3, False))

            elif c.getId() == CardId.SHRUG_IT_OFF:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(11 if up else 8)))
                self.addToBot(Actions.DrawCards(1))

            elif c.getId() == CardId.SPOT_WEAKNESS:
                self.addToBot(Actions.SpotWeaknessAction(t,4 if up else 3))

            elif c.getId() == CardId.THE_BOMB:
                self.addToBot(Actions.BuffPlayer(50 if up else 40))

            elif c.getId() == CardId.THINKING_AHEAD: # same as upgraded warcry
                self.addToBot(Actions.DrawCards(2))
                self.addToBot(Actions.WarcryAction())

            elif c.getId() == CardId.TRANSMUTATION:
                if self.player.energy > item.energyOnUse:
                    item.energyOnUse = self.player.energy
                if item.ignoreEnergyTotal == 0 and self.player.energy < item.energyOnUse:
                    item.energyOnUse = self.player.energy

                self.addToBot(Actions.TransmutationAction(up, item.energyOnUse, not(item.freeToPlay or c.freeToPlayOnce)))

            elif c.getId() == CardId.TRIP: # maybe fixed --- todo this doesn't work properly because it only requires a target when not upgraded, also the trip card doesn't uses its own implementation of debuff all enemy
                if up:
                    self.addToBot(Actions.DebuffAllEnemy(2, False))
                else:
                    self.addToBot(Actions.DebuffEnemy(t, 2, False))

            elif c.getId() == CardId.TRUE_GRIT:
                self.addToBot(Actions.GainBlock(self.calculateCardBlock(9 if up else 7)))
                if up:
                    self.addToBot(Actions.ChooseExhaustOne())
                else:
                    self.addToBot(Actions.ExhaustRandomCardInHand(1))

            elif c.getId() == CardId.VIOLENCE:
                self.addToBot(Actions.ViolenceAction(4 if up else 3))

            elif c.getId() == CardId.WARCRY:
                self.addToBot(Actions.DrawCards(2 if up else 1))
                self.addToBot(Actions.WarcryAction())

            else:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                std::cerr << "attempted to use unimplemented card: " << c.getName() << std::endl
                False = assert()
##endif

        def usePowerCard(self):
            item = self.curCardQueueItem
            c = item.card

            t = item.target
            up = c.isUpgraded()


            if c.getId() == CardId.BARRICADE:
                self.player.setHasStatus(True)

            elif c.getId() == CardId.BERSERK:
                self.player.energyPerTurn += 1
                self.addToBot(Actions.DebuffPlayer(1 if up else 2, False))

            elif c.getId() == CardId.BRUTALITY:
                self.addToBot(Actions.BuffPlayer(1))

            elif c.getId() == CardId.CORRUPTION:
                self.addToBot(Actions.BuffPlayer())

            elif c.getId() == CardId.COMBUST:
                self.addToBot(Actions.BuffPlayer(7 if up else 5))

            elif c.getId() == CardId.DEMON_FORM:
                self.addToBot(Actions.BuffPlayer(3 if up else 2))

            elif c.getId() == CardId.DARK_EMBRACE:
                self.addToBot(Actions.BuffPlayer(1))

            elif c.getId() == CardId.EVOLVE:
                self.addToBot(Actions.BuffPlayer(2 if up else 1))

            elif c.getId() == CardId.FEEL_NO_PAIN:
                self.addToBot(Actions.BuffPlayer(4 if up else 3))

            elif c.getId() == CardId.FIRE_BREATHING:
                self.addToBot(Actions.BuffPlayer(10 if up else 6))

            elif c.getId() == CardId.INFLAME:
                self.addToBot(Actions.BuffPlayer(3 if up else 2))

            elif c.getId() == CardId.JUGGERNAUT:
                self.addToBot(Actions.BuffPlayer(7 if up else 5))

            elif c.getId() == CardId.MAGNETISM:
                self.addToBot(Actions.BuffPlayer(1))

            elif c.getId() == CardId.MAYHEM:
                self.addToBot(Actions.BuffPlayer(1))

            elif c.getId() == CardId.METALLICIZE:
                self.addToBot(Actions.BuffPlayer(4 if up else 3))

            elif c.getId() == CardId.PANACHE:
                self.addToBot(Actions.BuffPlayer(14 if up else 10))

            elif c.getId() == CardId.RUPTURE:
                self.addToBot(Actions.BuffPlayer(2 if up else 1))

            elif c.getId() == CardId.SADISTIC_NATURE:
                self.addToBot(Actions.BuffPlayer(7 if up else 5))

            elif c.getId() == CardId.WRAITH_FORM:
                self.addToBot(Actions.BuffPlayer(3 if up else 2))
                self.addToBot(Actions.DebuffPlayer(1))

            else:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                std::cerr << "attempted to use unimplemented card: " << c.getName() << std::endl
                False = assert()
##endif


        def onUseAttackCard(self):
            item = self.curCardQueueItem
            c = item.card

            p = self.player
            p.attacksPlayedThisTurn += 1

            # ********* Powers onUseCard *********

            if p.hasStatus():
                self.addToBot(Actions.GainBlock(p.getStatus()))

            if (not item.purgeOnUse) and p.hasStatus():
                self.queuePurgeCard(c, item.target)
                p.decrementStatus()

            if (not item.purgeOnUse) and p.hasStatus():
                self.queuePurgeCard(c, item.target)
                p.decrementStatus()

            echoForm = p.getStatus()
            if (not item.purgeOnUse) and echoForm != 0:
                echoFormActive = self.player.cardsPlayedThisTurn - self.player.echoFormCardsDoubled <= echoForm is not None
                if echoFormActive:
                    self.player.echoFormCardsDoubled += 1
                    self.queuePurgeCard(c, item.target)

# C++ TO PYTHON CONVERTER TASK: The following assignment within expression was not converted by C++ to Python Converter:
# ORIGINAL LINE: if (p.hasStatus<PlayerStatus::PANACHE>() && --p.panacheCounter <= 0)
            if p.hasStatus() and --p.panacheCounter <= 0:
                self.addToBot(Actions.DamageAllEnemy(p.getStatus()))

            if p.hasStatus():
                self.addToBot(Actions.GainBlock(p.getStatus()))

            if p.hasStatus():
                p.removeStatus()

            if p.hasStatus():
                p.decrementStatus()

            if p.hasStatus():
                # todo does this need to be added to bot?
                self.addToBot(Actions.RemoveStatus())

            # ********* Relics onUseCard *********
            # todo order of relics

            if p.hasRelic():
                p.inkBottleCounter += 1
                if p.inkBottleCounter == 10:
                    p.inkBottleCounter = 0
                    self.addToBot(Actions.DrawCards(1))

            if p.hasRelic() and math.fmod(p.attacksPlayedThisTurn, 3) == 0:
                self.addToBot(Actions.BuffPlayer(1))

            if p.hasRelic():
                p.orangePelletsCardTypesPlayed.set(int(CardType.ATTACK), True) # set bit 0 true
                if p.orangePelletsCardTypesPlayed.all():
                    p.orangePelletsCardTypesPlayed.reset()
                    self.addToBot(Actions.RemovePlayerDebuffs())

            if p.hasRelic() and math.fmod(p.attacksPlayedThisTurn, 3) == 0:
                self.addToBot(Actions.GainBlock(4))

            if p.hasRelic() and math.fmod(p.attacksPlayedThisTurn, 3) == 0:
                self.addToBot(Actions.BuffPlayer(1))

            if p.hasRelic() and (not p.haveUsedNecronomiconThisTurn) and (not item.freeToPlay) and (not item.purgeOnUse) and (c.costForTurn >= 2 or c.isXCost() and item.energyOnUse >= 2):
                self.queuePurgeCard(c, item.target)
                p.haveUsedNecronomiconThisTurn = True

            if p.hasRelic():
                p.penNibCounter += 1
                if p.penNibCounter == 9:
                    self.addToBot(Actions.BuffPlayer(1))
                    p.penNibCounter = -1 # take note of this

            if p.hasRelic():
                self.addToBot(Actions.DualityAction())

            if p.hasRelic():
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (p.nunchakuCounter++ % 10 == 0)
                if math.fmod(p.nunchakuCounter, 10) == 0:
                    p.nunchakuCounter += 1
                    self.addToBot(Actions.GainEnergy(1))
                    p.nunchakuCounter = 0
                else:
                    p.nunchakuCounter += 1

            #
            #     *  for each card in hand : TriggerOnCardPlayed
            #     *  for each card in discardPile : TriggerOnCardPlayed
            #     *  for each card in drawPile : TriggerOnCardPlayed
            #

            # ********* Enemy Powers onUseCard *********

            # todo Choke Power

            m = self.monsters.arr[0]
            if m.hasStatus():
                self.addToBot(Actions.DamagePlayer(m.getStatus()))


        def onUseSkillCard(self):
            item = self.curCardQueueItem
            c = item.card

            p = self.player
            p.skillsPlayedThisTurn += 1

            # ********* Powers onUseCard *********

            if p.hasStatus():
                self.addToBot(Actions.GainBlock(p.getStatus()))

            if (not item.purgeOnUse) and p.hasStatus():
                self.queuePurgeCard(c, item.target)
                p.decrementStatus()

            if (not item.purgeOnUse) and p.hasStatus():
                self.queuePurgeCard(c, item.target)
                p.decrementStatus()

            echoForm = p.getStatus()
            if (not item.purgeOnUse) and echoForm != 0:
                echoFormActive = self.player.cardsPlayedThisTurn - self.player.echoFormCardsDoubled <= echoForm is not None
                if echoFormActive:
                    self.player.echoFormCardsDoubled += 1
                    self.queuePurgeCard(c, item.target)

            if p.hasStatus():
                self.addToBot(Actions.MakeTempCardInDrawPile(CardInstance(CardId.DAZED), 1, True))

# C++ TO PYTHON CONVERTER TASK: The following assignment within expression was not converted by C++ to Python Converter:
# ORIGINAL LINE: if (p.hasStatus<PlayerStatus::PANACHE>() && --p.panacheCounter <= 0)
            if p.hasStatus() and --p.panacheCounter <= 0:
                self.addToBot(Actions.DamageAllEnemy(p.getStatus()))

            # todo Storm
            # todo Heatsinks
            # todo BirdFacedUrn

            # ********* Relics onUseCard *********
            # todo ink bottle/ ornamental fan need to be ordered i believe

            if p.hasRelic():
                p.inkBottleCounter += 1
                if p.inkBottleCounter == 10:
                    p.inkBottleCounter = 0
                    self.addToBot(Actions.DrawCards(1))

            if p.hasRelic():
                p.orangePelletsCardTypesPlayed.set(int(CardType.SKILL), True) # set bit 0 true
                if p.orangePelletsCardTypesPlayed.all():
                    p.orangePelletsCardTypesPlayed.reset()
                    self.addToBot(Actions.RemovePlayerDebuffs())

            if p.hasRelic():
                if p.skillsPlayedThisTurn >= 3 and math.fmod(p.skillsPlayedThisTurn, 3) == 0:
                    self.addToBot(Actions.DamageAllEnemy(5))

            if p.hasRelic():
                # todo
                pass

            #
            #     *  for each card in hand : TriggerOnCardPlayed
            #     *  for each card in discardPile : TriggerOnCardPlayed
            #     *  for each card in drawPile : TriggerOnCardPlayed
            #

            # ********* Enemy Powers onUseCard *********
            # todo Choke Power

            m = self.monsters.arr[0]
            if m.hasStatus():
                m.buff(m.getStatus())

        def onUsePowerCard(self):
            item = self.curCardQueueItem
            c = item.card
            p = self.player

            if p.hasStatus():
                self.addToBot(Actions.GainBlock(p.getStatus()))

            if (not item.purgeOnUse) and p.hasStatus():
                self.queuePurgeCard(c, item.target)
                p.decrementStatus()

            echoForm = p.getStatus()
            if (not item.purgeOnUse) and echoForm != 0:
                echoFormActive = self.player.cardsPlayedThisTurn - self.player.echoFormCardsDoubled <= echoForm is not None
                if echoFormActive:
                    self.player.echoFormCardsDoubled += 1
                    self.queuePurgeCard(c, item.target)

            if p.hasStatus():
                self.addToBot(Actions.MakeTempCardInDrawPile(CardInstance(CardId.DAZED), 1, True))

# C++ TO PYTHON CONVERTER TASK: The following assignment within expression was not converted by C++ to Python Converter:
# ORIGINAL LINE: if (p.hasStatus<PlayerStatus::PANACHE>() && --p.panacheCounter <= 0)
            if p.hasStatus() and --p.panacheCounter <= 0:
                self.addToBot(Actions.DamageAllEnemy(p.getStatus()))

            # ********* Relics onUseCard *********

            if p.hasRelic():
                p.heal(2)

            if p.hasRelic():
                p.inkBottleCounter += 1
                if p.inkBottleCounter == 10:
                    p.inkBottleCounter = 0
                    self.addToBot(Actions.DrawCards(1))

            if p.hasRelic():
                p.orangePelletsCardTypesPlayed.set(int(CardType.POWER), True) # set bit 0 true
                if p.orangePelletsCardTypesPlayed.all():
                    p.orangePelletsCardTypesPlayed.reset()
                    self.addToBot(Actions.RemovePlayerDebuffs())

            if p.hasRelic():
                self.mummifiedHandOnUsePower()

            #    auto &m = monsters.optionMap[2]
            #    if (m.hasStatusInternal<MS::CURIOSITY>()) {
            #        m.buff<MS::STRENGTH>(m.getStatus<MS::CURIOSITY>())
            #    }

        def onUseStatusOrCurseCard(self):
            item = self.curCardQueueItem
            c = item.card
            p = self.player

            if p.hasStatus():
                self.addToBot(Actions.GainBlock(p.getStatus()))

            if (not item.purgeOnUse) and p.hasStatus():
                self.queuePurgeCard(c, item.target)
                p.decrementStatus()

            echoForm = p.getStatus()
            if (not item.purgeOnUse) and echoForm != 0:
                echoFormActive = self.player.cardsPlayedThisTurn - self.player.echoFormCardsDoubled <= echoForm is not None
                if echoFormActive:
                    self.player.echoFormCardsDoubled += 1
                    self.queuePurgeCard(c, item.target)

            if p.hasStatus():
                self.addToBot(Actions.MakeTempCardInDrawPile(CardInstance(CardId.DAZED), 1, True))

# C++ TO PYTHON CONVERTER TASK: The following assignment within expression was not converted by C++ to Python Converter:
# ORIGINAL LINE: if (p.hasStatus<PlayerStatus::PANACHE>() && --p.panacheCounter <= 0)
            if p.hasStatus() and --p.panacheCounter <= 0:
                self.addToBot(Actions.DamageAllEnemy(p.getStatus()))

            if c.getType() == CardType.CURSE:
                if p.hasRelic():
                    self.addToBot(Actions.PlayerLoseHp(1, True))
                    item.exhaustOnUse = True

            elif c.getType() == CardType.STATUS:
                if p.hasRelic():
                    item.exhaustOnUse = True

            if p.hasRelic():
                p.inkBottleCounter += 1
                if p.inkBottleCounter == 10:
                    p.inkBottleCounter = 0
                    self.addToBot(Actions.DrawCards(1))


        def onAfterUseCard(self):
            item = self.curCardQueueItem
            c = item.card

            if item.triggerOnUse:
                m = self.monsters.arr[0]
                if m.hasStatus():
                    timeWarp = m.getStatus()
                    if timeWarp == 11:
                        m.setStatus(0)
                        m.buff(2)
                        self.callEndTurnEarlySequence()

                    else:
                        m.setStatus(timeWarp + 1)
                        timeWarp += 1
                if m.hasStatus():
                    m.buff(1)
                if m.hasStatus():
                    self.addToBot(Actions.DamagePlayer(m.getStatus()))

            if item.purgeOnUse:
                return

            rebound = False
            c.freeToPlayOnce = False

            if c.getType() == CardType.POWER:
                c.id = CardId.INVALID
                return

            if self.player.hasStatus():
                if self.player.getStatus() == 1:
                    rebound = True
                    self.player.setHasStatus(False)

                else:
                    self.player.setStatusValueNoChecks(1)

            spoonProc = False
            if item.exhaustOnUse and self.player.hasRelic():
                spoonProc = self.cardRandomRng.randomBoolean()

            if item.exhaustOnUse and not spoonProc:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: triggerAndMoveToExhaustPile(c);
                self.triggerAndMoveToExhaustPile(sts.CardInstance(c))

            else:
                # targetCard.exhaustOnUseOnce = false
                # targetCard.dontTriggerOnUseCard = false
                # this.addToBot(new HandCheckAction())

                if rebound:
                    self.cards.moveToDrawPileTop(c)

                elif c.id == CardId.TANTRUM:
                    self.cards.shuffleIntoDrawPile(self.cardRandomRng, c)

                else:
                    # The game calls OnCardDrawOrDiscard here which only does two things:
                    # 1. sets the damage on all shivs in hand if you have accuracy power,
                    # 2. sets the cost of all skills in hand to -9 if you have corruption
                    # we will handle these tasks elsewhere
                    self.cards.moveToDiscardPile(c)
            # TODO these must be done in the cards method itself
            # todo make Accuracy part of calculateBaseDamage

            # this.targetCard.exhaustOnUseOnce = false
            #            this.targetCard.dontTriggerOnUseCard = false
            #            this.addToBot(new HandCheckAction())

        def setState(self, s):
            self.inputState = s

        def addToTop(self, a):
            actionQueue.pushFront(a)

        def addToBot(self, a):
            actionQueue.pushBack(a)


        # todo remove or replace other method that does this
        def addToTopCard(self, item):
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cardQueue.pushFront(item);
            self.cardQueue.pushFront(sts.CardQueueItem(item))

        def addToBotCard(self, item):
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cardQueue.pushBack(item);
            self.cardQueue.pushBack(sts.CardQueueItem(item))

        def checkCombat(self):
            if self.outcome == Outcome.PLAYER_VICTORY:
                self.clearPostCombatActions()

        def clearPostCombatActions(self):
            # todo?
            self.cleanCardQueue() # this is actually done when monsters are damaged but we can do here?
            #    actionQueue.clearOnCombatVictory()

            curIdx = actionQueue.front
            placeIdx = actionQueue.front

            i = 0
            while i < actionQueue.size:
                if curIdx >= actionQueue.getCapacity():
                    curIdx = 0
                shouldClear = actionQueue.bits.test(curIdx)

                if shouldClear:
                    actionQueue.size -= 1

                else:
                    if placeIdx >= actionQueue.getCapacity():
                        placeIdx = 0

                    actionQueue.bits.set(placeIdx, actionQueue.bits.test(curIdx))
                    actionQueue.arr[placeIdx] = actionQueue.arr[curIdx]
                    placeIdx += 1
                curIdx += 1
                i += 1

            actionQueue.back = math.fmod((actionQueue.front + actionQueue.size), actionQueue.getCapacity())

            #    auto actionQueueCopy = actionQueue
            #    actionQueue.clear()
            #    while (actionQueueCopy.size > 0) {
            #        if (!actionQueueCopy.bits[actionQueueCopy.front]) {
            #
            #            actionQueue.pushBack(actionQueueCopy.popFront())
            #        } else {
            #            actionQueueCopy.popFront()
            #        }
            #    }

        def cleanCardQueue(self):
            # todo
            # not sure where this matters, as we don't queue more than 1 item at a time in the hand
            pass

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isCardPlayAllowed() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isCardPlayAllowed() const
        def isCardPlayAllowed(self):
            if self.player.hasRelic() and self.player.cardsPlayedThisTurn >= 6:
                return False

            if self.cards.handNormalityCount != 0 and self.player.cardsPlayedThisTurn >= 3:
                return False

            return True

        # **********************


        # **********************

        def endTurn(self):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_assert
            assert not self.endTurnQueued
##endif //sts_assert
            # todo probably dont need a card queue item for this
            self.energyWasted += self.player.energy
            self.cardQueue.pushBack(CardQueueItem.endTurnItem())
            self.endTurnQueued = True

        def callEndOfTurnActions(self):

            # ********************* Player Relics OnPlayerEndTurn *********************

            if self.player.hasRelic():
                self.addToBot(Actions.GainBlock(self.cards.cardsInHand))

            if self.player.hasRelic():
                if self.player.hasEmptyOrb():
                    self.player.channelOrb.FROST

            if self.player.hasRelic():
                self.addToBot(Actions.CodexAction())

            if self.player.hasRelic():
                if self.player.block <= 0:
                    self.addToTop(Actions.GainBlock(6))

            if self.player.hasRelic():
                if self.turn == 6:
                    self.addToBot(Actions.DamageAllEnemy(52))

            # ********************* Player Powers AtEndOfTurnPreEndTurnCards *********************

            if self.player.hasStatus():
                self.addToBot(Actions.GainBlock(self.player.getStatus()))

            if self.player.hasStatus():
                self.addToBot(Actions.GainBlock(self.player.getStatus()))

            if self.player.hasStatus() and self.player.stance == Stance.CALM:
                self.addToBot(Actions.GainBlock(self.player.getStatus()))

            if self.player.orbSlots:
                self.addToBot(Actions.TriggerEndOfTurnOrbsAction())

            # todo for cards in hand call triggerOnEndOfTurnForPlayingCard

            i = 0
            while i < self.cards.cardsInHand:

                c = self.cards.hand[i]

                if (c.id == CardId.BURN) or (c.id == CardId.DECAY) or (c.id == CardId.DOUBT) or (c.id == CardId.SHAME) or (c.id == CardId.REGRET):
                        item = CardQueueItem()
                        item.triggerOnUse = False
                        item.regretCardCount = self.cards.cardsInHand
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: item.card = c;
                        item.card.copy_from(c)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: addToBotCard(item);
                        self.addToBotCard(sts.CardQueueItem(item))
                i += 1

            # todo stance onEndOfTurn

        def onTurnEnding(self):
            # AbstractRoom endTurn()

            # ********************* Player Powers atEndOfTurn *********************
            self.player.applyEndOfTurnPowers(self)
            self.addToBot(Actions.ClearCardQueue())
            self.addToBot(Actions.DiscardAtEndOfTurn())

            # todo reset card attributes here in draw, discard and hand
            self.cards.resetAttributesAtEndOfTurn()

            self.addToBot(Actions.UnnamedEndOfTurnAction())

        def callEndTurnEarlySequence(self):
            while not self.cardQueue.isEmpty():
                item = self.cardQueue.popFront()
                if item.autoplay and not item.purgeOnUse:
                    self.addToBot(Actions.TimeEaterPlayCardQueueItem(item))
            self.addToTopCard(CardQueueItem.endTurnItem())
            self.endTurnQueued = True

        def applyEndOfRoundPowers(self):
            i = 0
            while i < self.monsters.monsterCount:
                m = self.monsters.arr[i]
                if m.isDying() or m.isEscaping():
                    i += 1
                    continue
                m.applyEndOfTurnTriggers(self)
                i += 1

            self.player.applyAtEndOfRoundPowers()

            i = 0
            while i < self.monsters.monsterCount:
                m = self.monsters.arr[i]
                if m.isDying() or m.isEscaping():
                    i += 1
                    continue
                m.applyEndOfRoundPowers(self)
                i += 1

        def afterMonsterTurns(self):
            # ********* Enemy powers atEndOfRound *********
            if not self.skipMonsterTurn:
                self.applyEndOfRoundPowers()

            self.turn += 1
            self.skipMonsterTurn = False
            self.turnHasEnded = False

            # player stance atStartOfTurn
            if self.player.stance == Stance.DIVINITY:
                self.addToBot(Actions.ChangeStance.NEUTRAL)

            self.player.applyStartOfTurnRelics(self)

            # player applyStartOfTurnPreDrawCards() // no cards implement this
            # player.applyStartOfTurnCards() // only Eviscerate implements this

            self.player.applyStartOfTurnPowers((self))

            # player.applyStartOfTurnOrbs()
            #for each orb : OnStartOfTurn
            #if have relic cables: apply orb[0].OnStartOfTurn again

            if self.player.hasStatus():

                pass
            elif self.player.hasStatus():
                self.player.decrementStatus()

            elif self.player.hasRelic():
                self.player.block = max(0, self.player.block-15)

            else:
                self.player.block = 0

            if self.isBattleOver:
                return

            self.addToBot(Actions.DrawCards(int8_t(self.player.cardDrawPerTurn))) # in this action, an effect queue item is added to rechard energy lol

            if self.player.hasStatus():
                if self.player.wasJustApplied():
                    self.player.setJustApplied(False)
                else:
                    self.player.removeStatus()
                    self.player.cardDrawPerTurn += 1

            self.player.applyStartOfTurnPostDrawRelics(self)
            self.player.applyStartOfTurnPostDrawPowers(self)

            # this has to be here because some relics check this info.
            self.player.cardsPlayedThisTurn = 0
            self.player.attacksPlayedThisTurn = 0
            self.player.skillsPlayedThisTurn = 0
            self.player.cardsDiscardedThisTurn = 0

            self.player.rechargeEnergy(self) # this is called by the PlayerTurnEffect in game, I think it can be done here

        def obtainPotion(self, p):
            if self.potionCount == self.potionCapacity or self.player.hasRelic():
                return # no empty potion slots

            i = 0
            while i < self.potionCapacity:
                if self.potions[i] == Potion.EMPTY_POTION_SLOT:
                    self.potionCount += 1
                    self.potions[i] = p
                    return
                i += 1

            #  todo prevent this, do nothing for now
            #    assert(false); // unreachable

        def discardPotion(self, idx):
            self.potions[idx] = Potion.EMPTY_POTION_SLOT
            self.potionCount -= 1

        def drinkPotion(self, idx, target = 0):
            hasBark = self.player.hasRelic()
            p = self.potions[idx]
            self.discardPotion(idx)

            # todo - dont need to add to bot because always will have nothing in actionQueue?

            if p == Potion.AMBROSIA:
                self.addToBot(Actions.ChangeStance.DIVINITY)

            elif p == Potion.ANCIENT_POTION:
                self.addToBot(Actions.BuffPlayer(2 if hasBark else 1))

            elif p == Potion.ATTACK_POTION:
                self.addToBot(Actions.DiscoveryAction(CardType.ATTACK,2 if hasBark else 1))

            elif p == Potion.BLESSING_OF_THE_FORGE:
                self.addToBot(Actions.UpgradeAllCardsInHand())

            elif p == Potion.BLOCK_POTION:
                self.addToBot(Actions.GainBlock(20 if hasBark else 10))


            elif p == Potion.BLOOD_POTION:
                    healAmt = int((float((self.player.maxHp * (20 if hasBark else 40))) / 100.0))
                    self.addToBot(Actions.HealPlayer(healAmt))

            elif p == Potion.BOTTLED_MIRACLE:
                self.addToBot(Actions.MakeTempCardInHand(CardId.MIRACLE, False,4 if hasBark else 2))

            elif p == Potion.COLORLESS_POTION:
                self.addToBot(Actions.DiscoveryAction(CardType.STATUS,2 if hasBark else 1)) # status card type is being used to indicate colorless

            elif p == Potion.CULTIST_POTION:
                self.addToBot(Actions.BuffPlayer<PlayerStatus.RITUAL>(2 if hasBark else 1))

            elif p == Potion.CUNNING_POTION:
                self.addToBot(Actions.MakeTempCardInHand(CardId.SHIV, True,6 if hasBark else 3))

            elif p == Potion.DEXTERITY_POTION:
                self.addToBot(Actions.BuffPlayer(4 if hasBark else 2))

            elif p == Potion.DISTILLED_CHAOS:
                    cardsToPlay = 6 if hasBark else 3
                    for i in range(0, cardsToPlay):
                        self.addToBot(Actions.PlayTopCard(self.monsters.getRandomMonsterIdx(self.cardRandomRng), False))

            elif p == Potion.DUPLICATION_POTION:
                self.addToBot(Actions.BuffPlayer(2 if hasBark else 1))

            elif p == Potion.ELIXIR_POTION:
                self.addToBot(Actions.ExhaustMany(10))

            elif p == Potion.ENERGY_POTION:
                self.addToBot(Actions.GainEnergy(4 if hasBark else 2))

            elif p == Potion.ENTROPIC_BREW:
                    i = 0
                    while i < self.potionCapacity:
                        randomPotion = returnRandomPotion(self.potionRng, self.player.cc, True)
                        self.obtainPotion(randomPotion)
                        i += 1

            elif p == Potion.ESSENCE_OF_DARKNESS:
                self.addToBot(Actions.EssenceOfDarkness(2 if hasBark else 1))

            elif p == Potion.ESSENCE_OF_STEEL:
                self.addToBot(Actions.BuffPlayer(8 if hasBark else 4))

            elif p == Potion.EXPLOSIVE_POTION:
                    damage = 20 if hasBark else 10
                    self.addToBot(Actions.DamageAllEnemy(damage)) # todo does not having player be owner here matter?

            elif p == Potion.FEAR_POTION:
                self.addToBot(Actions.DebuffEnemy(target,6 if hasBark else 3, False))

            elif p == Potion.FIRE_POTION:
                self.addToBot(Actions.DamageEnemy(idx,40 if hasBark else 20))

            elif p == Potion.FLEX_POTION:
                self.addToBot(Actions.BuffPlayer(10 if hasBark else 5))
                self.addToBot(Actions.DebuffPlayer(10 if hasBark else 5))

            elif p == Potion.FOCUS_POTION:
                self.addToBot(Actions.BuffPlayer(4 if hasBark else 2))

            elif p == Potion.FRUIT_JUICE:
                self.player.increaseMaxHp(10 if hasBark else 5)

            elif p == Potion.GAMBLERS_BREW:
                self.addToBot(Actions.GambleAction())

            elif p == Potion.GHOST_IN_A_JAR:
                self.addToBot(Actions.BuffPlayer(2 if hasBark else 1))

            elif p == Potion.HEART_OF_IRON:
                self.addToBot(Actions.BuffPlayer(12 if hasBark else 6))

            elif p == Potion.LIQUID_BRONZE:
                self.addToBot(Actions.BuffPlayer(6 if hasBark else 3))

            elif p == Potion.LIQUID_MEMORIES:
                self.addToBot(Actions.BetterDiscardPileToHandAction(2 if hasBark else 1, CardSelectTask.LIQUID_MEMORIES_POTION))

            elif p == Potion.POISON_POTION:
                self.addToBot(Actions.DebuffEnemy(target,12 if hasBark else 6))

            elif p == Potion.POTION_OF_CAPACITY:
                self.addToBot(Actions.IncreaseOrbSlots(4 if hasBark else 2))

            elif p == Potion.POWER_POTION:
                self.haveUsedDiscoveryAction = True
                self.addToBot(Actions.DiscoveryAction(CardType.POWER,2 if hasBark else 1))

            elif p == Potion.REGEN_POTION:
                self.addToBot(Actions.BuffPlayer(10 if hasBark else 5))

            elif p == Potion.SKILL_POTION:
                self.addToBot(Actions.DiscoveryAction(CardType.SKILL,2 if hasBark else 1))

            elif p == Potion.SMOKE_BOMB:
                # todo
                pass

            elif p == Potion.SNECKO_OIL:
                self.addToBot(Actions.DrawCards(10 if hasBark else 5))
                self.addToBot(Actions.RandomizeHandCost())

            elif p == Potion.SPEED_POTION:
                self.addToBot(Actions.BuffPlayer(10 if hasBark else 5))
                self.addToBot(Actions.DebuffPlayer(10 if hasBark else 5))

            elif p == Potion.STANCE_POTION:
                self.addToBot(Actions.SetState(InputState.CHOOSE_STANCE_ACTION))

            elif p == Potion.STRENGTH_POTION:
                self.addToBot(Actions.BuffPlayer(4 if hasBark else 2))

            elif p == Potion.SWIFT_POTION:
                self.addToBot(Actions.DrawCards(6 if hasBark else 3))

            elif p == Potion.WEAK_POTION:
                self.addToBot(Actions.DebuffEnemy(target,6 if hasBark else 3, False))


            if p != Potion.AMBROSIA and p != Potion.ANCIENT_POTION and p != Potion.ATTACK_POTION and p != Potion.BLESSING_OF_THE_FORGE and p != Potion.BLOCK_POTION and p != Potion.BLOOD_POTION and p != Potion.BOTTLED_MIRACLE and p != Potion.COLORLESS_POTION and p != Potion.CULTIST_POTION and p != Potion.CUNNING_POTION and p != Potion.DEXTERITY_POTION and p != Potion.DISTILLED_CHAOS and p != Potion.DUPLICATION_POTION and p != Potion.ELIXIR_POTION and p != Potion.ENERGY_POTION and p != Potion.ENTROPIC_BREW and p != Potion.ESSENCE_OF_DARKNESS and p != Potion.ESSENCE_OF_STEEL and p != Potion.EXPLOSIVE_POTION and p != Potion.FEAR_POTION and p != Potion.FIRE_POTION and p != Potion.FLEX_POTION and p != Potion.FOCUS_POTION and p != Potion.FRUIT_JUICE and p != Potion.GAMBLERS_BREW and p != Potion.GHOST_IN_A_JAR and p != Potion.HEART_OF_IRON and p != Potion.LIQUID_BRONZE and p != Potion.LIQUID_MEMORIES and p != Potion.POISON_POTION and p != Potion.POTION_OF_CAPACITY and p != Potion.POWER_POTION and p != Potion.REGEN_POTION and p != Potion.SKILL_POTION and p != Potion.SMOKE_BOMB and p != Potion.SNECKO_OIL and p != Potion.SPEED_POTION and p != Potion.STANCE_POTION and p != Potion.STRENGTH_POTION and p != Potion.SWIFT_POTION and p != Potion.WEAK_POTION:
                std::cerr << self.seed << "invalid drink potion: " << int(p) << std::endl
                False = assert()


        def drawCards(self, count):
            if count <= 0 or self.player.hasStatus() or self.cards.drawPile.size() + self.cards.discardPile.size() == 0 or self.cards.cardsInHand == 10:
                return

            amountToDraw = min(10-self.cards.cardsInHand, count)

            if self.cards.drawPile.size() < amountToDraw:
                temp = amountToDraw-int(self.cards.drawPile.size())
                self.addToTop(Actions.DrawCards(auto(temp)))
                self.onShuffle()
                self.addToTop(Actions.EmptyDeckShuffle())

                if not self.cards.drawPile.empty():
                    self.drawCards(int(self.cards.drawPile.size())) # the game adds this to top
                return

            self.cardsDrawn += amountToDraw # statistic for monte carlo search
            self.cards.draw(self, amountToDraw)

        def discardAtEndOfTurn(self):
            retainCount = 0
            i = 0
            while i < self.cards.cardsInHand:
                c = self.cards.hand[i]
                if c.hasSelfRetain() or c.retain:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards.limbo[retainCount++] = c;
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
                    self.cards.limbo[retainCount].copy_from(c)
                    retainCount += 1
                i += 1
            if retainCount > 0:
                self.addToTop(Actions.RestoreRetainedCards(retainCount))

                placeIdx = 0
                i = 0
                while i < self.cards.cardsInHand:
                    c = self.cards.hand[i]
                    if c.hasSelfRetain() or c.retain:
                        i += 1
                        continue
                    else:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: cards.hand[placeIdx++] = cards.hand[i];
                        self.cards.hand[placeIdx] = self.cards.hand[i]
                        placeIdx += 1
                    i += 1
                self.cards.cardsInHand -= retainCount

            if (not self.player.hasRelic()) and not self.player.hasStatus():
                self.addToTop(Actions.DiscardAtEndOfTurnHelper())

            i = 0
            while i < self.cards.cardsInHand:
                c = self.cards.hand[i]
                if c.isEthereal():
                    self.addToTop(Actions.ExhaustSpecificCardInHand(i, c.uniqueId)) # c.triggerOnEndOfPlayerTurn
                i += 1


        def discardAtEndOfTurnHelper(self):
            if self.outcome != Outcome.UNDECIDED:
                return

            temp = self.cards.cardsInHand
            for i in range(temp-1, -1, -1):
                self.cards.notifyRemoveFromHand(self.cards.hand[i])
                self.cards.moveToDiscardPile(self.cards.hand[i])
                self.player.cardsDiscardedThisTurn += 1
            self.cards.cardsInHand = 0

        def playTopCardInDrawPile(self, monsterTargetIdx, exhausts):
            if self.cards.drawPile.empty():
                if not self.cards.discardPile.empty():
                    self.addToTop(Actions.PlayTopCard(monsterTargetIdx, exhausts))
                    self.addToTop(Actions.EmptyDeckShuffle())
                return

            item = CardQueueItem(self.cards.popFromDrawPile(), monsterTargetIdx, self.player.energy)
            item.exhaustOnUse = exhausts
            item.autoplay = True
            item.freeToPlay = True # todo remove the autoplay boolean? added this instead
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: addToTopCard(item);
            self.addToTopCard(sts.CardQueueItem(item))

        def moveToHandHelper(self, c):
            if self.cards.cardsInHand < 10:
                if self.player.hasStatus() and c.getType() == CardType.SKILL:
                    c.setCostForTurn(-9)
                self.cards.moveToHand(c)
            else:
                self.cards.moveToDiscardPile(c)

        def exhaustSpecificCardInHand(self, idx, uniqueId):

            foundIdx = -1

            if idx < self.cards.cardsInHand and self.cards.hand[idx].uniqueId == uniqueId:
                foundIdx = idx
            else:
                i = 0
                while i < self.cards.cardsInHand:
                    if self.cards.hand[idx].uniqueId == uniqueId:
                        foundIdx = i
                        break
                    i += 1

            if foundIdx == -1:
                std::cerr << "exhaustSpecificCardInHand: card not found in hand\n"
                return

            self.cards.notifyRemoveFromHand(self.cards.hand[foundIdx])
            self.triggerAndMoveToExhaustPile(list(self.cards.hand[foundIdx]))
            self.cards.cardsInHand -= 1

            i = foundIdx
            while i < self.cards.cardsInHand:
                self.cards.hand[i] = self.cards.hand[i+1]
                i += 1 # todo fixed the cached variables in cardmanager

        def restoreRetainedCards(self, count):
            for i in range(0, count):
                c = self.cards.limbo[i]
                # check that c retained or self retained?
                c.retain = False
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards.hand[cards.cardsInHand++] = c;
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
                self.cards.hand[self.cards.cardsInHand].copy_from(c)
                self.cards.cardsInHand += 1

        def exhaustTopCardInHand(self):
            if self.cards.cardsInHand <= 0:
                std::cerr << "exhaustTopCardInHand: no cards in hand"
                return

            self.cards.cardsInHand -= 1
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: auto &c = cards.hand[--cards.cardsInHand];
            c = self.cards.hand[self.cards.cardsInHand]
            self.cards.notifyRemoveFromHand(c)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: triggerAndMoveToExhaustPile(c);
            self.triggerAndMoveToExhaustPile(sts.CardInstance(c))

        # this is

        #void BattleContext::incrementDiscard() { // not for end of turn
        #    player.cardsDiscardedThisTurn++;
        #    if (!turnHasEnded) {
        #        // todo
        #    }
        #
        #//    ++totalDiscardedThisTurn;
        #//    if (!AbstractDungeon.actionManager.turnHasEnded && !endOfTurn) {
        #//        AbstractDungeon.player.updateCardsOnDiscard();
        #//        Iterator var1 = AbstractDungeon.player.relics.iterator();
        #//
        #//        while(var1.hasNext()) {
        #//            AbstractRelic r = (AbstractRelic)var1.next();
        #//            r.onManualDiscard();
        #//        }
        #//    }
        #}

        def triggerOnEndOfTurnForPlayingCards(self):
            #
            #    bool foundCurse
            #    do {
            #        foundCurse = false
            #
            #        for (int i = 0; i <= hand.size(); ++i) {
            #            switch (hand[i].id) {
            #                case CardId::DECAY:
            #                    addToTop(Actions::DamagePlayer(2))
            #                    foundCurse = true
            #                    break
            #
            #                case CardId::DOUBT:
            #                    addToTop( Actions::DebuffPlayer<PS::WEAK>(1) )
            #                    foundCurse = true
            #                    break
            #
            #                case CardId::SHAME:
            #                    addToTop( Actions::DebuffPlayer<PS::FRAIL>(1) )
            #                    foundCurse = true
            #                    break
            #
            #                case CardId::REGRET:
            #                    addToTop( Actions::PlayerLoseHp(hand.size(), true) )
            #                    foundCurse = true
            #                    break
            #
            #                case CardId::BURN:
            #                    addToTop( Actions::DamagePlayer(hand[i].upgraded ? 4 : 2) )
            #                    foundCurse = true
            #                    break
            #
            #                default:
            #                    break
            #            }
            #
            #            if (foundCurse) {
            #                hand.removeCardAtIdx(i)
            #            }
            #
            #        }
            #
            #    } while (foundCurse)

            pass

        def triggerOnOtherCardPlayed(self, usedCard):
            painCount = self.cards.handPainCount
            if usedCard.getId() == CardId.PAIN:
                painCount -= 1
            for i in range(0, painCount):
                self.addToTop(Actions.PlayerLoseHp(1))

            thousandCuts = self.player.getStatus()
            if thousandCuts != 0:
                self.addToBot(Actions.DamageAllEnemy(thousandCuts))

        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
        # ORIGINAL LINE: template <MonsterStatus s>
        def debuffEnemy(self, idx, amount, isSourceMonster = True):
            # todo poison and snake skull
            e = self.monsters.arr[idx]

            if e.hasStatus():
                e.decrementStatus()
                return

            e.addDebuff(amount, isSourceMonster)
            if self.player.hasStatus():
                self.addToBot(Actions.DamageEnemy(idx, self.player.getStatus()))

            if s == MonsterStatus.VULNERABLE and self.player.hasRelic():
                self.addToBot(Actions.DebuffEnemy(idx, 1, False))

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int calculateCardDamage(const CardInstance &card, int targetIdx, int baseDamage) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int calculateCardDamage(const CardInstance &card, int targetIdx, int baseDamage) const
        def calculateCardDamage(self, card, targetIdx, baseDamage):

            damage = float(baseDamage)

            # ****** Player Relics AtDamageModify ******

            if self.player.hasRelic() and card.isStrikeCard():
                damage += 3

            if self.player.hasRelic() and card.costForTurn == 0:
                damage += 4


            # ****** Player Powers AtDamageGive ******

            damage += float(self.player.getStatus())

            if self.player.hasStatus():
                damage += float(self.player.getStatus())

            if self.player.hasStatus():
                damage *= 2

            if self.player.hasStatus():
                damage *= 2

            if self.player.hasStatus():
                damage *= .75

            # ****** Stance AtDamageGive ******

            if self.player.stance == Stance.WRATH:
                damage *= 2
            elif self.player.stance == Stance.DIVINITY:
                damage *= 3

            # ****** Enemy Powers AtDamageReceive ******
            monster = self.monsters.arr[targetIdx]

            if monster.hasStatus():
                damage *= 1 + float(monster.getStatus()) * 0.1

            if monster.hasStatus():
                if self.player.hasRelic():
                    damage *= 1.75
                else:
                    damage *= 1.5


            # ****** Player Powers AtDamageGiveFinal ****** (none ?)
            # ****** Monster Powers AtDamageReceiveFinal ******

            if monster.hasStatus():
                damage *= .5

            if monster.hasStatus():
                damage = max(damage, 1.0)

            return max(0, int(damage))

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int calculateCardBlock(int baseBlock) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int calculateCardBlock(int baseBlock) const
        def calculateCardBlock(self, baseBlock):
            if self.player.hasStatus():
                return 0

            block = baseBlock
            if self.player.hasStatus():
                block = max(0, block + self.player.getStatus())

            if self.player.hasStatus<PlayerStatus.FRAIL>():
                return math.trunc(block * 3 / float(4))

            return block

        def queuePurgeCard(self, c, target):
            item = CardQueueItem()
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: item.card = c;
            item.card.copy_from(c)
            item.purgeOnUse = True
            item.target = target
            item.energyOnUse = self.curCardQueueItem.energyOnUse
            item.ignoreEnergyTotal = True
            item.autoplay = True
            self.addPurgeCardToCardQueue(item)

        def addPurgeCardToCardQueue(self, item):
            if self.cardQueue.size > 0:
                temp = self.cardQueue.front()
                self.cardQueue.front() = item
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cardQueue.pushFront(temp);
                self.cardQueue.pushFront(sts.CardQueueItem(temp))
            else:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cardQueue.pushFront(item);
                self.cardQueue.pushFront(sts.CardQueueItem(item))


        def noOpRollMove(self):
            self.aiRng.random(99)

        def onManualDiscard(self, c):
            if c.getId() == CardId.TACTICIAN:
                self.player.gainEnergy(2 if c.isUpgraded() else 1)
            elif c.getId() == CardId.REFLEX:
                self.addToBot(Actions.DrawCards(3 if c.isUpgraded() else 2))

        def onShuffle(self):
            if self.player.hasRelic():
                self.addToBot(Actions.GainBlock(6))

            if self.player.hasRelic():
                #        addToBot(Actions::SetState(InputState::SCRY, 3) ); // TODO SCRY Action
                pass

            if self.player.hasRelic<R.SUNDIAL>():
                if self.player.sundialCounter == 2:
                    self.player.sundialCounter = 0
                    self.addToBot(Actions.GainEnergy(2))
                else:
                    self.player.sundialCounter += 1

        def triggerAndMoveToExhaustPile(self, c):
            # player relics onExhaust
            # player powers onExhaust
            # (the card).triggerOnExhaust

            if self.player.hasRelic():
                self.addToTop(Actions.DamageAllEnemy(3))

            if self.player.hasRelic():
                id = getTrulyRandomCardInCombat(self.cardRandomRng, self.player.cc)
                self.addToBot(Actions.MakeTempCardInHand(id))

            if self.player.hasStatus():
                self.addToBot(Actions.DrawCards(self.player.getStatus()))

            if self.player.hasStatus():
                self.addToBot(Actions.GainBlock(self.player.getStatus()))

            if c.getId() == CardId.NECRONOMICURSE:
                self.addToBot(Actions.MakeTempCardInHand(CardId.NECRONOMICURSE))

            if c.getId() == CardId.SENTINEL:
                self.player.gainEnergy(3 if c.isUpgraded() else 2) # the game adds to bot here

            self.cards.moveToExhaustPile(c)

        def mummifiedHandOnUsePower(self):
            matchingIdxList = fixed_list()

            i = 0
            while i < self.cards.cardsInHand:
                c = self.cards.hand[i]
                canPick = c.cost > 0 and c.costForTurn > 0 and not c.freeToPlayOnce
                if canPick:
                    matchingIdxList.push_back(i)
                i += 1

            if matchingIdxList.empty():
                return

            for i in range(matchingIdxList.size()-1, -1, -1):
                uniqueId = self.cards.hand[matchingIdxList.get(i)].getUniqueId()
                if self.cardQueue.containsCardWithId(uniqueId):
                    matchingIdxList.remove(i)

            if matchingIdxList.empty():
                return

            selectedListIdx = self.cardRandomRng.random(0,matchingIdxList.size()-1)
            selectedHandIdx = matchingIdxList.get(selectedListIdx)
            self.cards.hand[selectedHandIdx].setCostForTurn(0)

        # card select screens
        def openDiscoveryScreen(self, discoveryCards, copyCount):
            self.inputState = InputState.CARD_SELECT
            self.cardSelectInfo.cardSelectTask = CardSelectTask.DISCOVERY
            self.cardSelectInfo.pickCount = 1
            self.cardSelectInfo.canPickAnyNumber = False
            self.cardSelectInfo.canPickZero = False
            self.cardSelectInfo.cards = list(discoveryCards)
            self.cardSelectInfo.discovery_CopyCount() = copyCount

        def openSimpleCardSelectScreen(self, task, count):
            self.inputState = InputState.CARD_SELECT
            self.cardSelectInfo.cardSelectTask = task
            self.cardSelectInfo.pickCount = count
            self.cardSelectInfo.canPickAnyNumber = False
            self.cardSelectInfo.canPickZero = False

        # single card select helpers
        def chooseArmamentsCard(self, handIdx):
            # todo cleaner solution

            validCards = fixed_list()
            invalidCards = fixed_list()
            i = 0
            while i < self.cards.cardsInHand:
                c = self.cards.hand[i]
                if i == handIdx:
                    i += 1
                    continue
                if c.canUpgrade():
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: validCards.push_back(c);
                    validCards.push_back(sts.CardInstance(c))
                else:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: invalidCards.push_back(c);
                    invalidCards.push_back(sts.CardInstance(c))
                i += 1

            cardToUpgrade = self.cards.hand[handIdx]
            cardToUpgrade.upgrade()

            i = 0
            for c in validCards:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: cards.hand[i++] = c;
                self.cards.hand[i] = c
                i += 1
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards.hand[i++] = cardToUpgrade;
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
            self.cards.hand[i].copy_from(cardToUpgrade)
            i += 1
            for c in invalidCards:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: cards.hand[i++] = c;
                self.cards.hand[i] = c
                i += 1


        def chooseCodexCard(self, id):
            c = CardInstance(id)
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: c.uniqueId = static_cast<short>(cards.nextUniqueCardId++);
            c.uniqueId = short(int((self.cards.nextUniqueCardId)))
            self.cards.nextUniqueCardId += 1
            self.cards.notifyAddCardToCombat(c)
            self.cards.shuffleIntoDrawPile(self.cardRandomRng, c)

        def chooseDiscardToHandCard(self, discardIdx, forZeroCost):
            c = self.cards.discardPile.get(discardIdx)
            self.cards.removeFromDiscard(discardIdx)
            if self.cardSelectInfo.cardSelectTask == CardSelectTask.LIQUID_MEMORIES_POTION:
                c.setCostForTurn(0)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: moveToHandHelper(c);
            self.moveToHandHelper(sts.CardInstance(c))

        def chooseDiscoveryCard(self, id):
            discoveryAmount = self.cardSelectInfo.data0
            c = CardInstance(id)
            c.setCostForTurn(0)

            for i in range(0, discoveryAmount):
                if self.cards.cardsInHand + 1 <= CardManager.MAX_HAND_SIZE:
                    if self.player.hasStatus() and c.getType() == CardType.SKILL:
                        c.setCostForTurn(-9)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cards.createTempCardInHand(c);
                    self.cards.createTempCardInHand(sts.CardInstance(c))

                else:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cards.createTempCardInDiscard(c);
                    self.cards.createTempCardInDiscard(sts.CardInstance(c))

        def chooseDualWieldCard(self, handIdx):

            # dual wield is so fucking buggy
            # if you dual wield a ritual dagger:
            # when there is no choice on which card to pick, the first one will change the card in the deck
            # when there **is** a choice on which card to pick, neither will change the card in the deck XDD

            copyCount = self.cardSelectInfo.dualWield_CopyCount()
            dualWieldCard = self.cards.hand[handIdx]

            # todo cleaner solution

            validCards = fixed_list()
            invalidCards = fixed_list()
            i = 0
            while i < self.cards.cardsInHand:
                c = self.cards.hand[i]
                if i == handIdx:
                    i += 1
                    continue
                if c.getType() == CardType.ATTACK or c.getType() == CardType.POWER:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: validCards.push_back(c);
                    validCards.push_back(sts.CardInstance(c))
                else:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: invalidCards.push_back(c);
                    invalidCards.push_back(sts.CardInstance(c))
                i += 1


            i = 0
            for c in validCards:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: cards.hand[i++] = c;
                self.cards.hand[i] = c
                i += 1
            for c in invalidCards:
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: cards.hand[i++] = c;
                self.cards.hand[i] = c
                i += 1

# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: dualWieldCard.uniqueId = static_cast<short>(cards.nextUniqueCardId++);
            dualWieldCard.uniqueId = short(int((self.cards.nextUniqueCardId))) # dual wield buggy
            self.cards.nextUniqueCardId += 1
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: cards.hand[i++] = dualWieldCard;
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
            self.cards.hand[i].copy_from(dualWieldCard)
            i += 1

            for x in range(0, copyCount):
                if self.cards.cardsInHand + 1 <= CardManager.MAX_HAND_SIZE:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cards.createTempCardInHand(dualWieldCard);
                    self.cards.createTempCardInHand(sts.CardInstance(dualWieldCard))

                else:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: cards.createTempCardInDiscard(dualWieldCard);
                    self.cards.createTempCardInDiscard(sts.CardInstance(dualWieldCard))



        def chooseExhaustOneCard(self, handIdx):
            c = self.cards.hand[handIdx]
            self.cards.removeFromHandAtIdx(handIdx)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: triggerAndMoveToExhaustPile(c);
            self.triggerAndMoveToExhaustPile(sts.CardInstance(c))

        def chooseExhumeCard(self, exhaustIdx):
            # todo game handles corruption here
            c = self.cards.exhaustPile.get(exhaustIdx)
            self.cards.removeFromExhaustPile(exhaustIdx)
            self.cards.notifyAddCardToCombat(c)

            self.moveToHandHelper(fixed_list(c))

        def chooseForethoughtCard(self, handIdx):
            if self.cards.hand[handIdx].cost > 0:
                self.cards.hand[handIdx].freeToPlayOnce = True

            self.cards.insertToDrawPile(0, self.cards.hand[handIdx])
            self.cards.removeFromHandAtIdx(handIdx)

        def chooseHeadbuttCard(self, discardIdx):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert discardIdx >= 0 and discardIdx < self.cards.discardPile.size()
##endif
            self.cards.moveToDrawPileTop(self.cards.discardPile.get(discardIdx))
            self.cards.removeFromDiscard(discardIdx)

        def chooseRecycleCard(self, handIdx):
            # todo
            pass

        def chooseWarcryCard(self, handIdx):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert handIdx >= 0 and handIdx < self.cards.cardsInHand
##endif
            self.cards.moveToDrawPileTop(self.cards.hand[handIdx])
            self.cards.removeFromHandAtIdx(handIdx)

        # multi card helpers
        def chooseDrawToHandCards(self, idxs, cardCount):
            for i in range(0, cardCount):
                drawIdx = idxs[i]
                c = self.cards.drawPile.get(drawIdx)
                self.cards.removeFromDrawPileAtIdx(drawIdx)
                self.moveToHandHelper(fixed_list(c))

        def chooseExhaustCards(self, idxs):
            if idxs.empty():
                return
            listCopy = idxs
            std::sort(listCopy.begin(), listCopy.end(), lambda a, b : b < a)

            # assume idxs is sorted in descending order
            for handIdx in listCopy:
                c = self.cards.hand[handIdx]
                self.cards.removeFromHandAtIdx(fixed_list(handIdx))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: triggerAndMoveToExhaustPile(c);
                self.triggerAndMoveToExhaustPile(sts.CardInstance(c))

        def chooseGambleCards(self, idxs):
            if idxs.empty():
                return
            listCopy = idxs
            std::sort(listCopy.begin(), listCopy.end(), lambda a, b : b < a)

            # assume idxs is sorted in descending order
            self.addToTop(Actions.DrawCards(listCopy.size()))
            for handIdx in listCopy:
                c = self.cards.hand[handIdx]
                self.cards.removeFromHandAtIdx(fixed_list(handIdx))
                self.cards.moveToDiscardPile(c)
                self.onManualDiscard(c)


    def left_shift(self, os, bc):
        os << "BattleContext: {\n"
        sts.printPotions(os, bc)
        sts.printRngCounters(os, bc)

        os << "\tactionQueueSize: " << bc.actionQueue.size << ", cardQueueSize: " << bc.cardQueue.size << ", turn: " << bc.turn << ", ascension " << bc.ascension << ", loopCount: " << bc.loopCount << ", sum: " << sts.BattleContext.sum << ", seed: " << bc.seed << "\n"

        os << bc.monsters
        os << bc.player
        os << bc.cards
        os << "}\n"
        return os

    # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
    # ORIGINAL LINE: template <PlayerStatus s>
    @staticmethod
    def BuffPlayer(amount):
        return Action([:=] (sts.BattleContext &bc) { if(s == PlayerStatus.CORRUPTION and (not bc.player.hasStatus())) { bc.cards.onBuffCorruption(); } bc.player.buff(amount); })

    # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
    # ORIGINAL LINE: template <PlayerStatus s>
    @staticmethod
    def DebuffPlayer(amount, isSourceMonster):
        return Action([:=] (sts.BattleContext &bc) { bc.player.debuff(amount, isSourceMonster); })

    # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
    # ORIGINAL LINE: template<PlayerStatus s>
    @staticmethod
    def DecrementStatus(amount):
        return Action([:=] (sts.BattleContext &bc) { bc.player.decrementStatus(amount); })

    # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
    # ORIGINAL LINE: template <PlayerStatus s>
    @staticmethod
    def RemoveStatus():
        return Action([:=] (sts.BattleContext &bc) { bc.player.setHasStatus(False); })

    # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
    # ORIGINAL LINE: template<MonsterStatus s>
    @staticmethod
    def BuffEnemy(idx, amount):
        return Action([:=] (sts.BattleContext &bc) { bc.monsters.arr[idx].buff(amount); })

    # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
    # ORIGINAL LINE: template <MonsterStatus s>
    @staticmethod
    def DebuffEnemy(idx, amount, isSourceMonster):
        return Action([:=] (sts.BattleContext &bc) { bc.debuffEnemy(idx, amount, isSourceMonster); })

    # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
    # ORIGINAL LINE: template <MonsterStatus s>
    @staticmethod
    def DebuffAllEnemy(amount, isSourceMonster):
        # todo this should just add all to bot immediately, not be called first
        # ^^ never mind i think adding to top is a workaround here

# C++ TO PYTHON CONVERTER TASK: The following assignment within expression was not converted by C++ to Python Converter:
# ORIGINAL LINE: return {[=] (BattleContext &bc) { for(int i = bc.monsters.monsterCount-1; i >= 0; --i) { if(bc.monsters.arr[i].isTargetable()) { bc.addToTop(Actions::DebuffEnemy<s>(i, amount, isSourceMonster)); } } }};
        return Action([:=] (sts.BattleContext &bc)
        {
            for(int i := bc.monsters.monsterCount-1; i >= 0; --i)
            {
                if(bc.monsters.arr[i].isTargetable()) { bc.addToTop(Actions.DebuffEnemy(i, amount, isSourceMonster)); }
            }
        })



class sts: #this class replaces the original namespace 'sts'
    BattleContext = thread_local()


class sts: #this class replaces the original namespace 'sts'


    @staticmethod
    def printRngCounters(os, bc):
        SEPARATOR = " "
        os << '\t'

        os << "aiRng: " << bc.aiRng.counter << SEPARATOR
        os << "cardRandomRng: " << bc.cardRandomRng.counter << SEPARATOR
        os << "shuffleRng: " << bc.shuffleRng.counter << SEPARATOR
        os << "miscRng: " << bc.miscRng.counter << SEPARATOR
        os << "monsterHpRng: " << bc.monsterHpRng.counter << SEPARATOR
        os << "potionRng: " << bc.potionRng.counter << SEPARATOR

        os << '\n'

    @staticmethod
    def printPotions(os, bc):
        S = "\n\t"
        os << "\t" << "potionCount: " << bc.potionCount
        os << S << "potionCapacity: " << bc.potionCapacity

        os << S << "{ "
        i = 0
        while i < bc.potionCapacity:
            os << sts.getPotionName(list(bc.potions[i])) << ", "
            i += 1
        os << "}\n"


