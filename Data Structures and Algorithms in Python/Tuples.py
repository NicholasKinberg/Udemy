# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
tuple1 = 'a', 'b', 'c', 'd', 'e'
# print(tuple1)
tuple2 = tuple('abcde')
# print(tuple2)
# tuple is immutable list
# if you insert negative number in [], Python prints indices backwards
# the below code will print 'd'
# print(tuple2[-2])
# for i in range(len(tuple2)):
#     print(tuple2[i])

def searchTuple(tuple, element):
    for i in range(0, len(tuple)):
        if tuple[i] == element:
            # when adding specific keys and values to return function, remember to add f'{} bla bla' so that it works
            return f'{element} is found at {i} index'
    return 'element not found'

# print(searchTuple(tuple2, element='d'))

def sum_product(tuple):
    tuple = list(tuple)
    sum_result = 0
    product_result = 1
    for i in tuple:
        sum_result += i
        product_result *= i
    return sum_result, product_result

# the below code block uses a lambda function (anonymous expression)
# can set lambda function equal to string, like g = lambda x: 3*x + 1
def tuple_elementwise_sum(tuple1, tuple2):
    res = tuple(map(lambda i, j: i + j, tuple1, tuple2))
    return res

def get_diagonal(tup):
    return tuple(tup[i][i] for i in range(len(tup)))

# the below code doesn't work b/c tuple2 isn't a 2D matrix
# print(get_diagonal(tuple2))