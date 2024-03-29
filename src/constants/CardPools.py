﻿from Cards import CardId, CardType


class TransformCardPool:  # this class replaces the original namespace 'TransformCardPool'
    colorCardPool = [
        [CardId.ANGER, CardId.CLEAVE, CardId.WARCRY, CardId.FLEX, CardId.IRON_WAVE, CardId.BODY_SLAM, CardId.TRUE_GRIT,
         CardId.SHRUG_IT_OFF, CardId.CLASH, CardId.THUNDERCLAP, CardId.POMMEL_STRIKE, CardId.TWIN_STRIKE,
         CardId.CLOTHESLINE, CardId.ARMAMENTS, CardId.HAVOC, CardId.HEADBUTT, CardId.WILD_STRIKE, CardId.HEAVY_BLADE,
         CardId.PERFECTED_STRIKE, CardId.SWORD_BOOMERANG, CardId.EVOLVE, CardId.UPPERCUT, CardId.GHOSTLY_ARMOR,
         CardId.FIRE_BREATHING, CardId.DROPKICK, CardId.CARNAGE, CardId.BLOODLETTING, CardId.RUPTURE,
         CardId.SECOND_WIND, CardId.SEARING_BLOW, CardId.BATTLE_TRANCE, CardId.SENTINEL, CardId.ENTRENCH, CardId.RAGE,
         CardId.FEEL_NO_PAIN, CardId.DISARM, CardId.SEEING_RED, CardId.DARK_EMBRACE, CardId.COMBUST, CardId.WHIRLWIND,
         CardId.SEVER_SOUL, CardId.RAMPAGE, CardId.SHOCKWAVE, CardId.METALLICIZE, CardId.BURNING_PACT, CardId.PUMMEL,
         CardId.FLAME_BARRIER, CardId.BLOOD_FOR_BLOOD, CardId.INTIMIDATE, CardId.HEMOKINESIS, CardId.RECKLESS_CHARGE,
         CardId.INFERNAL_BLADE, CardId.DUAL_WIELD, CardId.POWER_THROUGH, CardId.INFLAME, CardId.SPOT_WEAKNESS,
         CardId.DOUBLE_TAP, CardId.DEMON_FORM, CardId.BLUDGEON, CardId.FEED, CardId.LIMIT_BREAK, CardId.CORRUPTION,
         CardId.BARRICADE, CardId.FIEND_FIRE, CardId.BERSERK, CardId.IMPERVIOUS, CardId.JUGGERNAUT, CardId.BRUTALITY,
         CardId.REAPER, CardId.EXHUME, CardId.OFFERING, CardId.IMMOLATE],
        [CardId.CLOAK_AND_DAGGER, CardId.SNEAKY_STRIKE, CardId.DEADLY_POISON, CardId.DAGGER_SPRAY, CardId.BANE,
         CardId.BLADE_DANCE, CardId.DEFLECT, CardId.DAGGER_THROW, CardId.POISONED_STAB, CardId.ACROBATICS,
         CardId.QUICK_SLASH, CardId.SLICE, CardId.BACKFLIP, CardId.OUTMANEUVER, CardId.PREPARED, CardId.PIERCING_WAIL,
         CardId.SUCKER_PUNCH, CardId.DODGE_AND_ROLL, CardId.FLYING_KNEE, CardId.PREDATOR, CardId.ALL_OUT_ATTACK,
         CardId.DISTRACTION, CardId.FOOTWORK, CardId.ACCURACY, CardId.MASTERFUL_STAB, CardId.FLECHETTES,
         CardId.CONCENTRATE, CardId.BOUNCING_FLASK, CardId.BACKSTAB, CardId.DASH, CardId.EVISCERATE, CardId.REFLEX,
         CardId.INFINITE_BLADES, CardId.NOXIOUS_FUMES, CardId.HEEL_HOOK, CardId.TERROR, CardId.WELL_LAID_PLANS,
         CardId.FINISHER, CardId.ESCAPE_PLAN, CardId.CALCULATED_GAMBLE, CardId.SKEWER, CardId.RIDDLE_WITH_HOLES,
         CardId.ENDLESS_AGONY, CardId.SETUP, CardId.BLUR, CardId.CALTROPS, CardId.CHOKE, CardId.EXPERTISE,
         CardId.TACTICIAN, CardId.CATALYST, CardId.LEG_SWEEP, CardId.CRIPPLING_CLOUD, CardId.ALCHEMIZE,
         CardId.CORPSE_EXPLOSION, CardId.MALAISE, CardId.PHANTASMAL_KILLER, CardId.DIE_DIE_DIE, CardId.ADRENALINE,
         CardId.ENVENOM, CardId.DOPPELGANGER, CardId.BURST, CardId.WRAITH_FORM, CardId.TOOLS_OF_THE_TRADE,
         CardId.NIGHTMARE, CardId.UNLOAD, CardId.AFTER_IMAGE, CardId.BULLET_TIME, CardId.STORM_OF_STEEL,
         CardId.GLASS_KNIFE, CardId.A_THOUSAND_CUTS, CardId.GRAND_FINALE, 0],
        [CardId.GO_FOR_THE_EYES, CardId.BALL_LIGHTNING, CardId.STREAMLINE, CardId.RECURSION, CardId.COMPILE_DRIVER,
         CardId.BARRAGE, CardId.STACK, CardId.REBOUND, CardId.CLAW, CardId.COOLHEADED, CardId.TURBO,
         CardId.SWEEPING_BEAM, CardId.CHARGE_BATTERY, CardId.HOLOGRAM, CardId.BEAM_CELL, CardId.LEAP, CardId.COLD_SNAP,
         CardId.STEAM_BARRIER, CardId.DOOM_AND_GLOOM, CardId.DEFRAGMENT, CardId.CAPACITOR, CardId.WHITE_NOISE,
         CardId.SKIM, CardId.RECYCLE, CardId.SCRAPE, CardId.BULLSEYE, CardId.REPROGRAM, CardId.AUTO_SHIELDS,
         CardId.REINFORCED_BODY, CardId.DOUBLE_ENERGY, CardId.DARKNESS, CardId.RIP_AND_TEAR, CardId.FTL,
         CardId.FORCE_FIELD, CardId.EQUILIBRIUM, CardId.TEMPEST, CardId.HEATSINKS, CardId.STATIC_DISCHARGE,
         CardId.BOOT_SEQUENCE, CardId.CHILL, CardId.LOOP, CardId.SELF_REPAIR, CardId.MELTER, CardId.CHAOS,
         CardId.BLIZZARD, CardId.AGGREGATE, CardId.FUSION, CardId.CONSUME, CardId.GLACIER, CardId.SUNDER,
         CardId.HELLO_WORLD, CardId.OVERCLOCK, CardId.GENETIC_ALGORITHM, CardId.STORM, CardId.MULTI_CAST,
         CardId.HYPERBEAM, CardId.THUNDER_STRIKE, CardId.BIASED_COGNITION, CardId.MACHINE_LEARNING,
         CardId.ELECTRODYNAMICS, CardId.BUFFER, CardId.RAINBOW, CardId.SEEK, CardId.METEOR_STRIKE, CardId.ECHO_FORM,
         CardId.ALL_FOR_ONE, CardId.REBOOT, CardId.AMPLIFY, CardId.CREATIVE_AI, CardId.FISSION, CardId.CORE_SURGE, 0],
        [CardId.CONSECRATE, CardId.BOWLING_BASH, CardId.FLYING_SLEEVES, CardId.HALT, CardId.JUST_LUCKY,
         CardId.FLURRY_OF_BLOWS, CardId.PROTECT, CardId.THIRD_EYE, CardId.CRESCENDO, CardId.TRANQUILITY,
         CardId.EMPTY_BODY, CardId.SASH_WHIP, CardId.CUT_THROUGH_FATE, CardId.FOLLOW_UP, CardId.PRESSURE_POINTS,
         CardId.CRUSH_JOINTS, CardId.EVALUATE, CardId.PROSTRATE, CardId.EMPTY_FIST, CardId.PRAY, CardId.SIGNATURE_MOVE,
         CardId.WEAVE, CardId.EMPTY_MIND, CardId.NIRVANA, CardId.TANTRUM, CardId.CONCLUDE, CardId.WORSHIP,
         CardId.SWIVEL, CardId.PERSEVERANCE, CardId.MEDITATE, CardId.STUDY, CardId.WAVE_OF_THE_HAND,
         CardId.SANDS_OF_TIME, CardId.FEAR_NO_EVIL, CardId.REACH_HEAVEN, CardId.MENTAL_FORTRESS, CardId.DECEIVE_REALITY,
         CardId.RUSHDOWN, CardId.INNER_PEACE, CardId.COLLECT, CardId.WREATH_OF_FLAME, CardId.WALLOP,
         CardId.CARVE_REALITY, CardId.FASTING, CardId.LIKE_WATER, CardId.FOREIGN_INFLUENCE, CardId.WINDMILL_STRIKE,
         CardId.INDIGNATION, CardId.BATTLE_HYMN, CardId.TALK_TO_THE_HAND, CardId.SANCTITY, CardId.FORESIGHT,
         CardId.SIMMERING_FURY, CardId.WHEEL_KICK, CardId.JUDGMENT, CardId.CONJURE_BLADE, CardId.MASTER_REALITY,
         CardId.BRILLIANCE, CardId.DEVOTION, CardId.BLASPHEMY, CardId.RAGNAROK, CardId.LESSON_LEARNED, CardId.SCRAWL,
         CardId.VAULT, CardId.ALPHA, CardId.WISH, CardId.OMNISCIENCE, CardId.ESTABLISHMENT, CardId.SPIRIT_SHIELD,
         CardId.DEVA_FORM, CardId.DEUS_EX_MACHINA, 0]]
    cardPoolSize = [72, 71, 71, 71]

    def getPoolSizeForClass(cc):
        return TransformCardPool.cardPoolSize[int(cc)]


