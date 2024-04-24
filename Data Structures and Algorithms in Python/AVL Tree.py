# An AVL tree defined as a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees for any node cannot be more than one.
# nothing to do with values, everything to do with number of nodes that are left and right children
# use balancing through rotation to restore balance between -1 and 1 to AVL tree
# in cases without rotation, insert the node based on left being lesser than root node and right being greater than root node, no need for rotation
# in cases with rotation, insert root node as you normally would, conclude that AVL tree is now unbalanced, and fix this
    # focus on subtree into which you have inserted root node, and then reorient that tree such that...
    # ...inserted node is in correct position (left child is lesser than parent, right node is greater than parent)
import StacksAndQueuesForBinaryTrees as Queue
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue: # searches in left subtrees because left node value is less than root node value
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue) # recursive function to continue searching left subtree until nodeValue is found
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

# algorithm for left left condition
# rotateRight(disbalancedNode):
    # newRoot = disbalancedNode.leftChild
    # disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    # newRoot.rightChild = disbalancedNode
    # update height of disbalancedNode and newRoot
    # return newRoot

    # this algorithm assumes insertion of new node and forces one to identify the node at which AVL tree becomes disbalanced
    # note that left child of disbalancedNode is newRoot, so this algorithm hinges on identifying disbalancedNode, not new inserted node
    # note that rotation occurs with disbalancedNode becoming rightChild of newRoot



# algorithm for left right condition, two parts, two different disbalancedNode
# rotateLeft(disbalancedNode):
    # newRoot = disbalancedNode.rightChild
    # disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    # newRoot.leftChild = disbalancedNode
    # update height of disbalancedNode and newRoot
    # return newRoot
    
    # notice that for the first part of this algorithm (rotateLeft()), it treats immediate parent node as disbalancedNode instead of grandparent node

# rotateRight(disbalancedNode):
    # newRoot = disbalancedNode.leftChild
    # disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    # newRoot.rightChild = disbalancedNode
    # update height of disbalancedNode and newRoot
    # return newRoot



# algorithm for right right condition
# rotateLeft(disbalancedNode):

# algorithm for right left condition
# rotateRight(disbalancedNode):
# rotateLeft(disbalancedNode):