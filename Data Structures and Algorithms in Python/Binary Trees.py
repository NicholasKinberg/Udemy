# from first node, branches to two nodes, which continue to branch until reaching branch children which can be >=2
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
    def PrintTree(self):
        print(self.data)

    def insert(self, data):
        if self.data: # note that you don't need to say "is not None" because just saying if [insert data here] already asks the question of whether data is Null
            if data < self.data:
                if self.left is None:
                    self.left = Node(data) # inserting node where leftChild is None
                else:
                    self.left.insert(data) # recursive
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data) # inserting node where rightChild is None
                else:
                    self.right.insert(data) # recursivve
        else:
            self.data = data # inserting data entry where self.data is Null
    
    def inOrderTraversalandCount(self, root):
        res = [] # initialize empty list
        if root:
            res = self.inOrderTraversalandCount(root.leftChild)
            res.append(root.data) # append children
            res = res + self.inOrderTraversalandCount(root.rightChild)
        return len(res) + res # return length of res and res itself, thus producing count of nodes
    
    def height(self, root):
        res = []
        if root:
            res = self.inOrderTraversalandCount(root.leftChild)
            res.append(root.data)
        return len(res) + res

root = Node(27)
root.inOrderTraversalandCount(14)



# function called size that given binary tree, returns number of nodes it contains
# stack = a stack and insert root at first, count 0
# while stack is not empty, do this:
    # node = top element of stack, pop element
    # if node is not null, then
        # if left <= data of node <= right, then
            # count = count + 1
            # stack = push right of node and left of node into stack
        # otherwise when data of node < left, then
            # stack = push right of node into stack
            # otherwise,
            # stack = push left of node into stack
# return count

    # def getSize(self, stack, root, leftChild, rightChild):
    #     stack, count = [root], 0
    #     while stack is not None:
    #         for i in stack:
    #             node = stack[i], stack.pop(node)
    #         if leftChild <= node <= rightChild:
    #             count += 1