class TrulyRandomCardPool:  # this class replaces the original namespace 'TrulyRandomCardPool'
    POOL = [[CardId.SWORD_BOOMERANG, CardId.PERFECTED_STRIKE, CardId.HEAVY_BLADE, CardId.WILD_STRIKE, CardId.HEADBUTT,
             CardId.HAVOC, CardId.ARMAMENTS, CardId.CLOTHESLINE, CardId.TWIN_STRIKE, CardId.POMMEL_STRIKE,
             CardId.THUNDERCLAP, CardId.CLASH, CardId.SHRUG_IT_OFF, CardId.TRUE_GRIT, CardId.BODY_SLAM,
             CardId.IRON_WAVE, CardId.FLEX, CardId.WARCRY, CardId.CLEAVE, CardId.ANGER, CardId.EVOLVE, CardId.UPPERCUT,
             CardId.GHOSTLY_ARMOR, CardId.FIRE_BREATHING, CardId.DROPKICK, CardId.CARNAGE, CardId.BLOODLETTING,
             CardId.RUPTURE, CardId.SECOND_WIND, CardId.SEARING_BLOW, CardId.BATTLE_TRANCE, CardId.SENTINEL,
             CardId.ENTRENCH, CardId.RAGE, CardId.FEEL_NO_PAIN, CardId.DISARM, CardId.SEEING_RED, CardId.DARK_EMBRACE,
             CardId.COMBUST, CardId.WHIRLWIND, CardId.SEVER_SOUL, CardId.RAMPAGE, CardId.SHOCKWAVE, CardId.METALLICIZE,
             CardId.BURNING_PACT, CardId.PUMMEL, CardId.FLAME_BARRIER, CardId.BLOOD_FOR_BLOOD, CardId.INTIMIDATE,
             CardId.HEMOKINESIS, CardId.RECKLESS_CHARGE, CardId.INFERNAL_BLADE, CardId.DUAL_WIELD, CardId.POWER_THROUGH,
             CardId.INFLAME, CardId.SPOT_WEAKNESS, CardId.DOUBLE_TAP, CardId.DEMON_FORM, CardId.BLUDGEON, CardId.FEED,
             CardId.LIMIT_BREAK, CardId.CORRUPTION, CardId.BARRICADE, CardId.FIEND_FIRE, CardId.BERSERK,
             CardId.IMPERVIOUS, CardId.JUGGERNAUT, CardId.BRUTALITY, CardId.REAPER, CardId.EXHUME, CardId.OFFERING,
             CardId.IMMOLATE],
            [CardId.FLYING_KNEE, CardId.DODGE_AND_ROLL, CardId.SUCKER_PUNCH, CardId.PIERCING_WAIL, CardId.PREPARED,
             CardId.OUTMANEUVER, CardId.BACKFLIP, CardId.SLICE, CardId.QUICK_SLASH, CardId.ACROBATICS,
             CardId.POISONED_STAB, CardId.DAGGER_THROW, CardId.DEFLECT, CardId.BLADE_DANCE, CardId.BANE,
             CardId.DAGGER_SPRAY, CardId.DEADLY_POISON, CardId.SNEAKY_STRIKE, CardId.CLOAK_AND_DAGGER, CardId.PREDATOR,
             CardId.ALL_OUT_ATTACK, CardId.DISTRACTION, CardId.FOOTWORK, CardId.ACCURACY, CardId.MASTERFUL_STAB,
             CardId.FLECHETTES, CardId.CONCENTRATE, CardId.BOUNCING_FLASK, CardId.BACKSTAB, CardId.DASH,
             CardId.EVISCERATE, CardId.REFLEX, CardId.INFINITE_BLADES, CardId.NOXIOUS_FUMES, CardId.HEEL_HOOK,
             CardId.TERROR, CardId.WELL_LAID_PLANS, CardId.FINISHER, CardId.ESCAPE_PLAN, CardId.CALCULATED_GAMBLE,
             CardId.SKEWER, CardId.RIDDLE_WITH_HOLES, CardId.ENDLESS_AGONY, CardId.SETUP, CardId.BLUR, CardId.CALTROPS,
             CardId.CHOKE, CardId.EXPERTISE, CardId.TACTICIAN, CardId.CATALYST, CardId.LEG_SWEEP,
             CardId.CRIPPLING_CLOUD, CardId.ALCHEMIZE, CardId.CORPSE_EXPLOSION, CardId.MALAISE,
             CardId.PHANTASMAL_KILLER, CardId.DIE_DIE_DIE, CardId.ADRENALINE, CardId.ENVENOM, CardId.DOPPELGANGER,
             CardId.BURST, CardId.WRAITH_FORM, CardId.TOOLS_OF_THE_TRADE, CardId.NIGHTMARE, CardId.UNLOAD,
             CardId.AFTER_IMAGE, CardId.BULLET_TIME, CardId.STORM_OF_STEEL, CardId.GLASS_KNIFE, CardId.A_THOUSAND_CUTS,
             CardId.GRAND_FINALE, 0],
            [CardId.STEAM_BARRIER, CardId.COLD_SNAP, CardId.LEAP, CardId.BEAM_CELL, CardId.HOLOGRAM,
             CardId.CHARGE_BATTERY, CardId.SWEEPING_BEAM, CardId.TURBO, CardId.COOLHEADED, CardId.CLAW, CardId.REBOUND,
             CardId.STACK, CardId.BARRAGE, CardId.COMPILE_DRIVER, CardId.RECURSION, CardId.STREAMLINE,
             CardId.BALL_LIGHTNING, CardId.GO_FOR_THE_EYES, CardId.DOOM_AND_GLOOM, CardId.DEFRAGMENT, CardId.CAPACITOR,
             CardId.WHITE_NOISE, CardId.SKIM, CardId.RECYCLE, CardId.SCRAPE, CardId.BULLSEYE, CardId.REPROGRAM,
             CardId.AUTO_SHIELDS, CardId.REINFORCED_BODY, CardId.DOUBLE_ENERGY, CardId.DARKNESS, CardId.RIP_AND_TEAR,
             CardId.FTL, CardId.FORCE_FIELD, CardId.EQUILIBRIUM, CardId.TEMPEST, CardId.HEATSINKS,
             CardId.STATIC_DISCHARGE, CardId.BOOT_SEQUENCE, CardId.CHILL, CardId.LOOP, CardId.SELF_REPAIR,
             CardId.MELTER, CardId.CHAOS, CardId.BLIZZARD, CardId.AGGREGATE, CardId.FUSION, CardId.CONSUME,
             CardId.GLACIER, CardId.SUNDER, CardId.HELLO_WORLD, CardId.OVERCLOCK, CardId.GENETIC_ALGORITHM,
             CardId.STORM, CardId.MULTI_CAST, CardId.HYPERBEAM, CardId.THUNDER_STRIKE, CardId.BIASED_COGNITION,
             CardId.MACHINE_LEARNING, CardId.ELECTRODYNAMICS, CardId.BUFFER, CardId.RAINBOW, CardId.SEEK,
             CardId.METEOR_STRIKE, CardId.ECHO_FORM, CardId.ALL_FOR_ONE, CardId.REBOOT, CardId.AMPLIFY,
             CardId.CREATIVE_AI, CardId.FISSION, CardId.CORE_SURGE, 0],
            [CardId.EMPTY_FIST, CardId.PROSTRATE, CardId.EVALUATE, CardId.CRUSH_JOINTS, CardId.PRESSURE_POINTS,
             CardId.FOLLOW_UP, CardId.CUT_THROUGH_FATE, CardId.SASH_WHIP, CardId.EMPTY_BODY, CardId.TRANQUILITY,
             CardId.CRESCENDO, CardId.THIRD_EYE, CardId.PROTECT, CardId.FLURRY_OF_BLOWS, CardId.JUST_LUCKY, CardId.HALT,
             CardId.FLYING_SLEEVES, CardId.BOWLING_BASH, CardId.CONSECRATE, CardId.PRAY, CardId.SIGNATURE_MOVE,
             CardId.WEAVE, CardId.EMPTY_MIND, CardId.NIRVANA, CardId.TANTRUM, CardId.CONCLUDE, CardId.WORSHIP,
             CardId.SWIVEL, CardId.PERSEVERANCE, CardId.MEDITATE, CardId.STUDY, CardId.WAVE_OF_THE_HAND,
             CardId.SANDS_OF_TIME, CardId.FEAR_NO_EVIL, CardId.REACH_HEAVEN, CardId.MENTAL_FORTRESS,
             CardId.DECEIVE_REALITY, CardId.RUSHDOWN, CardId.INNER_PEACE, CardId.COLLECT, CardId.WREATH_OF_FLAME,
             CardId.WALLOP, CardId.CARVE_REALITY, CardId.FASTING, CardId.LIKE_WATER, CardId.FOREIGN_INFLUENCE,
             CardId.WINDMILL_STRIKE, CardId.INDIGNATION, CardId.BATTLE_HYMN, CardId.TALK_TO_THE_HAND, CardId.SANCTITY,
             CardId.FORESIGHT, CardId.SIMMERING_FURY, CardId.WHEEL_KICK, CardId.JUDGMENT, CardId.CONJURE_BLADE,
             CardId.MASTER_REALITY, CardId.BRILLIANCE, CardId.DEVOTION, CardId.BLASPHEMY, CardId.RAGNAROK,
             CardId.LESSON_LEARNED, CardId.SCRAWL, CardId.VAULT, CardId.ALPHA, CardId.WISH, CardId.OMNISCIENCE,
             CardId.ESTABLISHMENT, CardId.SPIRIT_SHIELD, CardId.DEVA_FORM, CardId.DEUS_EX_MACHINA, 0]]
    poolSize = [72, 71, 71, 71]

    # C++ TO PYTHON CONVERTER WARNING: Python has no equivalent to methods returning pointers to value types:
    # ORIGINAL LINE: static const CardId * getPoolForClass(CharacterClass cc)
    def getPoolForClass(cc):
        return TrulyRandomCardPool.POOL[int(cc)]

    def getPoolSizeForClass(cc):
        return TrulyRandomCardPool.poolSize[int(cc)]


