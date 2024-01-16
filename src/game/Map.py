from ..constants.Rooms import Room
    class MapNode:

        def __init__(self):
            # instance fields found by C++ to Python Converter:
            self.x = 0
            self.y = 0
            self.parentCount = 0
            self.parents = []
            self.edgeCount = 0
            self.edges = []
            self.room = Room.NONE

            def addParent(self,parent):
                self.parentCount +=1
                self.parents.append(parent)

            def addEdge(self,edge):
                cur = 0
                while 1:
                    if cur == self.edgeCount:
                        self.edges.append(edge)
                        self.edgeCount +=1
                        return
                    if edge == self.edges[cur]:
                        return
                    if edge < self.edges[cur]:



def insertEdge(mapNode:MapNode,dstX:int,idx:int):
    for


    class Map:

        def __init__(self):
            self.burningEliteX = -1
            self.burningEliteY = -1
            self.burningEliteBuff = -1
            self.nodes = [None for _ in range(15)]





