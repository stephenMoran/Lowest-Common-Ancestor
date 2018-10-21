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
            distToRoot = 0
        #Node method
        def pointsTo( self, node ):
            self.linksTo.append( node )
            DirectedGraph.linkCount += 1
            node.linksFrom = self
            if(node.distToRoot == 0 or node.distToRoot > self.distToRoot + 1)
                node.distToRoot = self.distToRoot + 1)

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
            for link in node.links:
                result += "{0} --> {1}\n".format( node.data, link.data )
        return result


#If two LCAS give the first found result

def findLCA(x, y):
    return lca

def bfs(graph, start):
    visited = []
    queue = [start]
    level = 0
    while queue:
        vertex = queue.pop(0)
        for (var i = 0; i < vertex.links.length; i++)
        {
            node = vertex.linksFrom[i]
            if node not in visited:
            visited[i]= node
            visited[i] = level
            queue.append(node)
        }
    return visited
