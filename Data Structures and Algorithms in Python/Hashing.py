# hashing is method of sorting and indexing data
# idea is to allow large amounts of data to be indexed using keys commonly created by formulas
# use hashing because it is time efficient for searching (O(1) or O(n))
# array or Python list has search time O(logN) because array or Python list can narrow down to specific set to optimize search
# linked list has search time O(n) because it loops through all items until it finds searched item
# tree has search time O(logN) because tree can narrow down to subtree in which to find searched item

# hash function: function used to map of arbitrary size to data of fixed size
# key: input data by user
# hash value: value returned by hash function
# hash table: data structure which implements associative array abstract data type, structure that can map keys to values
# collision: collision occurs when 2 different keys to hash function produce same output

# mod function
def mod(number, cellNumber): # cellNumber will represent total number of cells for the purposes of this file
    return number % cellNumber # % operator returns remainder
# if I were to enter mod(400, 24), this would return 16, so we would use 16 as key and 400 as hash value
# mod(400, 24)

# ASCII function
def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i) # returns unicode code point for one-character string
    return total % cellNumber # in this case, hash value is total unicode code point while key is output of this function (remainder of total/cellNumber)
# modASCII("ABC", 24)
# in ASCII conversion, A = 65, B = 66, C = 67, so summed up they equal 198, and 198 % 24 = 6, so index[6] = "ABC"

# properties of good hash function:
    # it distributes hash values uniformly across hash tables
    # it has to use all input data
    # it avoids collisions (where 2 different keys to hash function produce same output)

# collision resolution techniques