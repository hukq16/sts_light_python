from sts import *

#
# Created by gamerpuppy on 7/7/2021.
#


#
# Created by gamerpuppy on 7/4/2021.
#




class sts: #this class replaces the original namespace 'sts'

    class MonsterGroup:

        def __init__(self):
            # instance fields found by C++ to Python Converter:
            self.monstersAlive = 0
            self.monsterCount = 0
            self.arr = [None for _ in range(5)]


# C++ TO PYTHON CONVERTER TASK: The following line could not be converted:
        std::bitset<5> extraRollMoveOnTurn;
# C++ TO PYTHON CONVERTER TASK: The following line could not be converted:
        std::bitset<5> skipTurn;

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool areMonstersBasicallyDead() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool areMonstersBasicallyDead() const
        def areMonstersBasicallyDead(self):
            return self.monstersAlive <= 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getAliveCount() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getAliveCount() const
        def getAliveCount(self):
            return self.monstersAlive

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getTargetableCount() const; // calculated here, not fast
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getTargetableCount() const
        def getTargetableCount(self):
            count = 0
            i = 0
            while i < self.monsterCount:
                if self.arr[i].isTargetable():
                    count += 1
                i += 1
            return count

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getFirstTargetable() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getFirstTargetable() const
        def getFirstTargetable(self):
            i = 0
            while i < self.monsterCount:
                if self.arr[i].isTargetable():
                    return i
                i += 1
            return -1

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getRandomMonsterIdx(Random &rng, bool aliveOnly=true) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getRandomMonsterIdx(Random &rng, bool aliveOnly =true) const
        def getRandomMonsterIdx(self, rng, aliveOnly = True):
            if aliveOnly:
                if self.monstersAlive == 0:
                    return -1
                else:
                    aliveIdx = rng.random(self.monstersAlive-1)

                    i = 0
                    aliveEncountered = 0
                    while True:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
                        # seed 11195
                        if i >= self.monsterCount:
                            std::cerr << monsterIdStrings[int((self.arr[0].id))] << " " << monsterIdStrings[int((self.arr[1].id))] << " " << "count:" << self.monsterCount << " " << "alive:" << self.monstersAlive << std::endl
                            False = assert()