class AnyColorTypeCardPool:  # this class replaces the original namespace 'AnyColorTypeCardPool'
    COMMONCARDS = [CardId.ACROBATICS, CardId.ANGER, CardId.ARMAMENTS, CardId.BACKFLIP, CardId.BALL_LIGHTNING,
                   CardId.BANE, CardId.BARRAGE, CardId.BEAM_CELL, CardId.BLADE_DANCE, CardId.BODY_SLAM,
                   CardId.BOWLING_BASH, CardId.CLASH, CardId.TRANQUILITY, CardId.CLEAVE, CardId.CLOAK_AND_DAGGER,
                   CardId.CLOTHESLINE, CardId.COLD_SNAP, CardId.COMPILE_DRIVER, CardId.CONSECRATE,
                   CardId.CHARGE_BATTERY, CardId.COOLHEADED, CardId.CRESCENDO, CardId.CRUSH_JOINTS,
                   CardId.CUT_THROUGH_FATE, CardId.DAGGER_SPRAY, CardId.DAGGER_THROW, CardId.DEADLY_POISON,
                   CardId.DEFLECT, CardId.DODGE_AND_ROLL, CardId.EMPTY_BODY, CardId.EMPTY_FIST, CardId.EVALUATE,
                   CardId.FLEX, CardId.FLURRY_OF_BLOWS, CardId.FLYING_KNEE, CardId.FLYING_SLEEVES, CardId.FOLLOW_UP,
                   CardId.CLAW, CardId.GO_FOR_THE_EYES, CardId.HALT, CardId.HAVOC, CardId.HEADBUTT, CardId.HEAVY_BLADE,
                   CardId.HOLOGRAM, CardId.IRON_WAVE, CardId.JUST_LUCKY, CardId.LEAP, CardId.OUTMANEUVER,
                   CardId.PRESSURE_POINTS, CardId.PERFECTED_STRIKE, CardId.PIERCING_WAIL, CardId.POISONED_STAB,
                   CardId.POMMEL_STRIKE, CardId.PREPARED, CardId.PROSTRATE, CardId.PROTECT, CardId.QUICK_SLASH,
                   CardId.REBOUND, CardId.RECURSION, CardId.SASH_WHIP, CardId.SHRUG_IT_OFF, CardId.SLICE, CardId.STACK,
                   CardId.STEAM_BARRIER, CardId.STREAMLINE, CardId.SUCKER_PUNCH, CardId.SWEEPING_BEAM,
                   CardId.SWORD_BOOMERANG, CardId.THIRD_EYE, CardId.THUNDERCLAP, CardId.TRUE_GRIT, CardId.TURBO,
                   CardId.TWIN_STRIKE, CardId.SNEAKY_STRIKE, CardId.WARCRY, CardId.WILD_STRIKE]
    COMMONPOOLSIZE = 76

    UNCOMMONCARDS = [CardId.ACCURACY, CardId.RUSHDOWN, CardId.AGGREGATE, CardId.ALL_OUT_ATTACK, CardId.AUTO_SHIELDS,
                     CardId.BACKSTAB, CardId.BANDAGE_UP, CardId.BATTLE_TRANCE, CardId.BATTLE_HYMN, CardId.BLIND,
                     CardId.BLIZZARD, CardId.BLOOD_FOR_BLOOD, CardId.BLOODLETTING, CardId.BLUR, CardId.BOOT_SEQUENCE,
                     CardId.BOUNCING_FLASK, CardId.BURNING_PACT, CardId.CALCULATED_GAMBLE, CardId.CALTROPS,
                     CardId.CAPACITOR, CardId.CARNAGE, CardId.CARVE_REALITY, CardId.CATALYST, CardId.CHAOS,
                     CardId.CHILL, CardId.CHOKE, CardId.COLLECT, CardId.COMBUST, CardId.CONCENTRATE, CardId.CONCLUDE,
                     CardId.CONSUME, CardId.CRIPPLING_CLOUD, CardId.DARK_EMBRACE, CardId.DARK_SHACKLES, CardId.DARKNESS,
                     CardId.DASH, CardId.DECEIVE_REALITY, CardId.DEEP_BREATH, CardId.DEFRAGMENT, CardId.DISARM,
                     CardId.DISCOVERY, CardId.DISTRACTION, CardId.DOOM_AND_GLOOM, CardId.DOUBLE_ENERGY,
                     CardId.DRAMATIC_ENTRANCE, CardId.DROPKICK, CardId.DUAL_WIELD, CardId.EMPTY_MIND,
                     CardId.ENDLESS_AGONY, CardId.ENLIGHTENMENT, CardId.ENTRENCH, CardId.ESCAPE_PLAN, CardId.EVISCERATE,
                     CardId.EVOLVE, CardId.EXPERTISE, CardId.FTL, CardId.FASTING, CardId.FEAR_NO_EVIL,
                     CardId.FEEL_NO_PAIN, CardId.FINESSE, CardId.FINISHER, CardId.FIRE_BREATHING, CardId.FLAME_BARRIER,
                     CardId.FLASH_OF_STEEL, CardId.FLECHETTES, CardId.FOOTWORK, CardId.FORCE_FIELD,
                     CardId.FOREIGN_INFLUENCE, CardId.FORETHOUGHT, CardId.FUSION, CardId.GENETIC_ALGORITHM,
                     CardId.GHOSTLY_ARMOR, CardId.GLACIER, CardId.GOOD_INSTINCTS, CardId.HEATSINKS, CardId.HEEL_HOOK,
                     CardId.HELLO_WORLD, CardId.HEMOKINESIS, CardId.IMPATIENCE, CardId.INDIGNATION,
                     CardId.INFERNAL_BLADE, CardId.INFINITE_BLADES, CardId.INFLAME, CardId.INNER_PEACE,
                     CardId.INTIMIDATE, CardId.JACK_OF_ALL_TRADES, CardId.LEG_SWEEP, CardId.LIKE_WATER, CardId.BULLSEYE,
                     CardId.LOOP, CardId.MADNESS, CardId.MASTERFUL_STAB, CardId.MEDITATE, CardId.MELTER,
                     CardId.MENTAL_FORTRESS, CardId.METALLICIZE, CardId.MIND_BLAST, CardId.NIRVANA,
                     CardId.NOXIOUS_FUMES, CardId.PANACEA, CardId.PANIC_BUTTON, CardId.PERSEVERANCE,
                     CardId.POWER_THROUGH, CardId.PRAY, CardId.PREDATOR, CardId.PUMMEL, CardId.PURITY, CardId.RAGE,
                     CardId.RAMPAGE, CardId.REACH_HEAVEN, CardId.RECKLESS_CHARGE, CardId.RECYCLE, CardId.REFLEX,
                     CardId.REINFORCED_BODY, CardId.REPROGRAM, CardId.RIDDLE_WITH_HOLES, CardId.RIP_AND_TEAR,
                     CardId.RUPTURE, CardId.SANCTITY, CardId.SANDS_OF_TIME, CardId.SCRAPE, CardId.SEARING_BLOW,
                     CardId.SECOND_WIND, CardId.SEEING_RED, CardId.SELF_REPAIR, CardId.SENTINEL, CardId.SETUP,
                     CardId.SEVER_SOUL, CardId.SHOCKWAVE, CardId.SIGNATURE_MOVE, CardId.SKEWER, CardId.SKIM,
                     CardId.SPOT_WEAKNESS, CardId.STATIC_DISCHARGE, CardId.OVERCLOCK, CardId.STORM, CardId.STUDY,
                     CardId.SUNDER, CardId.SWIFT_STRIKE, CardId.SWIVEL, CardId.TACTICIAN, CardId.TALK_TO_THE_HAND,
                     CardId.TANTRUM, CardId.TEMPEST, CardId.TERROR, CardId.TRIP, CardId.EQUILIBRIUM, CardId.UPPERCUT,
                     CardId.SIMMERING_FURY, CardId.WALLOP, CardId.WAVE_OF_THE_HAND, CardId.WEAVE,
                     CardId.WELL_LAID_PLANS, CardId.WHEEL_KICK, CardId.WHIRLWIND, CardId.WHITE_NOISE,
                     CardId.WINDMILL_STRIKE, CardId.FORESIGHT, CardId.WORSHIP, CardId.WREATH_OF_FLAME]
    UNCOMMONPOOLSIZE = 160

    RARECARDS = [CardId.A_THOUSAND_CUTS, CardId.ADRENALINE, CardId.AFTER_IMAGE, CardId.ALL_FOR_ONE, CardId.ALPHA,
                 CardId.AMPLIFY, CardId.APOTHEOSIS, CardId.BARRICADE, CardId.BERSERK, CardId.BIASED_COGNITION,
                 CardId.BLASPHEMY, CardId.BLUDGEON, CardId.BRILLIANCE, CardId.BRUTALITY, CardId.BUFFER,
                 CardId.BULLET_TIME, CardId.BURST, CardId.CHRYSALIS, CardId.CONJURE_BLADE, CardId.CORE_SURGE,
                 CardId.CORPSE_EXPLOSION, CardId.CORRUPTION, CardId.CREATIVE_AI, CardId.DEMON_FORM,
                 CardId.DEUS_EX_MACHINA, CardId.DEVA_FORM, CardId.DEVOTION, CardId.DIE_DIE_DIE, CardId.DOPPELGANGER,
                 CardId.DOUBLE_TAP, CardId.ECHO_FORM, CardId.ELECTRODYNAMICS, CardId.ENVENOM, CardId.ESTABLISHMENT,
                 CardId.EXHUME, CardId.FEED, CardId.FIEND_FIRE, CardId.FISSION, CardId.GLASS_KNIFE, CardId.GRAND_FINALE,
                 CardId.HAND_OF_GREED, CardId.HYPERBEAM, CardId.IMMOLATE, CardId.IMPERVIOUS, CardId.JUDGMENT,
                 CardId.JUGGERNAUT, CardId.LESSON_LEARNED, CardId.LIMIT_BREAK, CardId.MACHINE_LEARNING,
                 CardId.MAGNETISM, CardId.MALAISE, CardId.MASTER_OF_STRATEGY, CardId.MASTER_REALITY, CardId.MAYHEM,
                 CardId.METAMORPHOSIS, CardId.METEOR_STRIKE, CardId.MULTI_CAST, CardId.NIGHTMARE, CardId.OFFERING,
                 CardId.OMNISCIENCE, CardId.PANACHE, CardId.PHANTASMAL_KILLER, CardId.RAGNAROK, CardId.RAINBOW,
                 CardId.REAPER, CardId.REBOOT, CardId.SADISTIC_NATURE, CardId.SCRAWL, CardId.SECRET_TECHNIQUE,
                 CardId.SECRET_WEAPON, CardId.SEEK, CardId.SPIRIT_SHIELD, CardId.STORM_OF_STEEL, CardId.THE_BOMB,
                 CardId.THINKING_AHEAD, CardId.THUNDER_STRIKE, CardId.TOOLS_OF_THE_TRADE, CardId.TRANSMUTATION,
                 CardId.UNLOAD, CardId.VAULT, CardId.ALCHEMIZE, CardId.VIOLENCE, CardId.WISH, CardId.WRAITH_FORM]
    RAREPOOLSIZE = 84


