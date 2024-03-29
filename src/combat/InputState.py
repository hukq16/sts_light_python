﻿from enum import Enum


class InputState(Enum):
    EXECUTING_ACTIONS = 0

    # player choice actions
    PLAYER_NORMAL = 1
    CARD_SELECT = 2

    CHOOSE_STANCE_ACTION = 3  # from stance potion
    CHOOSE_TOOLBOX_COLORLESS_CARD = 4
    CHOOSE_EXHAUST_POTION_CARDS = 5
    CHOOSE_GAMBLING_CARDS = 6
    CHOOSE_ENTROPIC_BREW_DISCARD_POTIONS = 7
    CHOOSE_DISCARD_CARDS = 8
    SCRY = 9

    # random actions
    SELECT_ENEMY_ACTIONS = 10
    FILL_RANDOM_POTIONS = 11
    SHUFFLE_INTO_DRAW_BURN = 12
    SHUFFLE_INTO_DRAW_VOID = 13
    SHUFFLE_INTO_DRAW_DAZED = 14
    SHUFFLE_INTO_DRAW_WOUND = 15
    SHUFFLE_INTO_DRAW_SLIMED = 16
    SHUFFLE_INTO_DRAW_ALL_STATUS = 17
    SHUFFLE_CUR_CARD_INTO_DRAW = 18
    SHUFFLE_DISCARD_TO_DRAW = 19
    INITIAL_SHUFFLE = 20

    CREATE_RANDOM_CARD_IN_HAND_POWER = 21
    CREATE_RANDOM_CARD_IN_HAND_COLORLESS = 22
    CREATE_RANDOM_CARD_IN_HAND_DEAD_BRANCH = 23

    SELECT_CARD_IN_HAND_EXHAUST = 24

    GENERATE_NILRY_CARDS = 25

    EXHAUST_RANDOM_CARD_IN_HAND = 26
    SELECT_STRANGE_SPOON_PROC = 27
    SELECT_ENEMY_THE_SPECIMEN_APPLY_POISON = 28
    SELECT_WARPED_TONGS_CARD = 29

    CREATE_ENCHIRIDION_POWER = 30

    SELECT_CONFUSED_CARD_COST = 31

    def __int__(self):
        return self.value
