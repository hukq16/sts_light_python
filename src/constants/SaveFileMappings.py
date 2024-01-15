#
# Created by gamerpuppy on 7/8/2021.
#



# C++ TO PYTHON CONVERTER WARNING: Statement interrupted by a preprocessor statement:
#The original statement from the file starts with:
#    JSON_HEDLEY_DIAGNOSTIC_PUSH
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file is ignored.



class sts: #this class replaces the original namespace 'sts'

# C++ TO PYTHON CONVERTER WARNING: The following constructor is declared outside of its associated class:
    def __init__(UnnamedParameter, ):

        sts.NLOHMANN_JSON_SERIALIZE_ENUM(Bonus, ({Bonus.INVALID, None},
        {Bonus.RANDOM_COLORLESS_2, "RANDOM_COLORLESS_2"},
        {Bonus.THREE_CARDS, "THREE_CARDS"},
        {Bonus.ONE_RANDOM_RARE_CARD, "ONE_RANDOM_RARE_CARD"},
        {Bonus.REMOVE_CARD, "REMOVE_CARD"},
        {Bonus.UPGRADE_CARD, "UPGRADE_CARD"},
        {Bonus.RANDOM_COLORLESS, "RANDOM_COLORLESS"},
        {Bonus.TRANSFORM_CARD, "TRANSFORM_CARD"},
        {Bonus.THREE_SMALL_POTIONS, "THREE_SMALL_POTIONS"},
        {Bonus.RANDOM_COMMON_RELIC, "RANDOM_COMMON_RELIC"},
        {Bonus.TEN_PERCENT_HP_BONUS, "TEN_PERCENT_HP_BONUS"},
        {Bonus.HUNDRED_GOLD, "HUNDRED_GOLD"},
        {Bonus.THREE_ENEMY_KILL, "THREE_ENEMY_KILL"},
        {Bonus.REMOVE_TWO, "REMOVE_TWO"},
        {Bonus.TRANSFORM_TWO_CARDS, "TRANSFORM_TWO_CARDS"},
        {Bonus.ONE_RARE_RELIC, "ONE_RARE_RELIC"},
        {Bonus.THREE_RARE_CARDS, "THREE_RARE_CARDS"},
        {Bonus.TWO_FIFTY_GOLD, "TWO_FIFTY_GOLD"},
        {Bonus.TWENTY_PERCENT_HP_BONUS, "TWENTY_PERCENT_HP_BONUS"},
        {Bonus.BOSS_RELIC, "BOSS_RELIC"})) NLOHMANN_JSON_SERIALIZE_ENUM(Drawback,
        {
            {Drawback.INVALID, None},
            {Drawback.NONE, "NONE"},
            {Drawback.TEN_PERCENT_HP_LOSS, "TEN_PERCENT_HP_LOSS"},
            {Drawback.NO_GOLD, "NO_GOLD"},
            {Drawback.CURSE, "CURSE"},
            {Drawback.PERCENT_DAMAGE, "PERCENT_DAMAGE"},
            {Drawback.LOSE_STARTER_RELIC, "LOSE_STARTER_RELIC"}
        })
    class Save: #this class replaces the original namespace 'Save'

        @staticmethod
        def from_json(UnnamedParameter, ):
            j.at("type").get_to(r.type)

            if (r.type == sts.Save.CombatRewardType.STOLEN_GOLD) or (r.type == sts.Save.CombatRewardType.GOLD):
                r.bonusGold = 0
                j.at("amount").get_to(r.amount)
                j.at("bonusGold").get_to(r.bonusGold)

            elif r.type == sts.Save.CombatRewardType.CARD:
                j.at("id").get_to(r.cardId)

            elif r.type == sts.Save.CombatRewardType.POTION:
                j.at("id").get_to(r.potionId)

            elif r.type == sts.Save.CombatRewardType.RELIC:
                j.at("id").get_to(r.relicId)