CURSECARDPOOL = [CardId.REGRET, CardId.INJURY, CardId.SHAME, CardId.PARASITE, CardId.NORMALITY, CardId.DOUBT,
                 CardId.WRITHE, CardId.PAIN, CardId.DECAY, CardId.CLUMSY]
CURSECARDPOOLSIZE = 10

SRCCOLORLESSCARDPOOL = [CardId.APOTHEOSIS, CardId.BANDAGE_UP, CardId.BLIND, CardId.CHRYSALIS, CardId.DARK_SHACKLES,
                        CardId.DEEP_BREATH, CardId.DISCOVERY, CardId.DRAMATIC_ENTRANCE, CardId.ENLIGHTENMENT,
                        CardId.FINESSE, CardId.FLASH_OF_STEEL, CardId.FORETHOUGHT, CardId.GOOD_INSTINCTS,
                        CardId.HAND_OF_GREED, CardId.IMPATIENCE, CardId.JACK_OF_ALL_TRADES, CardId.MADNESS,
                        CardId.MAGNETISM, CardId.MASTER_OF_STRATEGY, CardId.MAYHEM, CardId.METAMORPHOSIS,
                        CardId.MIND_BLAST, CardId.PANACEA, CardId.PANACHE, CardId.PANIC_BUTTON, CardId.PURITY,
                        CardId.SADISTIC_NATURE, CardId.SECRET_TECHNIQUE, CardId.SECRET_WEAPON, CardId.SWIFT_STRIKE,
                        CardId.THE_BOMB, CardId.THINKING_AHEAD, CardId.TRANSMUTATION, CardId.TRIP, CardId.VIOLENCE]
