

import math

#
# Created by gamerpuppy on 7/5/2021.
#

#
# Created by gamerpuppy on 7/4/2021.
#








class DamageInfo:

    def __init__(self,damage = 0, attackCount = 1):
        # instance fields found by C++ to Python Converter:
        self.damage = damage
        self.attackCount = attackCount



    class Monster:

        def _initialize_instance_fields(self):
            # instance fields found by C++ to Python Converter:
            self.idx = -1
            self.id = MonsterId.INVALID
            self.curHp = 0
            self.maxHp = 0
            self.block = 0
            self.isEscapingB = False
            self.halfDead = False
            self.escapeNext = False
            self.moveHistory = [MMID.INVALID, MMID.INVALID]
            self.statusBits = 0
            self.artifact = 0
            self.blockReturn = 0
            self.choked = 0
            self.corpseExplosion = 0
            self.lockOn = 0
            self.mark = 0
            self.metallicize = 0
            self.platedArmor = 0
            self.poison = 0
            self.regen = 0
            self.shackled = 0
            self.strength = 0
            self.vulnerable = 0
            self.weak = 0
            self.uniquePower0 = 0
            self.uniquePower1 = 0
            self.miscInfo = 0


        #        
        #         * Things to possibly cache about a monster
        #         * - damage actions
        #         * - death actions
        #         * - whether they are a minion leader
        #         


        #        bool isDyingB = false



        # Shield Gremlin target
        # GreenLouse / RedLouse D
        # Red Slaver entangled turn
        # hexaghost divider damage
        # Gremlin wizard charge
        # book of stabbing n
        # champ phase2
        # bronze orb have used stasis
        # bronze automaton lastBoostWasFlail
        # spiker thorn buff count
        # writhing mass used implant
        # darkling d
        # time eater has used haste
        # awakened one isPhase2

# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        Monster() = default
# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        Monster(const Monster& rhs) = default

        def setRandomHp(self, hpRng, higherHp):
            hpRange = monsterHpRange[int(self.id)][1 if higherHp else 0]
            self.curHp = hpRng.random(hpRange[0], hpRange[1])
            self.maxHp = self.curHp

// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        initHp(hpRng, ascension)
        def construct(self, bc, monsterId, monsterIdx):
            self.id = monsterId
            self.idx = monsterIdx
            self.initHp(bc.monsterHpRng, bc.ascension)

            if (self.id == MonsterId.GREEN_LOUSE) or (self.id == MonsterId.RED_LOUSE):
                if bc.ascension >= 2:
                    self.miscInfo = bc.monsterHpRng.random(6, 8)
                else:
                    self.miscInfo = bc.monsterHpRng.random(5, 7)

            elif self.id == MonsterId.DARKLING:
                if bc.ascension >= 2:
                    self.miscInfo = bc.monsterHpRng.random(9, 13)
                else:
                    self.miscInfo = bc.monsterHpRng.random(7, 11)


// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        initSpawnedMonster(bc, monsterId, monsterIdx, hp)

// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        preBattleAction(bc)

        def applyStartOfTurnPowers(self, bc):
            if not hasStatus():
                self.block = 0

            if hasStatus():
                setHasStatus(False)

            if hasStatus():
                setStatus(4 if bc.ascension >= 17 else 3)

            if hasStatus():
                setStatus(200 if bc.ascension >= 19 else 300)

            if hasStatus() and not bc.monsters.areMonstersBasicallyDead():
                bc.addToBot(Actions.PoisonLoseHpAction())

        def applyEndOfTurnTriggers(self, bc):
            # Monster Powers atEndOfTurnPreEndTurnCards and atEndOfTurn
            if hasStatus():
                self.addBlock(getStatus())

            if hasStatus():
                setStatus(3)

            if hasStatus():
                self.addBlock(getStatus())

            if hasStatus():
                decrementStatus()

            if hasStatus():
                self.heal(getStatus())

            if hasStatus():
                buff(getStatus())
                removeStatus()

        def applyEndOfRoundPowers(self, bc):
            # Monster Powers atEndOfRound
            if hasStatus<MS.RITUAL>():
                if wasJustApplied<MS.RITUAL>():
                    setJustApplied<MS.RITUAL>(False)
                else:
                    buff(getStatus<MS.RITUAL>())

            if hasStatus():
                setStatus(0)

            if hasStatus():
                decrementStatus()

            if hasStatus():
                if wasJustApplied():
                    setJustApplied(False)
                else:
                    decrementStatus()

            if hasStatus():
                if wasJustApplied():
                    setJustApplied(False)
                else:
                    decrementStatus()

            if hasStatus():
                buff(getStatus())


        # ***********************

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] const char *getName() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: const char *getName() const
        def getName(self):
            return monsterIdStrings[int(self.id)]

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool hasStatusInternal(MonsterStatus s) const; // only to be used by printLogs methods
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool hasStatusInternal(MonsterStatus s) const
        def hasStatusInternal(self, s):
            return (self.statusBits & (1 << int(s))) != 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getStatusInternal(MonsterStatus s) const; // only to be used by printLogs methods
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getStatusInternal(MonsterStatus s) const
        def getStatusInternal(self, s):
            if s == MS.STRENGTH:
                return self.strength

            if not self.hasStatusInternal(s):
                return 0

            if s == MS.ARTIFACT:
                return self.artifact

            elif s == MS.BLOCK_RETURN:
                return self.blockReturn

            elif s == MS.CHOKED:
                return self.choked

            elif s == MS.CORPSE_EXPLOSION:
                return self.corpseExplosion

            elif s == MS.LOCK_ON:
                return self.lockOn

            elif s == MS.MARK:
                return self.mark

            elif s == MS.METALLICIZE:
                return self.metallicize

            elif s == MS.PLATED_ARMOR:
                return self.platedArmor

            elif s == MS.POISON:
                return self.poison

            elif s == MS.REGEN:
                return self.regen

            elif s == MS.SHACKLED:
                return self.shackled

            elif s == MS.VULNERABLE:
                return self.vulnerable

            elif s == MS.WEAK:
                return self.weak

            elif (s == MS.ANGRY) or (s == MS.BEAT_OF_DEATH) or (s == MS.CURIOSITY) or (s == MS.CURL_UP) or (s == MS.ENRAGE) or (s == MS.FADING) or (s == MS.FLIGHT) or (s == MS.GENERIC_STRENGTH_UP) or (s == MS.INTANGIBLE) or (s == MS.MALLEABLE) or (s == MS.MODE_SHIFT) or (s == MS.RITUAL) or (s == MS.SLOW) or (s == MS.SPORE_CLOUD) or (s == MS.THIEVERY) or (s == MS.THORNS) or (s == MS.TIME_WARP):
                return self.uniquePower0

            elif (s == MS.INVINCIBLE) or (s == MS.REACTIVE) or (s == MS.SHARP_HIDE):
                return self.uniquePower1

                # boolean powers
            elif (s == MS.ASLEEP) or (s == MS.BARRICADE) or (s == MS.MINION) or (s == MS.MINION_LEADER) or (s == MS.PAINFUL_STABS) or (s == MS.REGROW) or (s == MS.SHIFTING) or (s == MS.STASIS):
                return 1 if True else 0 # already did status check above

            else:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                False = assert()
