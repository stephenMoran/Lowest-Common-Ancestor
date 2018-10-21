# Python Program to find the lowest common ancestor (LCA) of a Binary Tree
#O(n) runtime
#Assumptions: nobod inserts duplicate keys into the binary tree

#Class to represent a graph
class DirectedGraph:

    linkCount = 0
    #Class to represent graph nodes
    class Node:
        #Node constructor
        def __init__( self, data ):
            self.data = data
            self.linksTo = []
            self.linksFrom = []
            self.distToRoot = 0
        #Node method
        def pointsTo( self, node ):
            self.linksTo.append( node )
            DirectedGraph.linkCount += 1
            node.linksFrom.append(self)
            if node.distToRoot == 0 or node.distToRoot > self.distToRoot + 1:
                node.distToRoot = self.distToRoot + 1

    #Directed Graph constructor
    def __init__( self ):
        self.nodes = []
        self.nodeCount = 0
    #Directed Graph class methods
    #Adds new node to graph
    def newNode( self, data ):
        node = self.Node( data )
        self.nodes.append( node )
        self.nodeCount += 1
        return node
    #visualisation of graph
    def __repr__( self ):
        result = ""
        for node in self.nodes:
            for link in node.linksTo:
                result += "{0} --> {1}\n".format( node.data, link.data )
        return result


    #If two LCAS give the first found result
    def findLCA(self, x, y):
        parX = self.bfs(x)
        for i in parX:
            print(i.data)
        parY = self.bfs(y)
        for j in parY:
            print(j.data)
        commonNodes = self.common_elements(parX, parY)
        if commonNodes != []:
            maxDist = -1
            lca = 0
            for i in commonNodes:
                if i.distToRoot > maxDist:
                    lca = i.data
            return lca
        else:
            return -1



    #Use bfs to find all parents for x and y
    def bfs(self, start):
        visited = []
        queue = [start]
        level = 0
        while queue:
            vertex = queue.pop(0)
            for i in vertex.linksFrom:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        return visited

    def common_elements(self, list1, list2):
        return [element for element in list1 if element in list2]