SRCCOLORLESSCARDPOOLSIZE = 35

BASECOLORLESSPOOL = [CardId.DARK_SHACKLES, CardId.SADISTIC_NATURE, CardId.PANIC_BUTTON, CardId.TRIP,
                     CardId.DRAMATIC_ENTRANCE, CardId.IMPATIENCE, CardId.THE_BOMB, CardId.BLIND, CardId.BANDAGE_UP,
                     CardId.SECRET_TECHNIQUE, CardId.DEEP_BREATH, CardId.VIOLENCE, CardId.PANACHE, CardId.SECRET_WEAPON,
                     CardId.APOTHEOSIS, CardId.MAYHEM, CardId.HAND_OF_GREED, CardId.FLASH_OF_STEEL, CardId.FORETHOUGHT,
                     CardId.ENLIGHTENMENT, CardId.PURITY, CardId.PANACEA, CardId.TRANSMUTATION, CardId.CHRYSALIS,
                     CardId.DISCOVERY, CardId.FINESSE, CardId.MAGNETISM, CardId.MASTER_OF_STRATEGY,
                     CardId.GOOD_INSTINCTS, CardId.SWIFT_STRIKE, CardId.JACK_OF_ALL_TRADES, CardId.METAMORPHOSIS,
                     CardId.MIND_BLAST, CardId.THINKING_AHEAD, CardId.MADNESS]


class RarityCardPool:  # this class replaces the original namespace 'RarityCardPool'

    cardBlob = [CardId.ANGER, CardId.CLEAVE, CardId.WARCRY, CardId.FLEX, CardId.IRON_WAVE, CardId.BODY_SLAM,
                CardId.TRUE_GRIT, CardId.SHRUG_IT_OFF, CardId.CLASH, CardId.THUNDERCLAP, CardId.POMMEL_STRIKE,
                CardId.TWIN_STRIKE, CardId.CLOTHESLINE, CardId.ARMAMENTS, CardId.HAVOC, CardId.HEADBUTT,
                CardId.WILD_STRIKE, CardId.HEAVY_BLADE, CardId.PERFECTED_STRIKE, CardId.SWORD_BOOMERANG,
                CardId.SPOT_WEAKNESS, CardId.INFLAME, CardId.POWER_THROUGH, CardId.DUAL_WIELD, CardId.INFERNAL_BLADE,
                CardId.RECKLESS_CHARGE, CardId.HEMOKINESIS, CardId.INTIMIDATE, CardId.BLOOD_FOR_BLOOD,
                CardId.FLAME_BARRIER, CardId.PUMMEL, CardId.BURNING_PACT, CardId.METALLICIZE, CardId.SHOCKWAVE,
                CardId.RAMPAGE, CardId.SEVER_SOUL, CardId.WHIRLWIND, CardId.COMBUST, CardId.DARK_EMBRACE,
                CardId.SEEING_RED, CardId.DISARM, CardId.FEEL_NO_PAIN, CardId.RAGE, CardId.ENTRENCH, CardId.SENTINEL,
                CardId.BATTLE_TRANCE, CardId.SEARING_BLOW, CardId.SECOND_WIND, CardId.RUPTURE, CardId.BLOODLETTING,
                CardId.CARNAGE, CardId.DROPKICK, CardId.FIRE_BREATHING, CardId.GHOSTLY_ARMOR, CardId.UPPERCUT,
                CardId.EVOLVE, CardId.IMMOLATE, CardId.OFFERING, CardId.EXHUME, CardId.REAPER, CardId.BRUTALITY,
                CardId.JUGGERNAUT, CardId.IMPERVIOUS, CardId.BERSERK, CardId.FIEND_FIRE, CardId.BARRICADE,
                CardId.CORRUPTION, CardId.LIMIT_BREAK, CardId.FEED, CardId.BLUDGEON, CardId.DEMON_FORM,
                CardId.DOUBLE_TAP, CardId.CLOAK_AND_DAGGER, CardId.SNEAKY_STRIKE, CardId.DEADLY_POISON,
                CardId.DAGGER_SPRAY, CardId.BANE, CardId.BLADE_DANCE, CardId.DEFLECT, CardId.DAGGER_THROW,
                CardId.POISONED_STAB, CardId.ACROBATICS, CardId.QUICK_SLASH, CardId.SLICE, CardId.BACKFLIP,
                CardId.OUTMANEUVER, CardId.PREPARED, CardId.PIERCING_WAIL, CardId.SUCKER_PUNCH, CardId.DODGE_AND_ROLL,
                CardId.FLYING_KNEE, CardId.CRIPPLING_CLOUD, CardId.LEG_SWEEP, CardId.CATALYST, CardId.TACTICIAN,
                CardId.EXPERTISE, CardId.CHOKE, CardId.CALTROPS, CardId.BLUR, CardId.SETUP, CardId.ENDLESS_AGONY,
                CardId.RIDDLE_WITH_HOLES, CardId.SKEWER, CardId.CALCULATED_GAMBLE, CardId.ESCAPE_PLAN, CardId.FINISHER,
                CardId.WELL_LAID_PLANS, CardId.TERROR, CardId.HEEL_HOOK, CardId.NOXIOUS_FUMES, CardId.INFINITE_BLADES,
                CardId.REFLEX, CardId.EVISCERATE, CardId.DASH, CardId.BACKSTAB, CardId.BOUNCING_FLASK,
                CardId.CONCENTRATE, CardId.FLECHETTES, CardId.MASTERFUL_STAB, CardId.ACCURACY, CardId.FOOTWORK,
                CardId.DISTRACTION, CardId.ALL_OUT_ATTACK, CardId.PREDATOR, CardId.GRAND_FINALE, CardId.A_THOUSAND_CUTS,
                CardId.GLASS_KNIFE, CardId.STORM_OF_STEEL, CardId.BULLET_TIME, CardId.AFTER_IMAGE, CardId.UNLOAD,
                CardId.NIGHTMARE, CardId.TOOLS_OF_THE_TRADE, CardId.WRAITH_FORM, CardId.BURST, CardId.DOPPELGANGER,
                CardId.ENVENOM, CardId.ADRENALINE, CardId.DIE_DIE_DIE, CardId.PHANTASMAL_KILLER, CardId.MALAISE,
                CardId.CORPSE_EXPLOSION, CardId.ALCHEMIZE, CardId.GO_FOR_THE_EYES, CardId.BALL_LIGHTNING,
                CardId.STREAMLINE, CardId.RECURSION, CardId.COMPILE_DRIVER, CardId.BARRAGE, CardId.STACK,
                CardId.REBOUND, CardId.CLAW, CardId.COOLHEADED, CardId.TURBO, CardId.SWEEPING_BEAM,
                CardId.CHARGE_BATTERY, CardId.HOLOGRAM, CardId.BEAM_CELL, CardId.LEAP, CardId.COLD_SNAP,
                CardId.STEAM_BARRIER, CardId.STORM, CardId.GENETIC_ALGORITHM, CardId.OVERCLOCK, CardId.HELLO_WORLD,
                CardId.SUNDER, CardId.GLACIER, CardId.CONSUME, CardId.FUSION, CardId.AGGREGATE, CardId.BLIZZARD,
                CardId.CHAOS, CardId.MELTER, CardId.SELF_REPAIR, CardId.LOOP, CardId.CHILL, CardId.BOOT_SEQUENCE,
                CardId.STATIC_DISCHARGE, CardId.HEATSINKS, CardId.TEMPEST, CardId.EQUILIBRIUM, CardId.FORCE_FIELD,
                CardId.FTL, CardId.RIP_AND_TEAR, CardId.DARKNESS, CardId.DOUBLE_ENERGY, CardId.REINFORCED_BODY,
                CardId.AUTO_SHIELDS, CardId.REPROGRAM, CardId.BULLSEYE, CardId.SCRAPE, CardId.RECYCLE, CardId.SKIM,
                CardId.WHITE_NOISE, CardId.CAPACITOR, CardId.DEFRAGMENT, CardId.DOOM_AND_GLOOM, CardId.CORE_SURGE,
                CardId.FISSION, CardId.CREATIVE_AI, CardId.AMPLIFY, CardId.REBOOT, CardId.ALL_FOR_ONE, CardId.ECHO_FORM,
                CardId.METEOR_STRIKE, CardId.SEEK, CardId.RAINBOW, CardId.BUFFER, CardId.ELECTRODYNAMICS,
                CardId.MACHINE_LEARNING, CardId.BIASED_COGNITION, CardId.THUNDER_STRIKE, CardId.HYPERBEAM,
                CardId.MULTI_CAST, CardId.CONSECRATE, CardId.BOWLING_BASH, CardId.FLYING_SLEEVES, CardId.HALT,
                CardId.JUST_LUCKY, CardId.FLURRY_OF_BLOWS, CardId.PROTECT, CardId.THIRD_EYE, CardId.CRESCENDO,
                CardId.TRANQUILITY, CardId.EMPTY_BODY, CardId.SASH_WHIP, CardId.CUT_THROUGH_FATE, CardId.FOLLOW_UP,
                CardId.PRESSURE_POINTS, CardId.CRUSH_JOINTS, CardId.EVALUATE, CardId.PROSTRATE, CardId.EMPTY_FIST,
                CardId.WHEEL_KICK, CardId.SIMMERING_FURY, CardId.FORESIGHT, CardId.SANCTITY, CardId.TALK_TO_THE_HAND,
                CardId.BATTLE_HYMN, CardId.INDIGNATION, CardId.WINDMILL_STRIKE, CardId.FOREIGN_INFLUENCE,
                CardId.LIKE_WATER, CardId.FASTING, CardId.CARVE_REALITY, CardId.WALLOP, CardId.WREATH_OF_FLAME,
                CardId.COLLECT, CardId.INNER_PEACE, CardId.RUSHDOWN, CardId.DECEIVE_REALITY, CardId.MENTAL_FORTRESS,
                CardId.REACH_HEAVEN, CardId.FEAR_NO_EVIL, CardId.SANDS_OF_TIME, CardId.WAVE_OF_THE_HAND, CardId.STUDY,
                CardId.MEDITATE, CardId.PERSEVERANCE, CardId.SWIVEL, CardId.WORSHIP, CardId.CONCLUDE, CardId.TANTRUM,
                CardId.NIRVANA, CardId.EMPTY_MIND, CardId.WEAVE, CardId.SIGNATURE_MOVE, CardId.PRAY,
                CardId.DEUS_EX_MACHINA, CardId.DEVA_FORM, CardId.SPIRIT_SHIELD, CardId.ESTABLISHMENT,
                CardId.OMNISCIENCE, CardId.WISH, CardId.ALPHA, CardId.VAULT, CardId.SCRAWL, CardId.LESSON_LEARNED,
                CardId.RAGNAROK, CardId.BLASPHEMY, CardId.DEVOTION, CardId.BRILLIANCE, CardId.MASTER_REALITY,
                CardId.CONJURE_BLADE, CardId.JUDGMENT]
    groupOffset = [[0, 20, 56], [72, 91, 124], [143, 161, 197], [214, 233, 268]]
    groupSize = [[20, 36, 16], [19, 33, 19], [18, 36, 17], [19, 35, 17]]

    def getPoolOffset(color, rarity):
        return RarityCardPool.groupOffset[int(color)][int(rarity)]

    def getPoolSize(color, rarity):
        return RarityCardPool.groupSize[int(color)][int(rarity)]

    def getCardFromPool(color, rarity, poolIdx):
        startIdx = RarityCardPool.getPoolOffset(color, rarity)
        return RarityCardPool.cardBlob[startIdx + poolIdx]