##endif
                return 0


        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: template <MonsterStatus> [[nodiscard]] bool hasStatus() const
        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool hasStatus() const
        def hasStatus(self):
            return (self.statusBits & (1 << int(s))) != 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: template <MonsterStatus> [[nodiscard]] int getStatus() const
        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getStatus() const
        def getStatus(self):
            if s == MonsterStatus.STRENGTH:
                return self.strength

            if isBooleanPower(s):
                return 1 if hasStatus() else 0

            if not hasStatus():
                return 0

            if s == MonsterStatus.ARTIFACT:
                return self.artifact

            elif s == MonsterStatus.BLOCK_RETURN:
                return self.blockReturn

            elif s == MonsterStatus.CHOKED:
                return self.choked

            elif s == MonsterStatus.CORPSE_EXPLOSION:
                return self.corpseExplosion

            elif s == MonsterStatus.LOCK_ON:
                return self.lockOn

            elif s == MonsterStatus.MARK:
                return self.mark

            elif s == MonsterStatus.METALLICIZE:
                return self.metallicize

            elif s == MonsterStatus.PLATED_ARMOR:
                return self.platedArmor

            elif s == MonsterStatus.POISON:
                return self.poison

            elif s == MonsterStatus.REGEN:
                return self.regen

            elif s == MonsterStatus.SHACKLED:
                return self.shackled

            elif s == MonsterStatus.VULNERABLE:
                return self.vulnerable

            elif s == MonsterStatus.WEAK:
                return self.weak

            elif (s == MonsterStatus.ANGRY) or (s == MonsterStatus.BEAT_OF_DEATH) or (s == MonsterStatus.CURIOSITY) or (s == MonsterStatus.CURL_UP) or (s == MonsterStatus.ENRAGE) or (s == MonsterStatus.FADING) or (s == MonsterStatus.FLIGHT) or (s == MonsterStatus.GENERIC_STRENGTH_UP) or (s == MonsterStatus.INTANGIBLE) or (s == MonsterStatus.MALLEABLE) or (s == MonsterStatus.MODE_SHIFT) or (s == MonsterStatus.RITUAL) or (s == MonsterStatus.SLOW) or (s == MonsterStatus.SPORE_CLOUD) or (s == MonsterStatus.THIEVERY) or (s == MonsterStatus.THORNS) or (s == MonsterStatus.TIME_WARP):
                return self.uniquePower0

            elif (s == MonsterStatus.INVINCIBLE) or (s == MonsterStatus.REACTIVE) or (s == MonsterStatus.SHARP_HIDE):
                return self.uniquePower1

            else:
                return 0

        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
        # ORIGINAL LINE: template <MonsterStatus> void setHasStatus(bool value=true)
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
        def setHasStatus(self, value = True):
            if s == MonsterStatus.STRENGTH:
                return # should not be called
            if value:
                self.statusBits |= ulong((1 << int(s)))
            else:
                self.statusBits &= ulong(~(1 << int(s)))

        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
        # ORIGINAL LINE: template <MonsterStatus> void setStatus(int amount)
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
        def setStatus(self, amount):
            if isBooleanPower(s):
                setHasStatus(amount)
                return

            if s == MonsterStatus.ARTIFACT:
                self.artifact = sbyte(amount)
                return

            elif s == MonsterStatus.BLOCK_RETURN:
                self.blockReturn = sbyte(amount)
                return

            elif s == MonsterStatus.CHOKED:
                self.choked = sbyte(amount)
                return

            elif s == MonsterStatus.CORPSE_EXPLOSION:
                self.corpseExplosion = sbyte(amount)
                return

            elif s == MonsterStatus.LOCK_ON:
                self.lockOn = sbyte(amount)
                return

            elif s == MonsterStatus.MARK:
                self.mark = short(amount)
                return

            elif s == MonsterStatus.METALLICIZE:
                self.metallicize = sbyte(amount)
                return

            elif s == MonsterStatus.PLATED_ARMOR:
                self.platedArmor = sbyte(amount)
                return

            elif s == MonsterStatus.POISON:
                self.poison = sbyte(amount)
                return

            elif s == MonsterStatus.REGEN:
                self.regen = sbyte(amount)
                return

            elif s == MonsterStatus.SHACKLED:
                self.shackled = sbyte(amount)
                return

            elif s == MonsterStatus.STRENGTH:
                self.strength = amount
                return

            elif s == MonsterStatus.VULNERABLE:
                self.vulnerable = amount
                return

            elif s == MonsterStatus.WEAK:
                self.weak = amount
                return

            elif (s == MonsterStatus.ANGRY) or (s == MonsterStatus.BEAT_OF_DEATH) or (s == MonsterStatus.CURIOSITY) or (s == MonsterStatus.CURL_UP) or (s == MonsterStatus.ENRAGE) or (s == MonsterStatus.FADING) or (s == MonsterStatus.FLIGHT) or (s == MonsterStatus.GENERIC_STRENGTH_UP) or (s == MonsterStatus.INTANGIBLE) or (s == MonsterStatus.MALLEABLE) or (s == MonsterStatus.MODE_SHIFT) or (s == MonsterStatus.RITUAL) or (s == MonsterStatus.SLOW) or (s == MonsterStatus.SPORE_CLOUD) or (s == MonsterStatus.THIEVERY) or (s == MonsterStatus.THORNS) or (s == MonsterStatus.TIME_WARP):
                self.uniquePower0 = amount
                return

            elif (s == MonsterStatus.INVINCIBLE) or (s == MonsterStatus.REACTIVE) or (s == MonsterStatus.SHARP_HIDE):
                self.uniquePower1 = short(amount)
                return

        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
        # ORIGINAL LINE: template <MonsterStatus> void decrementStatus(int amount=1)
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
        def decrementStatus(self, amount = 1):
            if isBooleanPower(s):
                setHasStatus(False)
                return

            if s == MonsterStatus.STRENGTH:
                self.strength -= amount
                return

            if int(s) <= int(MonsterStatus.WEAK):
                newAmount = getStatus()-amount
                setStatus(newAmount)
                setHasStatus(newAmount)

            elif int(s) <= int(MonsterStatus.TIME_WARP):
                self.uniquePower0 -= amount
                if self.uniquePower0 == 0:
                    setHasStatus(False)

            else:
                self.uniquePower1 -= short(amount)
                if self.uniquePower1 == 0:
                    setHasStatus(False)

        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
        # ORIGINAL LINE: template <MonsterStatus> void addDebuff(int amount, bool isSourceMonster=true)
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
        def addDebuff(self, amount, isSourceMonster = True):
            if isSourceMonster and (s == MonsterStatus.WEAK or s == MonsterStatus.VULNERABLE):
                setJustApplied(True)

            if s == MonsterStatus.BLOCK_RETURN:
                self.blockReturn += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.CHOKED:
                self.choked += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.CORPSE_EXPLOSION:
                self.corpseExplosion += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.LOCK_ON:
                self.lockOn += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.MARK:
                self.mark += short(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.POISON:
                self.poison += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.STRENGTH:
                self.strength += amount
                setHasStatus(True)
                return

            elif s == MonsterStatus.VULNERABLE:
                self.vulnerable += amount
                setHasStatus(True)
                return

            elif s == MonsterStatus.WEAK:
                self.weak += amount
                setHasStatus(True)
                return

            else:
                False = assert()

        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
        # ORIGINAL LINE: template <MonsterStatus> void removeStatus()
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
        def removeStatus(self):
            # C++ TO PYTHON CONVERTER TASK: There is no equivalent in Python to 'static_assert':
            #        static_assert(s != MonsterStatus::STRENGTH)
            if hasStatus():
                setStatus(0)
                setHasStatus(False)

        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
        # ORIGINAL LINE: template <MonsterStatus> void buff(int amount=1)
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
        def buff(self, amount = 1):
            if isBooleanPower(s):
                setHasStatus(True)
                return

            if s == MonsterStatus.ARTIFACT:
                self.artifact += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.METALLICIZE:
                self.metallicize += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.PLATED_ARMOR:
                self.platedArmor += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.REGEN:
                self.regen += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.SHACKLED:
                self.shackled += sbyte(amount)
                setHasStatus(True)
                return

            elif s == MonsterStatus.STRENGTH:
                self.strength += amount
                return

            elif (s == MonsterStatus.ANGRY) or (s == MonsterStatus.BEAT_OF_DEATH) or (s == MonsterStatus.CURIOSITY) or (s == MonsterStatus.CURL_UP) or (s == MonsterStatus.ENRAGE) or (s == MonsterStatus.FADING) or (s == MonsterStatus.FLIGHT) or (s == MonsterStatus.GENERIC_STRENGTH_UP) or (s == MonsterStatus.INTANGIBLE) or (s == MonsterStatus.MALLEABLE) or (s == MonsterStatus.MODE_SHIFT) or (s == MonsterStatus.SLOW) or (s == MonsterStatus.SPORE_CLOUD) or (s == MonsterStatus.THIEVERY) or (s == MonsterStatus.THORNS) or (s == MonsterStatus.TIME_WARP):
                setHasStatus(True)
                self.uniquePower0 += amount
                return

            elif s == MonsterStatus.RITUAL:
                setJustApplied(True)
                setHasStatus(True)
                self.uniquePower0 += amount
                return

            elif (s == MonsterStatus.INVINCIBLE) or (s == MonsterStatus.REACTIVE) or (s == MonsterStatus.SHARP_HIDE):
                setHasStatus(True)
                self.uniquePower1 += short(amount)
                return


        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
        # ORIGINAL LINE: template <MonsterStatus> void setJustApplied(bool value)
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
        def setJustApplied(self, value):
            mask = 0
            if s == MonsterStatus.VULNERABLE:
                mask = ulong(0x1 << 63)
            elif s == MonsterStatus.WEAK:
                mask = ulong(0x1 << 62)
            elif s == MonsterStatus.RITUAL:
                mask = ulong(0x1 << 61)

            if value:
                self.statusBits |= mask
            else:
                self.statusBits &= ~mask

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: template <MonsterStatus> [[nodiscard]] bool wasJustApplied() const
        # C++ TO PYTHON CONVERTER TASK: C++ 'constraints' are not converted by C++ to Python Converter:
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <typename > requires MonsterStatus<>
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool wasJustApplied() const
        def wasJustApplied(self):
            mask = 0
            if s == MonsterStatus.VULNERABLE:
                mask = ulong(0x1 << 63)
            elif s == MonsterStatus.WEAK:
                mask = ulong(0x1 << 62)
            elif s == MonsterStatus.RITUAL:
                mask = ulong(0x1 << 61)
            return (self.statusBits & mask) != 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isAlive() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isAlive() const
        def isAlive(self):
            return self.curHp > 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isTargetable() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isTargetable() const
        def isTargetable(self):
            return not self.isDeadOrEscaped()

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isDying() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isDying() const
        def isDying(self):
            return self.curHp <= 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isEscaping() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isEscaping() const
        def isEscaping(self):
            return self.isEscapingB

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isDeadOrEscaped() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isDeadOrEscaped() const
        def isDeadOrEscaped(self):
            return self.isDying() or self.isHalfDead() or self.isEscaping()

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isHalfDead() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isHalfDead() const
        def isHalfDead(self):
            return self.halfDead

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool doesEscapeNext() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool doesEscapeNext() const
        def doesEscapeNext(self):
            return self.escapeNext

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isAttacking() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isAttacking() const
        def isAttacking(self):
            return isMoveAttack(self.moveHistory[0])

        # ***********************

        def heal(self, amount):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            if amount < 0:
                False = assert()
##endif

            self.curHp = min(self.maxHp, self.curHp + amount)

        def addBlock(self, amount):
            self.block += amount

        def die(self, bc):
            bc.monsters.monstersAlive -= 1

            if self.id == MonsterId.AWAKENED_ONE and self.miscInfo == 0:
                self.halfDead = True
                self.removeDebuffs()
                removeStatus()
                self.setMove(MonsterMoveId.AWAKENED_ONE_REBIRTH)
                bc.cardQueue.clear()

            elif bc.monsters.monstersAlive == 0 or hasStatus():
                #            bc.cleanCardQueue(); // todo should this really return like this?
                bc.outcome = Outcome.PLAYER_VICTORY
                return

            if hasStatus():
                # spore cloud always has a value of 2 in game
                bc.addToTop(Actions.DebuffPlayer(2, bc.turnHasEnded))

            elif hasStatus():
                self.resetAllStatusEffects()
                self.setMove(MMID.DARKLING_REGROW)
                self.halfDead = True

            elif hasStatus():
                self.returnStasisCard(bc)

            if hasStatus():
                damage = self.maxHp * getStatus()
                bc.addToBot(Actions.DamageAllEnemy(damage))

            if bc.player.hasRelic():
                bc.addToBot(Actions.GainEnergy(1))
                bc.addToBot(Actions.DrawCards(1))

            if bc.player.hasRelic():
                bc.addToBot(Actions.SetState(InputState.SELECT_ENEMY_THE_SPECIMEN_APPLY_POISON))

        def suicideAction(self, bc):
            if not self.isAlive():
                return

            bc.monsters.monstersAlive -= 1
            self.curHp = 0
            if bc.monsters.monstersAlive == 0:
                bc.outcome = Outcome.PLAYER_VICTORY

        def attackedUnblockedHelper(self, bc, damage):
            if bc.player.hasRelic() and damage > 0 and damage < 5:
                damage = 5

            if bc.player.hasStatus():
                bc.addToTop(Actions.DebuffEnemy(self.idx, bc.player.getStatus()))

            if hasStatus():
                damage = min(damage, getStatus())
                setStatus(getStatus() - damage)

            elif hasStatus():
                decrementStatus()
                if (not hasStatus()) and self.id == MonsterId.SHELLED_PARASITE:
                    self.setMove(MMID.SHELLED_PARASITE_STUNNED)

            elif hasStatus():
                bc.addToBot(Actions.MonsterGainBlock(self.idx, getStatus()))
                setHasStatus(False)

            elif hasStatus() and damage > 0:
                flight = getStatus()
                if flight == 1:
                    self.setMove(MMID.BYRD_STUNNED)
                setStatus(flight-1)

            elif hasStatus() or hasStatus():
                if hasStatus():
                    malleable = getStatus()
                    bc.addToBot(Actions.MonsterGainBlock(self.idx, malleable))
                    setStatus(malleable+1)
                if hasStatus():
                    if getStatus() == 0:
                        setStatus(1)
                        bc.addToBot(Actions.ReactiveRollMove())

                    else:
                        setStatus(getStatus()+1)

            elif hasStatus():
                bc.addToTop(Actions.DamagePlayer(getStatus()))

            elif hasStatus():
                # lagavulin
                setHasStatus(False)
                decrementStatus(8)

            elif hasStatus():
                addDebuff(-damage)
                buff(damage)

            self.curHp -= damage
            if self.curHp <= 0:
                self.curHp = 0
                self.die(bc)
            else:
                self.onHpLost(bc, damage)

        def attacked(self, bc, damage):
            if self.isDeadOrEscaped():
                std::cerr << bc.seed << " was dead when attacked" << self.idx << "\n" << bc
                False = assert()
                return

            if damage < 0:
                damage = 0

            if hasStatus():
                if damage > 0:
                    damage = 1

            if hasStatus():
                buff(getStatus())

            hadBlock = self.block > 0
            tempDamage = damage
            damage -= self.block
            self.block = max(0, self.block - tempDamage)

            if hadBlock and self.block == 0 and bc.player.hasRelic<RelicId.HAND_DRILL>():
                bc.addToBot(Actions.DebuffEnemy(self.idx, 2, False))

            if damage > 0:
                self.attackedUnblockedHelper(bc, damage)

        def damageUnblockedHelper(self, bc, damage):

            if hasStatus():
                damage = min(damage, getStatus())
                setStatus(getStatus() - damage)
            if hasStatus():
                # lagavulin
                setHasStatus(False)
                decrementStatus(8)
            if hasStatus():
                addDebuff(-damage)
                buff(damage)

            self.curHp = max(0, self.curHp-damage)
            if self.curHp == 0:
                self.die(bc)
            else:
                self.onHpLost(bc, damage)

        def damage(self, bc, damage):
            if self.isDeadOrEscaped():
                std::cerr << bc.seed << " was dead when damaged" << self.idx << "\n" << bc
                False = assert()
                return

            if damage < 0:
                damage = 0

            if hasStatus():
                if damage > 0:
                    damage = 1

            hadBlock = self.block > 0
            tempDamage = damage
            damage -= self.block
            self.block = max(0, self.block-tempDamage)

            if hadBlock and self.block == 0 and bc.player.hasRelic<RelicId.HAND_DRILL>():
                bc.addToBot(Actions.DebuffEnemy(self.idx, 2, False))

            if damage > 0:
                self.damageUnblockedHelper(bc, damage)
            else:
                return

        def onHpLost(self, bc, amount):
            atOrBelowHalf = self.curHp <= math.trunc(self.maxHp / float(2))
            if self.id == MonsterId.ACID_SLIME_L:
                if atOrBelowHalf:
                    self.moveHistory[0] = MMID.ACID_SLIME_L_SPLIT

            elif self.id == MonsterId.SLIME_BOSS:
                if atOrBelowHalf:
                    self.moveHistory[0] = MMID.SLIME_BOSS_SPLIT

            elif self.id == MonsterId.SPIKE_SLIME_L:
                if atOrBelowHalf:
                    self.moveHistory[0] = MMID.SPIKE_SLIME_L_SPLIT

            elif self.id == MonsterId.THE_GUARDIAN:
                if hasStatus():
                    newModeShiftAmount = getStatus() - amount
                    if newModeShiftAmount <= 0:
                        removeStatus()
                        self.setMove(MMID.THE_GUARDIAN_DEFENSIVE_MODE)
                        bc.addToBot(Actions.MonsterGainBlock(self.idx, 20))
                    else:
                        setStatus(newModeShiftAmount)


        def removeDebuffs(self):
            if getStatus() < 0:
                setStatus(0)

            removeStatus()
            removeStatus()
            removeStatus()
            removeStatus()
            removeStatus()
            removeStatus()
            removeStatus()
            removeStatus()
            removeStatus()

        def resetAllStatusEffects(self):
            self.statusBits = 0
            setStatus(0)
            self.block = 0

// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        setMove(moveId)
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool firstTurn() const; // only to be called in rollMove() before any moves are set
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool firstTurn() const
        def firstTurn(self):
            return self.moveHistory[0] is MMID.INVALID

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool lastMove(MonsterMoveId moveId) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool lastMove(MonsterMoveId moveId) const;
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        lastMove(moveId)
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool lastMoveBefore(MonsterMoveId moveId) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool lastMoveBefore(MonsterMoveId moveId) const;
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        lastMoveBefore(moveId)
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool lastTwoMoves(MonsterMoveId moveId) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool lastTwoMoves(MonsterMoveId moveId) const;
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        lastTwoMoves(moveId)
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool eitherLastTwo(MonsterMoveId moveId) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool eitherLastTwo(MonsterMoveId moveId) const
        def eitherLastTwo(self, moveId):
            return self.moveHistory[0] is moveId or self.moveHistory[1] is moveId

        def rollMove(self, bc):
            miscInfoCopy = self.miscInfo

            temp_ref_miscInfoCopy = RefObject(miscInfoCopy);
            move = self.getMoveForRoll(bc, temp_ref_miscInfoCopy, bc.aiRng.random(99))
            miscInfoCopy = temp_ref_miscInfoCopy.arg_value

            self.miscInfo = miscInfoCopy
            self.setMove(MMID(move))

        # todo make monsterData const as well and move logic to move actions
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] MMID getMoveForRoll(BattleContext &bc, int &monsterData, int roll) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: MMID getMoveForRoll(BattleContext &bc, int &monsterData, int roll) const;
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        getMoveForRoll(bc, monsterData, roll)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int calculateDamageToPlayer(const BattleContext &bc, int baseDamage) const

        # this is calculated at the player when the damage occurs in game, consider testing whether there are any scenarios when it can't be done before
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int calculateDamageToPlayer(const BattleContext &bc, int baseDamage) const
        def calculateDamageToPlayer(self, bc, baseDamage):
            p = bc.player
            damage = float((baseDamage + getStatus()))

            if p.hasStatus():
                facingSelf = p.lastTargetedMonster == self.idx or bc.monsters.arr[p.lastTargetedMonster].isDeadOrEscaped()
                if not facingSelf:
                    damage *= 1.5

            if hasStatus():
                if p.hasRelic():
                    damage *= 0.6
                else:
                    damage *= 0.75

            if p.hasStatus():
                if p.hasRelic():
                    damage *= 1.25
                else:
                    damage *= 1.5

            if p.stance == Stance.WRATH:
                damage *= 2

            # apply backIdx attack for spire guard elites

            if p.hasStatus():
                damage = min(damage, float(1))

            return max(int(math.floor(damage)), 0)

        def attackPlayerHelper(self, bc, baseDamage, times = 1):
            damage = self.calculateDamageToPlayer(bc, baseDamage)

            for i in range(0, times):
                bc.addToBot(Actions.AttackPlayer(self.idx, damage))

// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        takeTurn(bc)
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] DamageInfo getMoveBaseDamage(const BattleContext &bc) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: DamageInfo getMoveBaseDamage(const BattleContext &bc) const;
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        getMoveBaseDamage(bc)

        # monster specific functions

// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        stealGoldFromPlayer(bc, amount)
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        largeSlimeSplit(bc, mediumSlimeType, placeIdx, hp)
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        slimeBossSplit(bc, hp)
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        spawnBronzeOrbs(bc) // Bronze Automaton
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        stasisAction(bc) // Bronze Orb
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        returnStasisCard(bc)
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        reptomancerSummon(bc, daggerCount)

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] static int getAliveGremlinCount(const BattleContext &bc)
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        getAliveGremlinCount(bc)


    def left_shift(self, os, m):
        os << "{"
        os << m.idx << " " << sts.MONSTERIDSTRINGS[int(m.id)] << " hp:(" << m.curHp << "/" << m.maxHp << ")" << " block:(" << m.block << ") statusEffects:{"

        havePrint = False
        temp_ref_havePrint = RefObject(havePrint);
        sts.printIfHaveStatus(os, m, sts.MonsterStatus.STRENGTH, temp_ref_havePrint)
        havePrint = temp_ref_havePrint.arg_value
        i = static_cast<int>(MonsterStatus.ARTIFACT)
        while i <= int(sts.MonsterStatus.STASIS):
            s = i
            if s != sts.MonsterStatus.STRENGTH:
                temp_ref_havePrint2 = RefObject(havePrint);
                sts.printIfHaveStatus(os, m, auto(s), temp_ref_havePrint2)
                havePrint = temp_ref_havePrint2.arg_value
            i += 1
        os << "}"

        os << " halfDead: " << m.halfDead << ", moveHistory: { " << sts.MONSTERMOVESTRINGS[int(m.moveHistory[0])] << ", " << sts.MONSTERMOVESTRINGS[int(m.moveHistory[1])] << "}" << " nextActionDamage: " << " miscInfo: " << m.miscInfo << " uniquePower0: " << m.uniquePower0 << " uniquePower1: " << m.uniquePower1 << "}"
        return os



# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##pragma clang diagnostic push
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##pragma ide diagnostic ignored "cppcoreguidelines-narrowing-conversions"
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##pragma clang diagnostic pop


# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool Monster::lastMove(MMID moveId) const
def lastMove(moveId):
    return moveHistory[0] is moveId

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool Monster::lastMoveBefore(MMID moveId) const
def lastMoveBefore(moveId):
    return moveHistory[1] is moveId

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool Monster::lastTwoMoves(MMID moveId) const
def lastTwoMoves(moveId):
    return moveHistory[0] is moveId and moveHistory[1] is moveId

def setMove(moveId):
    moveHistory[1] = moveHistory[0]
    moveHistory[0] = moveId

class sts: #this class replaces the original namespace 'sts'

    @staticmethod
    def printIfHaveStatus(os, m, s, havePrint):
        if m.getStatusInternal(s) == 0:
            return os

        if havePrint.arg_value:
            os << ", "
        havePrint.arg_value = True

        os << '(' << sts.enemyStatusStrings[int(s)]
        if not sts.isBooleanPower(s):
            os << "," << m.getStatusInternal(s)
        os << ")"
        return os

