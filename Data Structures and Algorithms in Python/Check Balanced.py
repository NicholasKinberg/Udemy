# Problem statement: Implement a function to check if a binary tree is balanced. 
# For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
def isBalancedHelper(root):
    if root is None:
        return 0
    left = isBalancedHelper(root.left)
    if left == -1:
        return -1
    right = isBalancedHelper(root.right)
    if right == -1:
        return -1
    if abs(left-right)>1:
        return -1
    return max(left, right)

# pseudocode:
    # recursively obtain height of left and right subtrees, then subtract one from the other using an absolute value function that returns -1 if value is greater than 1

def isBalanced(root):
    return isBalancedHelper(root) > -1

# pseudocode:
    # isBalanced(root) returns False if function is lesser than -1, indicating imbalance

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        # initiate node class to implement AVL tree