class TypeRarityCardPool:  # this class replaces the original namespace 'TypeRarityCardPool'

    CARDBLOB = [CardId.ANGER, CardId.BODY_SLAM, CardId.CLASH, CardId.CLEAVE, CardId.CLOTHESLINE, CardId.HEADBUTT,
                CardId.HEAVY_BLADE, CardId.IRON_WAVE, CardId.PERFECTED_STRIKE, CardId.POMMEL_STRIKE,
                CardId.SWORD_BOOMERANG, CardId.THUNDERCLAP, CardId.TWIN_STRIKE, CardId.WILD_STRIKE,
                CardId.BLOOD_FOR_BLOOD, CardId.CARNAGE, CardId.DROPKICK, CardId.HEMOKINESIS, CardId.PUMMEL,
                CardId.RAMPAGE, CardId.RECKLESS_CHARGE, CardId.SEARING_BLOW, CardId.SEVER_SOUL, CardId.UPPERCUT,
                CardId.WHIRLWIND, CardId.BLUDGEON, CardId.FEED, CardId.FIEND_FIRE, CardId.IMMOLATE, CardId.REAPER,
                CardId.ARMAMENTS, CardId.FLEX, CardId.HAVOC, CardId.SHRUG_IT_OFF, CardId.TRUE_GRIT, CardId.WARCRY,
                CardId.BATTLE_TRANCE, CardId.BLOODLETTING, CardId.BURNING_PACT, CardId.DISARM, CardId.DUAL_WIELD,
                CardId.ENTRENCH, CardId.FLAME_BARRIER, CardId.GHOSTLY_ARMOR, CardId.INFERNAL_BLADE, CardId.INTIMIDATE,
                CardId.POWER_THROUGH, CardId.RAGE, CardId.SECOND_WIND, CardId.SEEING_RED, CardId.SENTINEL,
                CardId.SHOCKWAVE, CardId.SPOT_WEAKNESS, CardId.DOUBLE_TAP, CardId.EXHUME, CardId.IMPERVIOUS,
                CardId.LIMIT_BREAK, CardId.OFFERING, CardId.COMBUST, CardId.DARK_EMBRACE, CardId.EVOLVE,
                CardId.FEEL_NO_PAIN, CardId.FIRE_BREATHING, CardId.INFLAME, CardId.METALLICIZE, CardId.RUPTURE,
                CardId.BARRICADE, CardId.BERSERK, CardId.BRUTALITY, CardId.CORRUPTION, CardId.DEMON_FORM,
                CardId.JUGGERNAUT, CardId.BANE, CardId.DAGGER_SPRAY, CardId.DAGGER_THROW, CardId.FLYING_KNEE,
                CardId.POISONED_STAB, CardId.QUICK_SLASH, CardId.SLICE, CardId.SUCKER_PUNCH, CardId.SNEAKY_STRIKE,
                CardId.ALL_OUT_ATTACK, CardId.BACKSTAB, CardId.CHOKE, CardId.DASH, CardId.ENDLESS_AGONY,
                CardId.EVISCERATE, CardId.FINISHER, CardId.FLECHETTES, CardId.HEEL_HOOK, CardId.MASTERFUL_STAB,
                CardId.PREDATOR, CardId.RIDDLE_WITH_HOLES, CardId.SKEWER, CardId.DIE_DIE_DIE, CardId.GLASS_KNIFE,
                CardId.GRAND_FINALE, CardId.UNLOAD, CardId.ACROBATICS, CardId.BACKFLIP, CardId.BLADE_DANCE,
                CardId.CLOAK_AND_DAGGER, CardId.DEADLY_POISON, CardId.DEFLECT, CardId.DODGE_AND_ROLL,
                CardId.OUTMANEUVER, CardId.PIERCING_WAIL, CardId.PREPARED, CardId.BLUR, CardId.BOUNCING_FLASK,
                CardId.CALCULATED_GAMBLE, CardId.CATALYST, CardId.CONCENTRATE, CardId.CRIPPLING_CLOUD,
                CardId.DISTRACTION, CardId.ESCAPE_PLAN, CardId.EXPERTISE, CardId.LEG_SWEEP, CardId.REFLEX, CardId.SETUP,
                CardId.TACTICIAN, CardId.TERROR, CardId.ADRENALINE, CardId.BULLET_TIME, CardId.BURST,
                CardId.CORPSE_EXPLOSION, CardId.DOPPELGANGER, CardId.MALAISE, CardId.NIGHTMARE,
                CardId.PHANTASMAL_KILLER, CardId.STORM_OF_STEEL, CardId.ALCHEMIZE, CardId.ACCURACY, CardId.CALTROPS,
                CardId.FOOTWORK, CardId.INFINITE_BLADES, CardId.NOXIOUS_FUMES, CardId.WELL_LAID_PLANS,
                CardId.A_THOUSAND_CUTS, CardId.AFTER_IMAGE, CardId.ENVENOM, CardId.TOOLS_OF_THE_TRADE,
                CardId.WRAITH_FORM, CardId.BALL_LIGHTNING, CardId.BARRAGE, CardId.BEAM_CELL, CardId.COLD_SNAP,
                CardId.COMPILE_DRIVER, CardId.CLAW, CardId.GO_FOR_THE_EYES, CardId.REBOUND, CardId.STREAMLINE,
                CardId.SWEEPING_BEAM, CardId.BLIZZARD, CardId.DOOM_AND_GLOOM, CardId.FTL, CardId.BULLSEYE,
                CardId.MELTER, CardId.RIP_AND_TEAR, CardId.SCRAPE, CardId.SUNDER, CardId.ALL_FOR_ONE, CardId.CORE_SURGE,
                CardId.HYPERBEAM, CardId.METEOR_STRIKE, CardId.THUNDER_STRIKE, CardId.CHARGE_BATTERY, CardId.COOLHEADED,
                CardId.HOLOGRAM, CardId.LEAP, CardId.RECURSION, CardId.STACK, CardId.STEAM_BARRIER, CardId.TURBO,
                CardId.AGGREGATE, CardId.AUTO_SHIELDS, CardId.BOOT_SEQUENCE, CardId.CHAOS, CardId.CHILL, CardId.CONSUME,
                CardId.DARKNESS, CardId.DOUBLE_ENERGY, CardId.FORCE_FIELD, CardId.FUSION, CardId.GENETIC_ALGORITHM,
                CardId.GLACIER, CardId.RECYCLE, CardId.REINFORCED_BODY, CardId.REPROGRAM, CardId.SKIM, CardId.OVERCLOCK,
                CardId.TEMPEST, CardId.EQUILIBRIUM, CardId.WHITE_NOISE, CardId.AMPLIFY, CardId.FISSION,
                CardId.MULTI_CAST, CardId.RAINBOW, CardId.REBOOT, CardId.SEEK, CardId.CAPACITOR, CardId.DEFRAGMENT,
                CardId.HEATSINKS, CardId.HELLO_WORLD, CardId.LOOP, CardId.SELF_REPAIR, CardId.STATIC_DISCHARGE,
                CardId.STORM, CardId.BIASED_COGNITION, CardId.BUFFER, CardId.CREATIVE_AI, CardId.ECHO_FORM,
                CardId.ELECTRODYNAMICS, CardId.MACHINE_LEARNING, CardId.BOWLING_BASH, CardId.CONSECRATE,
                CardId.CRUSH_JOINTS, CardId.CUT_THROUGH_FATE, CardId.EMPTY_FIST, CardId.FLURRY_OF_BLOWS,
                CardId.FLYING_SLEEVES, CardId.FOLLOW_UP, CardId.JUST_LUCKY, CardId.SASH_WHIP, CardId.CARVE_REALITY,
                CardId.CONCLUDE, CardId.FEAR_NO_EVIL, CardId.REACH_HEAVEN, CardId.SANDS_OF_TIME, CardId.SIGNATURE_MOVE,
                CardId.TALK_TO_THE_HAND, CardId.TANTRUM, CardId.WALLOP, CardId.WEAVE, CardId.WHEEL_KICK,
                CardId.WINDMILL_STRIKE, CardId.BRILLIANCE, CardId.LESSON_LEARNED, CardId.RAGNAROK, CardId.TRANQUILITY,
                CardId.CRESCENDO, CardId.EMPTY_BODY, CardId.EVALUATE, CardId.HALT, CardId.PRESSURE_POINTS,
                CardId.PROSTRATE, CardId.PROTECT, CardId.THIRD_EYE, CardId.COLLECT, CardId.DECEIVE_REALITY,
                CardId.EMPTY_MIND, CardId.FOREIGN_INFLUENCE, CardId.INDIGNATION, CardId.INNER_PEACE, CardId.MEDITATE,
                CardId.PERSEVERANCE, CardId.PRAY, CardId.SANCTITY, CardId.SWIVEL, CardId.SIMMERING_FURY,
                CardId.WAVE_OF_THE_HAND, CardId.WORSHIP, CardId.WREATH_OF_FLAME, CardId.ALPHA, CardId.BLASPHEMY,
                CardId.CONJURE_BLADE, CardId.DEUS_EX_MACHINA, CardId.JUDGMENT, CardId.OMNISCIENCE, CardId.SCRAWL,
                CardId.SPIRIT_SHIELD, CardId.VAULT, CardId.WISH, CardId.RUSHDOWN, CardId.BATTLE_HYMN, CardId.FASTING,
                CardId.LIKE_WATER, CardId.MENTAL_FORTRESS, CardId.NIRVANA, CardId.STUDY, CardId.FORESIGHT,
                CardId.DEVA_FORM, CardId.DEVOTION, CardId.ESTABLISHMENT, CardId.MASTER_REALITY]
    groupOffset = [[[0, 14, 25], [30, 36, 53], [58, 58, 66]], [[72, 81, 94], [98, 108, 122], [132, 132, 138]],
                   [[143, 153, 161], [166, 174, 194], [200, 200, 208]],
                   [[214, 224, 236], [239, 248, 263], [273, 273, 281]]]
    groupSize = [[[14, 11, 5], [6, 17, 5], [0, 8, 6]], [[9, 13, 4], [10, 14, 10], [0, 6, 5]],
                 [[10, 8, 5], [8, 20, 6], [0, 8, 6]], [[10, 12, 3], [9, 15, 10], [0, 8, 4]]]

    def getPoolOffset(color, type, rarity):
        return TypeRarityCardPool.groupOffset[int(color)][int(type)][int(rarity)]

    def getPoolSize(color, type, rarity):
        return TypeRarityCardPool.groupSize[int(color)][int(type)][int(rarity)]

    def getCardFromPool(color, type, rarity, poolIdx):
        startIdx = TypeRarityCardPool.getPoolOffset(color, type, rarity)
        return TypeRarityCardPool.CARDBLOB[startIdx + poolIdx]


