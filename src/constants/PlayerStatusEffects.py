from enum import Enum


class PlayerStatus(Enum):
    # *********    Statuses that use JustApplied  ************
    INVALID = 0
    DOUBLE_DAMAGE = 1
    DRAW_REDUCTION = 2
    FRAIL = 3
    INTANGIBLE = 4
    VULNERABLE = 5
    WEAK = 6

    # *********    DEBUFFS   ************
    BIAS = 7
    CONFUSED = 8
    CONSTRICTED = 9
    ENTANGLED = 10
    FASTING = 11
    HEX = 12
    LOSE_DEXTERITY = 13
    LOSE_STRENGTH = 14
    NO_BLOCK = 15
    NO_DRAW = 16
    WRAITH_FORM = 17

    # *********    POWERS   ************
    # Bool
    BARRICADE = 18
    BLASPHEMER = 19
    CORRUPTION = 20
    ELECTRO = 21
    SURROUNDED = 22
    MASTER_REALITY = 23
    PEN_NIB = 24
    WRATH_NEXT_TURN = 25

    # Counter
    AMPLIFY = 26
    BLUR = 27
    BUFFER = 28
    COLLECT = 29
    DOUBLE_TAP = 30
    DUPLICATION = 31
    ECHO_FORM = 32
    FREE_ATTACK_POWER = 33
    REBOUND = 34
    MANTRA = 35

    # Intensity
    ACCURACY = 36  # todo implement
    AFTER_IMAGE = 37
    BATTLE_HYMN = 38
    BRUTALITY = 39
    BURST = 40
    COMBUST = 41
    CREATIVE_AI = 42
    DARK_EMBRACE = 43
    DEMON_FORM = 44
    DEVA = 45
    DEVOTION = 46
    DRAW_CARD_NEXT_TURN = 47
    ENERGIZED = 48
    ENVENOM = 49
    ESTABLISHMENT = 50
    EVOLVE = 51
    FEEL_NO_PAIN = 52
    FIRE_BREATHING = 53
    FLAME_BARRIER = 54
    FOCUS = 55
    FORESIGHT = 56
    HELLO_WORLD = 57
    INFINITE_BLADES = 58
    JUGGERNAUT = 59
    LIKE_WATER = 60
    LOOP = 61
    MAGNETISM = 62
    MAYHEM = 63
    METALLICIZE = 64
    NEXT_TURN_BLOCK = 65
    NOXIOUS_FUMES = 66
    OMEGA = 67
    PANACHE = 68
    PHANTASMAL = 69
    PLATED_ARMOR = 70
    RAGE = 71
    REGEN = 72
    RITUAL = 73
    RUPTURE = 74
    SADISTIC = 75
    STATIC_DISCHARGE = 76
    THORNS = 77
    THOUSAND_CUTS = 78
    TOOLS_OF_THE_TRADE = 79
    VIGOR = 80
    WAVE_OF_THE_HAND = 81

    # Duration
    EQUILIBRIUM = 82
    ARTIFACT = 83
    DEXTERITY = 84
    STRENGTH = 85

    # special
    THE_BOMB = 86
    def __int__(self):
        return self.value


class Stance(Enum):
    NEUTRAL = 0
    CALM = 1
    WRATH = 2
    DIVINITY = 3


class Orb(Enum):
    EMPTY = 0
    DARK = 1
    FROST = 2
    FUSION = 3
    LIGHTNING = 4
