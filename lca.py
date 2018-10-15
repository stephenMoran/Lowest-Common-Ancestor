# Python Program to find the lowest common ancestor (LCA) of a Binary Tree
#O(n) runtime
#Assumptions: nobod inserts duplicate keys into the binary tree

#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