class ColorlessRarityCardPool:  # this class replaces the original namespace 'ColorlessRarityCardPool'

    colorlessCardBlob = [CardId.BANDAGE_UP, CardId.BLIND, CardId.DARK_SHACKLES, CardId.DEEP_BREATH, CardId.DISCOVERY,
                         CardId.DRAMATIC_ENTRANCE, CardId.ENLIGHTENMENT, CardId.FINESSE, CardId.FLASH_OF_STEEL,
                         CardId.FORETHOUGHT, CardId.GOOD_INSTINCTS, CardId.IMPATIENCE, CardId.JACK_OF_ALL_TRADES,
                         CardId.MADNESS, CardId.MIND_BLAST, CardId.PANACEA, CardId.PANIC_BUTTON, CardId.PURITY,
                         CardId.SWIFT_STRIKE, CardId.TRIP, CardId.APOTHEOSIS, CardId.CHRYSALIS, CardId.HAND_OF_GREED,
                         CardId.MAGNETISM, CardId.MASTER_OF_STRATEGY, CardId.MAYHEM, CardId.METAMORPHOSIS,
                         CardId.PANACHE, CardId.SADISTIC_NATURE, CardId.SECRET_TECHNIQUE, CardId.SECRET_WEAPON,
                         CardId.THE_BOMB, CardId.THINKING_AHEAD, CardId.TRANSMUTATION, CardId.VIOLENCE]
    COLORLESSGROUPSIZE = [0, 20, 15]
    COLORLESSGROUPOFFSET = [0, 0, 20]

    def getGroupSize(rarity):
        return ColorlessRarityCardPool.COLORLESSGROUPSIZE[int(rarity)]

    def getCardAt(rarity, offset):
        startIdx = ColorlessRarityCardPool.COLORLESSGROUPOFFSET[int(rarity)]
        return ColorlessRarityCardPool.colorlessCardBlob[startIdx + offset]


