from enum import Enum


class MonsterStatus(Enum):
    ARTIFACT = 0
    BLOCK_RETURN = 1
    CHOKED = 2
    CORPSE_EXPLOSION = 3
    LOCK_ON = 4
    MARK = 5
    METALLICIZE = 6
    PLATED_ARMOR = 7
    POISON = 8
    REGEN = 9
    SHACKLED = 10
    STRENGTH = 11
    VULNERABLE = 12
    WEAK = 13

    # unique powers : two of these can't be on the same monster
    ANGRY = 14
    BEAT_OF_DEATH = 15
    CURIOSITY = 16
    CURL_UP = 17
    ENRAGE = 18
    FADING = 19
    FLIGHT = 20
    GENERIC_STRENGTH_UP = 21
    INTANGIBLE = 22  # differs from the game in that it always decrements at end of round
    MALLEABLE = 23
    MODE_SHIFT = 24
    RITUAL = 25  # todo just merge this with orb walker strength up
    SLOW = 26  # this should be set just to
    SPORE_CLOUD = 27
    THIEVERY = 28
    THORNS = 29
    TIME_WARP = 30

    # unique powers 2
    INVINCIBLE = 31
    REACTIVE = 32
    SHARP_HIDE = 33

    # bool powers, stored in statusbits
    ASLEEP = 34
    BARRICADE = 35
    MINION = 36
    MINION_LEADER = 37
    PAINFUL_STABS = 38
    REGROW = 39
    SHIFTING = 40
    STASIS = 41

    INVALID = 42


enemyStatusStrings = ["Artifact", "Block Return", "Choked", "Corpse Explosion", "Lock On", "Mark", "Metallicize",
                      "Plated Armor", "Poison", "Regen", "Shackled", "Strength", "Vulnerable", "Weak", "Angry",
                      "Beat Of Death", "Curiosity", "Curl Up", "Enrage", "Fading", "Flight", "Generic Strength Up",
                      "Intangible", "Malleable", "Mode Shift", "Ritual", "Slow", "Spore Cloud", "Thievery", "Thorns",
                      "Time Warp", "Invincible", "Reactive", "Sharp Hide", "Asleep", "Barricade", "Minion",
                      "Minion Leader", "Painful Stabs", "Regrow", "Shifting", "Stasis", "INVALID"]

monsterStatusEnumStrings = ["ARTIFACT", "BLOCK_RETURN", "CHOKED", "CORPSE_EXPLOSION", "LOCK_ON", "MARK", "METALLICIZE",
                            "PLATED_ARMOR", "POISON", "REGEN", "SHACKLED", "STRENGTH", "VULNERABLE", "WEAK", "ANGRY",
                            "BEAT_OF_DEATH", "CURIOSITY", "CURL_UP", "ENRAGE", "FADING", "FLIGHT",
                            "GENERIC_STRENGTH_UP", "INTANGIBLE", "MALLEABLE", "MODE_SHIFT", "RITUAL", "SLOW",
                            "SPORE_CLOUD", "THIEVERY", "THORNS", "TIME_WARP", "INVINCIBLE", "SHARP_HIDE", "ASLEEP",
                            "BARRICADE", "MINION", "MINION_LEADER", "PAINFUL_STABS", "REACTIVE", "REGROW", "SHIFTING",
                            "STASIS", "INVALID"]


def isBooleanPower(s):
    if (s == MonsterStatus.ASLEEP) or (s == MonsterStatus.BARRICADE) or (s == MonsterStatus.MINION) or (
            s == MonsterStatus.MINION_LEADER) or (s == MonsterStatus.PAINFUL_STABS) or (s == MonsterStatus.REGROW) or (
            s == MonsterStatus.SHIFTING) or (s == MonsterStatus.STASIS):
        return True

    else:
        return False
