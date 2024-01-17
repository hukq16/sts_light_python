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
    def __int__(self):
        return self.value


class Orb(Enum):
    EMPTY = 0
    DARK = 1
    FROST = 2
    FUSION = 3
    LIGHTNING = 4
    def __int__(self):
        return self.value


playerStatusStrings = {
    "INVALID", "Double Damage", "Draw Reduction", "Frail", "Intangible",
    "Vulnerable", "Weak", "Bias", "Confused", "Constricted", "Entangled",
    "Fasting", "Hex", "Lose Dexterity", "Lose Strength", "No Block",
    "No Draw", "Wraith Form", "Barricade", "Blasphemer", "Corruption",
    "Electro", "Surrounded", "Master Reality", "Pen Nib", "Wrath Next Turn",
    "Amplify", "Blur", "Buffer", "Collect", "Double Tap", "Duplication",
    "Echo Form", "Free Attack Power", "Rebound", "Mantra", "Accuracy",
    "After Image", "Battle Hymn", "Brutality", "Burst", "Combust",
    "Creative Ai", "Dark Embrace", "Demon Form", "Deva", "Devotion",
    "Draw Card Next Turn", "Energized", "Envenom", "Establishment",
    "Evolve", "Feel No Pain", "Fire Breathing", "Flame Barrier", "Focus",
    "Foresight", "Hello World", "Infinite Blades", "Juggernaut",
    "Like Water", "Loop", "Magnetism", "Mayhem", "Metallicize",
    "Next Turn Block", "Noxious Fumes", "Omega", "Panache", "Phantasmal",
    "Plated Armor", "Rage", "Regen", "Ritual", "Rupture", "Sadistic",
    "Static Discharge", "Thorns", "Thousand Cuts", "Tools Of The Trade",
    "Vigor", "Wave Of The Hand", "Equilibrium", "Artifact", "Dexterity",
    "Strength", "The Bomb",
}

playerStatusEnumStrings = (
    "INVALID", "DOUBLE_DAMAGE", "DRAW_REDUCTION", "FRAIL", "INTANGIBLE",
    "VULNERABLE", "WEAK", "BIAS", "CONFUSED", "CONSTRICTED", "ENTANGLED",
    "FASTING", "HEX", "LOSE_DEXTERITY", "LOSE_STRENGTH", "NO_BLOCK",
    "NO_DRAW", "WRAITH_FORM", "BARRICADE", "BLASPHEMER", "CORRUPTION",
    "ELECTRO", "SURROUNDED", "MASTER_REALITY", "PEN_NIB", "WRATH_NEXT_TURN",
    "AMPLIFY", "BLUR", "BUFFER", "COLLECT", "DOUBLE_TAP", "DUPLICATION",
    "ECHO_FORM", "FREE_ATTACK_POWER", "REBOUND", "MANTRA", "ACCURACY",
    "AFTER_IMAGE", "BATTLE_HYMN", "BRUTALITY", "BURST", "COMBUST",
    "CREATIVE_AI", "DARK_EMBRACE", "DEMON_FORM", "DEVA", "DEVOTION",
    "DRAW_CARD_NEXT_TURN", "ENERGIZED", "ENVENOM", "ESTABLISHMENT",
    "EVOLVE", "FEEL_NO_PAIN", "FIRE_BREATHING", "FLAME_BARRIER", "FOCUS",
    "FORESIGHT", "HELLO_WORLD", "INFINITE_BLADES", "JUGGERNAUT",
    "LIKE_WATER", "LOOP", "MAGNETISM", "MAYHEM", "METALLICIZE",
    "NEXT_TURN_BLOCK", "NOXIOUS_FUMES", "OMEGA", "PANACHE", "PHANTASMAL",
    "PLATED_ARMOR", "RAGE", "REGEN", "RITUAL", "RUPTURE", "SADISTIC",
    "STATIC_DISCHARGE", "THORNS", "THOUSAND_CUTS", "TOOLS_OF_THE_TRADE",
    "VIGOR", "WAVE_OF_THE_HAND", "EQUILIBRIUM", "ARTIFACT", "DEXTERITY",
    "STRENGTH", "THE_BOMB",
)

