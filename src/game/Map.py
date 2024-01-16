#
# Created by gamerpuppy on 6/24/2021.
#



from sts import *

def __init__(seed, ascension, act, assignBurningElite):
    self.Map = Map.fromSeed(seed,ascension,act,assignBurningElite)

def getNode(x, y):
    return nodes.at(y).at(x)

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: const MapNode &Map::getNode(int x, int y) const
def getNode(x, y):
    return nodes.at(y).at(x)

def fromSeed(seed, ascension, act, setBurning):
    map = Map()
    offset = 1 if act == 1 else act*(100*(act-1))
    mapRng = Random(seed+offset)
    initNodes(map)
    createPaths(map, mapRng)
    filterRedundantEdgesFromFirstRow(map)
    assignRooms(map, mapRng, ascension)
    if setBurning:
        assignBurningElite(map, mapRng)
        map.burningEliteBuff = mapRng.random(0,3)
    return Map(map)

def act4Map():
    map = Map()
    initNodes(map)
    restNode = map.getNode(3,0)
    shopNode = map.getNode(3,1)
    eliteNode = map.getNode(3,2)
    bossNode = map.getNode(3,3)

    restNode.room = Room.REST
    shopNode.room = Room.SHOP
    eliteNode.room = Room.ELITE
    bossNode.room = Room.BOSS

    restNode.addEdge(3)
    shopNode.addEdge(3)
    eliteNode.addEdge(3)

    bossNode.addParent(3) # not really necessary to add parents
    eliteNode.addParent(3)
    shopNode.addParent(3)

    return Map(map)

def normalizeParents():
    for row in range(1, 15):
        for col in range(0, 7):
            node = getNode(col, row)
            found = [False for _ in range(7)]
            i = 0
            while i < node.parentCount:
                found[node.parents[i]] = True
                i += 1
            node.parentCount = 0
            for i in range(0, 7):
                if found[i]:
                    node.addParent(i)

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: char MapNode::getRoomSymbol() const
def getRoomSymbol():
    return sts.getRoomSymbol(room)

def addParent(parent):
# C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
# ORIGINAL LINE: parents[parentCount++] = parent;
    parents[parentCount] = parent
    parentCount += 1

def addEdge(edge):
    cur = 0
    while True:
        if cur == edgeCount:
            edges[cur] = edge
            edgeCount += 1
            return

        if edge == edges[cur]:
            return

        if edge < edges[cur]:
            insertEdge(self, edge, cur)
            return
        cur += 1

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: inline int MapNode::getMaxEdge() const
def getMaxEdge():
    #    assert(edgeCount > 0)
    return edges.at(edgeCount-1)

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: inline int MapNode::getMinEdge() const
def getMinEdge():
    #    assert(edgeCount > 0)
    return edges.at(0)

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: inline int MapNode::getMaxXParent() const
def getMaxXParent():
    maxParent = parents[0]
    i = 1
    while i < parentCount:
        if parents[i] > maxParent:
            maxParent = parents[i]
        i += 1
    return maxParent

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: inline int MapNode::getMinXParent() const
def getMinXParent():
    minParent = parents[0]
    i = 1
    while i < parentCount:
        if parents[i] < minParent:
            minParent = parents[i]
        i += 1
    return minParent
            i += 1
            i += 1

# C++ TO PYTHON CONVERTER WARNING: 'const' methods are not available in Python:
# ORIGINAL LINE: str Map::toString(bool showRoomSymbols) const
def toString(showRoomSymbols):
    str = ""

    lastRow = 14
    left_padding_size = 5


    hitNonEmptyRow = False

    for y in range(14, -1, -1):

        if not hitNonEmptyRow:
            empty = True
            for x in range(0, 7):
                if getNode(x,y).parentCount > 0:
                    empty = False
                    break
            if empty:
                continue
            else:
                hitNonEmptyRow = True

        str.append("\n ").append(paddingGenerator(left_padding_size))
        for x in range(0, 7):
            node = getNode(x, y)
            right = " "
            mid = " "
            node_symbol = " "

            i = 0
            while i < node.edgeCount:
                edge = node.edges[i]
                if edge < x:
                    node_symbol = "\\"

                if edge == x:
                    mid = "|"

                if edge > x:
                    right = "/"
                i += 1
            str.append(node_symbol).append(mid).append(right)

        str.append("\n").append(str(y)).append(" ")
        str.append(paddingGenerator(left_padding_size - int(str(y).length())))

        for x in range(0, 7):
            node = getNode(x, y)
            node_symbol = " "

            if y == lastRow:
                for lower_node in nodes.at(y - 1):
                    i = 0
                    while i < lower_node.edgeCount:
                        if lower_node.edges[i] == x:
                            node_symbol = node.getRoomSymbol() if showRoomSymbols else '*'
                        i += 1
            else:
                if node.edgeCount > 0 or node.room == Room.BOSS:
                    node_symbol = node.getRoomSymbol() if showRoomSymbols else '*'
            str.append(" ").append(node_symbol).append(" ")

    return str

