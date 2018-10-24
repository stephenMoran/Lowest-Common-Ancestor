import lca
import pytest


"""

Tests that show findLCA assumptions

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


#Testing findLCA with no paths available
#Test fails. Error is thrown. We must assume the user will not try to pass a variable that
def test_lcaFind2():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n1.pointsTo(n3)
    n1.pointsTo(n2)

    assert dg.findLCA(n4, n2) == -1

"""


#**COMMON_ELEMENTS TESTS**

#commonElements test 1
#Testing with normal case
def test_common1():
    dg = lca.DirectedGraph()

    list1 = [1,2,3,4,5,6]
    list2 = [6,5,4,3,2]

    common = dg.commonElements(list1, list2)
    assert common == [2,3,4,5,6]

#commonElements test 2
#Testing with no common elements
def test_common2():
    dg = lca.DirectedGraph()

    list1 = [1,2,3,4,5,6]
    list2 = [7,8,9]

    common = dg.commonElements(list1, list2)
    assert common == []

#commonElements test 3
#Testing with empty lists
def test_common3():
    dg = lca.DirectedGraph()

    list1 = []
    list2 = []

    common = dg.commonElements(list1, list2)
    assert common == []

#commonElements test 4
#Testing with null arguements
def test_common4():
    dg = lca.DirectedGraph()

    list1 = None
    list2 = None

    common = dg.commonElements(list1, list2)
    assert common == []

#**LCA FUNCTION TESTS**

#LCA test 1
#Testing with simple binary tree
def test_lcaFind1():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n1.pointsTo(n3)
    n1.pointsTo(n2)

    assert dg.findLCA(n2, n3) == 1


#LCA test 2
#Testing findLCA with extra level tree
def test_lcaFind2():
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
    assert dg.findLCA(n5, n7) == 1

#LCA test 3
#Testing with extra level tree
def test_lcaFind3():
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
    n5.pointsTo(n11)
    n6.pointsTo(n12)
    assert dg.findLCA(n8, n10) == 2


#LCA test 4
#Testing where node is descendent of itself
def test_lcaFind4():
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
    n5.pointsTo(n11)
    n6.pointsTo(n12)
    assert dg.findLCA(n10, n2) == 2

#LCA test 5
#Testing incest case where we try find the LCA using the same node for both parameters
def test_lcaFind5():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n1.pointsTo(n3)
    n1.pointsTo(n2)
    assert dg.findLCA(n2, n2) == 2


#LCA test 6
#Testing with duplicate LCA
#Implementation returns first found result if there are more than one possible LCA's
def test_lcaFind6():
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
    n3.pointsTo(n5)
    n4.pointsTo(n6)
    n4.pointsTo(n7)
    n5.pointsTo(n6)
    n5.pointsTo(n7)
    assert dg.findLCA(n6, n7) == 4

#LCA test 7
#Testing when node has multiple parents
def test_lcaFind7():
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
    n1.pointsTo(n2)
    n1.pointsTo(n3)
    n2.pointsTo(n4)
    n2.pointsTo(n5)
    n2.pointsTo(n6)
    n4.pointsTo(n7)
    n4.pointsTo(n8)
    n4.pointsTo(n9)
    assert dg.findLCA(n8, n5) == 2

#LCA test 8
#Testing with cyclic graph
#We make assumption that user will only use Directed Acyclic graphs
def test_lcaFind8():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n4 = dg.newNode(4)
    n1.pointsTo(n2)
    n2.pointsTo(n3)
    n3.pointsTo(n4)
    n4.pointsTo(n1)
    assert dg.findLCA(n1, n2) == 1

#LCA test 9
#Testing when graph is disjoint and x and y have no common parent nodes
def test_lcaFind9():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n4 = dg.newNode(4)
    n5 = dg.newNode(5)
    n6 = dg.newNode(6)
    n1.pointsTo(n2)
    n1.pointsTo(n3)
    n4.pointsTo(n5)
    n4.pointsTo(n6)
    assert dg.findLCA(n2, n6) == -1

#LCA test 10
#Testing when graph is disjoint and x and y have no common parent nodes
def test_lcaFind10():
    dg = lca.DirectedGraph()
    n1 = None
    n2 = None

    assert dg.findLCA(n1, n2) == -1

#LCA test 11
#Testing when nodes parents have multiple parents
#Even though there are 3 possible parents, the program returns the first lca node encountered
def test_lcaFind111():
    dg = lca.DirectedGraph()
    n1 = dg.newNode(1)
    n2 = dg.newNode(2)
    n3 = dg.newNode(3)
    n4 = dg.newNode(4)
    n5 = dg.newNode(5)
    n6 = dg.newNode(6)
    n7 = dg.newNode(7)
    n8 = dg.newNode(8)
    n1.pointsTo(n2)
    n1.pointsTo(n3)
    n1.pointsTo(n8)
    n2.pointsTo(n4)
    n2.pointsTo(n5)
    n3.pointsTo(n4)
    n3.pointsTo(n5)
    n8.pointsTo(n4)
    n8.pointsTo(n5)
    n4.pointsTo(n6)
    n5.pointsTo(n7)
    assert dg.findLCA(n6, n7) == 2
