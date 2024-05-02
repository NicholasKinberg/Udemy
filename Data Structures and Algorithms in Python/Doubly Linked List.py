# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None # not necessarily circular, but using next and prev will enable doubly linked list

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None # initiate head and tail variables in DLL class instead of Node class
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += '<->'
            temp_node = temp_node.next # cycles through temp_node until it reaches end of DLL
        return result

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # node following tail will be new_node because of append
            new_node.prev = self.tail # node before new_node will be tail
            self.tail = new_node # new_node is now tail
        self.length += 1 # increase length of DLL by 1
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        # will use a while loop
        current_node = self.head
        while current_node:
            print(current_node.value) # add .value because node is just key, value is value tied to key
            current_node = current_node.next # no need to issue break command because self.tail = None, so it won't cycle because DLL is not circular doubly linked list
    
    def reverseTraverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.value == target: # for search function, implement function where value of current_node is checked for whether it equals target value
                return True
            current_node = current_node.next # in while loop, need to implement current_node = current_node.next to cycle through DLL
        return False