class RoomCounts:

    def __init__(self):
        # instance fields found by C++ to Python Converter:
        self.total = 0
        self.unassigned = 0


class RoomConstructorData:




    masks = [0x0101010101010101, 0x0202020202020202, 0x0404040404040404, 0x0808080808080808, 0x1010101010101010, 0x2020202020202020, 0x4040404040404040]


    def __init__(self, rooms, roomCount):
        # instance fields found by C++ to Python Converter:
        self.rooms = None
        self.roomCount = 0
        self.offset = 0
        self.rowData = 0
        self.prevRowData = 0
        self.siblingMasks = [0 for _ in range(Globals.MAP_WIDTH)]
        self.nextSiblingMasks = [0 for _ in range(Globals.MAP_WIDTH)]
        self.parentMasks = [0 for _ in range(Globals.MAP_WIDTH)]
        self.nextParentMasks = [0 for _ in range(Globals.MAP_WIDTH)]

        self.rooms = rooms
        self.roomCount = roomCount

    def setData(self, node):
        if node.edgeCount == 1:
            i = 0
            while i < node.edgeCount:
                self.nextParentMasks[node.edges[i]] |= ulong(0xFF << (node.x *8))
                i += 1

        else:
            siblingMask = 0
            i = 0
            while i < node.edgeCount:
                edge = node.edges[i]
                siblingMask |= ulong(0xFF << (node.edges[i]*8))
                self.nextSiblingMasks[edge] |= siblingMask
                self.nextParentMasks[edge] |= ulong(0xFF << (node.x *8))
                i += 1

    def setCurDataOnly(self, node):
        self.rowData |= ulong(1 << (node.room + node.x *8))

    def setNextDataOnly(self, node):
        if node.edgeCount == 1:
            i = 0
            while i < node.edgeCount:
                self.nextParentMasks[node.edges[i]] |= ulong(0xFF << (node.x *8))
                i += 1

        else:
            siblingMask = 0
            i = 0
            while i < node.edgeCount:
                edge = node.edges[i]
                siblingMask |= ulong(0xFF << (node.edges[i]*8))
                self.nextSiblingMasks[edge] |= siblingMask
                self.nextParentMasks[edge] |= ulong(0xFF << (node.x *8))
                i += 1

    def removeElement(self, idx):
        i = idx
        while i > self.offset:
# C++ TO PYTHON CONVERTER TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
# ORIGINAL LINE: rooms[i] = rooms[i-1];
            self.rooms[i].copy_from(self.rooms[i-1])
            i -= 1
        self.offset += 1

    def nextRow(self):
        self.prevRowData = self.rowData
        self.rowData = 0

        i = 0
        while i < Globals.MAP_WIDTH:
            self.siblingMasks[i] = self.nextSiblingMasks[i]
            self.nextSiblingMasks[i] = 0

            self.parentMasks[i] = self.nextParentMasks[i]
            self.nextParentMasks[i] = 0
            i += 1

            i += 1
                i += 1
                i += 1
                i += 1
                i += 1
                i += 1

class IntTuple:

    def _initialize_instance_fields(self):
        # instance fields found by C++ to Python Converter:
        self.x = 0
        self.y = 0


# C++ TO PYTHON CONVERTER TASK: Python has no equivalent to ' = default':
#    IntTuple() = default
# C++ TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
# ORIGINAL LINE: IntTuple(int x, int y) : x(x), y(y)
    def __init__(self, x, y):
        self._initialize_instance_fields()

        self.x = x
        self.y = y

