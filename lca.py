# Python Program to find the lowest common ancestor (LCA) of a Binary Tree
#O(n) runtime
#Binary tree node
class Node:
    #constructor
     def __init__(self, key):
         self.right = None
         self.left = None
         self.key = key

# Recursive function to find path from root to a given node
def findPath( root, path, keyToFind):
    #check if root is null
    if root is None:
            return False

    #begin path array with root
    path.append(root.key)

    # See if the k is same as root's key
    if root.key == keyToFind :
        return True

    #check if key is found in left or right subtrees
    if ((root.left != None and findPath(root.left, path, keyToFind)) or
            (root.right!= None and findPath(root.right, path, keyToFind))):
        return True

    #if path cannot be found empty the array and exit
    path.pop()
    return False


#Fucntion that determiens the lowest common ancestor
def findLCA(root, n1, n2):

    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    #If paths cannot be found exit
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        #when paths diverge we know that the LCA has been passed
        if path1[i] != path2[i]:
            break
        i += 1
    #backstep to find LCA va;ue and return
    return path1[i-1]
