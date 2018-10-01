import lca
import pytest


#pathFind test 1
#simple binary tree test. Testing right subtree
def test_pathFinder1():
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

#LCA test 1
#Testing with simple binary tree
def test_lcaFind1():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    assert lca.findLCA(root, 2, 3) == 1

#LCA test 2
#Testing findLCA with no paths available
def test_lcaFind2():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    assert lca.findLCA(root, 4, 3) == -1

#LCA test 3
#Testing findLCA with larger tree
def test_lcaFind3():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    root.left.left = lca.Node(4)
    root.left.right = lca.Node(5)
    root.right.left = lca.Node(6)
    root.right.right = lca.Node(7)
    assert lca.findLCA(root, 5, 7) == 1


#LCA test 4
#Testing findLCA with negative keys
def test_lcaFind4():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    root.left.left = lca.Node(4)
    root.left.right = lca.Node(5)
    assert lca.findLCA(root, -1 , -5) == -1

#LCA test 5
#Testing findLCA with null root
def test_lcaFind5():
    root = None
    assert lca.findLCA(root, 1 , 8) == -1

#LCA test 6
#Testing with larger tree
def test_lcaFind6():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    root.left.left = lca.Node(4)
    root.left.right = lca.Node(5)
    root.right.left = lca.Node(6)
    root.right.right = lca.Node(7)
    root.left.left.left = lca.Node(8)
    root.left.left.right = lca.Node(9)
    root.left.right.right = lca.Node(10)
    root.right.right.left = lca.Node(11)
    root.right.right.right = lca.Node(12)
    assert lca.findLCA(root, 8, 10) == 2


#LCA test 7
#Testing with duplicate keys
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
