import pytest
import lca

#simple binary tree test. Testing right subtree
def test_pathFinder1():
    path = []
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    assert lca.findPath(root, path, 3) == True

#simple binary tree test. Testing left subtree
def test_pathFinder2():
    path = []
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    assert lca.findPath(root, path, 2) == True

#Testing with null root
def test_pathFinder3():
    path = []
    root = None
    assert lca.findPath(root, path, 3) == False

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

#Testing with simple bianry tree
def test_lcaFind():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    assert lca.findLCA(root, 2, 3) == 1
