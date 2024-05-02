# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# functions to take a list of int, reverse that list, and ask whether the original equals the reverse
# one function to do all of this, function should take list of int
def palindrome(n):
    # where n is list of int
    reverse_n = []
    for i in reversed(n):
        reverse_n.append(i)
    if n == reverse_n:
        print("This list is a palindrome.")
    else:
        print("This list is not a palindrome.")

# palindrome(n=[1,2125,43,625,73658467596,5432,1456,7896,543,2145])
# palindrome(n=[1,2,3,3,2,1])
# OR

def palindromeDifferent(n):
    for i in n:
        for j in reversed(n):
            if i == j:
                print("This list is a palindrome.")
            else:
                print("This list is not a palindrome.")
                # problem is it is better to aggregate as set so that program prints once instead of several times

palindromeDifferent(n=[1,2,3,3,2,1])