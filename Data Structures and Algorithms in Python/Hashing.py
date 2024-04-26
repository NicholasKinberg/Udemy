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
# if I were to enter mod(400, 24), this would return 16, so we would use index 16 as key and 400 as hash value
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
# 1. direct chaining
# 2. open addressing
    # 2.1. linear probing
    # 2.2. quadratic probing
    # 2.3. double hasing

# direct chaining: implement buckets as linked list
    # implement linked list for single index position, linking keys that have same value

# open addressing: colliding elements are stored in other vacant buckets; for storage and lookup, we use "probing"
    # linear probing: places new key into closest following empty cell; so A goes to index[2], B goes to index[3] instead of index[2], and so on
    # quadratic probing: adding arbitrary quadratic polynomial to index until empty cell is found (adding squares of integers to index positions to obtain other index positions)
    # double hashing: interval between probes is computed by another hash function, so more than one hash function

# hash table can be full when size is preset, but this won't happen if one uses direct chaining (linked lists to link keys with same indices together)
# if hash table is full, can use open addressing to double the size of the hash table and recall hashing for current keys