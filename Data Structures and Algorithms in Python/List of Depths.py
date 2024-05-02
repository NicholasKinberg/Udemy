# when googling, if you find code suitable to problem, write the pseudocode behind the code and write your own code (find multiple methods and produce multiple pseudocodes)
# Problem statement: Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (ie , if you have a tree with depth D, you’ll have D linked lists)
class LinkedList: # linked list class to initialize linked list in functions
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val): # add function to add node to linked list
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    else:
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        if depthLeft > depthRight:
            return depthLeft
        else:
            depthRight

# pseudocode for depth(tree)
    # return tree height 0 if None
    # return tree height 1 if tree.left == None or tree.right == None
    # recursively add 1 to depth(tree.left) and 1 to depth(tree.right)
    # return whichever is greater

def treeToLinkedList(tree, custDict = {}, d = None):
    if d == None:
        d = depth(tree)
    if custDict.get(d) == None:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    if tree.left != None:
        custDict = treeToLinkedList(tree.left, custDict, d-1)
    if tree.right != None:
        custDict = treeToLinkedList(tree.right, custDict, d-1)
    return custDict

# pseudocode for treeToLinkedList(tree, custDict = {}, d = None)
    # if d is None, d is depth(tree)
        # if retrieving value of d (because we use get(key) to use get() function) is None, assign value to key d in linked list (each level of tree will have one key, so multiple values on certain tree level will have one key)
        # else add value of key d to linked list (and return custDict if d == 1 because custDict should just be root node in that case)
    # if tree left children exist, recursively create custom dictionaries for however many levels of the BST exist
    # if tree right children exist, recursively create custom dictionaries for however many levels of the BST exist