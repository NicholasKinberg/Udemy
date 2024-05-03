# Problem statement: implement a Fibonacci sequence
def Fibonacci(n):
    if n < 1:
        return ValueError
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(10))
# this is an example of a divide and conquer algorithm, because we are isolating a locally optimal solution and then applying recursion to produce the program
# note that in this sequence, since each number of the sequence is the sum of the two preceding numbers, the program needs recursion
# so when I declare that n = 10, the program is going through iterations all the way down to below 1, at which point the program terminates because of ValueError