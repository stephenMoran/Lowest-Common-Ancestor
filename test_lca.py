import pytest
import lca

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

def test_lcaFind4():
#LCA test 4
#Testing findLCA with negative keys
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    root.left.left = lca.Node(4)
    root.left.right = lca.Node(5)
    assert lca.findLCA(root, -1 , -5) == -1
