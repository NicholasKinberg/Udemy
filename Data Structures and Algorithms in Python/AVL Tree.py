# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
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

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild # new root should be less than disbalanced node in value and thus left child of disbalanced node
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild # disbalanced node's left child becomes right child of disbalanced node's new left child
    newRoot.rightChild = disbalancedNode # disbalanced node shifts to become new root's right child, thus completing the right rotation
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)) # update height of disbalanced node to 1 + height of new left or right child of disbalanced node
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)) # same for newRoot
    return newRoot # returns new root to notify user that right rotation is successful

def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild # identify newRoot as right child of disbalanced node because newRoot is greater than disbalanced node
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild # right child of disbalanced node becomes left child of right child
    newRoot.leftChild = disbalancedNode # left child of newRoot becomes disbalanced node
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)) # extend height of disbalanced node
    newRoot.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)) # extend height of newRoot
    return newRoot # returns new root to notify user that left rotation is successful

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild) # returns whether AVL tree is balanced, and an AVL tree is balanced if its balance is inclusive between -1 and 1

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue) # if there isn't a root node, insert one using AVLNode()
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue) # inserting left child because nodeValue is less than rootNode, recursive
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue) # inserting right child because nodeValue is greater than or equal to rootNode, recursive
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild)) # extend height of rootNode
    balance = getBalance(rootNode) # obtain balance of AVL tree to ascertain that AVL tree remains AVL tree
    if balance > 1 and nodeValue < rootNode.leftChild.data: # left left condition, use right rotate
        return rightRotate(rootNode) # note that if statement is asking whether balance is greater than 1, implying that height of rootNode.leftChild is greater than that of rootNode.rightChild
    if balance < 1 and nodeValue > rootNode.leftChild.data: # left right condition, use leftRotate then rightRotate
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data: # right right condition, use leftRotate
        return leftRotate(rootNode)
    if balance > -1 and nodeValue > rootNode.rightChild.data: # right left condition, use rightRotate then leftRotate
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return rightRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is not None or rootNode.leftChild is not None:
        return rootNode # return rootNode when it is alone
    return getMinValueNode(rootNode.leftChild) # recursive, pursuing left-most child because leftChild should be lesser than rootNode

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode # if only rootNode exists, return rootNode and delete AVL tree
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue) # recursive, deletes nodeValue in left subtree because leftChild is less than rootNode
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue) # recursive, deletes nodeValue in right subtree because rightChild is greater than rootNode
    else:
        if rootNode.leftChild is None: # if rootNode has no leftChild...
            temp = rootNode.rightChild # ...initialize temp variable as rightChild of rootNode
            rootNode = None # assign rootNode to None
            return temp # return only temp, to delete rootNode, because the else statement is contingent on nodeValue equalling rootNode.data
        elif rootNode.rightChild is None: # if rootNode has no rightChild...
            temp = rootNode.leftChild # ...initialize temp variable as leftChild of rootNode
            rootNode = None # assign rootNode to None
            return temp # return only temp, to delete rootNode, because the else statement is contingent on nodeValue equalling rootNode.data
        temp = getMinValueNode(rootNode.rightChild) # assign temp to getMinValueNode of right subtree
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) # recursive, delete specified temp.data given rootNode.rightChild
    balance = getBalance(rootNode) # obtain balance of edited AVL tree to reassert balance after deletion of temp
    if balance > 1 and getBalance(rootNode.leftChild) >= 0: # if height of left subtree is greater than that of right subtree and balance of left subtree is greater than or equal to 0...
        return rightRotate(rootNode) #...implement rightRotate on rootNode; left left condition, rightRotate
    if balance < -1 and getBalance(rootNode.rightChild) <= 0: # if height of left subtree is lesser than that of right subtree and balance of right subtree is lesser than or equal to 0...
        return leftRotate(rootNode) #...implement leftRotate on rootNode; right right condition, leftRotate
    if balance > 1 and getBalance(rootNode.leftChild) < 0: # if height of left subtree is greater than that of right subtree and balance of left subtree is lesser than 0...
        rootNode.leftChild = leftRotate(rootNode.leftChild) #...implement leftRotate of rootNode.leftChild
        return rightRotate(rootNode) # then implement rightRotate of rootNode; left right condition, leftRotate, rightRotate
    if balance < -1 and getBalance(rootNode.rightChild) > 0: # if height of left subtree is lesser than that of right subtree and balance of right subtree is greater than 0...
        rootNode.rightChild = rightRotate(rootNode.rightChild) #...implement rightRotate of rootNode.rightChild
        return leftRotate(rootNode) # then implement leftRotate of rootNode; right left condition, rightRotate, leftRotate
    return rootNode