# Python Program to find the lowest common ancestor (LCA) of a Binary Tree
#O(n) runtime
#Assumptions: nobod inserts duplicate keys into the binary tree

#Class to represent a graph
class DirectedGraph:

    linkCount = 0


    class Node:
        def __init__( self, data ):
            self.data = data
            self.links = []

    def pointsTo( self, node ):
      self.links.append( node )
      DirectedGraph.linkCount += 1


    def __init__( self ):
        self.nodes = []
        self.nodeCount = 0

    def newNode( self, data ):
        node = self.Node( data )
        self.nodes.append( node )
        self.nodeCount += 1
        return node
        
    def __repr__( self ):
        result = ""
        for node in self.nodes:
            for link in node.links:
                result += "{0} --> {1}\n".format( node.data, link.data )
        return result


#If two LCAS give the first found result
#
