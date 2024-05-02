# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# The Trie data structure is a tree-like data structure used for storing a dynamic set of strings. 
# It is commonly used for efficient retrieval and storage of keys in a large dataset. 
# The structure supports operations such as insertion, search, and deletion of keys, making it a valuable tool in fields like computer science and information retrieval. 
# In this article we are going to explore insertion and search operation in Trie Data Structure.

# trie structures info in hierarchy
# stores and searches strings in a space and time efficient way
# any node in trie can store non-repetitive multiple characters
# every node stores link of next character in string
# every node keeps track of "end of string"
# can use for spell-check, auto-complete

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
# insert string in trie
# each node is its own dict
# case 1: trie is blank
# case 2: new string's prefix is common to another string's prefix
# case 3: new string's prefix is already present as complete string
# case 4: string to be inserted is already present in trie

    def insertString(self, word):
        current = self.root # assign current to beginning of trie
        for i in word:
            ch = i
            node = current.children.get(ch) # get() method returns value of item with specified key
            if node == None: # if node you want to insert doesn't yet exist (case 1):
                node = TrieNode() # create new node with class TrieNode
                current.children.update({ch:node}) # children will be updated with character key and corresponding node value
            current = node # assign current to newly created node
        current.endOfString = True # state that this is the end of the string (trie) with the addition of the new node
        print("Success!")

# search for a string in a trie
# case 1: string does not exist in trie
# case 2: string does exist in trie
# case 3: string is prefix of another string but it does not exist in trie

    def searchString(self, word):
        currentNode = self.root # currentNode starts at beginning of trie
        for i in word: # iterating over string
            node = currentNode.children.get(i) # node iterates through each letter of word for which we are searching
            if node == None:
                return False # return False because if word entered does not exist in trie (case 1), have to return False
            currentNode = node # if node is not None (case 2), currentNode is assigned to each letter of word
        if currentNode.endOfString == True: # once currentNode reaches endOfString, endOfString is True, program returns True to indicate that word exists in trie
            return True
        else:
            return False

# deletion of a string from a trie
# case 1: some other prefix of string is same as one that we want to delete; ex.: (API, APPLE)
# case 2: string is prefix of another string; ex.: (API, APIS)
# case 3: other string is prefix of this string; ex.: (APIS, API)
# case 4: not any node depends on given string

def deleteString(root, word, index):
    ch = word[index] # variable ch is assigned to given index of given word as word is a string and string is iterable
    currentNode = root.children.get(ch) # currentNode assigned to given child of trie at position ch (ch is a key)
    canThisNodeBeDeleted = False # initialize canThisNodeBeDeleted as False for recursion later on
    # note that the following 3 lines deal with case 1: some other prefix of string is same as one that we want to delete (API, APPLE)
    if len(currentNode.children) > 1: # can only use recursion outside classes? anyway, if length of word is greater than 1...
        deleteString(currentNode, word, index+1) #...use recursion to delete string at index + 1
        return False
    # note that following 4 lines deal with case 2: string is prefix of another string (API, APIS)
    if index == len(word) - 1: # but if index == length of word - 1:
        if len(currentNode.children) >= 1: # and if lenght of currentNode.children is greater than or equal to 1:
            currentNode.endOfString = False # we have not yet reached endOfString, return False
            return False # returning False stops you from deleting node that could break entire trie
        # the next 3 lines can be used for case 4
        else:
            root.children.pop(ch) # otherwise we pop the given character out at given index and return True
            return True # we can pop the given character here because it doesn't extend to another part of trie, is not a prefix of another word (case 4)
    if currentNode.endOfString == True: # if endOfString is True, as in we have reached end of string:
        deleteString(currentNode, word, index+1) # use recursion to delete node at index+1, case 3, the given string is a suffix of another string
        return False
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True: # canThisNodeBeDeleted is initialized as False, so it can become True at some point and pop root.children
        root.children.pop(ch) # canThisNodeBeDeleted will equal True when the node in question has no dependencies, i.e. it is a suffix
        return True
    else:
        return False