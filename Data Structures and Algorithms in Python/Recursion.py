# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# recursion is a way of solving a problem by having the function call itself
# used when solution lies in smaller instance to same problem
# like a Russian nesting doll
# iteration is when a program runs until a condition is met, whereas recursion is when a program calls itself
# recursion in 3 steps:
    # 1. recursive case - the flow (problem that repeats itself in smaller and smaller iterations, like a factorial)
    # 2. base case - the stopping criterion, so recursion doesn't run forever
    # 3. unintentional case - the constraint, set inputs you can't enter so program doesn't break
def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer only!"
    if n == 1:
        return n # factorial is n * n - 1 * n - 2 * ... * n - (n - 1)
    else:
        return n * factorial(n-1) # don't complicate things, have confidence in your code and try it out

# print(factorial(5))

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are open")
    else:
        openRussianDoll(doll-1)

# openRussianDoll(doll=10)

def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

# recursiveMethod(n=10)

def powerOfTwoIterative(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power

# print(powerOfTwoIterative(5))

# write program to sum digits of positive integer number using recursion
def sumOfDigitsRecursive(n):
    if n == 0:
        return 0
    return (n % 10 + sumOfDigitsRecursive(int(n/10)))
    # this program works because it isolates the remainder from dividing by 10, thus isolating the last digit in each iteration

# print(sumOfDigitsRecursive(22345632))

# calculate power of a number using recursion
def powerOfNumber(x, y):
    assert int(y) == y, "For the purposes of this function, we will not include float exponents"
    if y == 0: # x stays the same, y decreases with each recursion
        return 1 # x times x, y times
    elif y < 0:
        return 1/x * powerOfNumber(x, y+1) # reverse the direction of recursion by adding 1 instead of subtracting 1
    return x * powerOfNumber(x, y-1)

print(powerOfNumber(3, 10))
# simplify recursion implementation by writing return x * function(x); in other words, write your intended function with the return statement and apply the other two rules
