# Python Program to find the lowest common ancestor (LCA) of a Binary Tree

#Binary tree node
class Node:
    #constructor
     def __init__(self, key):
     self.right = None
     self.left = None
     self.key = value

# Recursive function to find path from root to a given node
def findPath( root, path, keyToFind):
    #check if root is null
    if root is None
            return false

    #begin path array with root
    path.append(root.value)

    # See if the k is same as root's key
    if root.key == k :
        return True

    #check if key is found in left or right subtrees
    if ((root.left != None and findPath(root.left, path, keyToFind)) or
            (root.right!= None and findPath(root.right, path, keyToFind))):
        return True

    #if path cannot be found empty the array and exit
    path.pop()
    return False