##endif
                        if not self.arr[i].isDeadOrEscaped():
                            if aliveEncountered == aliveIdx:
                                return i
                            else:
                                aliveEncountered += 1
                        i += 1

            else:
                return rng.random(self.monsterCount - 1)

        # initialization

        def init(self, bc, encounter):
            self.createMonsters(bc, encounter)
            i = 0
            while i < self.monsterCount:
                if self.arr[i].idx != -1:
                    self.arr[i].rollMove(bc)
                i += 1

            i = 0
            while i < self.monsterCount:
                if self.arr[i].idx != -1:
                    self.arr[i].preBattleAction(bc)
                i += 1

        def createMonsters(self, bc, encounter):

            if encounter == MonsterEncounter.GREMLIN_GANG:
                    gremlinPool = [(int)MonsterId.MAD_GREMLIN, MonsterId.MAD_GREMLIN, MonsterId.SNEAKY_GREMLIN, MonsterId.SNEAKY_GREMLIN, MonsterId.FAT_GREMLIN, MonsterId.FAT_GREMLIN, MonsterId.SHIELD_GREMLIN, (int)MonsterId.GREMLIN_WIZARD]
                    lastIdx = 7
                    for i in range(0, 4):
                        idx = bc.miscRng.random(lastIdx)
                        gremlin = gremlinPool[idx]

                        while idx < lastIdx:
                            gremlinPool[idx] = gremlinPool[idx + 1]
                            idx += 1
                        lastIdx -= 1
                        self.createMonster(bc, gremlin)

            elif encounter == MonsterEncounter.SMALL_SLIMES:
                    if bc.miscRng.randomBoolean():
                        self.createMonster(bc, MonsterId.SPIKE_SLIME_S)
                        self.createMonster(bc, MonsterId.ACID_SLIME_M)
                    else:
                        self.createMonster(bc, MonsterId.ACID_SLIME_S)
                        self.createMonster(bc, MonsterId.SPIKE_SLIME_M)

            elif encounter == MonsterEncounter.LOTS_OF_SLIMES:
                    slimePool = [(int)MonsterId.SPIKE_SLIME_S, MonsterId.SPIKE_SLIME_S, MonsterId.SPIKE_SLIME_S, MonsterId.ACID_SLIME_S, (int)MonsterId.ACID_SLIME_S]
                    for i in range(4, -1, -1):
                        idx = bc.miscRng.random(i)
                        slime = slimePool[idx]
                        while idx < i:
                            slimePool[idx] = slimePool[idx + 1]
                            idx += 1
                        self.createMonster(bc, slime)

            elif encounter == MonsterEncounter.LARGE_SLIME:
                    id = MonsterId.ACID_SLIME_L if bc.miscRng.randomBoolean() else MonsterId.SPIKE_SLIME_L
                    self.createMonster(bc, id)

            elif encounter == MonsterEncounter.EXORDIUM_THUGS:
                self.createWeakWildlife(bc)
                self.createStrongHumanoid(bc)

            elif encounter == MonsterEncounter.EXORDIUM_WILDLIFE:
                self.createStrongWildlife(bc)
                self.createWeakWildlife(bc)

            elif encounter == MonsterEncounter.AUTOMATON:
                self.monsterCount = 1
                self.createMonster(bc, MonsterId.BRONZE_AUTOMATON)
                self.monsterCount += 1

            elif encounter == MonsterEncounter.AWAKENED_ONE:
                self.createMonster(bc, MonsterId.CULTIST)
                self.createMonster(bc, MonsterId.CULTIST)
                self.createMonster(bc, MonsterId.AWAKENED_ONE)

            elif encounter == MonsterEncounter.BOOK_OF_STABBING:
                self.createMonster(bc, MonsterId.BOOK_OF_STABBING)

            elif encounter == MonsterEncounter.BLUE_SLAVER:
                self.createMonster(bc, MonsterId.BLUE_SLAVER)

            elif encounter == MonsterEncounter.CENTURION_AND_HEALER:
                self.createMonster(bc, MonsterId.CENTURION)
                self.createMonster(bc, MonsterId.MYSTIC)

            elif encounter == MonsterEncounter.COLLECTOR:
                self.monsterCount = 2
                self.createMonster(bc, MonsterId.THE_COLLECTOR)

            elif encounter == MonsterEncounter.COLOSSEUM_EVENT_NOBS:
                self.createMonster(bc, MonsterId.TASKMASTER)
                self.createMonster(bc, MonsterId.GREMLIN_NOB)

            elif encounter == MonsterEncounter.COLOSSEUM_EVENT_SLAVERS:
                self.createMonster(bc, MonsterId.BLUE_SLAVER)
                self.createMonster(bc, MonsterId.RED_SLAVER)

            elif encounter == MonsterEncounter.CHAMP:
                self.createMonster(bc, MonsterId.THE_CHAMP)

            elif encounter == MonsterEncounter.CHOSEN:
                self.createMonster(bc, MonsterId.CHOSEN)

            elif encounter == MonsterEncounter.CHOSEN_AND_BYRDS:
                self.createMonster(bc, MonsterId.BYRD)
                self.createMonster(bc, MonsterId.CHOSEN)

            elif encounter == MonsterEncounter.CULTIST:
                self.createMonster(bc, MonsterId.CULTIST)

            elif encounter == MonsterEncounter.CULTIST_AND_CHOSEN:
                self.createMonster(bc, MonsterId.CULTIST)
                self.createMonster(bc, MonsterId.CHOSEN)

            elif encounter == MonsterEncounter.DONU_AND_DECA:
                self.createMonster(bc, MonsterId.DECA)
                self.createMonster(bc, MonsterId.DONU)

            elif encounter == MonsterEncounter.FOUR_SHAPES:
                self.createShapes(bc, 4)

            elif encounter == MonsterEncounter.GIANT_HEAD:
                self.createMonster(bc, MonsterId.GIANT_HEAD)

            elif encounter == MonsterEncounter.GREMLIN_LEADER:
                    self.arr[1].construct(bc, sts.MonsterGroup.getGremlin(bc.miscRng), 1)
                    self.arr[1].buff()

                    self.arr[2].construct(bc, sts.MonsterGroup.getGremlin(bc.miscRng), 2)
                    self.arr[2].buff()

                    self.arr[3].construct(bc, MonsterId.GREMLIN_LEADER, 3)
                    self.monstersAlive = 3
                    self.monsterCount = 4

            elif encounter == MonsterEncounter.GREMLIN_NOB:
                self.createMonster(bc, MonsterId.GREMLIN_NOB)

            elif encounter == MonsterEncounter.HEXAGHOST:
                self.createMonster(bc, MonsterId.HEXAGHOST)

            elif encounter == MonsterEncounter.JAW_WORM:
                self.createMonster(bc, MonsterId.JAW_WORM)

            elif encounter == MonsterEncounter.JAW_WORM_HORDE:
                    self.createMonster(bc, MonsterId.JAW_WORM)
                    self.createMonster(bc, MonsterId.JAW_WORM)
                    self.createMonster(bc, MonsterId.JAW_WORM)

                    strBuff = 5 if bc.ascension >= 17 else (4 if bc.ascension >= 2 else 3)
                    blockBuff = 9 if bc.ascension >= 17 else (6 if bc.ascension >= 2 else 5)
                    for i in range(0, 3):
                        m = bc.monsters.arr[i]
                        m.buff(strBuff)
                        m.addBlock(blockBuff)

                        firstMove = MMID.DARKLING_REGROW
                        m.moveHistory[0] = firstMove # it doesn't matter what this is as long as it is not invalid
                        # C++ TO PYTHON CONVERTER TASK: There is no equivalent in Python to 'static_assert':
                        #                static_assert(firstMove != MonsterMoveId::INVALID)


            elif encounter == MonsterEncounter.LAGAVULIN:
                self.createMonster(bc, MonsterId.LAGAVULIN)
                bc.monsters.arr[0].setHasStatus(True)

            elif encounter == MonsterEncounter.LAGAVULIN_EVENT:
                self.createMonster(bc, MonsterId.LAGAVULIN)

            elif encounter == MonsterEncounter.LOOTER:
                self.createMonster(bc, MonsterId.LOOTER)

            elif encounter == MonsterEncounter.MASKED_BANDITS_EVENT:
                self.createMonster(bc, MonsterId.POINTY)
                self.createMonster(bc, MonsterId.ROMEO)
                self.createMonster(bc, MonsterId.BEAR)

            elif encounter == MonsterEncounter.MAW:
                self.createMonster(bc, MonsterId.THE_MAW)

            elif encounter == MonsterEncounter.MUSHROOMS_EVENT:
                self.createMonster(bc, MonsterId.FUNGI_BEAST)
                self.createMonster(bc, MonsterId.FUNGI_BEAST)
                self.createMonster(bc, MonsterId.FUNGI_BEAST)

            elif encounter == MonsterEncounter.MYSTERIOUS_SPHERE_EVENT:
                self.createMonster(bc, MonsterId.ORB_WALKER)
                self.createMonster(bc, MonsterId.ORB_WALKER)

            elif encounter == MonsterEncounter.NEMESIS:
                self.createMonster(bc, MonsterId.NEMESIS)

            elif encounter == MonsterEncounter.ORB_WALKER:
                self.createMonster(bc, MonsterId.ORB_WALKER)

            elif encounter == MonsterEncounter.RED_SLAVER:
                self.createMonster(bc, MonsterId.RED_SLAVER)

            elif encounter == MonsterEncounter.REPTOMANCER:
                self.monsterCount += 1
                self.createMonster(bc, MonsterId.DAGGER)
                self.createMonster(bc, MonsterId.REPTOMANCER)
                self.monsterCount += 1
                self.createMonster(bc, MonsterId.DAGGER)

            elif encounter == MonsterEncounter.SENTRY_AND_SPHERE:
                self.createMonster(bc, MonsterId.SENTRY)
                self.createMonster(bc, MonsterId.SPHERIC_GUARDIAN)

            elif encounter == MonsterEncounter.SHELL_PARASITE:
                self.createMonster(bc, MonsterId.SHELLED_PARASITE)

            elif encounter == MonsterEncounter.SHELLED_PARASITE_AND_FUNGI:
                self.createMonster(bc, MonsterId.SHELLED_PARASITE)
                self.createMonster(bc, MonsterId.FUNGI_BEAST)

            elif encounter == MonsterEncounter.SHIELD_AND_SPEAR:
                self.createMonster(bc, MonsterId.SPIRE_SHIELD)
                self.createMonster(bc, MonsterId.SPIRE_SPEAR)

            elif encounter == MonsterEncounter.SLAVERS:
                self.createMonster(bc, MonsterId.BLUE_SLAVER)
                self.createMonster(bc, MonsterId.TASKMASTER)
                self.createMonster(bc, MonsterId.RED_SLAVER)

            elif encounter == MonsterEncounter.SNAKE_PLANT:
                self.createMonster(bc, MonsterId.SNAKE_PLANT)

            elif encounter == MonsterEncounter.SNECKO:
                self.createMonster(bc, MonsterId.SNECKO)

            elif encounter == MonsterEncounter.SPIRE_GROWTH:
                self.createMonster(bc, MonsterId.SPIRE_GROWTH)

            elif encounter == MonsterEncounter.SPHERE_AND_TWO_SHAPES:
                self.createMonster(bc, sts.MonsterGroup.getAncientShape(bc.miscRng))
                self.createMonster(bc, sts.MonsterGroup.getAncientShape(bc.miscRng))
                self.createMonster(bc, MonsterId.SPHERIC_GUARDIAN)

            elif encounter == MonsterEncounter.SPHERIC_GUARDIAN:
                self.createMonster(bc, MonsterId.SPHERIC_GUARDIAN)

            elif encounter == MonsterEncounter.SLIME_BOSS:
                self.createMonster(bc, MonsterId.SLIME_BOSS)

            elif encounter == MonsterEncounter.THE_GUARDIAN:
                self.createMonster(bc, MonsterId.THE_GUARDIAN)

            elif encounter == MonsterEncounter.THE_HEART:
                self.createMonster(bc, MonsterId.CORRUPT_HEART)

            elif encounter == MonsterEncounter.THREE_BYRDS:
                self.createMonster(bc, MonsterId.BYRD)
                self.createMonster(bc, MonsterId.BYRD)
                self.createMonster(bc, MonsterId.BYRD)

            elif encounter == MonsterEncounter.THREE_CULTIST:
                self.createMonster(bc, MonsterId.CULTIST)
                self.createMonster(bc, MonsterId.CULTIST)
                self.createMonster(bc, MonsterId.CULTIST)

            elif encounter == MonsterEncounter.THREE_DARKLINGS:
                self.createMonster(bc, MonsterId.DARKLING)
                self.createMonster(bc, MonsterId.DARKLING)
                self.createMonster(bc, MonsterId.DARKLING)

            elif encounter == MonsterEncounter.THREE_LOUSE:
                    self.createMonster(bc, sts.MonsterGroup.getLouse(bc.miscRng))
                    self.createMonster(bc, sts.MonsterGroup.getLouse(bc.miscRng))
                    self.createMonster(bc, sts.MonsterGroup.getLouse(bc.miscRng))

            elif encounter == MonsterEncounter.THREE_SENTRIES:
                self.createMonster(bc, MonsterId.SENTRY)
                self.createMonster(bc, MonsterId.SENTRY)
                self.createMonster(bc, MonsterId.SENTRY)

            elif encounter == MonsterEncounter.THREE_SHAPES:
                self.createShapes(bc, 3)

            elif encounter == MonsterEncounter.TIME_EATER:
                self.createMonster(bc, MonsterId.TIME_EATER)

            elif encounter == MonsterEncounter.TRANSIENT:
                self.createMonster(bc, MonsterId.TRANSIENT)

            elif encounter == MonsterEncounter.TWO_FUNGI_BEASTS:
                self.createMonster(bc, MonsterId.FUNGI_BEAST)
                self.createMonster(bc, MonsterId.FUNGI_BEAST)

            elif encounter == MonsterEncounter.TWO_LOUSE:
                    self.createMonster(bc, sts.MonsterGroup.getLouse(bc.miscRng))
                    self.createMonster(bc, sts.MonsterGroup.getLouse(bc.miscRng))

            elif encounter == MonsterEncounter.TWO_THIEVES:
                self.createMonster(bc, MonsterId.LOOTER)
                self.createMonster(bc, MonsterId.MUGGER)

            elif encounter == MonsterEncounter.WRITHING_MASS:
                self.createMonster(bc, MonsterId.WRITHING_MASS)

            else:
                False = assert()

        def createMonster(self, bc, id):
            self.arr[self.monsterCount].construct(bc, id, self.monsterCount)
            self.monsterCount += 1
            self.monstersAlive += 1

        def createStrongHumanoid(self, bc):
            temp = [Monster() for _ in range(3)]
            temp[0].construct(bc, MonsterId.CULTIST, self.monsterCount)
            temp[1].construct(bc, sts.MonsterGroup.getSlaver(bc.miscRng), self.monsterCount)
            temp[2].construct(bc, MonsterId.LOOTER, self.monsterCount)

            idx = bc.miscRng.random(2)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: arr[monsterCount++] = temp[idx];
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
            self.arr[self.monsterCount].copy_from(temp[idx])
            self.monsterCount += 1
            self.monstersAlive += 1 # todo this is hacky

        def createStrongWildlife(self, bc):
            temp = [Monster() for _ in range(2)]
            temp[0].construct(bc, MonsterId.FUNGI_BEAST, 0)
            temp[1].construct(bc, MonsterId.JAW_WORM, 0)
            idx = bc.miscRng.random(1)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: arr[monsterCount++] = temp[idx];
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
            self.arr[self.monsterCount].copy_from(temp[idx])
            self.monsterCount += 1
            self.monstersAlive += 1 # todo this is hacky

        def createWeakWildlife(self, bc):
            temp = [Monster() for _ in range(3)]
            temp[0].construct(bc, sts.MonsterGroup.getLouse(bc.miscRng), self.monsterCount)
            temp[1].construct(bc, MonsterId.SPIKE_SLIME_M, self.monsterCount)
            temp[2].construct(bc, MonsterId.ACID_SLIME_M, self.monsterCount)

            idx = bc.miscRng.random(2)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: arr[monsterCount++] = temp[idx];
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
            self.arr[self.monsterCount].copy_from(temp[idx])
            self.monsterCount += 1
            self.monstersAlive += 1 # todo this is hacky

        def createShapes(self, bc, count):
            shapePool = [(int)MonsterId.REPULSOR, MonsterId.REPULSOR, MonsterId.EXPLODER, MonsterId.EXPLODER, MonsterId.SPIKER, (int)MonsterId.SPIKER]
            lastIdx = 5
            for i in range(0, count):
                idx = bc.miscRng.random(lastIdx)
                shape = shapePool[idx]

                while idx < lastIdx:
                    shapePool[idx] = shapePool[idx + 1]
                    idx += 1
                lastIdx -= 1
                self.createMonster(bc, shape)

        @staticmethod
        def getAncientShape(miscRng):
            shapes = [(int)MonsterId.SPIKER, MonsterId.REPULSOR, (int)MonsterId.EXPLODER]
            return shapes[miscRng.random(2)]

        @staticmethod
        def getGremlin(rng):
            gremlins = [(int)MonsterId.MAD_GREMLIN, MonsterId.MAD_GREMLIN, MonsterId.SNEAKY_GREMLIN, MonsterId.SNEAKY_GREMLIN, MonsterId.FAT_GREMLIN, MonsterId.FAT_GREMLIN, MonsterId.SHIELD_GREMLIN, (int)MonsterId.GREMLIN_WIZARD]
            return gremlins[rng.random(7)]

        @staticmethod
        def getLouse(miscRng):
            if miscRng.randomBoolean():
                return MonsterId.RED_LOUSE
            else:
                return MonsterId.GREEN_LOUSE

        @staticmethod
        def getSlaver(miscRng):
            if miscRng.randomBoolean():
                return MonsterId.RED_SLAVER
            else:
                return MonsterId.BLUE_SLAVER

        # actions
        def doMonsterTurn(self, bc):
            m = self.arr[bc.monsterTurnIdx]
            if ((not m.isDeadOrEscaped()) or m.isHalfDead()) and not skipTurn[bc.monsterTurnIdx]:
                if skipTurn[bc.monsterTurnIdx]:
                    skipTurn.set(bc.monsterTurnIdx, False)
                else:
                    m.takeTurn(bc)

            if extraRollMoveOnTurn.test(bc.monsterTurnIdx):
                bc.noOpRollMove()
                extraRollMoveOnTurn.set(bc.monsterTurnIdx, False)

            bc.monsterTurnIdx += 1

        def applyPreTurnLogic(self, bc):
            i = 0
            while i < self.monsterCount:
                m = self.arr[i]
                if m.isDying() or m.isEscaping():
                    i += 1
                    continue
                m.applyStartOfTurnPowers(bc) # dont need to do this before I think
                i += 1

        def applyEmeraldEliteBuff(self, bc, buffType, act):
            i = 0
            while i < self.monsterCount:
                m = self.arr[i]

                if buffType == 0:
                    m.buff(act)

                elif buffType == 1:
                        increaseAmount = int(round(float(m.maxHp) * 0.25))
                        m.maxHp += increaseAmount
                        m.curHp += increaseAmount

                elif buffType == 2:
                    m.buff(act * 2 + 2)

                elif buffType == 3:
                    m.buff(act * 2 + 1)

                    # unreachable
                i += 1



    def left_shift(self, os, g):
        S = "\n\t"

        os << "MonsterGroup { "
        os << S << "monsterCount: " << g.monsterCount
        os << S << "monstersAlive: " << g.monstersAlive
        os << S << "extraRollMoveOnTurnBits: " << g.extraRollMoveOnTurn.to_string()

        i = 0
        while i < g.monsterCount:
            os << S << g.arr[i]
            i += 1
        os << "\n}\n"
        return os



