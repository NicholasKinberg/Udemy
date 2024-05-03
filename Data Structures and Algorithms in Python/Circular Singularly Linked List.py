# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# pseudocode for circular singularly linked list
# need at least two classes, one for the individual nodes, one for the entire CSLL
# node class:
    # initiate value and next variables, for the node itself and the value to which it will link
    # notice that there is only next and no prev, meaning that this list goes in only one direction

    # initiate __str__ to turn node into string

# circular singularly linked list class:
    # initiate at least the head and tail variables, to establish the beginning and end of a circular list
    # end will point to head and not vice versa because this is a circular SINGULARLY linked list
    # initiate a length variable that will allow us to determine length of CSLL later

    # initiate __str__ to read nodes as strings
        # create a temporary node variable and set it equal to head of CSLL
        # initiate an empty 'result' variable for later use
        # while the temporary variable is not empty...
            # ...we lengthen the result with each temporary node value
            # and we build the CSLL by assigning the temporary node to its next value, as we initiated in the Node class
            # and once the temporary node sets itself equal to the head of the CSLL, the while loop stops because we issue the 'break' command
            # for illustration, we set the 'result' variable equal to ' -> ' to make it look like a CSLL
            # the break command is crucial to make sure that the code doesn't run on an infinite loop
        # and we then return the result outside the while loop

    # to make the above summary cleaner, we initiate Node and CSLL classes
    # then we create head and tail variables and set temporary node equal to head
    # then we use a while loop to make it a circle, eventually breaking by setting the temporary node equal to the head again

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self) -> str:
        # initializing temp_node variable and setting equal to beginning of circular singularly linked list (CSLL)
        temp_node = self.head
        # result is empty, for initialization
        result = ''
        # while loop, while temp_node is not empty...
        while temp_node is not None:
            # ...result adds temp_node.value to itself
            result += str(temp_node.value)
            # temp_node is then assigned to next element in CSLL
            temp_node = temp_node.next
            # if temp_node is equal to beginning of data set, stop the while loop
            if temp_node == self.head:
                break
            # the below line of code adds arrows to the CSLL
            result += ' -> '
        return result
    
    def append(self, value):
        # initialize new_node variable and set equal to given Node value
        new_node = Node(value)
        if self.length == 0:
            # given CSLL length 0, self.head and self.tail will both equal new_node, new_node.next will equal new_node
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else: # setting self.tail.next equal to new_node to append, because appending puts new_node at end of CSLL
            # append by assigning value after self.tail to new_node
            self.tail.next = new_node
            # new_node.next becomes beginning of data set
            new_node.next = self.head
            # end of data set then becomes new_node
            self.tail = new_node
            # increase CSLL length by 1 for each addition
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            # same code as append(), for when CSLL is initially empty
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            # new_node.next becomes beginning of CSLL
            new_node.next = self.head
            # beginning of data set is then assigned to new_node
            self.head = new_node
            # value after self.tail becomes new_node
            self.tail.next = new_node
            # increase CSLL length by 1
        self.length += 1
    
    def delete(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = None
            self.tail = None
            new_node = None
        else:
            new_node = new_node.next.next
        self.length -= 1

    def traverse(self):
        current = self.head
        while(current):
            print(current.node)
            current = current.next
            if current == self.head:
                break
    
    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break # to break the while loop over the CSLL
        return False
    
    # to implement pop method, set node before node equal to node after node, maybe self.head = node.next?
    # popped node = None, None = self.tail?
    def get(self, index):
        current = self.head # think of setting a current variable to self.head as a pointer, pointer cycles through linked list
        for _ in range(index): # _ means for loop will loop through entire linked list and won't just stop at index
            current = current.next # current is assigned to and loops through current.next iterations until it reaches given index
        return current
    
    def remove(self, index):
        prev_node = self.get(index-1) # no need to initiate prev variable in Node class because we can just define prev as index-1
        popped_node = prev_node.next # popped node is the node following the previous node since prev_node is initiated with index-1
        # popped node now points to node following previous node
        prev_node.next = popped_node.next # node following previous node now points to node following popped node
        popped_node.next = None # popped node now points to nothing
        self.length -= 1
        return popped_node
# note that if I set x = y in one line and then set y = 0 in the next, x does NOT take on value of 0, x takes on value of y at time of assignment


