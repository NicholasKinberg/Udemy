class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def height(root):
    if root is None:
        return 0
    return 1 + height(root.left) # recursive program defaults to counting nodes you tell it to count

root = Node(10)
root.left = Node(9)
root.left.left = Node(8)
root.right = Node(7)
root.right.right = Node(6)

print("Number of nodes in the binary tree is:", count_nodes(root))
print("Height of binary tree is:", height(root))