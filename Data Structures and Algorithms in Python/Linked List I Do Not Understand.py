class Node:
    def __init__(self, data, value=0):
        # Node will be individual element that, when linked together, will form linked list
        self.data = data
        # "next" variable will be used to shift to next element in data set
        self.next = next
        self.value = value

# think of a linked list like a youtube music playlist, you can add and delete entries wherever you want
class LinkedList:
    def __init__(self):
        self.head = None
        # initiating linked list program
    def print_list(self):
        temp = self.head
        # initiating temporary variable, assigning to head of data set
        while temp:
            # while on head of data set, print head of data from Node class, end is space
            print(temp.data, end=" ")
            temp = temp.next
            # temp then switches to next entry, and so on to print the entire linked list
    def insertAtBeginning(self, new):
        # new node is new data from Node class
        new_node = Node(new)
        # new node switches to next node when referring to head of data
        new_node.next = self.head
        # head then becomes node before new node
        self.head = new_node
    def insertAtIndex(self, data, index):
        # new_node variable set equal to Node data
        new_node = Node(data)
        # set current_node equal to head of data
        current_node = self.head
        # initiate position variable equaling 0
        position = 0
        # user indicates index position at which they want to insert new data
        # so if position = 0 and 0 == index...
        if position == index:
            # we can just call the insertAtBeginning command we built previously
            self.insertAtBeginning(data)
        else:
            # otherwise, while current_node does not equal None and position (which equals 0) + 1 does not equal index...
            # ...assign position variable the value of position + 1 (remember that the while condition means this while loop will iterate until it reaches index position)
            while(current_node != None and position+1 != index):
                position = position+1
                # notice that code will iterate on position until position + 1 == index
                # code will continue iterating through data set, assigning current_node to current_node.next until position + 1 == index
                current_node = current_node.next
            if current_node != None:
                # if current_node does not equal none, new_node.next will assign to current_node.next
                new_node.next = current_node.next
                # and current_node.next will assign to new_node but not new_node.next so that code continues to iterate
                current_node.next = new_node
            else:
                # if index is not already present in data set, code will return "Index is not present"
                print("Index is not present")
    # program to update value at index position
    def updateNode(self, value, index):
        # set current_node equal to beginning of dataset
        current_node = self.head
        # initialize position variable at 0
        position = 0
        # if position == index provided by user...
        if position == index:
            # ...current node, which equals beginning of data set, will assign to value
            current_node.data = value
        else:
            # while loop where if current_node is not None and position (which equals 0) is not index...
            while(current_node != None and position != index):
                # position will assign to position + 1 to iterate until data set reaches indicated index position
                position = position+1
                # current_node will then assign to next position
                current_node = current_node.next
            if current_node != None:
                # and if current_node does not equal None, current_node will equal given value at indicated index position to update index position with that value
                current_node.data = value
            else:
                # else program will print "Index not present"
                print("Index not present")
    def removeFirstNode(self):
        # program to remove first node
        # if beginning of data set equals none, return nothing because there is nothing to do
        if self.head == None:
            return
        # otherwise, set beginning of data set to next entry in data set to "pop" first entry out
        self.head = self.head.next
    def removeLastNode(self):
        # program to remove last node
        # if beginning of data set equals none, return nothing because there is nothing in data set
        if self.head == None:
            return
        # otherwise, set current_node equal to beginning of data set
        current_node = self.head
        # initiate while loop to iterate across entire data set
        while(current_node.next.next):
            current_node = current_node.next
        # once you reach last node, set equal to None
        current_node.next = None
    def removeAtIndex(self, index):
        # program to remove value at given index position
        # if beginning of data set is already empty, return nothing
        if self.head == None:
            return
        # set variable current_node equal to beginning of data set
        current_node = self.head
        # set variable position equal to 0
        position = 0
        # if position equals index, just use removeFirstNode command from above
        if position == index:
            self.removeFirstNode()
        # else, while loop where current_node is not None and position + 1 does not equal given index...
        else:
            while current_node != None and position+1 != index:
                # ...add 1 to position variable and set current_node variable to next entry
                position = position+1
                current_node = current_node.next
            if current_node != None:
                # if current_node does not equal None, iterate until you reach end of data set (why not just class removeLastNode()?)
                current_node.next = current_node.next.next
            else:
                # otherwise just print "Index not present" because given index is not present in data set
                print("Index not present")
    def mergeTwoLists(self, l1, l2):
        # program to merge two lists
        # set prehead variable equal to value -1 for Node value
        prehead = Node(-1)
        # set prehead equal to prev variable
        prev = prehead
        # while loop for l1 and l2
        while l1 and l2:
            # if l1 value (declared in Node class) is less than or equal to l2 value, prev.next equals l1 and l1 is set to next l1 value
            if l1.value <= l2.value:
                prev.next = l1
                l1 = l1.next
            # else prev.next equals l2 and l2 is set to next l2 value
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        # prev.next is set to l1 if l1 is not None, otherwise prev.next is set to l2
        return prehead.next
    # OR
    def mergeTwoListsDifferent(self, l1, l2):
        if self.head == None:
            return
        new_list = l2.extend(l1)
        n = len(new_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if new_list[j] > new_list[j + 1]:
                    new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
        return new_list.head
    def deleteDuplicates1(self, head):
        # if data set is empty, return None
        if not head:
            return None
        # using set() command to remove nodes, set to seen variable
        seen = set()
        # create dummy node at Node(-1)
        dummy = Node(-1)
        # node after dummy node will be head
        dummy.next = head
        # set node before head, prev_node, equal to dummy
        prev_node = dummy
        # set current_node equal to head
        current_node = head
        # while loop where while current_node, if current_node is in set...
        while current_node:
            # ...prev_node equal to dummy equal to Node(-1), node after that which is prev_node.next...
            if current_node.value in seen:
                # ...set prev_node.next equal to current_node.next, which means...
                # ...notice that prev_node = dummy = -1
                # prev_node.next = head = current_node = 0
                # current_node.next = 1, so the while loop iterates across the linked list
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                # adding current_node.value to seen variable
                seen.add(current_node.value)
                # prev_node set equal to current_node
                prev_node = current_node
                # and current_node set equal to current_node.next
                current_node = current_node.next
        return dummy.next
        # summary: if current_node.value is in seen, which uses set() command to remove duplicates, program will remove duplicates
    # OR
    def deleteDuplicates2(self, head):
        # initiate current_node variable at head of LL
        current_node = head
        # while loop where current_node is not None and next node is not None
        while current_node is not None and current_node.next is not None:
            if current_node.value == current_node.next.value:
                # if current_node value equals next current_node value...
                # ...next current_node value is assigned to next next current_node value
                current_node.next = current_node.next.next
            else:
                # but if current_node value does not equal next current_node value, current_node is assigned to next current_node value
                current_node = current_node.next
        # then the program returns beginning of data set
        return head
    
    def deleteDuplicates3(self):
        current = self.head
        prev_node = None
        duplicate_dict = dict()
        while current:
            if current.value not in duplicate_dict:
                duplicate_dict[current.value] = None
                prev_node = current
            else:
                prev_node.next = current.next
            current = current.next
    
    def deleteDuplicates4(ll):
        if ll.head is None:
            return
        current_node = ll.head
        prev_node = None
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            prev_node = current_node
            current_node = current_node.next
        ll.tail = prev_node
        return ll.head

# Lessons: use while loops to iterate across data sets like linked lists that have indefinite sizes
    # Additionally, need to use while loop to iterate across LLs