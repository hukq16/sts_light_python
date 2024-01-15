from sts import *

#
# Created by gamerpuppy on 8/24/2021.
#

#
# Created by gamerpuppy on 7/4/2021.
#




class sts: #this class replaces the original namespace 'sts'

    class CardQueueItem:

        def _initialize_instance_fields(self):
            # instance fields found by C++ to Python Converter:
            self.card = CardInstance()
            self.target = 0
            self.isEndTurn = False
            self.triggerOnUse = True
            self.ignoreEnergyTotal = False
            self.energyOnUse = 0
            self.freeToPlay = False
            self.randomTarget = False
            self.autoplay = False
            self.regretCardCount = 0
            self.purgeOnUse = False
            self.exhaustOnUse = False

        #        int cardIdx

        # special data


# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        CardQueueItem() = default
# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: CardQueueItem(const CardInstance &card, int target, int energyOnUse) : card(card), target(target), energyOnUse(energyOnUse)
        def __init__(self, card, target, energyOnUse):
            self._initialize_instance_fields()

            self.card = sts.CardInstance(card)
            self.target = target
            self.energyOnUse = energyOnUse

        @staticmethod
        def endTurnItem():
            ret = CardQueueItem()
            ret.isEndTurn = True
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: return ret;
            return sts.CardQueueItem(ret)

    class CardQueue:

        def __init__(self):
            # instance fields found by C++ to Python Converter:
            self.size = 0
            self.backIdx = 0
            self.frontIdx = 0
            self.arr = [None for _ in range(sts.CardQueue.CAPACITY)]

        CAPACITY = 10

        def clear(self):
            self.size = 0
            self.backIdx = 0
            self.frontIdx = 0

        def pushFront(self, item):
            assert self.size != len(self.arr)
            self.frontIdx -= 1
            self.size += 1
            if self.frontIdx < 0:
                self.frontIdx = sts.CardQueue.CAPACITY - 1
            self.arr[self.frontIdx] = std::move(item)

        def pushBack(self, item):
            assert self.size != sts.CardQueue.CAPACITY
            self.arr[self.backIdx] = std::move(item)
            self.backIdx += 1
            self.size += 1
            if self.backIdx >= sts.CardQueue.CAPACITY:
                self.backIdx = 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool isEmpty() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool isEmpty() const
        def isEmpty(self):
            return self.size == 0

        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] bool containsCardWithId(int uniqueId) const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: bool containsCardWithId(int uniqueId) const
        def containsCardWithId(self, uniqueId):
            idx = self.frontIdx
            i = 0
            while i < self.size:
                if self.frontIdx >= sts.CardQueue.CAPACITY:
                    idx = 0
                if self.arr[idx].card.getUniqueId() == uniqueId:
                    return True
                i += 1
            return False

        def popFront(self):
            assert self.size > 0
            item = self.arr[self.frontIdx]
            self.frontIdx += 1
            self.size -= 1
            if self.frontIdx >= sts.CardQueue.CAPACITY:
                self.frontIdx = 0
            return item

        def popBack(self):
            assert self.size > 0
            self.backIdx -= 1
            self.size -= 1
            if self.backIdx < 0:
                self.backIdx = len(self.arr) - 1
            item = self.arr[self.backIdx]
            return item

        def front(self):
            assert self.size > 0
# C++ TO PYTHON CONVERTER TASK: The following line was determined to contain a copy constructor call - this should be verified and a copy constructor should be created:
# ORIGINAL LINE: return arr.at(frontIdx);
            return sts.CardQueueItem(self.arr[self.frontIdx])



