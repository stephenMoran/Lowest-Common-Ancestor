# Python Program to find the lowest common ancestor (LCA) of a directed acyclic graph


#Class to represent a graph
class DirectedGraph:

    linkCount = 0
    #Class to represent graph nodes
    class Node:
        #Node constructor
        def __init__( self, data ):
            self.data = data
            self.linksTo = []
            #maintaining linksFrom so a full list of parent nodes can be created for each node
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


    #find Lowest Common Ancestor function
    #Parameters - two nodes X and Y
    #Return - data held in LCA node
    #Will only give one answer even when there are two nodes that could be the LCA
    def findLCA(self, x, y):
        if(x is not None and y is not None):
            #find list of ancestors of node X
            parX = self.bfs(x)
            #find list of ancestors of node Y
            parY = self.bfs(y)
            #List of common parent ancestors
            commonNodes = self.commonElements(parX, parY)

            if commonNodes != []:
                maxDist = -1
                lca = 0
                for i in commonNodes:
                    print("\n")
                    print(i.data)
                    print(i.distToRoot)
                    #if new lca found, update
                    if i.distToRoot > maxDist:
                        maxDist = i.distToRoot
                        lca = i.data
                return lca
            else:
                return -1
        else:
            return  -1

s
    #Breadth First search to find all ancestors of a given node
    #Parameters - root node to begin the search from
    #Return - list of visited nodes
    #For this solution, the given node is the root and paths are found to all parent nodes
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
        visited.append(start)
        return visited

    #Find common elements function
    #Parameters - two lists of nodes
    #Return - List containing the intersection of the two lists
    def commonElements(self, list1, list2):
        if(list1 is not None and list2 is not None):
            return [element for element in list1 if element in list2]
        else:
            return []
