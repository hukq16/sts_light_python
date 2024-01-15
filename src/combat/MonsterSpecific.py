#
# Created by gamerpuppy on 8/21/2021.
#


from sts import *

import math

def initHp(hpRng, ascension):
    if id == MonsterId.INVALID:
        False = assert()

    elif id == MonsterId.ORB_WALKER:
        hpRng.random(90, 96) # first call is discarded by game
        setRandomHp(hpRng, ascension >= 7)

    elif (id == MonsterId.ACID_SLIME_L) or (id == MonsterId.ACID_SLIME_M) or (id == MonsterId.ACID_SLIME_S) or (id == MonsterId.BEAR) or (id == MonsterId.BLUE_SLAVER) or (id == MonsterId.BYRD) or (id == MonsterId.CENTURION) or (id == MonsterId.CHOSEN) or (id == MonsterId.CULTIST) or (id == MonsterId.DARKLING) or (id == MonsterId.EXPLODER) or (id == MonsterId.FAT_GREMLIN) or (id == MonsterId.FUNGI_BEAST) or (id == MonsterId.GREEN_LOUSE) or (id == MonsterId.GREMLIN_WIZARD) or (id == MonsterId.JAW_WORM) or (id == MonsterId.LOOTER) or (id == MonsterId.MAD_GREMLIN) or (id == MonsterId.MUGGER) or (id == MonsterId.MYSTIC) or (id == MonsterId.POINTY) or (id == MonsterId.RED_LOUSE) or (id == MonsterId.RED_SLAVER) or (id == MonsterId.REPULSOR) or (id == MonsterId.ROMEO) or (id == MonsterId.SHELLED_PARASITE) or (id == MonsterId.SHIELD_GREMLIN) or (id == MonsterId.SNAKE_PLANT) or (id == MonsterId.SNEAKY_GREMLIN) or (id == MonsterId.SNECKO) or (id == MonsterId.SPIKER) or (id == MonsterId.SPIKE_SLIME_L) or (id == MonsterId.SPIKE_SLIME_M) or (id == MonsterId.SPIKE_SLIME_S) or (id == MonsterId.SPIRE_GROWTH) or (id == MonsterId.WRITHING_MASS):
        setRandomHp(hpRng, ascension >= 7)

    elif (id == MonsterId.AWAKENED_ONE) or (id == MonsterId.BRONZE_AUTOMATON) or (id == MonsterId.CORRUPT_HEART) or (id == MonsterId.DECA) or (id == MonsterId.DONU) or (id == MonsterId.HEXAGHOST) or (id == MonsterId.SLIME_BOSS) or (id == MonsterId.THE_CHAMP) or (id == MonsterId.THE_COLLECTOR) or (id == MonsterId.THE_GUARDIAN) or (id == MonsterId.TIME_EATER) or (id == MonsterId.TORCH_HEAD):
        setRandomHp(hpRng, ascension >= 9)

    elif (id == MonsterId.BOOK_OF_STABBING) or (id == MonsterId.DAGGER) or (id == MonsterId.GIANT_HEAD) or (id == MonsterId.GREMLIN_LEADER) or (id == MonsterId.GREMLIN_NOB) or (id == MonsterId.LAGAVULIN) or (id == MonsterId.NEMESIS) or (id == MonsterId.SENTRY) or (id == MonsterId.SPIRE_SHIELD) or (id == MonsterId.SPIRE_SPEAR):
        setRandomHp(hpRng, ascension >= 8)

    elif id == MonsterId.REPTOMANCER:
        hpRng.random(180, 190)
        setRandomHp(hpRng, ascension >= 8)

    elif id == MonsterId.BRONZE_ORB:
        hpRng.random(52, 58)
        setRandomHp(hpRng, ascension >= 9)

    elif id == MonsterId.TASKMASTER:
        hpRng.random(54, 60)
        setRandomHp(hpRng, ascension >= 8)

    elif (id == MonsterId.SPHERIC_GUARDIAN) or (id == MonsterId.THE_MAW) or (id == MonsterId.TRANSIENT):
        curHp = monsterHpRange[int(id)][0][0]
        maxHp = curHp

    else:
        False = assert()

def preBattleAction(bc):
    asc4 = bc.ascension >= 4
    asc7 = bc.ascension >= 7
    asc9 = bc.ascension >= 9
    asc17 = bc.ascension >= 17
    asc18 = bc.ascension >= 18
    asc19 = bc.ascension >= 19

    hallwayDiffIdx = getTriIdx(bc.ascension, 2, 17)

    if id == MonsterId.CORRUPT_HEART:
            buff(2 if asc19 else 1)
            buff(200 if asc19 else 300)

    elif id == MonsterId.DAGGER:
        buff()

    elif id == MonsterId.DARKLING: # game adds regrow power
        buff()

    elif id == MonsterId.MAD_GREMLIN:
        buff(2 if asc17 else 1)

    elif id == MonsterId.EXPLODER: # game adds explosive power
        pass

    elif id == MonsterId.GIANT_HEAD: # game adds slow power
        setHasStatus(True)
        setStatus(0)

    elif id == MonsterId.GREMLIN_LEADER: # game adds MinionPower to all gremlins
        buff()

    elif id == MonsterId.TRANSIENT: # game adds ShiftingPower
        buff()
        buff(6 if asc17 else 5)

    elif id == MonsterId.BOOK_OF_STABBING: # game adds PainfulStabsPower
        buff()
        miscInfo += 1 # stab count

    elif id == MonsterId.FUNGI_BEAST: # game adds SporeCloudPower
        buff(2) # the value here isn't used. it is always 2

    elif id == MonsterId.AWAKENED_ONE:
        # buff minion leader only in stage 2
        if asc4:
            buff(2)
        buff(2 if asc19 else 1)
        buff(15 if asc19 else 10)

    elif (id == MonsterId.DECA) or (id == MonsterId.DONU):
        buff(3 if asc19 else 2)

    elif id == MonsterId.ORB_WALKER:
        buff(5 if asc17 else 3)

    elif id == MonsterId.SPIKER:
            thorns = [3, 4, 7]
            buff(thorns[hallwayDiffIdx])

    elif id == MonsterId.WRITHING_MASS:
            setHasStatus(True)
            setStatus(0)
            buff(3)

    elif id == MonsterId.BRONZE_AUTOMATON:
            buff()
            buff(3)

    elif id == MonsterId.TIME_EATER:
            buff(0)

    elif id == MonsterId.BYRD:
            buff(4 if asc17 else 3)

    elif (id == MonsterId.LOOTER) or (id == MonsterId.MUGGER):
        buff(20 if asc17 else 15)

    elif id == MonsterId.REPTOMANCER:
        buff()

    elif id == MonsterId.SHELLED_PARASITE:
            buff(14)
            addBlock(14)

    elif id == MonsterId.SNAKE_PLANT:
            buff(3)

    elif id == MonsterId.SPHERIC_GUARDIAN:
            # game adds barricade
            buff(3)
            buff()
            addBlock(40)

    elif id == MonsterId.SPIRE_SHIELD:
            bc.player.buff()
            buff(2 if asc18 else 1)

    elif id == MonsterId.SPIRE_SPEAR:
            buff(2 if asc18 else 1)

    elif id == MonsterId.THE_COLLECTOR:
        buff()


        # handle in MonsterGroup instead
        #        case MonsterId::JAW_WORM: {
        #            if (bc.act == 3) {
        #                const int str[] {3,4,5}
        #                buff<MS::STRENGTH>(str[hallwayDiffIdx])
        #            }
        #            break
        #        }

    elif id == MonsterId.LAGAVULIN:
        if hasStatus():
            buff(8)
            addBlock(8)

    elif (id == MonsterId.GREEN_LOUSE) or (id == MonsterId.RED_LOUSE):
            curlUpMin = 0
            curlUpMax = 0
            if asc17:
                curlUpMin = 9
                curlUpMax = 12
            elif asc7:
                curlUpMin = 4
                curlUpMax = 8
            else:
                curlUpMin = 3
                curlUpMax = 7
            buff(bc.monsterHpRng.random(curlUpMin, curlUpMax))

    elif id == MonsterId.SENTRY:
        buff(1)

    elif id == MonsterId.THE_GUARDIAN:
            # game adds ModeShiftPower
            d = 0
            if asc19:
                d = 40
            elif asc9:
                d = 35
            else:
                d = 30
            miscInfo = d
            buff(d)


