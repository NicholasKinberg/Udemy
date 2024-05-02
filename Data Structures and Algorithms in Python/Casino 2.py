# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
import random
def name():
    # need function to input name
    # need function to attach random number to name
    # need function to print name and random number in dictionary, key and value
    # problem with this function is that Python treats initiation of dictionary with just names as a set...
    # ...because those names do not have values (names are treated as keys)
    # two ways of solving this: giving each key a value 0 and updating values with random numbers or...
    # ...converting set to dictionary with random numbers
    dict = {}
    names = input("What is your name?")
    for name in names:
        dict[name] = random.randint(-10000, 10000)
    print(dict)

# need to edit function such that I can input multiple names and have the console return a random value for each
name()