# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# describe how you would use a single python list to implement three stacks
stack = []
# stack uses last-in, first-out format
stack.append('a')
stack.append('b')
stack.append('c')

# print(full_stack)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3 # notice that this variable isn't named in the function parentheses, set equal to a constant as an example
        self.custList = [0] * (stacksize * self.numberstacks) # stacksize multiplied by 3 for 3 stacks
        self.sizes = [0] * self.numberstacks # size of each stack is 3, 3 * 3 = 9
        self.stacksize = stacksize
    
    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize: # if statement to check whether index equals stacksize, checking whether full
            return True
        else:
            return False
    
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0: # produces length of stacks
            return True
        else:
            return False
    
    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize # returns index of top value by setting offset equal to stack number times stack size (two-dimensional)
        return offset + self.sizes[stacknum] - 1 # remember that python starts with index 0 so subtract 1 to obtain true index
    
    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return 'stack is full'
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item
    
    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return 'stack is empty'
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1 # subtracts value at last index position, LIFO
            return value
    
# implement queue class after stack class
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


# stack is last in, first out (LIFO)
# queue is first in, first out (FIFO)