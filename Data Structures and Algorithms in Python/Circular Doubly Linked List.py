# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# circular doubly linked list goes back and forth, in a circle (like a metro system)
# self.tail.next = Node(value) just means that self.tail will have in its .next address as Node(value), so Node(value) follows self.tail, and so on
from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None # need prev because doubly linked list
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' <-> '.join(values) # join values with a ' <-> '
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next # points to next node in list, extends length by 1
        return result
    
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
    
    def append(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode # set self.tail.next to newNode to append
            newNode.prev = self.tail # node previous to newNode becomes new self.tail
            self.tail = newNode # newest self.tail becomes newNode
        self.length += 1
        return self.tail
# note that if I set x = y in one line and then set y = 0 in the next, x does NOT take on value of 0, x takes on value of y at time of assignment