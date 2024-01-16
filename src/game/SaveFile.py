from sts import *

from enum import Enum
import math

#
# Created by gamerpuppy on 7/8/2021.
#

# C++ TO PYTHON CONVERTER WARNING: Statement interrupted by a preprocessor statement:
#The original statement from the file starts with:
#    JSON_HEDLEY_DIAGNOSTIC_PUSH
#Preprocessor-interrupted statements cannot be handled by this converter.
#The remainder of the header file is ignored.

#
# Created by gamerpuppy on 7/8/2021.
#








class sts: #this class replaces the original namespace 'sts'

# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class GameContext

    class Save: #this class replaces the original namespace 'Save'

        class RoomType(Enum):
            INVALID = 0
            EMPTY_ROOM = 1
            EVENT_ROOM = 2
            MONSTER_ROOM = 3
            MONSTER_ROOM_BOSS = 4
            MONSTER_ROOM_ELITE = 5
            REST_ROOM = 6
            SHOP_ROOM = 7
            TREASURE_ROOM = 8
            TREASURE_ROOM_BOSS = 9
            TRUE_VICTORY_ROOM = 10
            VICTORY_ROOM = 11

        class CombatRewardType(Enum):
            INVALID = 0
            GOLD = 1
            CARD = 2
            POTION = 3
            RELIC = 4
            STOLEN_GOLD = 5
            EMERALD_KEY = 6
            SAPPHIRE_KEY = 7

        class CombatReward:

            def __init__(self):
                # instance fields found by C++ to Python Converter:
                self.type = 0
                self.amount = -1
                self.bonusGold = -1
                self.cardId = CardId.INVALID
                self.potionId = Potion.INVALID
                self.relicId = RelicId.INVALID



    class Base64:
        CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

        @staticmethod
        def decodeChar(c):
            value = 0
            if c >= 'A' and c <= 'Z':
                value = c-'A'

            elif c >= 'a' and c <= 'z':
                value = c-'a'+26

            elif c >= '0' and c <= '9':
                value = c-'0'+52

            elif c == '+':
                value = 62

            elif c == '/':
                value = 63

            else:
                value = -1
            return chr(value)

        @staticmethod
        def encodeChar(dataMod64):
            return sts.Base64.CHARS[dataMod64]

        @staticmethod
        def decode(base64Str):
            out = ""

            totalBits = 0
            lastData = 0

            for i, unusedItem in enumerate(base64Str):
                c = base64Str[i]
                if c == '=':
                    paddingLength = 2 if (i + 1 < len(base64Str)) else 1
                    charsToDecode = 3-paddingLength
                    charsDecoded = math.fmod(int(len(out)), 3)
                    if charsToDecode < charsDecoded:
                        out.push_back(chr(lastData))
                    return out

                dataBits = Base64.decodeChar(c)
                totalBits += 6

                mod8 = math.fmod(totalBits, 8)
                if mod8 == 0:
                    value = chr((lastData | dataBits))
                    out.push_back(value)

                elif mod8 == 2:
                    value = chr((lastData | (dataBits >> 2)))
                    out.push_back(value)
                    lastData = (dataBits << 6) & 0xC0

                elif mod8 == 4:
                    value = chr((lastData | (dataBits >> 4)))
                    out.push_back(value)
                    lastData = (dataBits << 4) & 0xF0

                elif mod8 == 6:
                    lastData = (dataBits << 2) & 0xFC
            return out

        @staticmethod
        def encode(data):
            encoded = ""

            bits = 0
            bitCount = 0

            for c in data:

                if bitCount == 0:
                    encoded.push_back(sts.Base64.encodeChar(c >> 2))
                    bits = c & 0x3
                    bitCount = 2

                elif bitCount == 2:
                    encoded.push_back(sts.Base64.encodeChar(bits << 4 | c >> 4))
                    bits = c & 0xF
                    bitCount = 4

                else:
                    encoded.push_back(sts.Base64.encodeChar(bits << 2 | c >> 6))
                    encoded.push_back(sts.Base64.encodeChar(c & 0x3F))
                    bits = 0
                    bitCount = 0

            if bitCount == 2:
                encoded.push_back(sts.Base64.encodeChar(bits << 4))
                encoded.push_back('=')
                encoded.push_back('=')

            elif bitCount == 4:
                encoded.push_back(sts.Base64.encodeChar(bits << 2))
                encoded.push_back('=')


            return encoded

    class SaveFile:

        def _initialize_instance_fields(self):
            # instance fields found by C++ to Python Converter:
            self.json = ""
            self.seed = 0
            self.cc = 0
            self.ascension_level = 0
            self.act_num = 0
            self.gold = 0
            self.purgeCost = 0
            self.current_health = 0
            self.max_health = 0
            self.play_time = 0
            self.room_x = 0
            self.room_y = 0
            self.floor_num = 0
            self.post_combat = False
            self.smoked = False
            self.mugged = False
            self.current_room = 0
            self.potion_seed_count = 0
            self.relic_seed_count = 0
            self.event_seed_count = 0
            self.monster_seed_count = 0
            self.merchant_seed_count = 0
            self.card_random_seed_count = 0
            self.card_seed_count = 0
            self.treasure_seed_count = 0
            self.has_emerald_key = False
            self.has_ruby_key = False
            self.has_sapphire_key = False
            self.card_random_seed_randomizer = 0
            self.potion_chance = 0
            self.monsterChance = 0
            self.shopChance = 0
            self.treasureChance = 0
            self.chose_neow_reward = False
            self.neow_bonus = 0
            self.neow_cost = 0
            self.potions = []
            self.cards = []
            self.bottledCards = [None for _ in range(3)]
            self.relics = []
            self.relic_counters = []
            self.combat_rewards = []
            self.boss_relics = []
            self.shop_relics = []
            self.common_relics = []
            self.uncommon_relics = []
            self.rare_relics = []
            self.one_time_event_list = []
            self.event_list = []
            self.monster_list = []
            self.elite_monster_list = []
            self.boss_list = []













# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        SaveFile() = default
# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        SaveFile(const SaveFile &rhs) = default
# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: SaveFile(const str &json, sts::CharacterClass cc): json(json), cc(cc)
        def __init__(self, json, cc):
            self._initialize_instance_fields()

            self.json = json
            self.cc = sts.CharacterClass(cc)
            j = nlohmann.json.parse(json)

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_print_debug
            print("{0:>4d}".format(j), end = '')
            print("{0:d}".format('\n'), end = '')
##endif

            j.at("seed").get_to(self.seed)
            j.at("ascension_level").get_to(self.ascension_level)
            j.at("act_num").get_to(self.act_num)
            j.at("gold").get_to(self.gold)
            j.at("purgeCost").get_to(self.purgeCost)

            j.at("current_health").get_to(self.current_health)
            j.at("max_health").get_to(self.max_health)

            j.at("play_time").get_to(self.play_time)
            j.at("room_x").get_to(self.room_x)
            j.at("room_y").get_to(self.room_y)
            j.at("floor_num").get_to(self.floor_num)
            j.at("post_combat").get_to(self.post_combat)
            j.at("smoked").get_to(self.smoked)
            j.at("mugged").get_to(self.mugged)
            j.at("current_room").get_to(self.current_room)

            j.at("potion_seed_count").get_to(self.potion_seed_count)
            j.at("relic_seed_count").get_to(self.relic_seed_count)
            j.at("event_seed_count").get_to(self.event_seed_count)
            j.at("monster_seed_count").get_to(self.monster_seed_count)
            j.at("merchant_seed_count").get_to(self.merchant_seed_count)
            j.at("card_random_seed_count").get_to(self.card_random_seed_count)
            j.at("card_seed_count").get_to(self.card_seed_count)
            j.at("treasure_seed_count").get_to(self.treasure_seed_count)

            j.at("has_emerald_key").get_to(self.has_emerald_key)
            j.at("has_ruby_key").get_to(self.has_ruby_key)
            j.at("has_sapphire_key").get_to(self.has_sapphire_key)

            j.at("card_random_seed_randomizer").get_to(self.card_random_seed_randomizer)
            j.at("potion_chance").get_to(self.potion_chance)
            eventChances = [0 for _ in range(4)]
            j.at("event_chances").get_to(eventChances)
            self.monsterChance = eventChances[1]
            self.shopChance = eventChances[2]
            self.treasureChance = eventChances[3]

            j.at("chose_neow_reward").get_to(self.chose_neow_reward)
            j.at("neow_bonus").get_to(self.neow_bonus)
            j.at("neow_cost").get_to(self.neow_cost)

            j.at("potions").get_to(self.potions)

            for c in j.at("cards"):
                card = Card()
                c.at("id").get_to(card.id)

                upgrades = 0
                c.at("upgrades").get_to(upgrades)

                if card.id == CardId.SEARING_BLOW:
                    card.misc = short(upgrades)
                    card.upgraded = card.misc != 0
                else:
                    c.at("misc").get_to(card.misc)
                    card.upgraded = upgrades > 0
                self.cards.append(card)

            self.bottledCards = [CardId.INVALID, CardId.INVALID, CardId.INVALID]
            if j.contains("bottled_flame"):
                j.at("bottled_flame").get_to(self.bottledCards[0])
            if j.contains("bottled_lightning"):
                j.at("bottled_lightning").get_to(self.bottledCards[1])
            if j.contains("bottled_tornado"):
                j.at("bottled_tornado").get_to(self.bottledCards[2])

            j.at("relics").get_to(self.relics)
            j.at("relic_counters").get_to(self.relic_counters)

            if j.contains("combat_rewards"):
                j.at("combat_rewards").get_to(self.combat_rewards)

            j.at("boss_relics").get_to(self.boss_relics)
            j.at("shop_relics").get_to(self.shop_relics)
            j.at("common_relics").get_to(self.common_relics)
            j.at("uncommon_relics").get_to(self.uncommon_relics)
            j.at("rare_relics").get_to(self.rare_relics)

            j.at("event_list").get_to(self.event_list)
            j.at("one_time_event_list").get_to(self.one_time_event_list)
            j.at("monster_list").get_to(self.monster_list)
            j.at("elite_monster_list").get_to(self.elite_monster_list)
            j.at("boss_list").get_to(self.boss_list)

        @staticmethod
        def loadFromPath(path, cc):
            return SaveFile(sts.SaveFile.getJsonFromSaveFile(path), cc)

        @staticmethod
        def getJsonFromSaveFile(path):
            utf8Content = sts.SaveFile.readFileToStringHelper(path)
            dataBits = Base64.decode(utf8Content)
            json = Globals.xorWithKey(dataBits)

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_print_debug
            print(json, end = '')
##endif
            return auto(json)

        @staticmethod
        def writeJsonToSaveFile(jsonIs, savePath):
            j = nlohmann.json.parse(jsonIs)
            cleanedJsonStr = j.dump()

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_print_debug
            print(cleanedJsonStr, end = '')
##endif

            obfuscatedStr = Globals.xorWithKey(cleanedJsonStr)
            base64Encoding = Base64.encode(cleanedJsonStr)
            outFileStream = std::ofstream(savePath)
            outFileStream << base64Encoding

        @staticmethod
        def readFileToStringHelper(path):
            result = ""
            ifs = std::ifstream(path, std::ios.binary)
            ss = std::stringstream()

            if not ifs.is_open():
                result = ""
                return result
            elif ifs.eof():
                result = ""

            ss << ifs.rdbuf()
            result = ss.str()
            return result
