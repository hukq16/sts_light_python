#
# Created by gamerpuppy on 7/4/2021.
#





class sts: #this class replaces the original namespace 'sts'

# C++ TO PYTHON CONVERTER NOTE: Python has no need of forward class declarations:
#    class BattleContext
    class ActionFunction:
        def invoke(self, UnnamedParameter):
            pass


    class Action:

        def _initialize_instance_fields(self):
            # instance fields found by C++ to Python Converter:
            self.actFunc = ActionFunction()
            self.clearOnCombatVictory = True


# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        Action() = default
# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: Action(ActionFunction a) : actFunc(std::move(a))
        def __init__(self, a):
            self._initialize_instance_fields()

            self.actFunc = sts.ActionFunction(std::move(a))
# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: Action(ActionFunction a, bool b) : actFunc(std::move(a)), clearOnCombatVictory(b)
        def __init__(self, a, b):
            self._initialize_instance_fields()

            self.actFunc = sts.ActionFunction(std::move(a))
            self.clearOnCombatVictory = b


    # Simple deque
# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template<int capacity>
    class ActionQueue:

        def _initialize_instance_fields(self):
            # instance fields found by C++ to Python Converter:
            self.front = 0
            self.back = 0
            self.size = 0
            self.bits = std::bitset()
            self.arr = [None for _ in range(capacity)]
            self.arr = list(capacity)

# C++ TO PYTHON CONVERTER TASK: Python has no concept of a 'friend' class:
#        friend BattleContext

# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_action_queue_use_raw_array
# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#        ActionQueue() = default
# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: ActionQueue(const ActionQueue &rhs) : size(rhs.size), back(rhs.back), front(rhs.front), bits(rhs.bits)
        def __init__(self, rhs):
            self._initialize_instance_fields()

            self.size = rhs.size
            self.back = rhs.back
            self.front = rhs.front
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: this.bits = rhs.bits;
            self.bits.copy_from(rhs.bits)
            cur = rhs.front
            i = 0
            while i < rhs.size:
                if cur >= capacity:
                    cur = 0
                self.arr[cur] = rhs.arr[cur]
                i += 1
##else
##endif

// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        clear()
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        pushFront(a)
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        pushBack(a)
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        isEmpty()
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        popFront()
        # C++ TO PYTHON CONVERTER TASK: C++ attributes are not converted to Python:
        # ORIGINAL LINE: [[nodiscard]] int getCapacity() const
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int getCapacity() const;
// C++ TO PYTHON CONVERTER TASK: The implementation of the following method could not be found:
//        getCapacity()

# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template<int capacity>
    @staticmethod
    def clear():
        size = 0
        back = 0
        front = 0

# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template <int capacity>
    @staticmethod
    def pushFront(a):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
        assert size != capacity
##endif
        front -= 1
        size += 1
        if front < 0:
            front = capacity-1
        bits.set(front, a.clearOnCombatVictory)
        arr[front] = std::move(a.actFunc)

# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template<int capacity>
    @staticmethod
    def pushBack(a):
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
        if size >= capacity:
            False = assert()
##endif
        if back >= capacity:
            back = 0
        bits.set(back, a.clearOnCombatVictory)
        arr[back] = std::move(a.actFunc)
        back += 1
        size += 1

# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template<int capacity>
    @staticmethod
    def isEmpty():
        return size == 0

# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template<int capacity>
    @staticmethod
    def popFront():
# C++ TO PYTHON CONVERTER TASK: There is no preprocessor in Python:
##if sts_asserts
        assert size > 0
##endif
        a = arr[front]
        front += 1
        size -= 1
        if front >= capacity:
            front = 0
        return a

# C++ TO PYTHON CONVERTER TASK: The following C++ template specifier cannot be converted to Python:
# ORIGINAL LINE: template<int capacity>
    @staticmethod
# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: int ActionQueue<capacity>::getCapacity() const
    def getCapacity():
        return capacity



