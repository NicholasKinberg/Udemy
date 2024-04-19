class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# function prints location of value in memory
# new_node = Node(10)
# print(new_node)

# writing function to append to linked list or insert in middle of linked list 
class LinkedList:
    def __init__(self, value):
        # call class from above
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(Node.value)
            if temp_node is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    # the below code cycles through a linked list
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index-1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False
    
new_linked_list = LinkedList(10)
# you can use x = class() to run a class function but you must use x.method() to run an instance/method function
print(new_linked_list.append(10))