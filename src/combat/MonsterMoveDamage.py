#
# Created by gamerpuppy on 9/27/2021.
#


from sts import *

import math

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: DamageInfo Monster::getMoveBaseDamage(const BattleContext &bc) const
def getMoveBaseDamage(bc):
    asc2 = bc.ascension >= 2
    asc3 = bc.ascension >= 3
    asc4 = bc.ascension >= 4


    if moveHistory[0] == MonsterMoveId.ACID_SLIME_L_CORROSIVE_SPIT:
        return DamageInfo(12 if asc2 else 11)
    elif moveHistory[0] == MonsterMoveId.ACID_SLIME_L_TACKLE:
        return DamageInfo(18 if asc2 else 16)
    elif moveHistory[0] == MonsterMoveId.ACID_SLIME_M_CORROSIVE_SPIT:
        return DamageInfo(8 if asc2 else 7)
    elif moveHistory[0] == MonsterMoveId.ACID_SLIME_M_TACKLE:
        return DamageInfo(12 if asc2 else 10)
    elif moveHistory[0] == MonsterMoveId.ACID_SLIME_S_TACKLE:
        return DamageInfo(4 if asc2 else 3)

    elif moveHistory[0] == MonsterMoveId.AWAKENED_ONE_SLASH:
        return DamageInfo(20)
    elif moveHistory[0] == MonsterMoveId.AWAKENED_ONE_SOUL_STRIKE:
        return DamageInfo(6, 4)
    elif moveHistory[0] == MonsterMoveId.AWAKENED_ONE_DARK_ECHO:
        return DamageInfo(40)
    elif moveHistory[0] == MonsterMoveId.AWAKENED_ONE_SLUDGE:
        return DamageInfo(18)
    elif moveHistory[0] == MonsterMoveId.AWAKENED_ONE_TACKLE:
        return DamageInfo(10, 3)

    elif moveHistory[0] == MonsterMoveId.BEAR_LUNGE:
        return DamageInfo(10 if asc2 else 9)
    elif moveHistory[0] == MonsterMoveId.BEAR_MAUL:
        return DamageInfo(20 if asc2 else 18)

    elif moveHistory[0] == MonsterMoveId.BLUE_SLAVER_RAKE:
        return DamageInfo(8 if asc2 else 7)
    elif moveHistory[0] == MonsterMoveId.BLUE_SLAVER_STAB:
        return DamageInfo(13 if asc2 else 12)

    elif moveHistory[0] == MonsterMoveId.BOOK_OF_STABBING_MULTI_STAB:
        return DamageInfo(7 if asc3 else 6, miscInfo)
    elif moveHistory[0] == MonsterMoveId.BOOK_OF_STABBING_SINGLE_STAB:
        return DamageInfo(24 if asc3 else 21)

    elif moveHistory[0] == MonsterMoveId.BRONZE_AUTOMATON_FLAIL:
        return DamageInfo(8 if asc4 else 7, 2)
    elif moveHistory[0] == MonsterMoveId.BRONZE_AUTOMATON_HYPER_BEAM:
        return DamageInfo(50 if asc4 else 45)
    elif moveHistory[0] == MonsterMoveId.BRONZE_ORB_BEAM:
        return DamageInfo(8)

    elif moveHistory[0] == MonsterMoveId.BYRD_HEADBUTT:
        return DamageInfo(3)
    elif moveHistory[0] == MonsterMoveId.BYRD_PECK:
        return DamageInfo(1,6 if asc2 else 5)
    elif moveHistory[0] == MonsterMoveId.BYRD_SWOOP:
        return DamageInfo(14 if asc2 else 12)


    elif moveHistory[0] == MonsterMoveId.CENTURION_FURY:
        return DamageInfo(7 if asc2 else 6, 3)
    elif moveHistory[0] == MonsterMoveId.CENTURION_SLASH:
        return DamageInfo(14 if asc2 else 12)

    elif moveHistory[0] == MonsterMoveId.CHOSEN_POKE:
        return DamageInfo(6 if asc2 else 5, 2)
    elif moveHistory[0] == MonsterMoveId.CHOSEN_ZAP:
        return DamageInfo(21 if asc2 else 18)
    elif moveHistory[0] == MonsterMoveId.CHOSEN_DEBILITATE:
        return DamageInfo(12 if asc2 else 10)

    elif moveHistory[0] == MonsterMoveId.CORRUPT_HEART_BLOOD_SHOTS:
        return DamageInfo(2,15 if asc4 else 12)
    elif moveHistory[0] == MonsterMoveId.CORRUPT_HEART_ECHO:
        return DamageInfo(45 if asc4 else 40)

    elif moveHistory[0] == MonsterMoveId.CULTIST_DARK_STRIKE:
        return DamageInfo(6)

    elif moveHistory[0] == MonsterMoveId.DAGGER_STAB:
        return DamageInfo(9)
    elif moveHistory[0] == MonsterMoveId.DAGGER_EXPLODE:
        return DamageInfo(25)

    elif moveHistory[0] == MonsterMoveId.DARKLING_NIP:
        return DamageInfo(miscInfo + (2 if asc2 else 0))
    elif moveHistory[0] == MonsterMoveId.DARKLING_CHOMP:
        return DamageInfo(9 if asc2 else 8)

    elif moveHistory[0] == MonsterMoveId.DECA_BEAM:
        return DamageInfo(12 if asc4 else 10, 2)
    elif moveHistory[0] == MonsterMoveId.DONU_BEAM:
        return DamageInfo(12 if asc4 else 10, 2)

    elif moveHistory[0] == MonsterMoveId.EXPLODER_SLAM:
        return DamageInfo(11 if asc2 else 9)
    elif moveHistory[0] == MonsterMoveId.EXPLODER_EXPLODE:
        return DamageInfo(30) # todo should this be classified as move damage?

    elif moveHistory[0] == MonsterMoveId.FAT_GREMLIN_SMASH:
        return DamageInfo(5 if asc2 else 4)
    elif moveHistory[0] == MonsterMoveId.FUNGI_BEAST_BITE:
        return DamageInfo(6)

    elif moveHistory[0] == MonsterMoveId.GIANT_HEAD_COUNT:
        return DamageInfo(13)
    elif moveHistory[0] == MonsterMoveId.GIANT_HEAD_IT_IS_TIME:
            t = min(bc.getMonsterTurnNumber()-5, 6) * 5
            damage = (40 if asc3 else 30) + t
            return DamageInfo(damage)

    elif moveHistory[0] == MonsterMoveId.GREEN_LOUSE_BITE:
        return DamageInfo(miscInfo)

    elif moveHistory[0] == MonsterMoveId.GREMLIN_LEADER_STAB:
        return DamageInfo(6, 3)

    elif moveHistory[0] == MonsterMoveId.GREMLIN_NOB_RUSH:
        return DamageInfo(16 if asc3 else 14)
    elif moveHistory[0] == MonsterMoveId.GREMLIN_NOB_SKULL_BASH:
        return DamageInfo(8 if asc3 else 6)

    elif moveHistory[0] == MonsterMoveId.GREMLIN_WIZARD_ULTIMATE_BLAST:
        return DamageInfo(30 if asc2 else 25)

    elif moveHistory[0] == MonsterMoveId.HEXAGHOST_DIVIDER:
        return DamageInfo(miscInfo, 6)
    elif moveHistory[0] == MonsterMoveId.HEXAGHOST_INFERNO:
        return DamageInfo(3 if asc4 else 2, 6)
    elif moveHistory[0] == MonsterMoveId.HEXAGHOST_SEAR:
        return DamageInfo(6)
    elif moveHistory[0] == MonsterMoveId.HEXAGHOST_TACKLE:
        return DamageInfo(6 if asc4 else 5, 2)

    elif moveHistory[0] == MonsterMoveId.JAW_WORM_CHOMP:
        return DamageInfo(12 if asc2 else 11)
    elif moveHistory[0] == MonsterMoveId.JAW_WORM_THRASH:
        return DamageInfo(7)

    elif moveHistory[0] == MonsterMoveId.LAGAVULIN_ATTACK:
        return DamageInfo(20 if asc3 else 18)


    elif moveHistory[0] == MonsterMoveId.LOOTER_LUNGE:
        return DamageInfo(14 if asc2 else 12)
    elif moveHistory[0] == MonsterMoveId.LOOTER_MUG:
        return DamageInfo(11 if asc2 else 10)

    elif moveHistory[0] == MonsterMoveId.MAD_GREMLIN_SCRATCH:
        return DamageInfo(5 if asc2 else 4)

    elif moveHistory[0] == MonsterMoveId.MUGGER_MUG:
        return DamageInfo(11 if asc2 else 10)
    elif moveHistory[0] == MonsterMoveId.MUGGER_LUNGE:
        return DamageInfo(18 if asc2 else 16)

    elif moveHistory[0] == MonsterMoveId.MYSTIC_ATTACK_DEBUFF:
        return DamageInfo(9 if asc2 else 8)

    elif moveHistory[0] == MonsterMoveId.NEMESIS_ATTACK:
        return DamageInfo(7 if asc3 else 6, 3)
    elif moveHistory[0] == MonsterMoveId.NEMESIS_SCYTHE:
        return DamageInfo(45)

    elif moveHistory[0] == MonsterMoveId.ORB_WALKER_LASER:
        return DamageInfo(11 if asc2 else 10)
    elif moveHistory[0] == MonsterMoveId.ORB_WALKER_CLAW:
        return DamageInfo(16 if asc2 else 15)

    elif moveHistory[0] == MonsterMoveId.POINTY_ATTACK:
        return DamageInfo(6 if asc2 else 5, 2)

    elif moveHistory[0] == MonsterMoveId.RED_LOUSE_BITE:
        return DamageInfo(miscInfo)

    elif moveHistory[0] == MonsterMoveId.RED_SLAVER_SCRAPE:
        return DamageInfo(9 if asc2 else 8)
    elif moveHistory[0] == MonsterMoveId.RED_SLAVER_STAB:
        return DamageInfo(14 if asc2 else 13)

    elif moveHistory[0] == MonsterMoveId.REPTOMANCER_BIG_BITE:
        return DamageInfo(34 if asc3 else 30)
    elif moveHistory[0] == MonsterMoveId.REPTOMANCER_SNAKE_STRIKE:
        return DamageInfo(16 if asc3 else 13, 2)

    elif moveHistory[0] == MonsterMoveId.REPULSOR_BASH:
        return DamageInfo(13 if asc2 else 11)

    elif moveHistory[0] == MonsterMoveId.ROMEO_AGONIZING_SLASH:
        return DamageInfo(12 if asc2 else 10)
    elif moveHistory[0] == MonsterMoveId.ROMEO_CROSS_SLASH:
        return DamageInfo(17 if asc2 else 15)

    elif moveHistory[0] == MonsterMoveId.SENTRY_BEAM:
        return DamageInfo(10 if asc3 else 9)

    elif moveHistory[0] == MonsterMoveId.SHELLED_PARASITE_DOUBLE_STRIKE:
        return DamageInfo(7 if asc2 else 6, 2)
    elif moveHistory[0] == MonsterMoveId.SHELLED_PARASITE_FELL:
        return DamageInfo(21 if asc2 else 18)
    elif moveHistory[0] == MonsterMoveId.SHELLED_PARASITE_SUCK:
        return DamageInfo(12 if asc2 else 10)

    elif moveHistory[0] == MonsterMoveId.SHIELD_GREMLIN_SHIELD_BASH:
        return DamageInfo(8 if asc2 else 6)

    elif moveHistory[0] == MonsterMoveId.SLIME_BOSS_SLAM:
        return DamageInfo(38 if asc4 else 35)

    elif moveHistory[0] == MonsterMoveId.SNAKE_PLANT_CHOMP:
        return DamageInfo(8 if asc2 else 7, 3)

    elif moveHistory[0] == MonsterMoveId.SNEAKY_GREMLIN_PUNCTURE:
        return DamageInfo(10 if asc2 else 9)

    elif moveHistory[0] == MonsterMoveId.SNECKO_TAIL_WHIP:
        return DamageInfo(10 if asc2 else 8)
    elif moveHistory[0] == MonsterMoveId.SNECKO_BITE:
        return DamageInfo(18 if asc2 else 15)

    elif moveHistory[0] == MonsterMoveId.SPHERIC_GUARDIAN_SLAM:
        return DamageInfo(11 if asc2 else 10, 2)
    elif moveHistory[0] == MonsterMoveId.SPHERIC_GUARDIAN_HARDEN:
        return DamageInfo(11 if asc2 else 10)
    elif moveHistory[0] == MonsterMoveId.SPHERIC_GUARDIAN_ATTACK_DEBUFF:
        return DamageInfo(11 if asc2 else 10)

    elif moveHistory[0] == MonsterMoveId.SPIKER_CUT:
        return DamageInfo(9 if asc2 else 7)

    elif moveHistory[0] == MonsterMoveId.SPIKE_SLIME_L_FLAME_TACKLE:
        return DamageInfo(18 if asc2 else 16)
    elif moveHistory[0] == MonsterMoveId.SPIKE_SLIME_M_FLAME_TACKLE:
        return DamageInfo(10 if asc2 else 8)
    elif moveHistory[0] == MonsterMoveId.SPIKE_SLIME_S_TACKLE:
        return DamageInfo(6 if asc2 else 5)

    elif moveHistory[0] == MonsterMoveId.SPIRE_GROWTH_QUICK_TACKLE:
        return DamageInfo(18 if asc2 else 16)
    elif moveHistory[0] == MonsterMoveId.SPIRE_GROWTH_SMASH:
        return DamageInfo(25 if asc2 else 22)

    elif moveHistory[0] == MonsterMoveId.SPIRE_SHIELD_BASH:
        return DamageInfo(14 if asc3 else 12)
    elif moveHistory[0] == MonsterMoveId.SPIRE_SHIELD_SMASH:
        return DamageInfo(38 if asc3 else 34)

    elif moveHistory[0] == MonsterMoveId.SPIRE_SPEAR_BURN_STRIKE:
        return DamageInfo(6 if asc3 else 5, 2)
    elif moveHistory[0] == MonsterMoveId.SPIRE_SPEAR_SKEWER:
        return DamageInfo(10,4 if asc3 else 3)

    elif moveHistory[0] == MonsterMoveId.TASKMASTER_SCOURING_WHIP:
        return DamageInfo(7)

    elif moveHistory[0] == MonsterMoveId.TORCH_HEAD_TACKLE:
        return DamageInfo(7)

    elif moveHistory[0] == MonsterMoveId.THE_CHAMP_FACE_SLAP:
        return DamageInfo(14 if asc4 else 12)
    elif moveHistory[0] == MonsterMoveId.THE_CHAMP_HEAVY_SLASH:
        return DamageInfo(18 if asc4 else 16)
    elif moveHistory[0] == MonsterMoveId.THE_CHAMP_EXECUTE:
        return DamageInfo(10, 2)

    elif moveHistory[0] == MonsterMoveId.THE_COLLECTOR_FIREBALL:
        return DamageInfo(21 if asc4 else 18)

    elif moveHistory[0] == MonsterMoveId.THE_GUARDIAN_FIERCE_BASH:
        return DamageInfo(36 if asc4 else 32)
    elif moveHistory[0] == MonsterMoveId.THE_GUARDIAN_WHIRLWIND:
        return DamageInfo(5, 4)
    elif moveHistory[0] == MonsterMoveId.THE_GUARDIAN_ROLL_ATTACK:
        return DamageInfo(10 if asc4 else 9)
    elif moveHistory[0] == MonsterMoveId.THE_GUARDIAN_TWIN_SLAM:
        return DamageInfo(8, 2)

    elif moveHistory[0] == MonsterMoveId.THE_MAW_SLAM:
        return DamageInfo(30 if asc2 else 25)
    elif moveHistory[0] == MonsterMoveId.THE_MAW_NOM:
            t = math.trunc((bc.getMonsterTurnNumber() + 1) / float(2))
            return DamageInfo(5, t)

    elif moveHistory[0] == MonsterMoveId.TIME_EATER_REVERBERATE:
        return DamageInfo(8 if asc4 else 7, 3)
    elif moveHistory[0] == MonsterMoveId.TIME_EATER_HEAD_SLAM:
        return DamageInfo(32 if asc4 else 26)

    elif moveHistory[0] == MonsterMoveId.TRANSIENT_ATTACK:
            damage = (40 if asc2 else 30) + 10*(bc.getMonsterTurnNumber()-1)
            return DamageInfo(damage)

    elif moveHistory[0] == MonsterMoveId.WRITHING_MASS_FLAIL:
        return DamageInfo(16 if asc2 else 15)
    elif moveHistory[0] == MonsterMoveId.WRITHING_MASS_MULTI_STRIKE:
        return DamageInfo(9 if asc2 else 7, 3)
    elif moveHistory[0] == MonsterMoveId.WRITHING_MASS_STRONG_STRIKE:
        return DamageInfo(38 if asc2 else 32)

    else:
        return DamageInfo(0, 0)