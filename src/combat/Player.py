

import math
from ..constants.PlayerStatusEffects import Stance
from bitarray import bitarray
from ..constants.PlayerStatusEffects import PlayerStatus
from ..constants.Relics import RelicId
from ..constants.Cards import CardId
from CardInstance import CardInstance
from ..constants.Potions import Potion
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
            self.statusMap = {}
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
                    self.relicBits1 |= 1 << (int(r)-64)
            else:
                if int(r) < 64:
                    self.relicBits0 &= ~(1 << int(r))
                else:
                    self.relicBits1 &= ~(1 << (int(r)-64))

        def setHasStatus(self, s, value):
            #        static_assert(s != PlayerStatus::THE_BOMB)

            if (s == PlayerStatus.ARTIFACT) or (s == PlayerStatus.DEXTERITY) or (s == PlayerStatus.STRENGTH) or (s == PlayerStatus.FOCUS):
                return

            #static_assert(((int)s) < 64); // did we add too many status effects
            idx = int(s)
            if value:
                if idx < 64:
                    self.statusBits0 |= 1 << idx
                else:
                    self.statusBits1 |= 1 << (idx-64)
            else:
                if idx < 64:
                    self.statusBits0 &= ~(1 << idx)
                else:
                    self.statusBits1 &= ~(1 << (idx-64))


        def setStatusValueNoChecks(self, s,value):
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


        def removeStatus(self,s):
            self.setHasStatus(s,value=False)


        def decrementStatus(self, s,amount = 1):
            if s == PlayerStatus.ARTIFACT:
                self.artifact -= amount

            elif s == PlayerStatus.DEXTERITY:
                self.dexterity -= amount # dexterity should not be used by "hasStatusInternal"

            elif s == PlayerStatus.FOCUS:
                self.focus -= amount

            elif s == PlayerStatus.STRENGTH:
                self.strength -= amount # strength should not be used by "hasStatusInternal"

            else:
                self.statusMap[s] -= amount
                if not self.statusMap[s]:
                    self.setHasStatus(s,value=False)


        def decrementIfNotJustApplied(self,s):
            if self.wasJustApplied(s,):
                self.setJustApplied(s,False)
            else:
                self.decrementStatus(s,1)


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
                return (self.statusBits1 & (1 << (idx-64))) != 0


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


        def wasJustApplied(self,s):
            return (self.justAppliedBits & (1 << int(s))) != 0


    # to be used by:
    # frail
    # vulnerable
    # weak
    # double damage
    # draw reduction
    # intangible
        def setJustApplied(self, s,value):
            if value:
                self.justAppliedBits |= (1 << int(s))
            else:
                self.justAppliedBits &= ~(1 << int(s))


        def hasRelicRuntime(self, r):
            if int(r) < 64:
                return (self.relicBits0 & (1 << int(r))) != 0
            else:
                return (self.relicBits1 & (1 << (int(r)-64))) != 0

        def hasRelic(self,r):
            if int(r) < 64:
                return (self.relicBits0 & (1 << int(r))) != 0
            else:
                return (self.relicBits1 & (1 << (int(r)-64))) != 0

        def hasStatus(self,s):
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
                return (self.statusBits1 & (1 << (idx-64))) != 0

        def getStatus(self,s):
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

        def buff(self, s,amount = 1):
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
                self.setHasStatus(s,True)
                return

            if s == PlayerStatus.DOUBLE_DAMAGE or s == PlayerStatus.INTANGIBLE:
                self.setJustApplied(s,True)

            if s == PlayerStatus.COMBUST:
                self.combustHpLoss += 1

            if s == PlayerStatus.PANACHE and not self.hasStatus(s):
                self.panacheCounter = 5

            if self.hasStatus(s):
                self.statusMap[s] += amount
            else:
                self.setHasStatus(s,True)
                self.statusMap[s] = amount


        def debuff(self, s, amount, isSourceMonster = True):
            if amount == 0:
                return

            if s == PlayerStatus.WEAK and self.hasRelic():
                return

            if s == PlayerStatus.FRAIL and self.hasRelic():
                return

            if self.hasStatus(s):
                self.decrementStatus(s,1)
                return

            if s == PlayerStatus.WEAK or s == PlayerStatus.FRAIL or s == PlayerStatus.VULNERABLE or s == PlayerStatus.DRAW_REDUCTION:
                if isSourceMonster and not self.hasStatus(s):
                    self.setJustApplied(s,True)

            if s == PlayerStatus.DRAW_REDUCTION:
                self.cardDrawPerTurn -= 1
                self.setJustApplied(s,True)
                self.setHasStatus(s,True)
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
                self.setHasStatus(s,True)
                return

            if self.hasStatus(s):
                self.statusMap[s] += amount
            else:
                self.statusMap[s] = amount

            self.setHasStatus(s,True)


        def changeStance(self,s):
            self.stance = s

        def removeDebuffs(self):
            if self.getStatus(PlayerStatus.STRENGTH) < 0:
                self.setStatusValueNoChecks(PlayerStatus.STRENGTH,0)
            if self.getStatus(PlayerStatus.DEXTERITY) < 0:
                self.setStatusValueNoChecks(PlayerStatus.DEXTERITY,0)

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
                self.debuff(PlayerStatus.STRENGTH,3)

        def damage(self, bc, calculatedDamage, selfDamage = False):

            assert calculatedDamage >= 0


            damage = calculatedDamage

            if damage > 0 and self.hasStatus(PlayerStatus.INTANGIBLE):
                damage = 1

            savedBlock = self.block
            self.block = max(0, self.block-damage)
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
            self.block = max(0, self.block-damage)
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

            if damage > 0 and damage <=5 and self.hasRelic(RelicId.TORII):
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

        def hpWasLost(self, bc, amount, selfDamage = False):
            assert amount > 0

            wasBloodied = bool(self.curHp <= math.trunc(self.maxHp / float(2)))

            self.curHp = max(0, self.curHp-amount)

            if selfDamage and self.hasStatus(PlayerStatus.RUPTURE):
                self.buff(PlayerStatus.STRENGTH,self.getStatus(PlayerStatus.RUPTURE))

            # todo - does order acquired matter with centennial/runic?
            # relics wasHpLost
            # -centennial-puzzle
            # -emotion chip
            # -runic cube
            # -self forming clay

            if self.hasRelic(RelicId.CENTENNIAL_PUZZLE):
                self.setHasRelic(RelicId.CENTENNIAL_PUZZLE,False)
                bc.addToTop(Actions.DrawCards(3))

            if self.hasRelic(RelicId.EMOTION_CHIP):
                # todo
                pass

            if self.hasRelic(RelicId.SELF_FORMING_CLAY):
                self.buff(PlayerStatus.NEXT_TURN_BLOCK,3)

            if self.hasRelic(RelicId.RUNIC_CUBE):
                bc.addToTop(Actions.DrawCards(1))

            if self.hasRelic(RelicId.RED_SKULL) and (not wasBloodied) and self.curHp <= math.trunc(self.maxHp / float(2)):
                self.buff(PlayerStatus.STRENGTH,3)

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
                    self.setHasRelic(RelicId.LIZARD_TAIL,False)
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

            if hasRelic():
                return

            self.gold += amount
            if hasRelic<R.BLOODY_IDOL>():
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
                bc.addToBot(Actions.DamageAllEnemy(int8_t(self.bomb1)))
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: bomb1 = bomb2;
            self.bomb1.copy_from(self.bomb2)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: bomb2 = bomb3;
            self.bomb2.copy_from(self.bomb3)
            self.bomb3 = 0

            for pair in self.statusMap:
                if not self.hasStatusRuntime(pair.first):
                    continue

                if pair.first == PlayerStatus.BURST:
                    bc.addToBot(Actions.RemoveStatus())

                elif pair.first == PlayerStatus.COMBUST:
                    if not bc.monsters.areMonstersBasicallyDead():
                        bc.addToBot(Actions.PlayerLoseHp(int8_t(self.combustHpLoss), True)) # todo combust doesnt stack hp loss correctly
                        bc.addToBot(Actions.DamageAllEnemy(pair.second))

                elif pair.first == PlayerStatus.CONSTRICTED:
                    bc.addToBot(Actions.DamagePlayer(pair.second))

                elif pair.first == PlayerStatus.DOUBLE_TAP:
                    bc.addToBot(Actions.RemoveStatus())

                elif pair.first == PlayerStatus.ENTANGLED:
                    bc.addToBot(Actions.RemoveStatus())

                elif pair.first == PlayerStatus.EQUILIBRIUM:
                    # todo if card is ethereal set to retain
                    pass

                elif pair.first == PlayerStatus.ESTABLISHMENT:
                    # todo addToBot establishmentPowerAction
                    pass

                elif pair.first == PlayerStatus.LOSE_DEXTERITY:
                    bc.addToBot(Actions.DebuffPlayer(-pair.second))
                    bc.addToBot(Actions.RemoveStatus())

                elif pair.first == PlayerStatus.LOSE_STRENGTH:
                    bc.addToBot(Actions.DebuffPlayer(-pair.second))
                    bc.addToBot(Actions.RemoveStatus())

                elif pair.first == PlayerStatus.NO_DRAW:
                    bc.addToBot(Actions.RemoveStatus())

                elif pair.first == PlayerStatus.OMEGA:
                    bc.addToBot(Actions.DamageAllEnemy(pair.second))

                elif pair.first == PlayerStatus.RAGE:
                    removeStatus()

                elif pair.first == PlayerStatus.REBOUND:
                    bc.addToBot(Actions.RemoveStatus())

                elif pair.first == PlayerStatus.REGEN:
                    bc.addToTop(Actions.HealPlayer(pair.second))
                    bc.addToTop(Actions.DecrementStatus())

                    #case RetainCardPower -> if not has relic runic pyramid and not has power equilibrium, addToBot retain cards action

                elif pair.first == PlayerStatus.RITUAL:
                    bc.addToBot(Actions.BuffPlayer(pair.second))
                    # case TheBomb

                elif pair.first == PlayerStatus.WRAITH_FORM: # todo does this debuff or just decrement?
                    bc.addToBot(Actions.DecrementStatus(pair.second))


        def applyAtEndOfRoundPowers(self):
            if hasStatus<PlayerStatus.FRAIL>():
                decrementIfNotJustApplied<PlayerStatus.FRAIL>()

            if hasStatus():
                decrementIfNotJustApplied()

            if hasStatus():
                decrementIfNotJustApplied()

            # handling this later so it is not removed before block check
            #    if (hasStatusInternal<PS::BLUR>()) {
            #        decrementStatus<PS::BLUR>()
            #    }

            if hasStatus():
                decrementIfNotJustApplied()

            # handle elsewhere
            #    if (hasStatusInternal<PS::DRAW_REDUCTION>()) {
            #        decrementStatus<PS::DRAW_REDUCTION>()
            #    }

            if hasStatus():
                decrementStatus()

            if hasStatus():
                decrementStatus()

            if hasStatus():
                decrementStatus()

            if hasStatus():
                decrementStatus()

            if hasStatus():
                decrementStatus()

        def applyStartOfTurnRelics(self, bc):
            #****** Player relics atTurnStart ******
            if hasRelic():
                if self.attacksPlayedThisTurn == 0:
                    bc.addToBot(Actions.GainEnergy(1))

            if hasRelic():
                buff(2)
                i = 0
                while i < bc.monsters.monsterCount:
                    if bc.monsters.arr[i].isTargetable():
                        bc.monsters.arr[i].buff(1)
                    i += 1

            if hasRelic<R.CAPTAINS_WHEEL>():
                if bc.turn == 2:
                    bc.addToBot(Actions.GainBlock(18))

            if hasRelic():
                bc.addToBot(Actions.BuffPlayer(1))
                # todo handle mantra change stance

            if hasRelic():
                # todo if lost hp last turn addToBot(new ImpulseAction())
                pass

            if hasRelic():
                self.happyFlowerCounter += 1
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (++happyFlowerCounter == 3)
                if self.happyFlowerCounter == 3:
                    self.happyFlowerCounter = 0
                    bc.addToBot(Actions.GainEnergy(1))

            if hasRelic():
                if bc.turn == 1:
                    bc.addToBot(Actions.GainBlock(14))

            if hasRelic():
                self.incenseBurnerCounter += 1
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (++incenseBurnerCounter == 6)
                if self.incenseBurnerCounter == 6:
                    self.incenseBurnerCounter = 0
                    bc.addToBot(Actions.BuffPlayer(1))

            if hasRelic():
                self.inserterCounter += 1
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: if (++inserterCounter == 2)
                if self.inserterCounter == 2:
                    self.inserterCounter = 0 # todo
                    bc.addToBot(Action([:=](BattleContext &bc) { bc.player.increaseOrbSlots(1); }))

            if hasRelic():
                bc.addToBot(Actions.DamageAllEnemy(3))

            if hasRelic():
                self.haveUsedNecronomiconThisTurn = False

            if hasRelic():
                orangePelletsCardTypesPlayed.reset()


        def applyStartOfTurnPowers(self, bc):
            # ****** Player powers atStartOfTurn ******
            for pair in self.statusMap:
                if not self.hasStatusRuntime(pair.first):
                    continue

                if pair.first == PlayerStatus.BATTLE_HYMN:
                    bc.addToBot(Actions.MakeTempCardInHand(CardId.SMITE, hasStatus(), pair.second))

                elif pair.first == PlayerStatus.BIAS:
                    bc.addToBot(Actions.DecrementStatus(pair.second))

                elif pair.first == PlayerStatus.CREATIVE_AI:
                    #                bc.addToBot( Actions::SetState(InputState::CREATE_RANDOM_CARD_IN_HAND_POWER, pair.second) ); // todo
                    pass

                elif pair.first == PlayerStatus.ECHO_FORM:
                    self.echoFormCardsDoubled = 0

                elif pair.first == PlayerStatus.BLASPHEMER:
                    removeStatus()
                    bc.addToBot(Actions.PlayerLoseHp(9999))

                elif pair.first == PlayerStatus.FASTING:
                    #  add energy dont need? just change energy per turn instead
                    pass

                elif pair.first == PlayerStatus.FORESIGHT:
                    if bc.cards.drawPile.empty():
                        bc.addToTop(Actions.SetState(InputState.SHUFFLE_DISCARD_TO_DRAW))
                    #                bc.addToBot( Actions::SetState(InputState::SCRY, pair.second) ); // tood

                elif pair.first == PlayerStatus.FLAME_BARRIER:
                    removeStatus()

                elif pair.first == PlayerStatus.HELLO_WORLD: # todo
                    removeStatus()

                elif pair.first == PlayerStatus.INFINITE_BLADES:
                    bc.addToBot(Actions.MakeTempCardInHand(CardId.SHIV, hasStatus(), pair.second))

                elif pair.first == PlayerStatus.LOOP:
                    # todo do amount times : call orb[0].onStartOfTurn, orb[0].onEndOfTurn
                    pass

                elif pair.first == PlayerStatus.MAGNETISM:
                    #                bc.addToBot( Actions::SetState(InputState::CREATE_RANDOM_CARD_IN_HAND_COLORLESS, pair.second) )
                    pass

                elif pair.first == PlayerStatus.MAYHEM:
                    i = 0
                    while i < pair.second:
                        #                    bc.addToBot( Actions::PlayTopCard(false, ) ); // todo fix target
                        i += 1

                elif pair.first == PlayerStatus.NEXT_TURN_BLOCK:
                    bc.addToBot(Actions.GainBlock(pair.second))
                    removeStatus()

                    # todo  case NightMarePower: this.bc.addToBot(new MakeTempCardInHandAction(this.card, this.amount)); bc.addToBot remove power

                elif pair.first == PlayerStatus.PANACHE:
                    self.panacheCounter = 5

                elif pair.first == PlayerStatus.PHANTASMAL:
                    decrementStatus<PlayerStatus.PHANTASMAL>()
                    bc.addToBot(Actions.BuffPlayer())

                    # time maze not used in standard modes

                elif pair.first == PlayerStatus.WRATH_NEXT_TURN:
                    removeStatus()
                    bc.addToBot(Actions.ChangeStance.WRATH)



        def applyStartOfTurnPostDrawRelics(self, bc):
            # ****** Player Relics AtTurnStartPostDraw ******
            if hasRelic():
                if self.cardsPlayedThisTurn <= 3:
                    bc.addToBot(Actions.DrawCards(3))

            if hasRelic():
                bc.addToBot(Actions.UpgradeRandomCardAction())

        def applyStartOfTurnPostDrawPowers(self, bc):
            # ****** Player Powers AtStartOfTurnPostDraw ******
            for pair in self.statusMap:
                if not self.hasStatusRuntime(pair.first):
                    continue

                if pair.first == PlayerStatus.BRUTALITY:
                    bc.addToBot(Actions.PlayerLoseHp(pair.second))
                    bc.addToBot(Actions.DrawCards(pair.second))

                elif pair.first == PlayerStatus.DEMON_FORM:
                    bc.addToBot(Actions.BuffPlayer(pair.second))

                elif pair.first == PlayerStatus.DEVOTION: # the implementation of this is really weird in the game code
                    bc.addToBot(Actions.BuffPlayer(pair.second)) # todo make buffing mantra switch stance

                elif pair.first == PlayerStatus.DRAW_CARD_NEXT_TURN:
                    bc.addToBot(Actions.DrawCards(pair.second))
                    removeStatus()

                elif pair.first == PlayerStatus.NOXIOUS_FUMES:
                    bc.addToBot(Actions.DebuffAllEnemy(pair.second))

                elif pair.first == PlayerStatus.TOOLS_OF_THE_TRADE:
                    bc.addToBot(Actions.DrawCards(pair.second))
                    #                bc.addToBot( Actions::SetState(InputState::CHOOSE_DISCARD_CARDS, pair.second) )


        def rechargeEnergy(self, bc):
            if hasRelic():
                self.gainEnergy(int8_t(self.energyPerTurn))
            else:
                self.energy = self.energyPerTurn

            # ****** Player powers onEnergyRecharge ******
            if hasStatus():
                decrementStatus()
                bc.addToBot(Actions.MakeTempCardInHand(CardId.MIRACLE))

            if hasStatus():
                self.gainEnergy(int16_t(self.devaFormEnergyPerTurn))
                self.devaFormEnergyPerTurn += getStatus()

            if hasStatus():
                self.gainEnergy(getStatus())
                removeStatus()

