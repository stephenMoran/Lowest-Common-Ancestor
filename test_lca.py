import lca
import pytest


#pathFind test 1
#simple binary tree test. Testing right subtree
"""
Specific function tests
def test_pathFinder1():
    dg = DirectedGraph()
    n0 = dg.newNode(1)
    n1 = dg.newNode(2)
    n2 = dg.newNode(3)
    path = []
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    assert lca.findPath(root, path, 3) == True

#pathFind test 2
#simple binary tree test. Testing left subtree
def test_pathFinder2():
    path = []
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    assert lca.findPath(root, path, 2) == True

#pathFind test 3
#Testing with null root
def test_pathFinder3():
    path = []
    root = None
    assert lca.findPath(root, path, 3) == False

#pathFind test 4
#Testing with larger tree
def test_pathFinder4():
    path = []
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    root.left.left = lca.Node(4)
    root.left.right = lca.Node(5)
    root.right.right = lca.Node(6)
    root.right.left = lca.Node(7)
    assert lca.findPath(root, path , 7) == True
"""

#LCA test 1
#Testing with simple binary tree
def test_lcaFind1():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n1.pointsTo(n3)
    n1.pointsTo(n2)

    assert lca.findLCA(n2, n3) == 1

#LCA test 2
#Testing findLCA with no paths available
def test_lcaFind2():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n1.pointsTo(n3)
    n1.pointsTo(n2)

    assert lca.findLCA(n4, n2) == -1

#LCA test 3
#Testing findLCA with extra level tree
def test_lcaFind3():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n4 = dg.newNode(4)
    n5 = dg.newNode(5)
    n6 = dg.newNode(6)
    n7 = dg.newNode(7)
    n1.pointsTo(n2)
    n1.pointsTo(n3)
    n2.pointsTo(n4)
    n2.pointsTo(n5)
    n3.pointsTo(n6)
    n3.pointsTo(n7)
    assert lca.findLCA(n5, n7) == 1

#LCA test 4
#Testing with extra level tree
def test_lcaFind6():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n4 = dg.newNode(4)
    n5 = dg.newNode(5)
    n6 = dg.newNode(6)
    n7 = dg.newNode(7)
    n8 = dg.newNode(8)
    n9 = dg.newNode(9)
    n10 = dg.newNode(10)
    n11 = dg.newNode(11)
    n12 = dg.newNode(12)
    n1.pointsTo(n2)
    n1.pointsTo(n3)
    n2.pointsTo(n4)
    n2.pointsTo(n5)
    n3.pointsTo(n6)
    n3.pointsTo(n7)
    n4.pointsTo(n8)
    n4.pointsTo(n9)
    n5.pointsTo(n10)
    n5.pointssTo(n11)
    n6.pointsTo(n12)
    assert lca.findLCA(n8, n10) == 2

'''
#LCA test 5
#Testing with duplicate keys
#Test fails. We must assume that the user will use unique keys with API
def test_lcaFind7():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    root.left.left = lca.Node(4)
    root.left.right = lca.Node(5)
    root.right.left = lca.Node(6)
    root.right.right = lca.Node(7)
    root.left.left.left = lca.Node(8)
    root.left.left.right = lca.Node(3)
    root.left.right.right = lca.Node(10)
    assert lca.findLCA(root, 3, 10) == 1
'''
#LCA test 6
#Testing where node is descendent of itself
def test_lcaFind8():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n4 = dg.newNode(4)
    n5 = dg.newNode(5)
    n6 = dg.newNode(6)
    n7 = dg.newNode(7)
    n8 = dg.newNode(8)
    n9 = dg.newNode(9)
    n10 = dg.newNode(10)
    n11 = dg.newNode(11)
    n12 = dg.newNode(12)
    n1.pointsTo(n2)
    n1.pointsTo(n3)
    n2.pointsTo(n4)
    n2.pointsTo(n5)
    n3.pointsTo(n6)
    n3.pointsTo(n7)
    n4.pointsTo(n8)
    n4.pointsTo(n9)
    n5.pointsTo(n10)
    n5.pointssTo(n11)
    n6.pointsTo(n12)
    assert lca.findLCA(n10, n2) == 2

#LCA test 7
#Testing incest case where we try find the LCA using the same node for both parameters
def test_lcaFind9():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n1.pointsTo(n3)
    n1.pointsTo(n2)
    assert lca.findLCA(n2, n2) == 2
