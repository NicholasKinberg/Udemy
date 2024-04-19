import random
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Casino:
    def __init__(self, person, amount):
        self.person = None
        self.amount = amount
    
    def enter(self, person):
        node = Node(person, self.person)
        self.person = node

    def linkedlist(self, person):
        if self.person is None:
            print('this casino is empty')
            return
        
        itr = self.person
        llstr = ''
        while itr:
            llstr += str(itr.data) + '---'
            itr = itr.next
        
        print(llstr)

    def win_and_leave(self, person, amount):
        amount = random.randint(-10000, 10000)
        return person + ' has left the casino with $' + amount
### problem with above line of code is it might not specify that I want someone to enter who is entering casino
### add functionality that returns an error if user mentions someone not in the casino, also other Udemy instructions