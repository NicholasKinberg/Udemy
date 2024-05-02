# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# binary search tree
# each node has two children at most
# left child has value less than parent node
# right child has value greater than parent node
# this layout allows for efficient searching, insertion, deletion operations on data sorted in tree
import StacksAndQueuesForBinaryTrees as Queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
# insertNode() only began to work once I set the program outside the class BSTNode
# function didn't work as recursive inside class because I didn't use self.insertNode()
# need to use self.function() if I want to use recursion within a class
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue) # O(n/2) because it iterates over half of n due to inserting left or right child, not both
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"
# pre-order traversal works by going from root node to left-most node, so root node, left node, left node, ..., left node on left side
# then pre-order traversal goes to right nodes on left side, then to right side, then to all left nodes on right side, then right nodes on right side
def preOrderTraversal(rootNode):
    if not rootNode:
        return None
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# in-order traversal works subtree by subtree, so if I have a subtree of a parent node and two children...
# ...I use in-order traversal by going from left child (smallest node) to parent to right child (largest node)
def inOrderTraversal(rootNode):
    if not rootNode:
        return None
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# post-order traversal starts from last left-most node and cycles through right child, then parent node, and starts again, until ending at root node
def postOrderTraversal(rootNode):
    if not rootNode:
        return None
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# level-order traversal traverses BST by starting at root node and then going level by level, left to right

def levelOrderTraversal(rootNode):
    queue = []
    if not rootNode:
        return None
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)