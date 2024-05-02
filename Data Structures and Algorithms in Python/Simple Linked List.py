# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
class Node:
    # need functions for insertion, deletion, traversal, search
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
    def getNextNode(self):
        return self.next
    def setNextNode(self, node):
        self.next = node
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 1
    def getSize(self):
        return self.size
    def addNode(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size += 1
    def remove_first_node(self):
        if(self.head == None):
            return
        self.head = self.head.next
    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1 # initiated position variable equalling zero to then iterate until it reached given index
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next # once while loop reaches given index, set next to nextnextnext to remove nextnext
            else:
                print("Index not present")
    def print_method(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next