import math
from ..constants.PlayerStatusEffects import Stance
from bitarray import bitarray
from ..constants.PlayerStatusEffects import PlayerStatus, playerStatusStrings
from ..constants.Relics import RelicId, getRelicName
from ..constants.Cards import CardId
from CardInstance import CardInstance
from ..constants.Potions import Potion
from InputState import InputState


class Player:

    def __init__(self):
        self.cc = None
        self.gold = 0
        self.curHp = 8000
        self.maxHp = 80
        self.energy = 0
        self.energyPerTurn = 3
        self.cardDrawPerTurn = 5
        self.stance = Stance.NEUTRAL
        self.orbSlots = 0
        self.lastTargetedMonster = 1
        self.block = 0
        self.artifact = 0
        self.dexterity = 0
        self.focus = 0
        self.strength = 0
        self.justAppliedBits = 0
        self.statusBits0 = 0
        self.statusBits1 = 0
        self.statusMap = dict.fromkeys([e for e in PlayerStatus], 0)
        self.relicBits0 = 0
        self.relicBits1 = 0
        self.happyFlowerCounter = 0
        self.incenseBurnerCounter = 0
        self.inkBottleCounter = 0
        self.inserterCounter = 0
        self.nunchakuCounter = 0
        self.penNibCounter = 0
        self.sundialCounter = 0
        self.haveUsedNecronomiconThisTurn = False
        self.combustHpLoss = 0
        self.devaFormEnergyPerTurn = 0
        self.echoFormCardsDoubled = 0
        self.panacheCounter = 0
        self.cardsPlayedThisTurn = 0
        self.attacksPlayedThisTurn = 0
        self.skillsPlayedThisTurn = 0
        self.cardsDiscardedThisTurn = 0
        self.lastAttackUnblockedDamage = 0
        self.timesDamagedThisCombat = 0
        self.bomb1 = 0
        self.bomb2 = 0
        self.bomb3 = 0
        self.orangePelletsCardTypesPlayed = bitarray(3)

    # todo rework all of the power data structures...

    def setHasRelic(self, r, value):
        if value:
            if int(r) < 64:
                self.relicBits0 |= 1 << int(r)
            else:
                self.relicBits1 |= 1 << (int(r) - 64)
        else:
            if int(r) < 64:
                self.relicBits0 &= ~(1 << int(r))
            else:
                self.relicBits1 &= ~(1 << (int(r) - 64))

    def setHasStatus(self, s, value):
        #        static_assert(s != PlayerStatus::THE_BOMB)

        if (s == PlayerStatus.ARTIFACT) or (s == PlayerStatus.DEXTERITY) or (s == PlayerStatus.STRENGTH) or (
                s == PlayerStatus.FOCUS):
            return

        # static_assert(((int)s) < 64); // did we add too many status effects
        idx = int(s)
        if value:
            if idx < 64:
                self.statusBits0 |= 1 << idx
            else:
                self.statusBits1 |= 1 << (idx - 64)
        else:
            if idx < 64:
                self.statusBits0 &= ~(1 << idx)
            else:
                self.statusBits1 &= ~(1 << (idx - 64))

    def setStatusValueNoChecks(self, s, value):
        if s == PlayerStatus.ARTIFACT:
            self.artifact = value

        elif s == PlayerStatus.DEXTERITY:
            self.dexterity = value

        elif s == PlayerStatus.FOCUS:
            self.focus = value

        elif s == PlayerStatus.STRENGTH:
            self.strength = value

        else:
            self.statusMap[s] = value

    def removeStatus(self, s):
        self.setHasStatus(s, value=False)

    def decrementStatus(self, s, amount=1):
        if s == PlayerStatus.ARTIFACT:
            self.artifact -= amount

        elif s == PlayerStatus.DEXTERITY:
            self.dexterity -= amount  # dexterity should not be used by "hasStatusInternal"

        elif s == PlayerStatus.FOCUS:
            self.focus -= amount

        elif s == PlayerStatus.STRENGTH:
            self.strength -= amount  # strength should not be used by "hasStatusInternal"

        else:
            self.statusMap[s] -= amount
            if not self.statusMap[s]:
                self.setHasStatus(s, value=False)

    def decrementIfNotJustApplied(self, s):
        if self.wasJustApplied(s, ):
            self.setJustApplied(s, False)
        else:
            self.decrementStatus(s, 1)

    def hasStatusRuntime(self, s):
        if s == PlayerStatus.ARTIFACT:
            return self.artifact != 0

        elif s == PlayerStatus.DEXTERITY:
            return self.dexterity != 0

        elif s == PlayerStatus.FOCUS:
            return self.focus != 0

        elif s == PlayerStatus.STRENGTH:
            return self.strength != 0

        idx = int(s)
        if idx < 64:
            return (self.statusBits0 & (1 << idx)) != 0
        else:
            return (self.statusBits1 & (1 << (idx - 64))) != 0

    def getStatusRuntime(self, s):
        if s == PlayerStatus.ARTIFACT:
            return self.artifact
        elif s == PlayerStatus.DEXTERITY:
            return self.dexterity
        elif s == PlayerStatus.FOCUS:
            return self.focus
        elif s == PlayerStatus.STRENGTH:
            return self.strength
        else:
            if self.hasStatusRuntime(s):
                return self.statusMap[s]
            else:
                return 0

    def wasJustApplied(self, s):
        return (self.justAppliedBits & (1 << int(s))) != 0

    # to be used by:
    # frail
    # vulnerable
    # weak
    # double damage
    # draw reduction
    # intangible
    def setJustApplied(self, s, value):
        if value:
            self.justAppliedBits |= (1 << int(s))
        else:
            self.justAppliedBits &= ~(1 << int(s))

    def hasRelicRuntime(self, r):
        if int(r) < 64:
            return (self.relicBits0 & (1 << int(r))) != 0
        else:
            return (self.relicBits1 & (1 << (int(r) - 64))) != 0

    def hasRelic(self, r):
        if int(r) < 64:
            return (self.relicBits0 & (1 << int(r))) != 0
        else:
            return (self.relicBits1 & (1 << (int(r) - 64))) != 0

    def hasStatus(self, s):
        #        static_assert(s != PlayerStatus::THE_BOMB)

        if s == PlayerStatus.ARTIFACT:
            return self.artifact != 0

        elif s == PlayerStatus.DEXTERITY:
            return self.dexterity != 0

        elif s == PlayerStatus.FOCUS:
            return self.focus != 0

        elif s == PlayerStatus.STRENGTH:
            return self.strength != 0

        idx = int(s)
        if idx < 64:
            return (self.statusBits0 & (1 << idx)) != 0
        else:
            return (self.statusBits1 & (1 << (idx - 64))) != 0

    def getStatus(self, s):
        if s == PlayerStatus.ARTIFACT:
            return self.artifact
        elif s == PlayerStatus.DEXTERITY:
            return self.dexterity
        elif s == PlayerStatus.STRENGTH:
            return self.strength
        else:
            if self.hasStatus(s):
                return self.statusMap[s]
            else:
                return 0

    # to be used by:
    # frail
    # vulnerable
    # weak
    # double damage
    # draw reduction
    # intangible

    def buff(self, s, amount=1):
        # corruption effects handled elsewhere

        if amount == 0:
            return

        if s == PlayerStatus.ARTIFACT:
            self.artifact += amount
            return

        elif s == PlayerStatus.DEXTERITY:
            self.dexterity += amount
            return

        elif s == PlayerStatus.FOCUS:
            self.focus += amount
            return

        elif s == PlayerStatus.STRENGTH:
            self.strength += amount
            return

        if s == PlayerStatus.THE_BOMB:
            self.bomb3 += amount
            return

        if s == PlayerStatus.BARRICADE or s == PlayerStatus.CORRUPTION or s == PlayerStatus.CONFUSED or s == PlayerStatus.PEN_NIB or s == PlayerStatus.SURROUNDED:
            self.setHasStatus(s, True)
            return

        if s == PlayerStatus.DOUBLE_DAMAGE or s == PlayerStatus.INTANGIBLE:
            self.setJustApplied(s, True)

        if s == PlayerStatus.COMBUST:
            self.combustHpLoss += 1

        if s == PlayerStatus.PANACHE and not self.hasStatus(s):
            self.panacheCounter = 5

        if self.hasStatus(s):
            self.statusMap[s] += amount
        else:
            self.setHasStatus(s, True)
            self.statusMap[s] = amount

    def debuff(self, s, amount, isSourceMonster=True):
        if amount == 0:
            return

        if s == PlayerStatus.WEAK and self.hasRelic(RelicId.GINGER):
            return

        if s == PlayerStatus.FRAIL and self.hasRelic(RelicId.TURNIP):
            return

        if self.hasStatus(s):
            self.decrementStatus(s, 1)
            return

        if s == PlayerStatus.WEAK or s == PlayerStatus.FRAIL or s == PlayerStatus.VULNERABLE or s == PlayerStatus.DRAW_REDUCTION:
            if isSourceMonster and not self.hasStatus(s):
                self.setJustApplied(s, True)

        if s == PlayerStatus.DRAW_REDUCTION:
            self.cardDrawPerTurn -= 1
            self.setJustApplied(s, True)
            self.setHasStatus(s, True)
            return

        if s == PlayerStatus.STRENGTH:
            self.strength += amount
            return
        if s == PlayerStatus.DEXTERITY:
            self.dexterity += amount
            return
        if s == PlayerStatus.FOCUS:
            self.focus += amount
            return

        if s == PlayerStatus.CONFUSED or s == PlayerStatus.HEX:
            self.setHasStatus(s, True)
            return

        if self.hasStatus(s):
            self.statusMap[s] += amount
        else:
            self.statusMap[s] = amount

        self.setHasStatus(s, True)

    def changeStance(self, s):
        self.stance = s

    def removeDebuffs(self):
        if self.getStatus(PlayerStatus.STRENGTH) < 0:
            self.setStatusValueNoChecks(PlayerStatus.STRENGTH, 0)
        if self.getStatus(PlayerStatus.DEXTERITY) < 0:
            self.setStatusValueNoChecks(PlayerStatus.DEXTERITY, 0)

        self.removeStatus(PlayerStatus.BIAS)
        self.removeStatus(PlayerStatus.CONFUSED)
        self.removeStatus(PlayerStatus.CONSTRICTED)

        if self.hasStatus(PlayerStatus.DRAW_REDUCTION):
            self.cardDrawPerTurn += 1
            self.removeStatus(PlayerStatus.DRAW_REDUCTION)

        self.removeStatus(PlayerStatus.ENTANGLED)
        self.removeStatus(PlayerStatus.FASTING)
        self.removeStatus(PlayerStatus.FRAIL)
        self.removeStatus(PlayerStatus.HEX)
        self.removeStatus(PlayerStatus.LOSE_DEXTERITY)
        self.removeStatus(PlayerStatus.LOSE_STRENGTH)
        self.removeStatus(PlayerStatus.NO_BLOCK)
        self.removeStatus(PlayerStatus.NO_DRAW)
        self.removeStatus(PlayerStatus.VULNERABLE)
        self.removeStatus(PlayerStatus.WEAK)
        self.removeStatus(PlayerStatus.WRAITH_FORM)

    def increaseMaxHp(self, amount):
        self.maxHp += amount
        self.heal(amount)

    def heal(self, amount):
        if self.hasRelic(RelicId.MARK_OF_THE_BLOOM):
            return

        if self.hasRelic(RelicId.MAGIC_FLOWER):
            amount = math.trunc(amount * 3 / float(2))

        wasBloodied = self.curHp <= math.trunc(self.maxHp / float(2))

        self.curHp = min(int(self.maxHp), self.curHp + amount)

        if wasBloodied and self.curHp > math.trunc(self.maxHp / float(2)) and self.hasRelic(RelicId.RED_SKULL):
            self.debuff(PlayerStatus.STRENGTH, 3)

    def damage(self, bc, calculatedDamage, selfDamage=False):

        assert calculatedDamage >= 0

        damage = calculatedDamage

        if damage > 0 and self.hasStatus(PlayerStatus.INTANGIBLE):
            damage = 1

        savedBlock = self.block
        self.block = max(0, self.block - damage)
        damage -= savedBlock

        damage -= self.block
        if damage > 0:
            self.block = 0

        if damage > 0 and self.hasStatus(PlayerStatus.BUFFER):
            self.decrementStatus(PlayerStatus.BUFFER)
            damage = 0

        if damage > 0 and self.hasRelic(RelicId.TUNGSTEN_ROD):
            damage -= 1

        if damage > 0:
            self.hpWasLost(bc, damage, selfDamage)

    def attacked(self, bc, enemyIdx, calculatedDamage):
        assert calculatedDamage >= 0

        # assume intangible is already handled

        damage = calculatedDamage
        savedBlock = self.block
        self.block = max(0, self.block - damage)
        damage -= savedBlock

        # buffer triggers before tungsten rod in the game's implementation
        # cases where tungsten rod would prevent damage // todo check if this is true
        if damage > 0 and self.hasStatus(PlayerStatus.BUFFER):
            self.decrementStatus(PlayerStatus.BUFFER)
            damage = 0

        if self.hasStatus(PlayerStatus.THORNS):
            bc.addToTop(Actions.DamageEnemy(enemyIdx, self.getStatus(PlayerStatus.THORNS)))

        if self.hasStatus(PlayerStatus.FLAME_BARRIER):
            bc.addToTop(Actions.DamageEnemy(enemyIdx, self.getStatus(PlayerStatus.FLAME_BARRIER)))

        if damage > 0 and damage <= 5 and self.hasRelic(RelicId.TORII):
            damage = 1

        if damage > 0 and self.hasRelic(RelicId.TUNGSTEN_ROD):
            damage -= 1

        if damage > 0:
            self.lastAttackUnblockedDamage = damage

            if self.hasStatus(PlayerStatus.PLATED_ARMOR):
                self.decrementStatus(PlayerStatus.PLATED_ARMOR)

            if bc.monsters.arr[enemyIdx].hasStatus(PlayerStatus.PLATED_ARMOR):
                bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.WOUND)))

            self.hpWasLost(bc, damage, False)

        else:
            self.lastAttackUnblockedDamage = 0

    def loseHp(self, bc, amount, selfDamage):
        if self.hasStatus(PlayerStatus.INTANGIBLE):
            amount = 1

        if amount > 0 and self.hasRelic(RelicId.TUNGSTEN_ROD):
            amount -= 1
            if amount == 0:
                return

        self.hpWasLost(bc, amount, selfDamage)

    def hpWasLost(self, bc, amount, selfDamage=False):
        assert amount > 0

        wasBloodied = bool(self.curHp <= math.trunc(self.maxHp / float(2)))

        self.curHp = max(0, self.curHp - amount)

        if selfDamage and self.hasStatus(PlayerStatus.RUPTURE):
            self.buff(PlayerStatus.STRENGTH, self.getStatus(PlayerStatus.RUPTURE))

        # todo - does order acquired matter with centennial/runic?
        # relics wasHpLost
        # -centennial-puzzle
        # -emotion chip
        # -runic cube
        # -self forming clay

        if self.hasRelic(RelicId.CENTENNIAL_PUZZLE):
            self.setHasRelic(RelicId.CENTENNIAL_PUZZLE, False)
            bc.addToTop(Actions.DrawCards(3))

        if self.hasRelic(RelicId.EMOTION_CHIP):
            # todo
            pass

        if self.hasRelic(RelicId.SELF_FORMING_CLAY):
            self.buff(PlayerStatus.NEXT_TURN_BLOCK, 3)

        if self.hasRelic(RelicId.RUNIC_CUBE):
            bc.addToTop(Actions.DrawCards(1))

        if self.hasRelic(RelicId.RED_SKULL) and (not wasBloodied) and self.curHp <= math.trunc(self.maxHp / float(2)):
            self.buff(PlayerStatus.STRENGTH, 3)

        bc.cards.onTookDamage()
        self.timesDamagedThisCombat += 1

        if self.curHp <= 0:
            self.wouldDie(bc)

    def wouldDie(self, bc):
        # assume fairy and lizard tail heal for greater than zero - max hp is not less than ~8
        self.curHp = 0
        if not self.hasRelic(RelicId.MARK_OF_THE_BLOOM):
            i = 0
            while i < bc.potionCapacity:
                if bc.potions[i] == Potion.FAIRY_POTION:
                    bc.discardPotion(i)
                    healAmount = max(1, int((float(self.maxHp) * (0.6 if self.hasRelic(RelicId.SACRED_BARK) else 0.3))))
                    self.heal(healAmount)
                    return
                i += 1

            if self.hasRelic(RelicId.LIZARD_TAIL):
                self.setHasRelic(RelicId.LIZARD_TAIL, False)
                self.heal(math.trunc(self.maxHp / float(2)))
                return

        bc.outcome = Outcome.PLAYER_LOSS

    def gainBlock(self, bc, amount):
        if amount <= 0:
            return

        self.block += amount

        if self.hasStatus(PlayerStatus.JUGGERNAUT):
            bc.addToBot(Actions.DamageRandomEnemy(self.getStatus(PlayerStatus.JUGGERNAUT)))

        # todo watcher weak power

    def gainGold(self, bc, amount):
        # C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
        ##if sts_asserts
        assert amount > 0
        ##endif

        if self.hasRelic(RelicId.ECTOPLASM):
            return

        self.gold += amount
        if self.hasRelic(RelicId.BLOODY_IDOL):
            self.heal(5)

    def useEnergy(self, amount):
        # C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
        ##if sts_asserts
        assert self.energy >= amount
        ##endif

        self.energy -= amount

    def gainEnergy(self, amount):
        self.energy += amount

    def increaseOrbSlots(self, amount):
        # todo
        pass

    def channelOrb(self, orb):
        # todo
        pass

    # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
    # ORIGINAL LINE: [[nodiscard]] bool hasEmptyOrb() const
    # C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
    # ORIGINAL LINE: bool hasEmptyOrb() const
    def hasEmptyOrb(self):
        return False

    def applyEndOfTurnPowers(self, bc):
        if self.bomb1:
            bc.addToBot(Actions.DamageAllEnemy(int(self.bomb1)))

        self.bomb1 = self.bomb2

        self.bomb2 = self.bomb3
        self.bomb3 = 0

        for pair, value in self.statusMap:
            if not self.hasStatusRuntime(pair):
                continue

            if pair == PlayerStatus.BURST:
                bc.addToBot(Actions.RemoveStatus())

            elif pair == PlayerStatus.COMBUST:
                if not bc.monsters.areMonstersBasicallyDead():
                    bc.addToBot(Actions.PlayerLoseHp(int(self.combustHpLoss),
                                                     True))  # todo combust doesnt stack hp loss correctly
                    bc.addToBot(Actions.DamageAllEnemy(value))

            elif pair == PlayerStatus.CONSTRICTED:
                bc.addToBot(Actions.DamagePlayer(value))

            elif pair == PlayerStatus.DOUBLE_TAP:
                bc.addToBot(Actions.RemoveStatus())

            elif pair == PlayerStatus.ENTANGLED:
                bc.addToBot(Actions.RemoveStatus())

            elif pair == PlayerStatus.EQUILIBRIUM:
                # todo if card is ethereal set to retain
                pass

            elif pair == PlayerStatus.ESTABLISHMENT:
                # todo addToBot establishmentPowerAction
                pass

            elif pair == PlayerStatus.LOSE_DEXTERITY:
                bc.addToBot(Actions.DebuffPlayer(-value))
                bc.addToBot(Actions.RemoveStatus())

            elif pair == PlayerStatus.LOSE_STRENGTH:
                bc.addToBot(Actions.DebuffPlayer(-value))
                bc.addToBot(Actions.RemoveStatus())

            elif pair == PlayerStatus.NO_DRAW:
                bc.addToBot(Actions.RemoveStatus())

            elif pair == PlayerStatus.OMEGA:
                bc.addToBot(Actions.DamageAllEnemy(value))

            elif pair == PlayerStatus.RAGE:
                self.removeStatus(PlayerStatus.RAGE)

            elif pair == PlayerStatus.REBOUND:
                bc.addToBot(Actions.RemoveStatus())

            elif pair == PlayerStatus.REGEN:
                bc.addToTop(Actions.HealPlayer(value))
                bc.addToTop(Actions.DecrementStatus())

                # case RetainCardPower -> if not has relic runic pyramid and not has power equilibrium, addToBot retain cards action

            elif pair == PlayerStatus.RITUAL:
                bc.addToBot(Actions.BuffPlayer(value))
                # case TheBomb

            elif pair == PlayerStatus.WRAITH_FORM:  # todo does this debuff or just decrement?
                bc.addToBot(Actions.DecrementStatus(value))

    def applyAtEndOfRoundPowers(self):
        if self.hasStatus(PlayerStatus.FRAIL):
            self.decrementIfNotJustApplied(PlayerStatus.FRAIL)

        if self.hasStatus(PlayerStatus.VULNERABLE):
            self.decrementIfNotJustApplied(PlayerStatus.VULNERABLE)

        if self.hasStatus(PlayerStatus.WEAK):
            self.decrementIfNotJustApplied(PlayerStatus.WEAK)

        # handling this later so it is not removed before block check
        #    if (hasStatusInternal<PS::BLUR>()) {
        #        decrementStatus<PS::BLUR>()
        #    }

        if self.hasStatus(PlayerStatus.DOUBLE_DAMAGE):
            self.decrementIfNotJustApplied(PlayerStatus.DOUBLE_DAMAGE)

        # handle elsewhere
        #    if (hasStatusInternal<PS::DRAW_REDUCTION>()) {
        #        decrementStatus<PS::DRAW_REDUCTION>()
        #    }

        if self.hasStatus(PlayerStatus.DUPLICATION):
            self.decrementStatus(PlayerStatus.DUPLICATION)

        if self.hasStatus(PlayerStatus.EQUILIBRIUM):
            self.decrementStatus(PlayerStatus.EQUILIBRIUM)

        if self.hasStatus(PlayerStatus.INTANGIBLE):
            self.decrementStatus(PlayerStatus.INTANGIBLE)

        if self.hasStatus(PlayerStatus.NO_BLOCK):
            self.decrementStatus(PlayerStatus.NO_BLOCK)

        if self.hasStatus(PlayerStatus.WAVE_OF_THE_HAND):
            self.decrementStatus(PlayerStatus.WAVE_OF_THE_HAND)

    def applyStartOfTurnRelics(self, bc):
        # ****** Player relics atTurnStart ******
        if self.hasRelic(RelicId.ART_OF_WAR):
            if self.attacksPlayedThisTurn == 0:
                bc.addToBot(Actions.GainEnergy(1))

        if self.hasRelic(RelicId.BRIMSTONE):
            self.buff(PlayerStatus.STRENGTH, 2)
            i = 0
            while i < bc.monsters.monsterCount:
                if bc.monsters.arr[i].isTargetable():
                    bc.monsters.arr[i].buff(1)
                i += 1

        if self.hasRelic(RelicId.CAPTAINS_WHEEL):
            if bc.turn == 2:
                bc.addToBot(Actions.GainBlock(18))

        if self.hasRelic(RelicId.DAMARU):
            bc.addToBot(Actions.BuffPlayer(1))
            # todo handle mantra change stance

        if self.hasRelic(RelicId.EMOTION_CHIP):
            # todo if lost hp last turn addToBot(new ImpulseAction())
            pass

        if self.hasRelic(RelicId.HAPPY_FLOWER):
            self.happyFlowerCounter += 1
            if self.happyFlowerCounter == 3:
                self.happyFlowerCounter = 0
                bc.addToBot(Actions.GainEnergy(1))

        if self.hasRelic(RelicId.HORN_CLEAT):
            if bc.turn == 1:
                bc.addToBot(Actions.GainBlock(14))

        if self.hasRelic(RelicId.INCENSE_BURNER):
            self.incenseBurnerCounter += 1
            if self.incenseBurnerCounter == 6:
                self.incenseBurnerCounter = 0
                bc.addToBot(Actions.BuffPlayer(1))

        if self.hasRelic(RelicId.INSERTER):
            self.inserterCounter += 1
            if self.inserterCounter == 2:
                self.inserterCounter = 0  # todo
                # bc.addToBot(Action([ :=](BattleContext & bc)
                # {bc.player.increaseOrbSlots(1);}))

            if self.hasRelic(RelicId.MERCURY_HOURGLASS):
                bc.addToBot(Actions.DamageAllEnemy(3))

            if self.hasRelic(RelicId.NECRONOMICON):
                self.haveUsedNecronomiconThisTurn = False

            if self.hasRelic(RelicId.ORANGE_PELLETS):
                self.orangePelletsCardTypesPlayed.setall(0)

    def applyStartOfTurnPowers(self, bc):
        # ****** Player powers atStartOfTurn ******
        for pair, value in self.statusMap:
            if not self.hasStatusRuntime(pair):
                continue

            if pair == PlayerStatus.BATTLE_HYMN:
                bc.addToBot(
                    Actions.MakeTempCardInHand(CardId.SMITE, self.hasStatus(PlayerStatus.MASTER_REALITY), value))

            elif pair == PlayerStatus.BIAS:
                bc.addToBot(Actions.DecrementStatus(value))

            elif pair == PlayerStatus.CREATIVE_AI:
                #                bc.addToBot( Actions::SetState(InputState::CREATE_RANDOM_CARD_IN_HAND_POWER, value) ); // todo
                pass

            elif pair == PlayerStatus.ECHO_FORM:
                self.echoFormCardsDoubled = 0

            elif pair == PlayerStatus.BLASPHEMER:
                self.removeStatus(PlayerStatus.BLASPHEMER)
                bc.addToBot(Actions.PlayerLoseHp(9999))

            elif pair == PlayerStatus.FASTING:
                #  add energy dont need? just change energy per turn instead
                pass

            elif pair == PlayerStatus.FORESIGHT:
                if bc.cards.drawPile.empty():
                    bc.addToTop(Actions.SetState(InputState.SHUFFLE_DISCARD_TO_DRAW))
                #                bc.addToBot( Actions::SetState(InputState::SCRY, value) ); // tood

            elif pair == PlayerStatus.FLAME_BARRIER:
                self.removeStatus(PlayerStatus.FLAME_BARRIER)

            elif pair == PlayerStatus.HELLO_WORLD:  # todo
                self.removeStatus(PlayerStatus.HELLO_WORLD)

            elif pair == PlayerStatus.INFINITE_BLADES:
                bc.addToBot(
                    Actions.MakeTempCardInHand(CardId.SHIV, self.hasStatus(PlayerStatus.INFINITE_BLADES), value))

            elif pair == PlayerStatus.LOOP:
                # todo do amount times : call orb[0].onStartOfTurn, orb[0].onEndOfTurn
                pass

            elif pair == PlayerStatus.MAGNETISM:
                #                bc.addToBot( Actions::SetState(InputState::CREATE_RANDOM_CARD_IN_HAND_COLORLESS, value) )
                pass

            elif pair == PlayerStatus.MAYHEM:
                i = 0
                while i < value:
                    #                    bc.addToBot( Actions::PlayTopCard(false, ) ); // todo fix target
                    i += 1

            elif pair == PlayerStatus.NEXT_TURN_BLOCK:
                bc.addToBot(Actions.GainBlock(value))
                self.removeStatus(PlayerStatus.NEXT_TURN_BLOCK)

                # todo  case NightMarePower: this.bc.addToBot(new MakeTempCardInHandAction(this.card, this.amount)); bc.addToBot remove power

            elif pair == PlayerStatus.PANACHE:
                self.panacheCounter = 5

            elif pair == PlayerStatus.PHANTASMAL:
                self.decrementStatus(PlayerStatus.PHANTASMAL)
                bc.addToBot(Actions.BuffPlayer())

                # time maze not used in standard modes

            elif pair == PlayerStatus.WRATH_NEXT_TURN:
                self.removeStatus(PlayerStatus.WRATH_NEXT_TURN)
                bc.addToBot(Actions.ChangeStance.WRATH)

    def applyStartOfTurnPostDrawRelics(self, bc):
        # ****** Player Relics AtTurnStartPostDraw ******
        if self.hasRelic(RelicId.POCKETWATCH):
            if self.cardsPlayedThisTurn <= 3:
                bc.addToBot(Actions.DrawCards(3))

        if self.hasRelic(RelicId.WARPED_TONGS):
            bc.addToBot(Actions.UpgradeRandomCardAction())

    def applyStartOfTurnPostDrawPowers(self, bc):
        # ****** Player Powers AtStartOfTurnPostDraw ******
        for pair, value in self.statusMap:
            if not self.hasStatusRuntime(pair):
                continue

            if pair == PlayerStatus.BRUTALITY:
                bc.addToBot(Actions.PlayerLoseHp(value))
                bc.addToBot(Actions.DrawCards(value))

            elif pair == PlayerStatus.DEMON_FORM:
                bc.addToBot(Actions.BuffPlayer(value))

            elif pair == PlayerStatus.DEVOTION:  # the implementation of this is really weird in the game code
                bc.addToBot(Actions.BuffPlayer(value))  # todo make buffing mantra switch stance

            elif pair == PlayerStatus.DRAW_CARD_NEXT_TURN:
                bc.addToBot(Actions.DrawCards(value))
                self.removeStatus(PlayerStatus.DRAW_CARD_NEXT_TURN)

            elif pair == PlayerStatus.NOXIOUS_FUMES:
                bc.addToBot(Actions.DebuffAllEnemy(value))

            elif pair == PlayerStatus.TOOLS_OF_THE_TRADE:
                bc.addToBot(Actions.DrawCards(value))
                #                bc.addToBot( Actions::SetState(InputState::CHOOSE_DISCARD_CARDS, value) )

    def rechargeEnergy(self, bc):
        if self.hasRelic(RelicId.ICE_CREAM):
            self.gainEnergy(int(self.energyPerTurn))
        else:
            self.energy = self.energyPerTurn

        # ****** Player powers onEnergyRecharge ******
        if self.hasStatus(PlayerStatus.COLLECT):
            self.decrementStatus(PlayerStatus.COLLECT)
            bc.addToBot(Actions.MakeTempCardInHand(CardId.MIRACLE))

        if self.hasStatus(PlayerStatus.DEVA):
            self.gainEnergy(int(self.devaFormEnergyPerTurn))
            self.devaFormEnergyPerTurn += self.getStatus(PlayerStatus.DEVA)

        if self.hasStatus(PlayerStatus.ENERGIZED):
            self.gainEnergy(self.getStatus(PlayerStatus.ENERGIZED))
            self.removeStatus(PlayerStatus.ENERGIZED)

        # def left_shift(self, os, p):
        #     os << "Player: {\n"
        #
        #     os << "\t" << "hp:(" << p.curHp << "/" << p.maxHp << ")" << " energy:(" << p.energy << "/" << int(p.energyPerTurn) << ") block:(" << p.block << ")\n"
        #
        #     printStatusEffects(os, p)
        #     printRelics(os, p)
        #     printAllInfos(os, p)
        #
        #     os << "}\n"
        #     return os

    def printRelics(self):
        os = []
        os.append("\tRelics: ")

        i = int(RelicId.AKABEKO)
        while i <= int(RelicId.WRIST_BLADE):
            r = i
            if self.hasRelicRuntime(r):
                os.append(getRelicName(r) + ", ")
            i += 1
        os.append("\n")
        return os

    def printAllInfos(self):
        os = []
        s = ", "
        os.append("\t" + "Relic Counters: ")
        os.append("" + "happyFlowerCounter: " + str(int(self.happyFlowerCounter)))
        os.append(s + "incenseBurnerCounter: " + str(int(self.incenseBurnerCounter)))
        os.append(s + "inkBottleCounter: " + str(int(self.inkBottleCounter)))
        os.append(s + "inserterCounter: " + str(int(self.inserterCounter)))
        os.append(s + "nunchakuCounter: " + str(int(self.nunchakuCounter)))
        os.append(s + "penNibCounter: " + str(int(self.penNibCounter)))
        os.append(s + "sundialCounter: " + str(int(self.sundialCounter)))
        os.append("\n\t" + "Status Counters: ")
        os.append("" + "combustHpLoss: " + str(int(self.combustHpLoss)))
        os.append(s + "devaFormEnergyPerTurn: " + str(int(self.devaFormEnergyPerTurn)))
        os.append(s + "echoFormCardsDoubled: " + str(int(self.echoFormCardsDoubled)))
        os.append(s + "panacheCounter: " + str(int(self.panacheCounter)))
        os.append(s + "TheBomb: { 1=" + str(int(self.bomb1)) + ", 2=" + str(int(self.bomb2)) + ", 3=" + str(
            int(self.bomb3)) + " }")
        os.append("\n\t" + "Misc: ")
        os.append("" + "cardsPlayedThisTurn: " + str(int(self.cardsPlayedThisTurn)))
        os.append(s + "attacksPlayedThisTurn: " + str(int(self.attacksPlayedThisTurn)))
        os.append(s + "skillsPlayedThisTurn: " + str(int(self.skillsPlayedThisTurn)))
        os.append(s + "orangePelletsCardTypesPlayed: {" + (
            "Attack," if self.orangePelletsCardTypesPlayed[0] else "") + (
                      "Skill," if self.orangePelletsCardTypesPlayed[1] else "") + (
                      "Power," if self.orangePelletsCardTypesPlayed[2] else "") + "}")
        os.append(s + "cardsDiscardedThisTurn: " + str(int(self.cardsDiscardedThisTurn)))
        os.append(s + "gold: " + str(int(self.gold)) + '\n')
        return os

    def printIfHaveStatus(self, s: PlayerStatus):
        os = []
        if not self.hasStatusRuntime(s):
            return os
        desc = playerStatusStrings[s.value]
        return os.append(f"({desc},{self.getStatusRuntime(s)}), ")

    def printStatusEffects(self):
        os = []
        os.append("\tStatusEffects: {")
        if self.hasStatus(PlayerStatus.CONFUSED):
            os.append("(Confused), ")
        if self.hasStatus(PlayerStatus.CORRUPTION):
            os.append("(Corruption), ")
        if self.hasStatus(PlayerStatus.BARRICADE):
            os.append("(Barricade), ")
        self.printIfHaveStatus(PlayerStatus.ARTIFACT)
        self.printIfHaveStatus(PlayerStatus.DEXTERITY)
        self.printIfHaveStatus(PlayerStatus.FOCUS)
        self.printIfHaveStatus(PlayerStatus.STRENGTH)
        for pair in self.statusMap:
            self.printIfHaveStatus(pair)
        os.append("}\n")
        return os

    def __str__(self):
        os = []
        os.append("Player: {")
        os.append(
            f"\thp:({self.curHp}/{self.maxHp}) energy:({self.energy}/{int(self.energyPerTurn)}) block:({self.block})")
        os.append(self.printStatusEffects())
        os.append(self.printRelics())
        os.append(self.printAllInfos())
        os.append("}")
        return "\n".join(os)
