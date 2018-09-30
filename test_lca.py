import pytest
import lca

#simple binary tree test
def test_pathFinder1():
    path = []
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    assert lca.findPath(root, path, 3) == True

#Testing with null root
def test_pathFinder2():
    path = []
    root = None
    assert lca.findPath(root, path, 3) == False