def takeTurn(bc):
    asc = bc.ascension

    asc2 = bc.ascension >= 2
    asc3 = bc.ascension >= 3
    asc4 = bc.ascension >= 4
    asc9 = bc.ascension >= 9
    asc17 = bc.ascension >= 17
    asc18 = bc.ascension >= 18
    asc19 = bc.ascension >= 19
    hallwayIdx = getTriIdx(asc, 2, 17)
    eliteDiffIdx = getTriIdx(bc.ascension, 3, 18)
    bossDiffIdx = getTriIdx(bc.ascension, 4, 19)


        # ************ ACID_SLIME_L ************

    if moveHistory[0] == MMID.ACID_SLIME_L_CORROSIVE_SPIT:
        attackPlayerHelper(bc,12 if asc2 else 11)
        bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.SLIMED), 2))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.ACID_SLIME_L_LICK:
        bc.addToBot(Actions.DebuffPlayer(2, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.ACID_SLIME_L_SPLIT:
        largeSlimeSplit(bc, MonsterId.ACID_SLIME_M, idx, curHp)

    elif moveHistory[0] == MMID.ACID_SLIME_L_TACKLE:
        attackPlayerHelper(bc,18 if asc2 else 16)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.ACID_SLIME_M_CORROSIVE_SPIT:
        attackPlayerHelper(bc,8 if asc2 else 7)
        bc.addToBot(Actions.MakeTempCardInDiscard(CardId.SLIMED))
        bc.addToBot(Actions.RollMove(idx))

        # ************ ACID_SLIME_M ************

    elif moveHistory[0] == MMID.ACID_SLIME_M_LICK:
        bc.addToBot(Actions.DebuffPlayer(1, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.ACID_SLIME_M_TACKLE:
        attackPlayerHelper(bc,12 if asc2 else 10)
        bc.addToBot(Actions.RollMove(idx))

        # ************ ACID_SLIME_S ************

    elif moveHistory[0] == MMID.ACID_SLIME_S_LICK:
        bc.addToBot(Actions.DebuffPlayer(1, True))
        setMove(MMID.ACID_SLIME_S_TACKLE)

    elif moveHistory[0] == MMID.ACID_SLIME_S_TACKLE:
        attackPlayerHelper(bc,4 if asc2 else 3)
        setMove(MMID.ACID_SLIME_S_LICK)

        # ************ RED MASK BOIS ************

    elif moveHistory[0] == MMID.BEAR_BEAR_HUG:
        bc.player.debuff(-4 if asc17 else -2)
        setMove(MMID.BEAR_LUNGE)

    elif moveHistory[0] == MMID.BEAR_LUNGE:
        attackPlayerHelper(bc,10 if asc2 else 9)
        bc.addToBot(Actions.MonsterGainBlock(idx, 9))
        setMove(MMID.BEAR_MAUL)

    elif moveHistory[0] == MMID.BEAR_MAUL:
        attackPlayerHelper(bc,20 if asc2 else 18)
        setMove(MMID.BEAR_LUNGE)

    elif moveHistory[0] == MMID.POINTY_ATTACK:
        attackPlayerHelper(bc,6 if asc2 else 5, 2)

    elif moveHistory[0] == MMID.ROMEO_AGONIZING_SLASH:
        attackPlayerHelper(bc,12 if asc2 else 10)
        bc.addToBot(Actions.DebuffPlayer(3 if asc17 else 2, True))
        setMove(MMID.ROMEO_CROSS_SLASH)

    elif moveHistory[0] == MMID.ROMEO_CROSS_SLASH:
        attackPlayerHelper(bc,17 if asc2 else 15)
        setMove(MMID.ROMEO_AGONIZING_SLASH)

    elif moveHistory[0] == MMID.ROMEO_MOCK: # 2
        setMove(MMID.ROMEO_AGONIZING_SLASH)

        # ************ BLUE SLAVER ************

    elif moveHistory[0] == MMID.BLUE_SLAVER_RAKE:
        # 4
        attackPlayerHelper(bc,8 if asc2 else 7)
        bc.addToBot(Actions.DebuffPlayer(2 if asc17 else 1, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.BLUE_SLAVER_STAB:
        # 1
        attackPlayerHelper(bc,13 if asc2 else 12)
        bc.addToBot(Actions.RollMove(idx))

        # ************ BOOK OF STABBING ************

    elif moveHistory[0] == MMID.BOOK_OF_STABBING_MULTI_STAB:
        attackPlayerHelper(bc,7 if asc3 else 6, miscInfo)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.BOOK_OF_STABBING_SINGLE_STAB:
        attackPlayerHelper(bc,24 if asc3 else 21)
        bc.addToBot(Actions.RollMove(idx))


        # ************ BRONZE AUTOMATON ************


    elif moveHistory[0] == MMID.BRONZE_AUTOMATON_BOOST:
            buff(4 if asc4 else 3)
            addBlock(12 if asc9 else 9)
            lastBoostWasFlail = miscInfo
            if lastBoostWasFlail:
                setMove(MMID.BRONZE_AUTOMATON_HYPER_BEAM)
                lastBoostWasFlail = False
            else:
                setMove(MMID.BRONZE_AUTOMATON_FLAIL)
                lastBoostWasFlail = True
            bc.noOpRollMove()

    elif moveHistory[0] == MMID.BRONZE_AUTOMATON_FLAIL: # 1
        attackPlayerHelper(bc,8 if asc4 else 7, 2)
        setMove(MMID.BRONZE_AUTOMATON_BOOST)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.BRONZE_AUTOMATON_HYPER_BEAM: # 2
        attackPlayerHelper(bc,50 if asc4 else 45)
        if asc19:
            setMove(MMID.BRONZE_AUTOMATON_BOOST)
        else:
            setMove(MMID.BRONZE_AUTOMATON_STUNNED)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.BRONZE_AUTOMATON_SPAWN_ORBS: # 4
        spawnBronzeOrbs(bc)
        setMove(MMID.BRONZE_AUTOMATON_FLAIL)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.BRONZE_AUTOMATON_STUNNED: # 3
        setMove(MMID.BRONZE_AUTOMATON_FLAIL)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.BRONZE_ORB_BEAM:
        attackPlayerHelper(bc, 8)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.BRONZE_ORB_STASIS:
        stasisAction(bc)
        miscInfo = 1
        rollMove(bc)

    elif moveHistory[0] == MMID.BRONZE_ORB_SUPPORT_BEAM:
        bc.monsters.arr[1].addBlock(12)
        rollMove(bc)


        # ************ BYRD ************

    elif moveHistory[0] == MMID.BYRD_CAW:
        buff(1)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.BYRD_FLY:
        buff(4 if asc17 else 3)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.BYRD_HEADBUTT:
        attackPlayerHelper(bc, 3)
        setMove(MMID.BYRD_FLY)

    elif moveHistory[0] == MMID.BYRD_PECK:
        attackPlayerHelper(bc, 1,6 if asc2 else 5)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.BYRD_STUNNED:
        bc.noOpRollMove()
        setMove(MMID.BYRD_HEADBUTT)

    elif moveHistory[0] == MMID.BYRD_SWOOP:
        attackPlayerHelper(bc,14 if asc2 else 12)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.CENTURION_DEFEND:
            if bc.monsters.getAliveCount() > 1:
                mystic = bc.monsters.arr[1]
                mystic.addBlock(20 if asc17 else 15)
            rollMove(bc)

    elif moveHistory[0] == MMID.CENTURION_FURY:
        attackPlayerHelper(bc,7 if asc2 else 6, 3)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.CENTURION_SLASH:
        attackPlayerHelper(bc,14 if asc2 else 12)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.MYSTIC_ATTACK_DEBUFF:
            attackPlayerHelper(bc,9 if asc2 else 8)
            bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(2, True))
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.MYSTIC_BUFF:
            strAmts = [2, 3, 4]
            strBuff = strAmts[hallwayIdx]
            if bc.monsters.monstersAlive > 1:
                knight = bc.monsters.arr[0]
                knight.buff(strBuff)
            buff(strBuff)
            rollMove(bc)

    elif moveHistory[0] == MMID.MYSTIC_HEAL:
            healAmt = 20 if asc17 else 16
            if bc.monsters.monstersAlive > 1:
                knight = bc.monsters.arr[0]
                knight.heal(healAmt)
            heal(healAmt)
            rollMove(bc)


        # ************ CHOSEN ************

    elif moveHistory[0] == MMID.CHOSEN_DEBILITATE: # 3
        attackPlayerHelper(bc,12 if asc2 else 10)
        bc.addToBot(Actions.DebuffPlayer(2, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.CHOSEN_DRAIN: # 2
        bc.addToBot(Actions.DebuffPlayer(3, True))
        buff(3)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.CHOSEN_HEX: # 4
        bc.addToBot(Actions.DebuffPlayer(1))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.CHOSEN_POKE: # 5
        attackPlayerHelper(bc,6 if asc2 else 5, 2)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.CHOSEN_ZAP: # 1
        attackPlayerHelper(bc,21 if asc2 else 18)
        bc.addToBot(Actions.RollMove(idx))

        # ************ FAT GREMLIN ************

    elif moveHistory[0] == MMID.FAT_GREMLIN_SMASH:
            attackPlayerHelper(bc,5 if asc2 else 4)
            bc.addToBot(Actions.DebuffPlayer(1, True))
            if asc17:
                bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(1, True))

            if doesEscapeNext():
                setMove(MMID.GENERIC_ESCAPE_MOVE)
            else:
                bc.addToBot(Actions.NoOpRollMove())

    elif moveHistory[0] == MMID.MAD_GREMLIN_SCRATCH:
            attackPlayerHelper(bc,5 if asc2 else 4)
            if doesEscapeNext():
                setMove(MMID.GENERIC_ESCAPE_MOVE)
            else:
                bc.addToBot(Actions.NoOpRollMove())

    elif moveHistory[0] == MMID.SNEAKY_GREMLIN_PUNCTURE:
            attackPlayerHelper(bc,10 if asc2 else 9)
            if doesEscapeNext():
                setMove(MMID.GENERIC_ESCAPE_MOVE)

    elif moveHistory[0] == MMID.CULTIST_DARK_STRIKE:
        attackPlayerHelper(bc, 6)
        bc.addToBot(Actions.NoOpRollMove())

    elif moveHistory[0] == MMID.CULTIST_INCANTATION:
            ritualAmount = [3, 4, 5]
            buff<MS.RITUAL>(ritualAmount[hallwayIdx])
            setMove(MMID.CULTIST_DARK_STRIKE)
            bc.noOpRollMove()

        # ************ FUNGI BEAST ************

    elif moveHistory[0] == MMID.FUNGI_BEAST_BITE:
        attackPlayerHelper(bc, 6)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.FUNGI_BEAST_GROW:
            strengthBuff = [3, 4, 5]
            buff(strengthBuff[hallwayIdx])
            bc.addToBot(Actions.RollMove(idx))

        # ************ GREMLIN LEADER ************

        #        
        #         *  Gremlin Leader always lives in the 4th monster slot (idx=3)
        #         *  Up to 3 minions can be alive at the same time
        #         

    elif moveHistory[0] == MMID.GREMLIN_LEADER_ENCOURAGE:
            strBuff = [3, 4, 5]
            strGain = strBuff[eliteDiffIdx]

            bc.aiRng.random(0, 2) # for in game quote
            # buff all monsters
            # not going to use action queue here, doesn't seem necessary
            for i in range(0, 3):
                minion = bc.monsters.arr[i]
                if not minion.isDying():
                    minion.buff(strGain)
                    minion.addBlock(10 if asc3 else 6)
            buff(strGain)
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.GREMLIN_LEADER_RALLY:
            # summon two gremlins in open slots
            bc.addToBot(Actions.SummonGremlins())
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.GREMLIN_LEADER_STAB:
            attackPlayerHelper(bc, 6, 3)
            bc.addToBot(Actions.RollMove(idx))

        # ************ GREEN LOUSE ************

    elif moveHistory[0] == MMID.GREEN_LOUSE_BITE:
        attackPlayerHelper(bc, miscInfo)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.GREEN_LOUSE_SPIT_WEB:
        bc.addToBot(Actions.DebuffPlayer(2)) # isSourceMonster true
        bc.addToBot(Actions.RollMove(idx))

        # ************ GREMLIN NOB ************

    elif moveHistory[0] == MMID.GREMLIN_NOB_BELLOW:
        buff(3 if asc18 else 2)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.GREMLIN_NOB_RUSH:
        attackPlayerHelper(bc,16 if asc3 else 14)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.GREMLIN_NOB_SKULL_BASH:
        attackPlayerHelper(bc,8 if asc3 else 6)
        bc.addToBot(Actions.DebuffPlayer(2, True))
        bc.addToBot(Actions.RollMove(idx))

        # ************ GREMLIN WIZARD ************

    elif moveHistory[0] == MMID.GREMLIN_WIZARD_CHARGING:
            miscInfo += 1
            if miscInfo == 3:
                setMove(MMID.GREMLIN_WIZARD_ULTIMATE_BLAST)

    elif moveHistory[0] == MMID.GREMLIN_WIZARD_ULTIMATE_BLAST:
            attackPlayerHelper(bc,30 if asc2 else 25)
            if not asc17:
                miscInfo = 0 # gremlin wizard charge
                setMove(MMID.GREMLIN_WIZARD_CHARGING)

        # ************ HEXAGHOST ************

    elif moveHistory[0] == MMID.HEXAGHOST_ACTIVATE:
            miscInfo = math.trunc(bc.player.curHp / float(12)) + 1 # set divider damage
            setMove(MMID.HEXAGHOST_DIVIDER)
            bc.noOpRollMove()

    elif moveHistory[0] == MMID.HEXAGHOST_DIVIDER: # 1
        attackPlayerHelper(bc, miscInfo, 6)
        uniquePower0 = 0
        setMove(MMID.HEXAGHOST_SEAR)
        bc.addToBot(Actions.NoOpRollMove())

    elif moveHistory[0] == MMID.HEXAGHOST_INFERNO: # 6
        attackPlayerHelper(bc,3 if asc4 else 2, 6)
        uniquePower0 = 0
        setMove(MMID.HEXAGHOST_SEAR)
        bc.addToBot(Actions.NoOpRollMove())

    elif moveHistory[0] == MMID.HEXAGHOST_INFLAME: # 3
        addBlock(12)
        buff(3 if asc19 else 2)
        uniquePower0 += 1
        setMove(MMID.HEXAGHOST_TACKLE)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.HEXAGHOST_SEAR: # 4
        attackPlayerHelper(bc, 6)
        bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.BURN, bc.turn > 8),2 if asc19 else 1))
        if uniquePower0 == 0:
            setMove(MMID.HEXAGHOST_TACKLE)

        elif uniquePower0 == 2:
            setMove(MMID.HEXAGHOST_INFLAME)

        else:
            setMove(MMID.HEXAGHOST_INFERNO)
        uniquePower0 += 1
        bc.addToBot(Actions.NoOpRollMove())

    elif moveHistory[0] == MMID.HEXAGHOST_TACKLE: # 2
        attackPlayerHelper(bc,6 if asc4 else 5, 2)
        setMove(MMID.HEXAGHOST_SEAR)
        uniquePower0 += 1
        bc.addToBot(Actions.NoOpRollMove())


        # ************ JAW WORM ************

    elif moveHistory[0] == MMID.JAW_WORM_CHOMP:
        attackPlayerHelper(bc,12 if asc2 else 11)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.JAW_WORM_BELLOW:
            strengthBuff = [3, 4, 5]
            buff(strengthBuff[hallwayIdx])
            bc.addToBot(Actions.MonsterGainBlock(idx,9 if asc17 else 6))
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.JAW_WORM_THRASH:
        attackPlayerHelper(bc, 7)
        bc.addToBot(Actions.MonsterGainBlock(idx, 5))
        bc.addToBot(Actions.RollMove(idx))

        # ************ LAGAVULIN ************

    elif moveHistory[0] == MMID.LAGAVULIN_ATTACK:
        attackPlayerHelper(bc,20 if asc3 else 18)
        if lastTwoMoves(MMID.LAGAVULIN_ATTACK):
            setMove(MMID.LAGAVULIN_SIPHON_SOUL)
        else:
            setMove(MMID.LAGAVULIN_ATTACK)
        bc.addToBot(Actions.NoOpRollMove())

    elif moveHistory[0] == MMID.LAGAVULIN_SIPHON_SOUL:
        Actions.DebuffPlayer(-2 if asc18 else -1).actFunc.invoke(bc)
        Actions.DebuffPlayer(-2 if asc18 else -1).actFunc.invoke(bc)
        setMove(MMID.LAGAVULIN_ATTACK)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.LAGAVULIN_SLEEP:
        if bc.turn == 2 or not hasStatus():
            setMove(MMID.LAGAVULIN_ATTACK)
        else:
            setMove(MMID.LAGAVULIN_SLEEP)
        bc.noOpRollMove()

        # ************ LOOTER ************

    elif moveHistory[0] == MMID.LOOTER_ESCAPE:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert curHp > 0
##endif
            isEscapingB = True
            bc.monsters.monstersAlive -= 1
            if bc.monsters.getAliveCount() == 0:
                bc.outcome = Outcome.PLAYER_VICTORY

    elif moveHistory[0] == MMID.LOOTER_LUNGE:
            stealGoldFromPlayer(bc, getStatus())
            attackPlayerHelper(bc,14 if asc2 else 12)
            setMove(MMID.LOOTER_SMOKE_BOMB)

    elif moveHistory[0] == MMID.LOOTER_MUG:
            if bc.getMonsterTurnNumber() == 1:
                bc.aiRng.randomBoolean(0.6) # for a dialog message in game
            stealGoldFromPlayer(bc, getStatus())
            attackPlayerHelper(bc,11 if asc2 else 10)
            if bc.getMonsterTurnNumber() == 1:
                setMove(MMID.LOOTER_MUG)

            else:
                nextMove = MMID.LOOTER_SMOKE_BOMB if bc.aiRng.randomBoolean(0.5) else MMID.LOOTER_LUNGE

                setMove(nextMove)

    elif moveHistory[0] == MMID.LOOTER_SMOKE_BOMB:
            addBlock(6)
            setMove(MMID.LOOTER_ESCAPE)

        # ************ MUGGER ************

    elif moveHistory[0] == MMID.MUGGER_ESCAPE:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            assert curHp > 0
##endif
            isEscapingB = True
            bc.monsters.monstersAlive -= 1
            if bc.monsters.getAliveCount() == 0:
                bc.outcome = Outcome.PLAYER_VICTORY

    elif moveHistory[0] == MMID.MUGGER_LUNGE:
            bc.aiRng.random(2) # for a dialog message in gam
            stealGoldFromPlayer(bc, getStatus())
            attackPlayerHelper(bc,18 if asc2 else 16)
            setMove(MMID.MUGGER_SMOKE_BOMB)

    elif moveHistory[0] == MMID.MUGGER_MUG:
            bc.aiRng.random(2) # for a dialog message in game
            if bc.getMonsterTurnNumber() == 2:
                bc.aiRng.randomBoolean(0.6) # for a dialog message in game
            stealGoldFromPlayer(bc, getStatus())
            attackPlayerHelper(bc,11 if asc2 else 10)

            if bc.getMonsterTurnNumber() == 2:
                nextMove = MMID.MUGGER_SMOKE_BOMB if bc.aiRng.randomBoolean(0.5) else MMID.MUGGER_LUNGE

                setMove(nextMove)

            else:
                setMove(MMID.MUGGER_MUG)

    elif moveHistory[0] == MMID.MUGGER_SMOKE_BOMB:
            addBlock(17 if asc17 else 11)
            setMove(MMID.MUGGER_ESCAPE)

    elif moveHistory[0] == MMID.ORB_WALKER_CLAW: # 2
        attackPlayerHelper(bc,16 if asc2 else 15)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.ORB_WALKER_LASER:
            attackPlayerHelper(bc,11 if asc2 else 10)
            bc.addToBot(Actions.ShuffleTempCardIntoDrawPile(CardId.BURN, 1))
            bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.BURN)))
            bc.addToBot(Actions.RollMove(idx))

        # ************ RED LOUSE ************

    elif moveHistory[0] == MMID.RED_LOUSE_BITE:
        attackPlayerHelper(bc, miscInfo)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.RED_LOUSE_GROW:
        buff(4 if asc17 else 3)
        bc.addToBot(Actions.RollMove(idx))

        # ************ RED SLAVER ************

    elif moveHistory[0] == MMID.RED_SLAVER_ENTANGLE:
        bc.addToBot(Actions.DebuffPlayer(1))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.RED_SLAVER_SCRAPE:
        attackPlayerHelper(bc,9 if asc2 else 8)
        bc.addToBot(Actions.DebuffPlayer(2 if asc17 else 1))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.RED_SLAVER_STAB:
        attackPlayerHelper(bc,14 if asc2 else 13)
        bc.addToBot(Actions.RollMove(idx))

        # ************ SENTRY ************

    elif moveHistory[0] == MMID.SENTRY_BEAM:
        attackPlayerHelper(bc,10 if asc3 else 9)
        setMove(MMID.SENTRY_BOLT)
        bc.addToBot(Actions.NoOpRollMove())

    elif moveHistory[0] == MMID.SENTRY_BOLT:
        bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.DAZED),3 if asc18 else 2))
        setMove(MMID.SENTRY_BEAM)
        bc.addToBot(Actions.NoOpRollMove())


        # ************ SHELLED PARASITE ************

    elif moveHistory[0] == MMID.SHELLED_PARASITE_DOUBLE_STRIKE: # 2
        attackPlayerHelper(bc,7 if asc2 else 6, 2)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SHELLED_PARASITE_FELL: # 1
        attackPlayerHelper(bc,21 if asc2 else 18)
        bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(2, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SHELLED_PARASITE_STUNNED: # 4
        setMove(MMID.SHELLED_PARASITE_FELL)
        rollMove(bc)

    elif moveHistory[0] == MMID.SHELLED_PARASITE_SUCK: # 3
        bc.addToBot(Actions.VampireAttack(calculateDamageToPlayer(bc,12 if asc2 else 10)))
        bc.addToBot(Actions.RollMove(idx))

        # ************ SHIELD GREMLIN ************

    elif moveHistory[0] == MMID.SHIELD_GREMLIN_PROTECT:
            blockAmounts = [7, 8, 11]
            blockAmount = blockAmounts[getTriIdx(asc, 7, 17)]
            bc.addToBot(Actions.GainBlockRandomEnemy(idx, blockAmount))
            if bc.monsters.getAliveCount() <= 1:
                setMove(MMID.SHIELD_GREMLIN_SHIELD_BASH)

    elif moveHistory[0] == MMID.SHIELD_GREMLIN_SHIELD_BASH:
        attackPlayerHelper(bc,8 if asc2 else 6)

        # ************ SLIME BOSS ************

    elif moveHistory[0] == MMID.SLIME_BOSS_GOOP_SPRAY:
        Actions.MakeTempCardInDiscard(CardInstance(CardId.SLIMED),5 if asc19 else 3).actFunc.invoke(bc)
        setMove(MMID.SLIME_BOSS_PREPARING)

    elif moveHistory[0] == MMID.SLIME_BOSS_PREPARING:
        setMove(MMID.SLIME_BOSS_SLAM)

    elif moveHistory[0] == MMID.SLIME_BOSS_SLAM:
        attackPlayerHelper(bc,38 if asc4 else 35)
        setMove(MMID.SLIME_BOSS_GOOP_SPRAY) # the attack is executed after, which is critical

    elif moveHistory[0] == MMID.SLIME_BOSS_SPLIT:
        slimeBossSplit(bc, curHp)

        # ************ SNAKE PLANT ************

    elif moveHistory[0] == MMID.SNAKE_PLANT_CHOMP:
        attackPlayerHelper(bc,8 if asc2 else 7, 3)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SNAKE_PLANT_ENFEEBLING_SPORES:
        bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(2, True))
        bc.addToBot(Actions.DebuffPlayer(2, True))
        bc.addToBot(Actions.RollMove(idx))


        # ************ SNECKO ************

    elif moveHistory[0] == MMID.SNECKO_BITE: # 2
        attackPlayerHelper(bc,18 if asc2 else 15)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SNECKO_PERPLEXING_GLARE: # 1
        bc.addToBot(Actions.DebuffPlayer())
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SNECKO_TAIL_WHIP: # 3
        attackPlayerHelper(bc,10 if asc2 else 8)
        bc.addToBot(Actions.DebuffPlayer(2, True))
        if asc17:
            bc.addToBot(Actions.DebuffPlayer(2, True))
        bc.addToBot(Actions.RollMove(idx))

        # ************ SPHERIC_GUARDIAN ************

    elif moveHistory[0] == MMID.SPHERIC_GUARDIAN_ACTIVATE: # 2
        addBlock(35 if asc17 else 25)
        setMove(MMID.SPHERIC_GUARDIAN_ATTACK_DEBUFF)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.SPHERIC_GUARDIAN_ATTACK_DEBUFF: # 4
        attackPlayerHelper(bc,11 if asc2 else 10)
        bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(5, True))
        setMove(MMID.SPHERIC_GUARDIAN_SLAM)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.SPHERIC_GUARDIAN_HARDEN: # 3
        bc.addToBot(Actions.MonsterGainBlock(idx, 15))
        attackPlayerHelper(bc,11 if asc2 else 10)
        setMove(MMID.SPHERIC_GUARDIAN_SLAM)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.SPHERIC_GUARDIAN_SLAM: # 1
        attackPlayerHelper(bc,11 if asc2 else 10, 2)
        setMove(MMID.SPHERIC_GUARDIAN_HARDEN)
        bc.noOpRollMove()

        # ************ SPIKE SLIME M ************

    elif moveHistory[0] == MMID.SPIKE_SLIME_M_LICK:
            bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(1))
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SPIKE_SLIME_M_FLAME_TACKLE:
            attackPlayerHelper(bc,10 if asc2 else 8)
            bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.SLIMED)))
            bc.addToBot(Actions.RollMove(idx))

        # ************ SPIKE SLIME L ************

    elif moveHistory[0] == MMID.SPIKE_SLIME_L_FLAME_TACKLE:
        attackPlayerHelper(bc,18 if asc2 else 16)
        bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.SLIMED), 2))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SPIKE_SLIME_L_LICK: # 4
        bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(3 if asc17 else 2, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SPIKE_SLIME_L_SPLIT: # 3
        largeSlimeSplit(bc, MonsterId.SPIKE_SLIME_M, idx, curHp)

        # ************ SPIKE SLIME S ************

    elif moveHistory[0] == MMID.SPIKE_SLIME_S_TACKLE:
            attackPlayerHelper(bc,6 if asc2 else 5)
            bc.addToBot(Actions.NoOpRollMove())

        # ************ TASKMASTER ************

    elif moveHistory[0] == MMID.TASKMASTER_SCOURING_WHIP: # todo buff after calculating damage so no need to add to bot?
        attackPlayerHelper(bc, 7)
        if asc18:
            bc.addToBot(Actions.BuffEnemy(idx, 1))
            bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.WOUND), 3))

        elif asc3:
            bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.WOUND), 2))

        else:
            bc.addToBot(Actions.MakeTempCardInDiscard(CardInstance(CardId.WOUND)))
        bc.noOpRollMove()

        # ************ THE CHAMP ************

    elif moveHistory[0] == MMID.THE_CHAMP_ANGER:
            strAmts = [6, 9, 12]
            removeDebuffs()
            buff(strAmts[bossDiffIdx])
            rollMove(bc)

    elif moveHistory[0] == MMID.THE_CHAMP_DEFENSIVE_STANCE:
            blockAmts = [15, 18, 20]
            metallicizeAmts = [5, 6, 7]
            buffIdx = getTriIdx(bc.ascension, 9, 19)

            blockAmt = blockAmts[buffIdx]
            metallicizeAmt = metallicizeAmts[buffIdx]

            addBlock(blockAmt)
            buff(metallicizeAmt)

            rollMove(bc)

    elif moveHistory[0] == MMID.THE_CHAMP_EXECUTE:
            attackPlayerHelper(bc, 10, 2)
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.THE_CHAMP_FACE_SLAP:
            attackPlayerHelper(bc,14 if asc4 else 12)
            bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(2, True))
            bc.addToBot(Actions.DebuffPlayer(2, True))
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.THE_CHAMP_GLOAT:
            strAmts = [3, 4, 5]
            buff(strAmts[bossDiffIdx])
            rollMove(bc)

    elif moveHistory[0] == MMID.THE_CHAMP_HEAVY_SLASH:
            attackPlayerHelper(bc,18 if asc4 else 16)
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.THE_CHAMP_TAUNT:
            bc.player.debuff(2, True)
            bc.player.debuff(2, True)
            rollMove(bc)

        # ************ THE COLLECTOR ************

    elif moveHistory[0] == MMID.THE_COLLECTOR_BUFF:
            strAmounts = [3, 4, 5]
            blockAmounts = [15, 18, 23]

            for i in range(0, 2):
                torchHead = bc.monsters.arr[i]
                if not torchHead.isDying():
                    torchHead.buff(strAmounts[bossDiffIdx])
            buff(strAmounts[bossDiffIdx])
            addBlock(blockAmounts[bossDiffIdx])

            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.THE_COLLECTOR_FIREBALL: # 2
        attackPlayerHelper(bc,21 if asc4 else 18)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.THE_COLLECTOR_MEGA_DEBUFF: # 4
        bc.addToBot(Actions.DebuffPlayer(3, True))
        bc.addToBot(Actions.DebuffPlayer(3, True))
        bc.addToBot(Actions.DebuffPlayer<PlayerStatus.FRAIL>(3, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.THE_COLLECTOR_SPAWN: # 5, 1(initial spawn)
        bc.addToBot(Actions.SpawnTorchHeads())
        bc.addToBot(Actions.RollMove(idx))

        # ************ THE GUARDIAN ************

    elif moveHistory[0] == MMID.THE_GUARDIAN_CHARGING_UP:
        addBlock(9)
        setMove(MMID.THE_GUARDIAN_FIERCE_BASH)

    elif moveHistory[0] == MMID.THE_GUARDIAN_DEFENSIVE_MODE:
        buff(4 if asc19 else 3)
        setMove(MMID.THE_GUARDIAN_ROLL_ATTACK)

    elif moveHistory[0] == MMID.THE_GUARDIAN_FIERCE_BASH:
        attackPlayerHelper(bc,36 if asc4 else 32)
        setMove(MMID.THE_GUARDIAN_VENT_STEAM)

    elif moveHistory[0] == MMID.THE_GUARDIAN_ROLL_ATTACK:
        attackPlayerHelper(bc,10 if asc4 else 9)
        setMove(MMID.THE_GUARDIAN_TWIN_SLAM)

    elif moveHistory[0] == MMID.THE_GUARDIAN_TWIN_SLAM:
        attackPlayerHelper(bc, 8, 2)
        removeStatus()
        miscInfo += 10
        setMove(MMID.THE_GUARDIAN_WHIRLWIND)
        bc.addToBot(Actions.BuffEnemy(idx, miscInfo))

    elif moveHistory[0] == MMID.THE_GUARDIAN_VENT_STEAM:
        bc.addToBot(Actions.DebuffPlayer(2, True))
        bc.addToBot(Actions.DebuffPlayer(2, True))
        setMove(MMID.THE_GUARDIAN_WHIRLWIND)

    elif moveHistory[0] == MMID.THE_GUARDIAN_WHIRLWIND:
        attackPlayerHelper(bc, 5, 4)
        setMove(MMID.THE_GUARDIAN_CHARGING_UP)


        # ************ TORCH HEAD ************

    elif moveHistory[0] == MMID.TORCH_HEAD_TACKLE:
        attackPlayerHelper(bc, 7)

        # ************ SHAPES ************

    elif moveHistory[0] == MMID.EXPLODER_EXPLODE:
        bc.addToBot(Actions.DamagePlayer(30))
        bc.addToBot(Actions.SuicideAction(idx, True))
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.EXPLODER_SLAM: # 1
        attackPlayerHelper(bc,11 if asc2 else 9)
        if lastTwoMoves(MMID.EXPLODER_SLAM):
            setMove(MMID.EXPLODER_EXPLODE)
        else:
            setMove(MonsterMoveId.EXPLODER_SLAM)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.REPULSOR_BASH: # 2
        attackPlayerHelper(bc,13 if asc2 else 11)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.REPULSOR_REPULSE: # 1
        Actions.ShuffleTempCardIntoDrawPile(CardId.DAZED, 2).actFunc.invoke(bc)
        rollMove(bc)

    elif moveHistory[0] == MMID.SPIKER_CUT: # 1
        attackPlayerHelper(bc,9 if asc2 else 7)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SPIKER_SPIKE: # 2
        miscInfo += 1 # used thorns count
        buff(2)
        rollMove(bc)


        # ************ THE MAW ************

    elif moveHistory[0] == MMID.THE_MAW_DROOL: # 4
        buff(5 if asc17 else 3)
        rollMove(bc)

    elif moveHistory[0] == MMID.THE_MAW_NOM:
            t = math.trunc((bc.getMonsterTurnNumber() + 1) / float(2))
            attackPlayerHelper(bc, 5, t)
            setMove(MMID.THE_MAW_DROOL)
            bc.noOpRollMove()

    elif moveHistory[0] == MMID.THE_MAW_ROAR:
            bc.player.debuff(5 if asc17 else 3, True)
            bc.player.debuff<PlayerStatus.FRAIL>(5 if asc17 else 3, True)
            rollMove(bc)

    elif moveHistory[0] == MMID.THE_MAW_SLAM: # 3
        attackPlayerHelper(bc,30 if asc2 else 25)
        bc.addToBot(Actions.RollMove(idx))

        # ************ DARKLING ************

    elif moveHistory[0] == MMID.DARKLING_CHOMP:
        attackPlayerHelper(bc,9 if asc2 else 8)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.DARKLING_HARDEN:
        addBlock(12)
        if asc17:
            buff(2)
        rollMove(bc)

    elif moveHistory[0] == MMID.DARKLING_NIP:
            damage = miscInfo + (2 if asc2 else 0) # todo maybe make d part of the miscInfo at prebattle
            attackPlayerHelper(bc, damage)
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.DARKLING_REGROW:
        # do nothing
        rollMove(bc)

    elif moveHistory[0] == MMID.DARKLING_REINCARNATE:
        # revive with 50% hp
        # todo does it heep its buffs and debuffs?
# C++ TO PYTHON CONVERTER TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        curHp = maxHp / 2
        halfDead = False
        bc.monsters.monstersAlive += 1

        buff()
        if bc.player.hasRelic():
            buff(1)

        rollMove(bc)

        # ************ SPIRE GROWTH ************

    elif moveHistory[0] == MMID.SPIRE_GROWTH_QUICK_TACKLE: # 1
        attackPlayerHelper(bc,18 if asc2 else 16)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SPIRE_GROWTH_SMASH: # 3
        attackPlayerHelper(bc,25 if asc2 else 22)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SPIRE_GROWTH_CONSTRICT: # 2
        bc.player.debuff(12 if asc17 else 10)
        bc.addToBot(Actions.RollMove(idx))

        # ************ TRANSIENT ************

    elif moveHistory[0] == MMID.TRANSIENT_ATTACK:

            damage = (40 if asc2 else 30) + 10*(bc.getMonsterTurnNumber()-1)
            attackPlayerHelper(bc, damage)
            if getStatus() == 1:
                bc.addToBot(Actions.SuicideAction(idx, False))
            bc.noOpRollMove()
            decrementStatus()

        # ************ WRITHING MASS ************

    elif moveHistory[0] == MMID.WRITHING_MASS_FLAIL: # 2
        attackPlayerHelper(bc,16 if asc2 else 15)
        bc.addToBot(Actions.MonsterGainBlock(idx,18 if asc2 else 16))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.WRITHING_MASS_IMPLANT: # 4
        miscInfo = True
        if not bc.player.hasRelic():
            if bc.player.hasRelic():
                bc.player.increaseMaxHp(6)
        rollMove(bc)

    elif moveHistory[0] == MMID.WRITHING_MASS_MULTI_STRIKE: # 1
        attackPlayerHelper(bc,9 if asc2 else 7, 3)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.WRITHING_MASS_STRONG_STRIKE: # 0
        attackPlayerHelper(bc,38 if asc2 else 32)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.WRITHING_MASS_WITHER: # 3
        attackPlayerHelper(bc,12 if asc2 else 10)
        bc.addToBot(Actions.DebuffPlayer(2, True))
        bc.addToBot(Actions.DebuffPlayer(2, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.GIANT_HEAD_COUNT: # 3
        attackPlayerHelper(bc, 13)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.GIANT_HEAD_GLARE: # 1
        bc.player.debuff(1, True)
        rollMove(bc)

    elif moveHistory[0] == MMID.GIANT_HEAD_IT_IS_TIME:
            t = min(bc.getMonsterTurnNumber()-5, 6) * 5
            damage = (40 if asc3 else 30) + t
            attackPlayerHelper(bc, damage) # todo this can be done immediately
            bc.noOpRollMove()

    elif moveHistory[0] == MMID.NEMESIS_ATTACK:
        attackPlayerHelper(bc,7 if asc3 else 6, 3)
        bc.addToBot(Actions.RollMove(idx))
        if not hasStatus():
            bc.addToBot(Actions.BuffEnemy(idx, 2))

    elif moveHistory[0] == MMID.NEMESIS_DEBUFF:
        Actions.MakeTempCardInDiscard(CardInstance(CardId.BURN),5 if asc3 else 3).actFunc.invoke(bc)
        rollMove(bc)
        if not hasStatus():
            buff(2)

    elif moveHistory[0] == MMID.NEMESIS_SCYTHE:
        attackPlayerHelper(bc, 45)
        bc.addToBot(Actions.RollMove(idx))
        if not hasStatus():
            bc.addToBot(Actions.BuffEnemy(idx, 2))

    elif moveHistory[0] == MMID.REPTOMANCER_BIG_BITE: # 3
        attackPlayerHelper(bc,34 if asc3 else 30)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.REPTOMANCER_SNAKE_STRIKE: # 1
        attackPlayerHelper(bc,16 if asc3 else 13, 2)
        bc.addToBot(Actions.DebuffPlayer(1, True))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.REPTOMANCER_SUMMON: # 2
        reptomancerSummon(bc,2 if asc18 else 1)
        rollMove(bc)

    elif moveHistory[0] == MMID.DAGGER_STAB:
        attackPlayerHelper(bc, 9)
        bc.addToBot(Actions.MakeTempCardInDiscard(CardId.WOUND))
        setMove(MMID.DAGGER_EXPLODE)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.DAGGER_EXPLODE:
        attackPlayerHelper(bc, 25)
        bc.addToBot(Actions.SuicideAction(idx, True))
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.TIME_EATER_HASTE:
        miscInfo = True # set have used haste true
# C++ TO PYTHON CONVERTER TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        curHp = maxHp / 2
        if asc19:
            addBlock(32)
        removeDebuffs() # also removes shackled here
        rollMove(bc)

    elif moveHistory[0] == MMID.TIME_EATER_HEAD_SLAM:
        attackPlayerHelper(bc,32 if asc4 else 26)
        bc.addToBot(Actions.DebuffPlayer(1, True))
        if asc19:
            bc.addToBot(Actions.MakeTempCardInDiscard(CardId.SLIMED, 2))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.TIME_EATER_REVERBERATE:
        attackPlayerHelper(bc,8 if asc4 else 7, 3)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.TIME_EATER_RIPPLE: # 3
        addBlock(20)
        bc.player.debuff(1, True)
        bc.player.debuff(1, True)
        if asc19:
            bc.player.debuff<PlayerStatus.FRAIL>(1, True)
        rollMove(bc)

    elif moveHistory[0] == MMID.DONU_BEAM:
        attackPlayerHelper(bc,12 if asc4 else 10, 2)
        setMove(MonsterMoveId.DONU_CIRCLE_OF_POWER)

    elif moveHistory[0] == MMID.DONU_CIRCLE_OF_POWER:
        bc.monsters.arr[0].buff(3) # shouldn't matter if deca is dead
        buff(3)
        setMove(MonsterMoveId.DONU_BEAM)

    elif moveHistory[0] == MMID.DECA_BEAM:
        attackPlayerHelper(bc,12 if asc4 else 10, 2)
        bc.addToBot(Actions.MakeTempCardInDiscard(CardId.DAZED, 2))
        setMove(MonsterMoveId.DECA_SQUARE_OF_PROTECTION)

    elif moveHistory[0] == MMID.DECA_SQUARE_OF_PROTECTION:
            deca = self
            donu = bc.monsters.arr[1]
            deca.addBlock(16)
            donu.addBlock(16)
            if asc19:
                deca.buff(3)
                donu.buff(3)
            setMove(MonsterMoveId.DECA_BEAM)

    elif moveHistory[0] == MMID.AWAKENED_ONE_DARK_ECHO:
        if halfDead:
            std::cerr << bc << std::endl
            False = assert()
        attackPlayerHelper(bc, 40)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.AWAKENED_ONE_REBIRTH:
            maxHp = 320 if asc9 else 300
            curHp = maxHp
            halfDead = False
            miscInfo = True
            strength = max(0,strength)
            bc.monsters.monstersAlive += 1
            buff()
            setMove(MonsterMoveId.AWAKENED_ONE_DARK_ECHO)
            bc.noOpRollMove()

    elif moveHistory[0] == MMID.AWAKENED_ONE_SLASH:
        if halfDead:
            std::cerr << bc << std::endl
            False = assert()
        attackPlayerHelper(bc, 20)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.AWAKENED_ONE_SLUDGE:
        if halfDead:
            std::cerr << bc << std::endl
            False = assert()
        attackPlayerHelper(bc, 18)
        bc.addToBot(Actions.ShuffleTempCardIntoDrawPile(CardId.VOID))
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.AWAKENED_ONE_SOUL_STRIKE:
        if halfDead:
            std::cerr << bc << std::endl
            False = assert()
        attackPlayerHelper(bc, 6, 4)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.AWAKENED_ONE_TACKLE:
        if halfDead:
            std::cerr << bc << std::endl
            False = assert()
        attackPlayerHelper(bc, 10, 3)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SPIRE_SHIELD_BASH: # 1
        attackPlayerHelper(bc,14 if asc3 else 12)
        if bc.player.orbSlots > 0:
            bc.addToBot(Actions.SpireShieldDebuff())
        else:
            bc.player.debuff(-1)
        if lastMoveBefore(MonsterMoveId.SPIRE_SHIELD_SMASH) or lastMoveBefore(MonsterMoveId.INVALID):
            setMove(MonsterMoveId.SPIRE_SHIELD_FORTIFY)
        else:
            setMove(MonsterMoveId.SPIRE_SHIELD_SMASH)
        bc.noOpRollMove()


    elif moveHistory[0] == MMID.SPIRE_SHIELD_FORTIFY: # 2
        addBlock(30)
        bc.monsters.arr[1].addBlock(30)
        if lastMoveBefore(MonsterMoveId.SPIRE_SHIELD_SMASH) or lastMoveBefore(MonsterMoveId.INVALID):
            setMove(MonsterMoveId.SPIRE_SHIELD_BASH)
        else:
            setMove(MonsterMoveId.SPIRE_SHIELD_SMASH)
        bc.noOpRollMove()


    elif moveHistory[0] == MMID.SPIRE_SHIELD_SMASH:
            damageOutput = calculateDamageToPlayer(bc,38 if asc3 else 34)
            bc.addToBot(Actions.AttackPlayer(idx, auto(damageOutput)))
            bc.addToBot(Actions.MonsterGainBlock(idx,99 if asc18 else damageOutput))
            bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.SPIRE_SPEAR_BURN_STRIKE: # 1
        attackPlayerHelper(bc,6 if asc3 else 5, 2)
        if asc18:
            bc.addToBot(Actions.MakeTempCardInDrawPile(CardId.BURN, 2, False))
        else:
            bc.addToBot(Actions.MakeTempCardInDiscard(CardId.BURN, 2))
        if lastMoveBefore(MonsterMoveId.SPIRE_SPEAR_SKEWER):
            setMove(MonsterMoveId.SPIRE_SPEAR_PIERCER)
        else:
            setMove(MonsterMoveId.SPIRE_SPEAR_SKEWER)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.SPIRE_SPEAR_PIERCER: # 2
        buff(2)
        bc.monsters.arr[0].buff(2)
        if lastMoveBefore(MonsterMoveId.SPIRE_SPEAR_SKEWER):
            setMove(MonsterMoveId.SPIRE_SPEAR_BURN_STRIKE)
        else:
            setMove(MonsterMoveId.SPIRE_SPEAR_SKEWER)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.SPIRE_SPEAR_SKEWER: # 3
        attackPlayerHelper(bc, 10,4 if asc3 else 3)
        bc.addToBot(Actions.RollMove(idx))

    elif moveHistory[0] == MMID.CORRUPT_HEART_BLOOD_SHOTS: # 1
        attackPlayerHelper(bc, 2,15 if asc4 else 12)
        if math.fmod(bc.getMonsterTurnNumber(), 3) == 0:
            setMove(MonsterMoveId.CORRUPT_HEART_BUFF)
        else:
            setMove(MonsterMoveId.CORRUPT_HEART_ECHO)
        bc.noOpRollMove()

    elif moveHistory[0] == MMID.CORRUPT_HEART_BUFF:
            # remove negative str and buff 2
            newStr = max(0, getStatus()) + 2
            setStatus(newStr)
            buffCount = math.trunc(bc.getMonsterTurnNumber() / float(3))
            if buffCount == 1:
                buff(2)
            elif buffCount == 2:
                buff(1)
            elif buffCount == 3:
                buff()
            elif buffCount == 4:
                buff(10)
            else:
                buff(50)
            rollMove(bc)

    elif moveHistory[0] == MMID.CORRUPT_HEART_DEBILITATE: # 3
        bc.player.debuff(2, True)
        bc.player.debuff(2, True)
        bc.player.debuff<PlayerStatus.FRAIL>(2, True)
        Actions.ShuffleTempCardIntoDrawPile(CardId.DAZED).actFunc.invoke(bc)
        Actions.ShuffleTempCardIntoDrawPile(CardId.SLIMED).actFunc.invoke(bc)
        Actions.ShuffleTempCardIntoDrawPile(CardId.WOUND).actFunc.invoke(bc)
        Actions.ShuffleTempCardIntoDrawPile(CardId.BURN).actFunc.invoke(bc)
        Actions.ShuffleTempCardIntoDrawPile(CardId.VOID).actFunc.invoke(bc)
        rollMove(bc)

    elif moveHistory[0] == MMID.CORRUPT_HEART_ECHO: # 2
        attackPlayerHelper(bc,45 if asc4 else 40)
        if math.fmod(bc.getMonsterTurnNumber(), 3) == 0:
            setMove(MonsterMoveId.CORRUPT_HEART_BUFF)
        else:
            setMove(MonsterMoveId.CORRUPT_HEART_BLOOD_SHOTS)
        bc.noOpRollMove()


    elif moveHistory[0] == MMID.INVALID:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            std::cerr << bc.seed << " "
            x = int(moveHistory[0])
            if x >= 0 and x <= int(MMID.WRITHING_MASS_STRONG_STRIKE):
                std::cerr << monsterIdStrings[int(id)] << " " << monsterMoveStrings[x] << std::endl
            False = assert()
##endif

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: MMID Monster::getMoveForRoll(BattleContext &bc, int &monsterData, const int roll) const
def getMoveForRoll(bc, monsterData, roll):
    asc17 = bc.ascension >= 17
    asc18 = bc.ascension >= 18
    asc19 = bc.ascension >= 19


    if id == MonsterId.ACID_SLIME_S:
            if asc17:
                return (MMID.ACID_SLIME_S_LICK)

            elif bc.aiRng.randomBoolean():
                return (MMID.ACID_SLIME_S_TACKLE)

            else:
                return (MMID.ACID_SLIME_S_LICK)


    elif id == MonsterId.ACID_SLIME_M:
            # corrosive spit = 1
            # tackle = 2
            # lick = 4
            if asc17:
                # START ASCENSION 17
                if roll < 40:
                    if lastTwoMoves(MMID.ACID_SLIME_M_CORROSIVE_SPIT):
                        if bc.aiRng.randomBoolean():
                            return (MMID.ACID_SLIME_M_TACKLE)
                        else:
                            return (MMID.ACID_SLIME_M_LICK)
                    else:
                        return (MMID.ACID_SLIME_M_CORROSIVE_SPIT)

                elif roll < 80:
                    if lastTwoMoves(MMID.ACID_SLIME_M_TACKLE):
                        if bc.aiRng.randomBoolean(0.5):
                            return (MMID.ACID_SLIME_M_CORROSIVE_SPIT)
                        else:
                            return (MMID.ACID_SLIME_M_LICK)
                    else:
                        return (MMID.ACID_SLIME_M_TACKLE)

                elif lastMove(MMID.ACID_SLIME_M_LICK):
                    if bc.aiRng.randomBoolean(0.4):
                        return (MMID.ACID_SLIME_M_CORROSIVE_SPIT)
                    else:
                        return (MMID.ACID_SLIME_M_TACKLE)
                else:
                    return (MMID.ACID_SLIME_M_LICK)
                # END ASCENSION 17

            elif roll < 30:
                if lastTwoMoves(MMID.ACID_SLIME_M_CORROSIVE_SPIT):
                    if bc.aiRng.randomBoolean():
                        return (MMID.ACID_SLIME_M_TACKLE)
                    else:
                        return (MMID.ACID_SLIME_M_LICK)
                else:
                    return (MMID.ACID_SLIME_M_CORROSIVE_SPIT)

            elif roll < 70:
                if lastMove(MMID.ACID_SLIME_M_TACKLE):
                    if bc.aiRng.randomBoolean(0.4):
                        return (MMID.ACID_SLIME_M_CORROSIVE_SPIT)
                    else:
                        return (MMID.ACID_SLIME_M_LICK)
                else:
                    return (MMID.ACID_SLIME_M_TACKLE)

            elif lastTwoMoves(MMID.ACID_SLIME_M_LICK):
                if bc.aiRng.randomBoolean(0.4):
                    return (MMID.ACID_SLIME_M_CORROSIVE_SPIT)
                else:
                    return (MMID.ACID_SLIME_M_TACKLE)
            else:
                return (MMID.ACID_SLIME_M_LICK)

    elif id == MonsterId.ACID_SLIME_L:
            # 1 corrosive spit
            # 2 tackle
            # 3 split
            # 4 lick

            if asc17:
                if roll < 40:
                    if lastTwoMoves(MMID.ACID_SLIME_M_CORROSIVE_SPIT):
                        if bc.aiRng.randomBoolean(0.6):
                            return (MMID.ACID_SLIME_L_TACKLE)
                        else:
                            return (MMID.ACID_SLIME_L_LICK)
                    else:
                        return (MMID.ACID_SLIME_L_CORROSIVE_SPIT)

                elif roll < 70:
                    if lastTwoMoves(MMID.ACID_SLIME_L_TACKLE):
                        if bc.aiRng.randomBoolean(0.6):
                            return (MMID.ACID_SLIME_L_CORROSIVE_SPIT)
                        else:
                            return (MMID.ACID_SLIME_L_LICK)
                    else:
                        return (MMID.ACID_SLIME_L_TACKLE)
                elif lastMove(MMID.ACID_SLIME_L_LICK):
                    if bc.aiRng.randomBoolean(0.4):
                        return (MMID.ACID_SLIME_L_CORROSIVE_SPIT)
                    else:
                        return (MMID.ACID_SLIME_L_TACKLE)
                else:
                    return (MMID.ACID_SLIME_L_LICK)

            elif roll < 30:
                if lastTwoMoves(MMID.ACID_SLIME_L_CORROSIVE_SPIT):
                    if bc.aiRng.randomBoolean():
                        return (MMID.ACID_SLIME_L_TACKLE)
                    else:
                        return (MMID.ACID_SLIME_L_LICK)
                else:
                    return (MMID.ACID_SLIME_L_CORROSIVE_SPIT)
            elif roll < 70:
                if lastMove(MMID.ACID_SLIME_L_TACKLE):
                    if bc.aiRng.randomBoolean(0.4):
                        return (MMID.ACID_SLIME_L_CORROSIVE_SPIT)
                    else:
                        return (MMID.ACID_SLIME_L_LICK)
                else:
                    return (MMID.ACID_SLIME_L_TACKLE)
            elif lastTwoMoves(MMID.ACID_SLIME_L_LICK):
                if bc.aiRng.randomBoolean(0.4):
                    return (MMID.ACID_SLIME_L_CORROSIVE_SPIT)
                else:
                    return (MMID.ACID_SLIME_L_TACKLE)
            else:
                return (MMID.ACID_SLIME_L_LICK)

    elif id == MonsterId.BLUE_SLAVER:
            if roll >= 40 and not lastTwoMoves(MMID.BLUE_SLAVER_STAB):
                return (MMID.BLUE_SLAVER_STAB)

            elif (not lastTwoMoves(MMID.BLUE_SLAVER_RAKE)) or (asc17 and (not lastMove(MMID.BLUE_SLAVER_RAKE))):
                return (MMID.BLUE_SLAVER_RAKE)

            else:
                return (MMID.BLUE_SLAVER_STAB)

    elif id == MonsterId.BRONZE_AUTOMATON:
            return (MMID.BRONZE_AUTOMATON_SPAWN_ORBS)

    elif id == MonsterId.BRONZE_ORB:
            # 1 beam
            # 2 support beam
            # 3 stasis
            haveUsedStasis = miscInfo
            if haveUsedStasis is None and roll >= 25:
                return (MMID.BRONZE_ORB_STASIS)

            elif roll >= 70 and not lastTwoMoves(MMID.BRONZE_ORB_SUPPORT_BEAM):
                return (MMID.BRONZE_ORB_SUPPORT_BEAM)

            elif not lastTwoMoves(MMID.BRONZE_ORB_BEAM):
                return (MMID.BRONZE_ORB_BEAM)

            else:
                return (MMID.BRONZE_ORB_SUPPORT_BEAM)

    elif id == MonsterId.BYRD:
            # 1 peck
            # 2 fly
            # 3 swoop
            # 4 stunned
            # 5 headbutt
            # 6 caw

            # handled during turn
            #            if (!hasStatusInternal<MS::FLIGHT>()) {
            #                return (MMID::BYRD_HEADBUTT)
            #                break
            #            }

            if firstTurn():
                if bc.aiRng.randomBoolean(0.375):
                    return (MMID.BYRD_CAW)
                else:
                    return (MMID.BYRD_PECK)
                break

            if roll < 50:
                if lastTwoMoves(MMID.BYRD_PECK):
                    if bc.aiRng.randomBoolean(0.4):
                        return (MMID.BYRD_SWOOP)
                    else:
                        return (MMID.BYRD_CAW)
                else:
                    return (MMID.BYRD_PECK)
                break

            if roll < 70:
                if lastMove(MMID.BYRD_SWOOP):
                    if bc.aiRng.randomBoolean(0.375):
                        return (MMID.BYRD_CAW)
                    else:
                        return (MMID.BYRD_PECK)
                else:
                    return (MMID.BYRD_SWOOP)
                break

            if lastMove(MMID.BYRD_CAW):
                if bc.aiRng.randomBoolean(0.2857):
                    return (MMID.BYRD_SWOOP)
                else:
                    return (MMID.BYRD_PECK)
            else:
                return (MMID.BYRD_CAW)

    elif id == MonsterId.CENTURION:
            # 1 Slash
            # 2 Defend
            # 3 Fury

            mysticAlive = bc.monsters.getAliveCount() > 1

            if roll >= 65 and (not lastTwoMoves(MMID.CENTURION_DEFEND)) and not lastTwoMoves(MMID.CENTURION_FURY):
                if mysticAlive:
                    return (MMID.CENTURION_DEFEND)
                else:
                    return (MMID.CENTURION_FURY)
                break

            if not lastTwoMoves(MMID.CENTURION_SLASH):
                return (MMID.CENTURION_SLASH)
                break

            if mysticAlive:
                return (MMID.CENTURION_DEFEND)
            else:
                return (MMID.CENTURION_FURY)

    elif id == MonsterId.MYSTIC:
            # 1 attack debuff
            # 2 heal
            # 3 buff

            healNeedAmt = 21 if asc17 else 16
            knight = bc.monsters.arr[0]

            if maxHp-curHp >= healNeedAmt or knight.isAlive() and knight.maxHp-knight.curHp >= healNeedAmt:
                return (MMID.MYSTIC_HEAL)
                break

            if roll >= 40 and ((not lastMove(MMID.MYSTIC_ATTACK_DEBUFF)) if asc17 else (not lastTwoMoves(MMID.MYSTIC_ATTACK_DEBUFF))):
                return (MMID.MYSTIC_ATTACK_DEBUFF)
                break

            if not lastTwoMoves(MMID.MYSTIC_BUFF):
                return (MMID.MYSTIC_BUFF)

            else:
                return (MMID.MYSTIC_ATTACK_DEBUFF)

    elif id == MonsterId.CHOSEN:
            # 1 zap
            # 2 drain
            # 3 debilitate
            # 4 hex
            # 5 poke

            if asc17:
                if firstTurn():
                    return (MMID.CHOSEN_HEX)

                elif (not lastMove(MMID.CHOSEN_DEBILITATE)) and not lastMove(MMID.CHOSEN_DRAIN):
                    if roll < 50:
                        return (MMID.CHOSEN_DEBILITATE)
                    else:
                        return (MMID.CHOSEN_DRAIN)

                elif roll < 40:
                    return (MMID.CHOSEN_ZAP)

                else:
                    return (MMID.CHOSEN_POKE)

                break

            # Ascension < 17
            if firstTurn():
                return (MMID.CHOSEN_POKE)

            elif lastMoveBefore(MMID.INVALID):
                return (MMID.CHOSEN_HEX)

            elif (not lastMove(MMID.CHOSEN_DEBILITATE)) and not lastMove(MMID.CHOSEN_DRAIN):
                if roll < 50:
                    return (MMID.CHOSEN_DEBILITATE)
                else:
                    return (MMID.CHOSEN_DRAIN)
            elif roll < 40:
                return (MMID.CHOSEN_ZAP)
            else:
                return (MMID.CHOSEN_POKE)

    elif id == MonsterId.BOOK_OF_STABBING:
            # 1 multi stab
            # 2 single stab
# C++ TO PYTHON CONVERTER TASK: Python does not have an equivalent to references to variables:
# ORIGINAL LINE: auto &stabCount = monsterData;
            stabCount = monsterData.arg_value
            if roll < 15:
                if lastMove(MMID.BOOK_OF_STABBING_SINGLE_STAB):
                    stabCount += 1
                    return (MMID.BOOK_OF_STABBING_MULTI_STAB)
                else:
                    return (MMID.BOOK_OF_STABBING_SINGLE_STAB)
                    if asc18:
                        stabCount += 1
            elif lastTwoMoves(MMID.BOOK_OF_STABBING_MULTI_STAB):
                return (MMID.BOOK_OF_STABBING_SINGLE_STAB)
                if asc18:
                    stabCount += 1
            else:
                stabCount += 1
                return (MMID.BOOK_OF_STABBING_MULTI_STAB)

    elif id == MonsterId.CULTIST:
            if lastMove(MMID.INVALID):
                return (MMID.CULTIST_INCANTATION)
            else:
                return (MMID.CULTIST_DARK_STRIKE)

    elif id == MonsterId.FAT_GREMLIN:
            return (MMID.FAT_GREMLIN_SMASH)

    elif id == MonsterId.FUNGI_BEAST:
            # 1 FUNGI_BEAST_BITE
            # 2 FUNGI_BEAST_GROW
            if roll < 60:
                if lastTwoMoves(MMID.FUNGI_BEAST_BITE):
                    return (MMID.FUNGI_BEAST_GROW)
                else:
                    return (MMID.FUNGI_BEAST_BITE)

            elif lastMove(MMID.FUNGI_BEAST_GROW):
                return (MMID.FUNGI_BEAST_BITE)

            else:
                return (MMID.FUNGI_BEAST_GROW)

    elif id == MonsterId.GREEN_LOUSE:
            if roll < 25:
                if lastMove(MMID.GREEN_LOUSE_SPIT_WEB) and (asc17 or lastTwoMoves(MMID.GREEN_LOUSE_SPIT_WEB)):
                    return (MMID.GREEN_LOUSE_BITE)
                else:
                    return (MMID.GREEN_LOUSE_SPIT_WEB)

            elif lastTwoMoves(MMID.GREEN_LOUSE_BITE):
                return (MMID.GREEN_LOUSE_SPIT_WEB)

            else:
                return (MMID.GREEN_LOUSE_BITE)

    elif id == MonsterId.GREMLIN_LEADER:
            # 2 RALLY
            # 3 ENCOURAGE
            # 4 STAB
            numAliveGremlins = Monster.getAliveGremlinCount(bc)
            if numAliveGremlins == 0:

                if roll < 75:
                    if lastMove(MMID.GREMLIN_LEADER_RALLY):
                        return (MMID.GREMLIN_LEADER_STAB)
                    else:
                        return (MMID.GREMLIN_LEADER_RALLY)
                elif lastMove(MMID.GREMLIN_LEADER_STAB):
                    return (MMID.GREMLIN_LEADER_RALLY)
                else:
                    return (MMID.GREMLIN_LEADER_STAB)

            elif numAliveGremlins == 1:

                if roll < 50:
                    if lastMove(MMID.GREMLIN_LEADER_RALLY):
                        roll2 = bc.aiRng.random(50, 99)
                        if roll2 < 80:
                            return (MMID.GREMLIN_LEADER_ENCOURAGE)
                        else:
                            return (MMID.GREMLIN_LEADER_STAB)
                    else:
                        return (MMID.GREMLIN_LEADER_RALLY)

                elif roll < 80:
                    if lastMove(MMID.GREMLIN_LEADER_ENCOURAGE):
                        return (MMID.GREMLIN_LEADER_STAB)
                    else:
                        return (MMID.GREMLIN_LEADER_ENCOURAGE)

                elif lastMove(MMID.GREMLIN_LEADER_STAB):
                    roll2 = bc.aiRng.random(0, 80)
                    if roll2 < 50:
                        return (MMID.GREMLIN_LEADER_RALLY)
                    else:
                        return (MMID.GREMLIN_LEADER_ENCOURAGE)

                else:
                    return (MMID.GREMLIN_LEADER_STAB)

            else:

                if roll < 66:
                    if lastMove(MMID.GREMLIN_LEADER_ENCOURAGE):
                        return (MMID.GREMLIN_LEADER_STAB)
                    else:
                        return (MMID.GREMLIN_LEADER_ENCOURAGE)

                elif lastMove(MMID.GREMLIN_LEADER_STAB):
                    return (MMID.GREMLIN_LEADER_ENCOURAGE)

                else:
                    return (MMID.GREMLIN_LEADER_STAB)


    elif id == MonsterId.GREMLIN_NOB:
            # 1 Rush
            # 2 Skull Bash
            # 3 BELLOW

            if lastMove(MMID.INVALID):
                return (MMID.GREMLIN_NOB_BELLOW)
                break

            if asc18:
                if not lastTwoMoves(MMID.GREMLIN_NOB_SKULL_BASH):
                    return (MMID.GREMLIN_NOB_RUSH)
                    break

                if lastTwoMoves(MMID(MMID.GREMLIN_NOB_RUSH)):
                    return (MMID.GREMLIN_NOB_SKULL_BASH)

                else:
                    return (MMID.GREMLIN_NOB_RUSH)
                break

            if roll < 33 or lastTwoMoves(MMID.GREMLIN_NOB_RUSH):
                return (MMID.GREMLIN_NOB_SKULL_BASH)

            else:
                return (MMID.GREMLIN_NOB_RUSH)

    elif id == MonsterId.GREMLIN_WIZARD:
            monsterData.arg_value = 1 # gremlin wizard charge
            return (MMID.GREMLIN_WIZARD_CHARGING)

    elif id == MonsterId.HEXAGHOST:
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
            firstTurn = assert()
##endif
            return (MMID.HEXAGHOST_ACTIVATE)

    elif id == MonsterId.JAW_WORM:
            if firstTurn():
                return (MMID.JAW_WORM_CHOMP)
                break

            if roll < 25:
                if lastMove(MMID.JAW_WORM_CHOMP):
                    if bc.aiRng.randomBoolean(0.5625):
                        return (MMID.JAW_WORM_BELLOW)
                    else:
                        return (MMID.JAW_WORM_THRASH)

                else:
                    return (MMID.JAW_WORM_CHOMP)

            elif roll < 55:
                if lastTwoMoves(MMID.JAW_WORM_THRASH):
                    if bc.aiRng.randomBoolean(0.357):
                        return (MMID.JAW_WORM_CHOMP)
                    else:
                        return (MMID.JAW_WORM_BELLOW)

                else:
                    return (MMID.JAW_WORM_THRASH)

            elif lastMove(MMID.JAW_WORM_BELLOW):
                if bc.aiRng.randomBoolean(0.416):
                    return (MMID.JAW_WORM_CHOMP)
                else:
                    return (MMID.JAW_WORM_THRASH)

            else:
                return (MMID.JAW_WORM_BELLOW)

    elif id == MonsterId.LAGAVULIN: # called first turn only
        if hasStatus():
            return (MMID.LAGAVULIN_SLEEP)
        else:
            return (MMID.LAGAVULIN_SIPHON_SOUL)

    elif id == MonsterId.LOOTER: # called first turn only
        return (MMID.LOOTER_MUG)

    elif id == MonsterId.MAD_GREMLIN:
        return (MMID.MAD_GREMLIN_SCRATCH)

    elif id == MonsterId.MUGGER: # called first turn only
        return (MMID.MUGGER_MUG)

    elif id == MonsterId.NEMESIS:
            # 2 attack
            # 3 scythe
            # 4 debuff

            if firstTurn():
                if roll < 50:
                    return MMID.NEMESIS_ATTACK
                else:
                    return MMID.NEMESIS_DEBUFF

            if roll < 30:
                if not eitherLastTwo(MMID.NEMESIS_SCYTHE):
                    return MMID.NEMESIS_SCYTHE

                elif bc.aiRng.randomBoolean():
                    if not lastTwoMoves(MMID.NEMESIS_ATTACK):
                        return MMID.NEMESIS_ATTACK
                    else:
                        return MMID.NEMESIS_DEBUFF

                elif not lastMove(MMID.NEMESIS_DEBUFF):
                    return MMID.NEMESIS_DEBUFF

                else:
                    return MMID.NEMESIS_ATTACK

            if roll < 65:
                if not lastTwoMoves(MMID.NEMESIS_ATTACK):
                    return MMID.NEMESIS_ATTACK

                elif (not bc.aiRng.randomBoolean()) or eitherLastTwo(MMID.NEMESIS_SCYTHE):
                    return MMID.NEMESIS_DEBUFF

                else:
                    return MMID.NEMESIS_SCYTHE

            if not lastMove(MMID.NEMESIS_DEBUFF):
                return MMID.NEMESIS_DEBUFF

            if bc.aiRng.randomBoolean() and not eitherLastTwo(MMID.NEMESIS_SCYTHE):
                return MMID.NEMESIS_SCYTHE

            return MMID.NEMESIS_ATTACK

    elif id == MonsterId.ORB_WALKER:
            if roll < 40:
                if not lastTwoMoves(MMID.ORB_WALKER_CLAW):
                    return (MMID.ORB_WALKER_CLAW)
                else:
                    return (MMID.ORB_WALKER_LASER)
            elif not lastTwoMoves(MMID.ORB_WALKER_LASER):
                return (MMID.ORB_WALKER_LASER)
            else:
                return (MMID.ORB_WALKER_CLAW)

    elif id == MonsterId.RED_LOUSE:
            if roll < 25:
                if lastMove(MMID.RED_LOUSE_GROW) and (asc17 or lastTwoMoves(MMID.RED_LOUSE_GROW)):
                    return (MMID.RED_LOUSE_BITE)
                else:
                    return (MMID.RED_LOUSE_GROW)

            elif lastTwoMoves(MMID.RED_LOUSE_BITE):
                return (MMID.RED_LOUSE_GROW)

            else:
                return (MMID.RED_LOUSE_BITE)

    elif id == MonsterId.REPTOMANCER:
            # 1 snake strike
            # 2 summon
            # 3 big bite
            if firstTurn():
                return MMID.REPTOMANCER_SUMMON

            myRoll = roll
            canSpawn = bc.monsters.monstersAlive < 4

            while True:
                if myRoll < 33:
                    if not lastMove(MMID.REPTOMANCER_SNAKE_STRIKE):
                        return MMID.REPTOMANCER_SNAKE_STRIKE
                    else:
                        myRoll = bc.aiRng.random(33, 99)

                if myRoll < 66:
                    if (not lastTwoMoves(MMID.REPTOMANCER_SUMMON)) and canSpawn:
                        return MMID.REPTOMANCER_SUMMON
                    else:
                        return MMID.REPTOMANCER_SNAKE_STRIKE

                if not lastMove(MMID.REPTOMANCER_BIG_BITE):
                    return MMID.REPTOMANCER_BIG_BITE

                # getMove(0-65)
                # could probably unroll this but would be big
                myRoll = bc.aiRng.random(0, 65)

    elif id == MonsterId.DAGGER:
            return MMID.DAGGER_STAB

    elif id == MonsterId.SENTRY:
            if firstTurn():
                if math.fmod(idx, 2) == 0:
                    return (MMID.SENTRY_BOLT)
                else:
                    return (MMID.SENTRY_BEAM)

    elif id == MonsterId.SHELLED_PARASITE:
            # 1 fell
            # 2 double strike
            # 3 suck
            # 4 stunned
            if firstTurn():
                if asc17:
                    return (MMID.SHELLED_PARASITE_FELL)
                else:
                    if bc.aiRng.randomBoolean():
                        return (MMID.SHELLED_PARASITE_DOUBLE_STRIKE)
                    else:
                        return (MMID.SHELLED_PARASITE_SUCK)
                break

            roll2 = 100

            if roll < 20:
                if not lastMove(MMID.SHELLED_PARASITE_FELL):
                    return (MMID.SHELLED_PARASITE_FELL)
                    break
                roll2 = bc.aiRng.random(20,99)

            if roll < 60 or roll2 < 60:
                if not lastTwoMoves(MMID.SHELLED_PARASITE_DOUBLE_STRIKE):
                    return (MMID.SHELLED_PARASITE_DOUBLE_STRIKE)
                else:
                    return (MMID.SHELLED_PARASITE_SUCK)

            elif not lastTwoMoves(MMID.SHELLED_PARASITE_SUCK):
                return (MMID.SHELLED_PARASITE_SUCK)

            else:
                return (MMID.SHELLED_PARASITE_DOUBLE_STRIKE)

    elif id == MonsterId.SHIELD_GREMLIN:
            return (MMID.SHIELD_GREMLIN_PROTECT)

    elif id == MonsterId.SLIME_BOSS:
            # 1 SLIME_BOSS_PREPARING
            # 2 SLIME_BOSS_SLAM
            # 3 SLIME_BOSS_SPLIT
            # 4 SLIME_BOSS_GOOP_SPRAY
            if firstTurn():
                return (MMID.SLIME_BOSS_GOOP_SPRAY)

    elif id == MonsterId.SNAKE_PLANT:
            # 1 chomp
            # 2 enfeebling spores
            if asc17:
                if roll < 65:
                    if lastTwoMoves(MMID.SNAKE_PLANT_CHOMP):
                        return (MMID.SNAKE_PLANT_ENFEEBLING_SPORES)
                    else:
                        return (MMID.SNAKE_PLANT_CHOMP)
                elif not lastTwoMoves(MMID.SNAKE_PLANT_ENFEEBLING_SPORES):
                    return (MMID.SNAKE_PLANT_ENFEEBLING_SPORES)
                else:
                    return (MMID.SNAKE_PLANT_CHOMP)
                break

            if roll < 65:
                if lastTwoMoves(MMID.SNAKE_PLANT_CHOMP):
                    return (MMID.SNAKE_PLANT_ENFEEBLING_SPORES)
                else:
                    return (MMID.SNAKE_PLANT_CHOMP)
            elif lastMove(MMID.SNAKE_PLANT_ENFEEBLING_SPORES):
                return (MMID.SNAKE_PLANT_CHOMP)
            else:
                return (MMID.SNAKE_PLANT_ENFEEBLING_SPORES)

    elif id == MonsterId.SNEAKY_GREMLIN:
        return (MMID.SNEAKY_GREMLIN_PUNCTURE)

    elif id == MonsterId.SNECKO:
            # 1 perplexing glare
            # 2 bite
            # 3 tail whip
            if firstTurn():
                return (MMID.SNECKO_PERPLEXING_GLARE)

            elif roll < 40 or lastTwoMoves(MMID.SNECKO_BITE):
                return (MMID.SNECKO_TAIL_WHIP)

            else:
                return (MMID.SNECKO_BITE)

    elif id == MonsterId.SPHERIC_GUARDIAN: # called first turn only
        return (MMID.SPHERIC_GUARDIAN_ACTIVATE)

    elif id == MonsterId.SPIKE_SLIME_S:
        return (MMID.SPIKE_SLIME_S_TACKLE)

    elif id == MonsterId.RED_SLAVER:
            # 1 Stab
            # 2 Entangle
            # 3 Scrape
            usedEntangle = miscInfo

            if lastMove(MMID.INVALID):
                return (MMID.RED_SLAVER_STAB)

            elif roll >= 75 and not usedEntangle:
                return (MMID.RED_SLAVER_ENTANGLE)

            elif roll >= 50 and usedEntangle and not lastTwoMoves(MMID.RED_SLAVER_STAB):
                return (MMID.RED_SLAVER_STAB)

            elif (not lastTwoMoves(MMID.RED_SLAVER_SCRAPE)) or (asc17 and (not lastMove(MMID.RED_SLAVER_SCRAPE))):
                return (MMID.RED_SLAVER_SCRAPE)

            else:
                return (MMID.RED_SLAVER_STAB)



    elif id == MonsterId.SPIKE_SLIME_L:
            # 1 flame tackle
            # 3 split
            # 4 lick
            if roll < 30:
                if lastTwoMoves(MMID.SPIKE_SLIME_L_FLAME_TACKLE):
                    return (MMID.SPIKE_SLIME_L_LICK)
                else:
                    return (MMID.SPIKE_SLIME_L_FLAME_TACKLE)

            elif lastTwoMoves(MMID.SPIKE_SLIME_L_LICK) or (asc17 and lastMove(MMID.SPIKE_SLIME_L_LICK)):
                return (MMID.SPIKE_SLIME_L_FLAME_TACKLE)

            else:
                return (MMID.SPIKE_SLIME_L_LICK)


    elif id == MonsterId.SPIKE_SLIME_M:
            # 1 SPIKE_SLIME_M_FLAME_TACKLE
            # 4 SPIKE_SLIME_M_LICK
            if roll < 30:
                if lastTwoMoves(MMID.SPIKE_SLIME_M_FLAME_TACKLE):
                    return (MMID.SPIKE_SLIME_M_LICK)
                else:
                    return (MMID.SPIKE_SLIME_M_FLAME_TACKLE)
            elif lastTwoMoves(MMID.SPIKE_SLIME_M_LICK) or (asc17 and lastMove(MMID.SPIKE_SLIME_M_LICK)):
                return (MMID.SPIKE_SLIME_M_FLAME_TACKLE)
            else:
                return (MMID.SPIKE_SLIME_M_LICK)

    elif id == MonsterId.TASKMASTER:
            return (MMID.TASKMASTER_SCOURING_WHIP)

    elif id == MonsterId.THE_CHAMP:
            # 1 Heavy Slash
            # 2 Defensive Stance
            # 3 Execute
            # 4 Face Slap
            # 5 Gloat
            # 6 Taunt
            # 7 Anger

            # is in phase2
            if (monsterData.arg_value & 0x4) != 0:
                if (not lastMove(MMID.THE_CHAMP_EXECUTE)) and not lastMoveBefore(MMID.THE_CHAMP_EXECUTE):
                    return (MMID.THE_CHAMP_EXECUTE)
                    break

            else:
# C++ TO PYTHON CONVERTER TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
                if curHp < maxHp / 2:
                    monsterData.arg_value |= 0x4
                    return (MMID.THE_CHAMP_ANGER)
                    break

                elif math.fmod((bc.getMonsterTurnNumber()+1), 4) == 0:
                    return (MMID.THE_CHAMP_TAUNT)
                    break


            # check if should use defensive stance
            defensiveStanceUseCount = miscInfo & 0x3
            rollThreshold = 30 if asc19 else 15
            if roll <= rollThreshold and (not lastMove(MMID.THE_CHAMP_DEFENSIVE_STANCE)) and defensiveStanceUseCount < 2:
                monsterData.arg_value += 1
                return (MMID.THE_CHAMP_DEFENSIVE_STANCE)
                break

            if roll <= 30 and (not lastMove(MMID.THE_CHAMP_GLOAT)) and not lastMove(MMID.THE_CHAMP_DEFENSIVE_STANCE):
                return (MMID.THE_CHAMP_GLOAT)

            elif roll <= 55 and not lastMove(MMID.THE_CHAMP_FACE_SLAP):
                return (MMID.THE_CHAMP_FACE_SLAP)

            elif not lastMove(MMID.THE_CHAMP_HEAVY_SLASH):
                return (MMID.THE_CHAMP_HEAVY_SLASH)

            else:
                return (MMID.THE_CHAMP_FACE_SLAP)

    elif id == MonsterId.THE_COLLECTOR:
            # 1 initial spawn
            # 2 fireball
            # 3 buff
            # 4 mega debuff
            # 5 spawn

            # first turn always spawn
            if firstTurn():
                return (MMID.THE_COLLECTOR_SPAWN)
                break

            # always uses mega debuff turn 4
            if bc.getMonsterTurnNumber() == 3:
                return (MMID.THE_COLLECTOR_MEGA_DEBUFF)
                break

            canUseSpawn = bc.monsters.monstersAlive < 3 and not lastMove(MMID.THE_COLLECTOR_SPAWN)

            if roll <= 25 and canUseSpawn:
                return (MMID.THE_COLLECTOR_SPAWN)
                break

            if roll <= 70 and not lastTwoMoves(MMID.THE_COLLECTOR_FIREBALL):
                return (MMID.THE_COLLECTOR_FIREBALL)
                break

            if lastMove(MMID.THE_COLLECTOR_BUFF):
                return (MMID.THE_COLLECTOR_FIREBALL)

            else:
                return (MMID.THE_COLLECTOR_BUFF)

    elif id == MonsterId.THE_GUARDIAN:
            return (MMID.THE_GUARDIAN_CHARGING_UP)

        # RED MASK BOIS

    elif id == MonsterId.BEAR:
            return (MMID.BEAR_BEAR_HUG)

    elif id == MonsterId.ROMEO:
            return (MMID.ROMEO_MOCK)

    elif id == MonsterId.POINTY:
            return (MMID.POINTY_ATTACK)

        # SHAPES
    elif id == MonsterId.EXPLODER:
            # first turn only
            return (MMID.EXPLODER_SLAM)

    elif id == MonsterId.REPULSOR:
            if roll < 20 and not lastMove(MMID.REPULSOR_BASH):
                return (MMID.REPULSOR_BASH)
            else:
                return (MMID.REPULSOR_REPULSE)

    elif id == MonsterId.SPIKER:
            # times used thorns > 5
            if miscInfo > 5 or roll < 50 and not lastMove(MMID.SPIKER_CUT):
                return (MMID.SPIKER_CUT)
            else:
                return (MMID.SPIKER_SPIKE)

    elif id == MonsterId.THE_MAW:
            if firstTurn():
                return (MMID.THE_MAW_ROAR)

            elif roll < 50 and not lastMove(MMID.THE_MAW_NOM):
                return (MMID.THE_MAW_NOM)

            elif not lastMove(MMID.THE_MAW_SLAM):
                # dont include not last move nom condition, because it can't be, we handle in the move logic
                return (MMID.THE_MAW_SLAM)

            else:
                return (MMID.THE_MAW_DROOL)

    elif id == MonsterId.DARKLING:
            # 1 chomp
            # 2 harden
            # 3 nip
            # 4 regrow
            # 5 reincarnate
            myRoll = roll

            if firstTurn():
                if myRoll < 50:
                    return MMID.DARKLING_HARDEN
                else:
                    return MMID.DARKLING_NIP

            if halfDead:
                return MMID.DARKLING_REINCARNATE

            if myRoll < 40:
                if (not lastMove(MMID.DARKLING_CHOMP)) and idx != 1:
                    return MMID.DARKLING_CHOMP
                else:
                    myRoll = bc.aiRng.random(40, 99)

            if myRoll < 70:
                if not lastMove(MMID.DARKLING_HARDEN):
                    return MMID.DARKLING_HARDEN
                else:
                    return MMID.DARKLING_NIP

            if not lastTwoMoves(MMID.DARKLING_NIP):
                return MMID.DARKLING_NIP

            else:
                # one of last two moves was darkling nip
                return getMoveForRoll(bc, monsterData.arg_value, bc.aiRng.random(0, 99))

    elif id == MonsterId.SPIRE_GROWTH:
            useConstrict = (not bc.player.hasStatus()) and (not lastMove(MMID.SPIRE_GROWTH_CONSTRICT)) and (asc17 or roll >= 50)
            if useConstrict:
                return (MMID.SPIRE_GROWTH_CONSTRICT)

            elif roll < 50 and not lastTwoMoves(MMID.SPIRE_GROWTH_QUICK_TACKLE):
                return (MMID.SPIRE_GROWTH_QUICK_TACKLE)

            elif not lastTwoMoves(MMID.SPIRE_GROWTH_SMASH):
                return (MMID.SPIRE_GROWTH_SMASH)

            else:
                return (MMID.SPIRE_GROWTH_QUICK_TACKLE)

    elif id == MonsterId.TRANSIENT:
            return (MMID.TRANSIENT_ATTACK)

    elif id == MonsterId.WRITHING_MASS:
            # 0 strong strike
            # 1 multi strike
            # 2 flail
            # 3 wither
            # 4 implant
            if firstTurn():
                if roll < 33:
                    return (MMID.WRITHING_MASS_MULTI_STRIKE)

                elif roll < 66:
                    return (MMID.WRITHING_MASS_FLAIL)

                else:
                    return (MMID.WRITHING_MASS_WITHER)

            haveUsedImplant = miscInfo
            myRoll = roll
            while True:

                if myRoll < 10:
                    if not lastMove(MMID.WRITHING_MASS_STRONG_STRIKE):
                        return (MMID.WRITHING_MASS_STRONG_STRIKE)
                    myRoll = bc.aiRng.random(10, 99)

                if myRoll < 20:
                    if (not haveUsedImplant) and not lastMove(MMID.WRITHING_MASS_IMPLANT):
                        return (MMID.WRITHING_MASS_IMPLANT)

                    elif bc.aiRng.randomBoolean(0.1):
                        return (MMID.WRITHING_MASS_STRONG_STRIKE)
                    myRoll = bc.aiRng.random(20, 99)

                if myRoll < 40:
                    if not lastMove(MMID.WRITHING_MASS_WITHER):
                        return MMID.WRITHING_MASS_WITHER

                    # last move was wither
                    if bc.aiRng.randomBoolean(0.4):
                        myRoll = bc.aiRng.random(0, 19)
                        if myRoll < 10:
                            return (MMID.WRITHING_MASS_STRONG_STRIKE)

                        else:
                            if not haveUsedImplant:
                                return (MMID.WRITHING_MASS_IMPLANT)

                            elif bc.aiRng.randomBoolean(0.1):
                                return (MMID.WRITHING_MASS_STRONG_STRIKE)

                            else:
                                myRoll = bc.aiRng.random(20, 99)
                                continue
                    myRoll = bc.aiRng.random(40, 99)

                if myRoll < 70:
                    if not lastMove(MMID.WRITHING_MASS_MULTI_STRIKE):
                        return MMID.WRITHING_MASS_MULTI_STRIKE

                    elif bc.aiRng.randomBoolean(0.3):
                        return MMID.WRITHING_MASS_FLAIL

                    else:
                        myRoll = bc.aiRng.random(0, 39)
                        continue

                if not lastMove(MMID.WRITHING_MASS_FLAIL):
                    return MMID.WRITHING_MASS_FLAIL

                else:
                    return (MMID.WRITHING_MASS_WITHER)

    elif id == MonsterId.GIANT_HEAD:
            # 1 glare
            # 2 it is time
            # 3 count
            if bc.getMonsterTurnNumber() >= 4:
                return MMID.GIANT_HEAD_IT_IS_TIME

            if roll < 50:
                if not lastTwoMoves(MMID.GIANT_HEAD_GLARE):
                    return MMID.GIANT_HEAD_GLARE
                else:
                    return MMID.GIANT_HEAD_COUNT

            # roll >= 50
            if not lastTwoMoves(MMID.GIANT_HEAD_COUNT):
                return MMID.GIANT_HEAD_COUNT
            else:
                return MMID.GIANT_HEAD_GLARE

    elif id == MonsterId.TIME_EATER:
            # 2 reverberate
            # 3 ripple
            # 4 head slam
            # 5 haste
            usedHaste = miscInfo
# C++ TO PYTHON CONVERTER TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            underHalfHp = curHp < maxHp/2
            if (not usedHaste) and underHalfHp:
                return MonsterMoveId.TIME_EATER_HASTE

            myRoll = roll
            if myRoll < 45:
                if not lastTwoMoves(MonsterMoveId.TIME_EATER_REVERBERATE):
                    return MonsterMoveId.TIME_EATER_REVERBERATE
                myRoll = bc.aiRng.random(50,99)

            if myRoll < 80:
                if not lastMove(MonsterMoveId.TIME_EATER_HEAD_SLAM):
                    return MonsterMoveId.TIME_EATER_HEAD_SLAM
                if bc.aiRng.randomBoolean(0.66):
                    return MonsterMoveId.TIME_EATER_REVERBERATE
                return MonsterMoveId.TIME_EATER_RIPPLE

            if lastMove(MMID.TIME_EATER_RIPPLE):
                myRoll = bc.aiRng.random(74)
                if myRoll < 45:
                    return MonsterMoveId.TIME_EATER_REVERBERATE
                else:
                    return MonsterMoveId.TIME_EATER_HEAD_SLAM

            return MonsterMoveId.TIME_EATER_RIPPLE

    elif id == MonsterId.DECA:
            return MonsterMoveId.DECA_BEAM

    elif id == MonsterId.DONU:
            return MonsterMoveId.DONU_CIRCLE_OF_POWER

    elif id == MonsterId.AWAKENED_ONE:
            # 1 slash
            # 2 soul strike
            # 3 rebirth
            # 5 dark echo
            # 6 sludge
            # 8 tackle

            if halfDead:
                return MonsterMoveId.AWAKENED_ONE_REBIRTH

            phase2 = miscInfo
            if not phase2:
                if firstTurn():
                    return MonsterMoveId.AWAKENED_ONE_SLASH

                if roll < 25:
                    if lastMove(MonsterMoveId.AWAKENED_ONE_SOUL_STRIKE):
                        return MonsterMoveId.AWAKENED_ONE_SLASH
                    else:
                        return MonsterMoveId.AWAKENED_ONE_SOUL_STRIKE

                if not lastTwoMoves(MonsterMoveId.AWAKENED_ONE_SLASH):
                    return MonsterMoveId.AWAKENED_ONE_SLASH
                else:
                    return MonsterMoveId.AWAKENED_ONE_SOUL_STRIKE

            # phase 2

            if roll < 50:
                if not lastTwoMoves(MonsterMoveId.AWAKENED_ONE_SLUDGE):
                    return MonsterMoveId.AWAKENED_ONE_SLUDGE
                else:
                    return MonsterMoveId.AWAKENED_ONE_TACKLE

            if not lastTwoMoves(MonsterMoveId.AWAKENED_ONE_TACKLE):
                return MonsterMoveId.AWAKENED_ONE_TACKLE
            else:
                return MonsterMoveId.AWAKENED_ONE_SLUDGE

    elif id == MonsterId.CORRUPT_HEART:
            if firstTurn():
                return MonsterMoveId.CORRUPT_HEART_DEBILITATE
            # only called if not going to buff
            if bc.aiRng.randomBoolean():
                return MonsterMoveId.CORRUPT_HEART_BLOOD_SHOTS
            else:
                return MonsterMoveId.CORRUPT_HEART_ECHO

    elif id == MonsterId.SPIRE_SHIELD:
            # 1 bash
            # 2 fortify
            # 3 smash
            if bc.aiRng.randomBoolean():
                return MonsterMoveId.SPIRE_SHIELD_FORTIFY
            else:
                return MonsterMoveId.SPIRE_SHIELD_BASH

    elif id == MonsterId.SPIRE_SPEAR:
            if firstTurn():
                return MonsterMoveId.SPIRE_SPEAR_BURN_STRIKE
            if bc.aiRng.randomBoolean():
                return MonsterMoveId.SPIRE_SPEAR_PIERCER
            else:
                return MonsterMoveId.SPIRE_SPEAR_BURN_STRIKE

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
    std::cerr << "getMove did not return a value " << bc.seed << " " << int(id) << std::endl
    False = assert()
##endif
    return MMID.INVALID

def initSpawnedMonster(bc, monsterId, monsterIdx, hp):
    idx = monsterIdx
    id = monsterId
    curHp = hp
    maxHp = hp
    rollMove(bc)

def stealGoldFromPlayer(bc, amount):
    theftAmount = min(int(bc.player.gold), amount)
    if theftAmount > 0:
        miscInfo += theftAmount
        bc.player.gold -= theftAmount
        bc.setRequiresStolenGoldCheck(True)

def largeSlimeSplit(bc, mediumSlimeType, placeIdx, hp):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
    assert hp > 0
    assert bc.monsters.monstersAlive > 0
##endif
    idx1 = placeIdx
    idx2 = placeIdx + 1

    bc.monsters.arr[idx1] = Monster()
    bc.monsters.arr[idx1].initSpawnedMonster(bc, mediumSlimeType, idx1, hp)

    bc.monsters.arr[idx2] = Monster()
    bc.monsters.arr[idx2].initSpawnedMonster(bc, mediumSlimeType, idx2, hp)

    if bc.player.hasRelic():
        bc.monsters.arr[idx1].buff(1)
        bc.monsters.arr[idx2].buff(1)

    bc.monsters.monstersAlive += 1
    bc.monsters.monsterCount = min(bc.monsters.monsterCount+1, 4)

    bc.noOpRollMove()
    bc.monsters.extraRollMoveOnTurn.set(idx2, True)
    bc.monsterTurnIdx += 1

def slimeBossSplit(bc, hp):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
    assert hp > 0
    assert bc.monsters.monstersAlive > 0
##endif
    IDX1 = 0
    IDX2 = 2

    bc.monsters.arr[IDX1] = Monster()
    bc.monsters.arr[IDX1].initSpawnedMonster(bc, MonsterId.SPIKE_SLIME_L, IDX1, hp)

    bc.monsters.arr[IDX2] = Monster()
    bc.monsters.arr[IDX2].initSpawnedMonster(bc, MonsterId.ACID_SLIME_L, IDX2, hp)

    if bc.player.hasRelic():
        bc.monsters.arr[IDX1].buff(1)
        bc.monsters.arr[IDX2].buff(1)

    bc.monsters.monsterCount = 3
    bc.monsters.monstersAlive = 2
    bc.monsterTurnIdx = 3

def spawnBronzeOrbs(bc):

    orb1 = bc.monsters.arr[0]
    orb2 = bc.monsters.arr[2]

    orb1.construct(bc, MonsterId.BRONZE_ORB, 0)
    orb2.construct(bc, MonsterId.BRONZE_ORB, 2)

    orb1.buff()
    orb2.buff()

    if bc.player.hasRelic():
        orb1.buff(1)
        orb2.buff(1)

    orb1.rollMove(bc)
    orb2.rollMove(bc)

    bc.monsters.monstersAlive += 2
    bc.monsterTurnIdx += 1


class StasisPair:

    def __init__(self):
        # instance fields found by C++ to Python Converter:
        self.groupIdx = 0
        self.idOrder = 0


# returns index of card to remove
# list is guaranteed to not be empty

def stasisAction(bc):
    cards = bc.cards
    if cards.drawPile.empty() and cards.discardPile.empty():
        return # do nothing

    stasisCard = CardInstance()
    if cards.drawPile.empty():
        removeIdx = stasisHelper(bc.cardRandomRng, cards.discardPile.begin(), cards.discardPile.end())

        stasisCard = cards.discardPile.get(removeIdx)
        cards.removeFromDiscard(removeIdx)

    else:
        removeIdx = stasisHelper(bc.cardRandomRng, cards.drawPile.begin(), cards.drawPile.end())

        stasisCard = cards.drawPile.get(removeIdx)
        cards.removeFromDrawPileAtIdx(removeIdx)

    cards.notifyRemoveFromCombat(stasisCard)
    cards.stasisCards[min(1, idx)] = stasisCard

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
    if stasisCard.getId() == CardId.INVALID:
        std::cerr << bc << std::endl
        False = assert()
##endif
    buff()


def returnStasisCard(bc):
    stasisCard = bc.cards.stasisCards[min(idx,1)]

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
    if stasisCard.id == CardId.INVALID:
        std::cerr << bc.seed << " " << bc.loopCount << " stasis card invalid" << idx << "\n" << bc << std::endl
    assert stasisCard.id != CardId.INVALID
##endif

    bc.cards.notifyAddCardToCombat(stasisCard)
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: bc.moveToHandHelper(stasisCard);
    bc.moveToHandHelper(sts.CardInstance(stasisCard))
    stasisCard = CardInstance(CardId.INVALID)

def reptomancerSummon(bc, daggerCount):
    daggerIdxs = [0 for _ in range(2)]
    reptoSummonHelper(bc, daggerIdxs, daggerCount)

    for i in range(0, daggerCount):
        daggerIdx = daggerIdxs[i]
        dagger = bc.monsters.arr[daggerIdx]
        dagger = Monster()
        dagger.construct(bc, MonsterId.DAGGER, daggerIdx)
        bc.monsters.monstersAlive += 1
        dagger.setMove(MMID.DAGGER_STAB)
        dagger.buff()
        if bc.player.hasRelic():
            dagger.buff(1)

        bc.noOpRollMove()
        bc.monsters.skipTurn.set(daggerIdx, True)

    #    std::cout << "repto summon: " << daggerIdxs[0] << " " << daggerIdxs[1] << '\n'

def getAliveGremlinCount(bc):
    count = 0
    for i in range(0, 3):
        m = bc.monsters.arr[i]
        if not m.isDying():
            count += 1
    return count
