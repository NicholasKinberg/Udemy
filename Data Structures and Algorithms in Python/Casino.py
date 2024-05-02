# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
import random
class Casino:
    # names = ['Sarah', 'Joseph',' Abhishek', 'Nicholas',' Bill', 'Trevor',
    #          'Michael', 'Jared', 'Jessica', 'Jennifer', 'Stephanie', 'Todd']
    # program the function to reject any name not above
    def __init__(self, name, enter, exit, winnings=random.randint(-10000, 10000)):
        self.name = name
        self.enter = enter
        self.exit = exit
        self.winnings = winnings
# a person enters the casino
# the function should randomize how much a person wins
# think of each instance as individual function, such that the function directly below will return a random number...
# ...for the person who enters the casino
    def name(self):
        dict = {}
        self.name = input("What is your name?")
        return dict([(self.name, random.randint(-10000, 10000)) for self.name in dict])

    def enter(self):
        self.enter = input("Would you like to enter the casino? Type 'Yes' or 'No'.")
        if self.enter == 'Yes':
            return f"{self.name} has entered the casino."
        else:
            return f"{self.name} has refused to enter the casino."

    def exit(self):
        self.exit = input("Would you like to leave the casino? Type 'Yes' or 'No'.")
        if self.exit == 'Yes':
            return f"{self.name} has exited the casino."
        else:
            return f"{self.name} will stay in the casino."
        
    def winnings(self):
        winnings = winnings.randint(0, 10000)
        if winnings > 0:
            return f"{self.name} has won {self.winnings}!"
        if winnings < 0:
            return f"{self.name} has lost {self.winnings}."
        else:
            return f"{self.name} has not won anything."
    
    # I added the code below to stop the terminal from reporting the memory position of a Casino object
    # the problem is that I want the function to take the example 4 lines below
    def __repr__(self):
        return "meaningful representation (or is it?)"

print(Casino('Nicholas', True, False))
# once you finish this function, edit the function so that specific names are entered into the function
# additionally, if someone enters a name not in the array already in the function, say that this person is not allowed in the casino