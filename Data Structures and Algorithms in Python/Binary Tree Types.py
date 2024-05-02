# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# implementation of binary trees with linked lists or Python lists
import StacksAndQueuesForBinaryTrees as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode: # O(1) time
        return
    print(rootNode.data) # O(1) time, just printing rootNode
    preOrderTraversal(rootNode.leftChild) # O(n/2) because traversing half of list, on left
    preOrderTraversal(rootNode.rightChild) # O(n/2) because traversing half of list, on right

def inOrderTraversal(rootNode): # in order traversal starts with the left-most deepest node, then expands to and traverses its tree, then expands to and traverses that tree, and so on until it traverses the whole BT
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data) # the order in which you place the print(rootNode.data) command MATTERS
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
# post order traversal goes down to deepest left-most node, but instead of going straight to its parent, it then goes to the rightChild at its level, then goes to parent, and so on
# however, post order traversal doesn't arrive at root node until last recursion

# level order traversal traverses by level of node, level 1 for root, level 2 for after level 1, and so on

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode) # use value later in this program because we use it to establish values for nodes in StacksAndQueuesForBinaryTrees
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)