# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
dict1 = dict()
dict2 = {}
# print(dict1)
# print(dict2)

dict3 = dict(a='b', c='d', e='f')
# print(dict3)

dict4 = {'name': 'Nicholas', 'age': 26}
dict4['age'] = 27
# print(dict4)
dict4['address'] = 'Arlington'
# print(dict4)
# the above code has time complexity O(1), space complexity O(1)

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

# print(traverseDict(dict=dict4))

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'key does not exist'

# print(searchDict(dict4, value='Abhishek'))

def count_word_frequency(words):
    count = {}
    for word in words:
        # get() command arguments: (1) i in list, (2) starting value (which is 0 in this case)
        count[word] = count.get(word, 0) + 1
    return count

# print(count_word_frequency(words=['sdf','sdf','ghrew','awef','awef']))

def merge_dicts(dict1, dict2):
    # create a copy of dict1
    dict3 = dict1.copy()
    # loop over keys and values in dict2 items
    for key, value in dict2.items():
        # dict3 obtains key and value from dict2 items while already having copied dict1
        dict3[key] = dict3.get(key, 0) + value
    # return dict3 after having added dict1 to dict2
    return dict3

def filter_dict(my_dict, condition):
    # filters a dictionary by searching for specific key and value
    return {key: value for key, value in my_dict.items() if condition(key, value)}