# C++ TO PYTHON CONVERTER TASK: Python has no concept of a 'friend' function:
# ORIGINAL LINE: friend std::ostream& operator <<(std::ostream &os, const Player &p);
        def left_shift(self, os, p):
            os << "Player: {\n"

            os << "\t" << "hp:(" << p.curHp << "/" << p.maxHp << ")" << " energy:(" << p.energy << "/" << int(p.energyPerTurn) << ") block:(" << p.block << ")\n"

            printStatusEffects(os, p)
            printRelics(os, p)
            printAllInfos(os, p)

            os << "}\n"
            return os

// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//    operator <<(os, p)



class sts: #this class replaces the original namespace 'sts'

    #    void printRelicCounters(std::ostream &os, const Player &p) {
    #        const std::string s = " ";
    #
    #        if (p.hasRelic<R::INK_BOTTLE>()) {
    #            os << s << "inkBottleCounter: " << p.inkBottleCounter;
    #        }
    #
    #        if (p.hasRelic<R::INSERTER>()) {
    #            os << "inserterCounter: " << p.inserterCounter << " ";
    #        }
    #
    #        if (p.hasRelic<R::NUNCHAKU>()) {
    #            os << "nunchakuCounter: " << p.nunchakuCounter << " ";
    #        }
    #
    #        if (p.hasRelic<R::LETTER_OPENER>()) {
    #            os << "skillsPlayedThisTurn: " << p.skillsPlayedThisTurn << " ";
    #        }
    #
    #    }
    #
    #    void printStatusCounters(std::ostream &os, const Player &p) {
    #
    #        if (p.hasStatusInternal<PS::COMBUST>()) {
    #            os << "combustHpLoss: " << p.combustHpLoss << " ";
    #        }
    #
    #        if (p.hasStatusInternal<PS::DEVA>()) {
    #            os << "devaFormEnergyPerTurn: " << p.devaFormEnergyPerTurn << " ";
    #        }
    #
    #        if (p.hasStatusInternal<PS::ECHO_FORM>()) {
    #            os << "panacheCounter: " << p.panacheCounter << " ";
    #        }
    #
    #
    #        if (p.hasStatusInternal<PS::PANACHE>()) {
    #            os << "panacheCounter: " << p.panacheCounter << " ";
    #        }
    #    }

    @staticmethod
    def printRelics(os, p):
        os << "\t" << "Relics: "

        # this is slow and stupid
        i = int(sts.RelicId.AKABEKO)
        while i <= int(sts.RelicId.WRIST_BLADE):
            r = i

            if p.hasRelicRuntime(auto(r)):
                os << sts.getRelicName(auto(r)) << ", "

            i += 1
        os << "\n"

    @staticmethod
    def printAllInfos(os, p):
        S = ", "

        os << "\t" << "Relic Counters: " << "" << "happyFlowerCounter: " << int(p.happyFlowerCounter) << S << "incenseBurnerCounter: " << int(p.incenseBurnerCounter) << S << "inkBottleCounter: " << int(p.inkBottleCounter) << S << "inserterCounter: " << int(p.inserterCounter) << S << "nunchakuCounter: " << int(p.nunchakuCounter) << S << "penNibCounter: " << int(p.penNibCounter) << S << "sundialCounter: " << int(p.sundialCounter) << "\n\t" << "Status Counters: " << "" << "combustHpLoss: " << int(p.combustHpLoss) << S << "devaFormEnergyPerTurn: " << int(p.devaFormEnergyPerTurn) << S << "echoFormCardsDoubled: " << int(p.echoFormCardsDoubled) << S << "panacheCounter: " << int(p.panacheCounter) << S << "TheBomb: { 1=" << int(p.bomb1) << ", 2=" << int(p.bomb2) << ", 3=" << int(p.bomb3) << " }" << "\n\t" << "Misc: " << "" << "cardsPlayedThisTurn: " << int(p.cardsPlayedThisTurn) << S << "attacksPlayedThisTurn: " << int(p.attacksPlayedThisTurn) << S << "skillsPlayedThisTurn: " << int(p.skillsPlayedThisTurn)


        os << S << "orangePelletsCardTypesPlayed: {" << ("Attack," if p.orangePelletsCardTypesPlayed.test(0) else "") << ("Skill," if p.orangePelletsCardTypesPlayed.test(1) else "") << ("Power," if p.orangePelletsCardTypesPlayed.test(2) else "") << "}"

        os << S << "cardsDiscardedThisTurn: " << int(p.cardsDiscardedThisTurn)
        os << S << "gold: " << int(p.gold) << '\n'


    @staticmethod
    def printStatusEffects(os, p):
        os << "\tStatusEffects: {"
        if p.hasStatus():
            os << "(Confused), "
        if p.hasStatus():
            os << "(Corruption), "
        if p.hasStatus():
            os << "(Barricade), "

        Globals.printIfHaveStatus(p, os, PlayerStatus.ARTIFACT)
        Globals.printIfHaveStatus(p, os, PlayerStatus.DEXTERITY)
        Globals.printIfHaveStatus(p, os, PlayerStatus.FOCUS)
        Globals.printIfHaveStatus(p, os, PlayerStatus.STRENGTH)
        for pair in p.statusMap:
            Globals.printIfHaveStatus(p, os, pair.first)
        os << "}\n"