class CombatTypeCardPool:  # this class replaces the original namespace 'CombatTypeCardPool'

    CARDBLOB = [CardId.SWORD_BOOMERANG, CardId.PERFECTED_STRIKE, CardId.HEAVY_BLADE, CardId.WILD_STRIKE,
                CardId.HEADBUTT, CardId.CLOTHESLINE, CardId.TWIN_STRIKE, CardId.POMMEL_STRIKE, CardId.THUNDERCLAP,
                CardId.CLASH, CardId.BODY_SLAM, CardId.IRON_WAVE, CardId.CLEAVE, CardId.ANGER, CardId.UPPERCUT,
                CardId.DROPKICK, CardId.CARNAGE, CardId.SEARING_BLOW, CardId.WHIRLWIND, CardId.SEVER_SOUL,
                CardId.RAMPAGE, CardId.PUMMEL, CardId.BLOOD_FOR_BLOOD, CardId.HEMOKINESIS, CardId.RECKLESS_CHARGE,
                CardId.BLUDGEON, CardId.FIEND_FIRE, CardId.IMMOLATE]
    SKILLS = [CardId.HAVOC, CardId.ARMAMENTS, CardId.SHRUG_IT_OFF, CardId.TRUE_GRIT, CardId.FLEX, CardId.WARCRY,
              CardId.GHOSTLY_ARMOR, CardId.BLOODLETTING, CardId.SECOND_WIND, CardId.BATTLE_TRANCE, CardId.SENTINEL,
              CardId.ENTRENCH, CardId.RAGE, CardId.DISARM, CardId.SEEING_RED, CardId.SHOCKWAVE, CardId.BURNING_PACT,
              CardId.FLAME_BARRIER, CardId.INTIMIDATE, CardId.INFERNAL_BLADE, CardId.DUAL_WIELD, CardId.POWER_THROUGH,
              CardId.SPOT_WEAKNESS, CardId.DOUBLE_TAP, CardId.LIMIT_BREAK, CardId.IMPERVIOUS, CardId.EXHUME,
              CardId.OFFERING]
    POWERS = [CardId.EVOLVE, CardId.FIRE_BREATHING, CardId.RUPTURE, CardId.FEEL_NO_PAIN, CardId.DARK_EMBRACE,
              CardId.COMBUST, CardId.METALLICIZE, CardId.INFLAME, CardId.DEMON_FORM, CardId.CORRUPTION,
              CardId.BARRICADE, CardId.BERSERK, CardId.JUGGERNAUT, CardId.BRUTALITY]

    def getPoolSize(cc, type):
        return 14 if type == CardType.POWER else 28

    def getCardAt(cc, type, offset):
        if type == CardType.ATTACK:
            return CombatTypeCardPool.CARDBLOB[offset]

        elif type == CardType.SKILL:
            return CombatTypeCardPool.SKILLS[offset]

        elif type == CardType.POWER:
            return CombatTypeCardPool.POWERS[offset]

        else:
            return CombatTypeCardPool.POWERS[offset]


class CombatCardPool:  # this class replaces the original namespace 'CombatCardPool'
    CARDBLOB = [CardId.SWORD_BOOMERANG, CardId.PERFECTED_STRIKE, CardId.HEAVY_BLADE, CardId.WILD_STRIKE,
                CardId.HEADBUTT, CardId.HAVOC, CardId.ARMAMENTS, CardId.CLOTHESLINE, CardId.TWIN_STRIKE,
                CardId.POMMEL_STRIKE, CardId.THUNDERCLAP, CardId.CLASH, CardId.SHRUG_IT_OFF, CardId.TRUE_GRIT,
                CardId.BODY_SLAM, CardId.IRON_WAVE, CardId.FLEX, CardId.WARCRY, CardId.CLEAVE, CardId.ANGER,
                CardId.EVOLVE, CardId.UPPERCUT, CardId.GHOSTLY_ARMOR, CardId.FIRE_BREATHING, CardId.DROPKICK,
                CardId.CARNAGE, CardId.BLOODLETTING, CardId.RUPTURE, CardId.SECOND_WIND, CardId.SEARING_BLOW,
                CardId.BATTLE_TRANCE, CardId.SENTINEL, CardId.ENTRENCH, CardId.RAGE, CardId.FEEL_NO_PAIN, CardId.DISARM,
                CardId.SEEING_RED, CardId.DARK_EMBRACE, CardId.COMBUST, CardId.WHIRLWIND, CardId.SEVER_SOUL,
                CardId.RAMPAGE, CardId.SHOCKWAVE, CardId.METALLICIZE, CardId.BURNING_PACT, CardId.PUMMEL,
                CardId.FLAME_BARRIER, CardId.BLOOD_FOR_BLOOD, CardId.INTIMIDATE, CardId.HEMOKINESIS,
                CardId.RECKLESS_CHARGE, CardId.INFERNAL_BLADE, CardId.DUAL_WIELD, CardId.POWER_THROUGH, CardId.INFLAME,
                CardId.SPOT_WEAKNESS, CardId.DOUBLE_TAP, CardId.DEMON_FORM, CardId.BLUDGEON, CardId.LIMIT_BREAK,
                CardId.CORRUPTION, CardId.BARRICADE, CardId.FIEND_FIRE, CardId.BERSERK, CardId.IMPERVIOUS,
                CardId.JUGGERNAUT, CardId.BRUTALITY, CardId.EXHUME, CardId.OFFERING, CardId.IMMOLATE]

    def getPoolSize(cc):
        return 70

    def getCardAt(cc, offset):
        return CombatCardPool.CARDBLOB[offset]


class CombatColorlessCardPool:  # this class replaces the original namespace 'CombatColorlessCardPool'

    CARDS = [CardId.MADNESS, CardId.THINKING_AHEAD, CardId.MIND_BLAST, CardId.METAMORPHOSIS, CardId.JACK_OF_ALL_TRADES,
             CardId.SWIFT_STRIKE, CardId.GOOD_INSTINCTS, CardId.MASTER_OF_STRATEGY, CardId.MAGNETISM, CardId.FINESSE,
             CardId.DISCOVERY, CardId.CHRYSALIS, CardId.TRANSMUTATION, CardId.PANACEA, CardId.PURITY,
             CardId.ENLIGHTENMENT, CardId.FORETHOUGHT, CardId.FLASH_OF_STEEL, CardId.HAND_OF_GREED, CardId.MAYHEM,
             CardId.APOTHEOSIS, CardId.SECRET_WEAPON, CardId.PANACHE, CardId.VIOLENCE, CardId.DEEP_BREATH,
             CardId.SECRET_TECHNIQUE, CardId.BLIND, CardId.THE_BOMB, CardId.IMPATIENCE, CardId.DRAMATIC_ENTRANCE,
             CardId.TRIP, CardId.PANIC_BUTTON, CardId.SADISTIC_NATURE, CardId.DARK_SHACKLES]

    def getPoolSize(self):
        return 34

    def getCardAt(offset):
        return CombatColorlessCardPool.CARDS[offset]
