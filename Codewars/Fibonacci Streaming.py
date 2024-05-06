# You're going to provide a needy programmer a utility method that generates an infinite amount of sequential fibonacci numbers.
# To do this write a 'generator' starting with 1
# Note that a generator has no need for an argument, so code will look like all_fibonacci_numbers() because the method just generates the same numbers no matter what
# A fibonacci sequence starts with two 1s. Every element afterwards is the sum of the two previous elements. See:
# 1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...
def all_fibonacci_numbers():
    a, b = 1, 1
    while 1:
        yield a # use yield command that acts as generator rather than simple return command
        a, b = b, a + b
    return a, b
############################################################
def all_fibonacci_numbers():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b