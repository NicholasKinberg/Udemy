list = ['a', 'b', 'c', 'd']
list.pop(1)
# print(list)
### first insert() argument is positional, second is value
list.insert(3, 234)
# print(list)
del list[0:2]
# print(list)

new_list = [231,4235,32465,34,6354,745,37,45673,4566,53421,532,543,476,84,563]
def is_target_in_list(new_list, target):
    if target in new_list:
        print(f'{target} is in list')
    else:
        print(f'{target} not in list')

# is_target_in_list(new_list, 45673)

### use i, value in enumerate(list) to iterate over list, to use built-in value function to set equal to int, and to return i (position of target)
def linear_search(new_list, target):
    for i, value in enumerate(new_list):
        if value == target:
            print(i)

# linear_search(new_list, 34)
# del list
# ### function to enter individual values and then take average of values added to data
# myList = list()
# while (True):
#     inp = input('enter a number, any number: ')
#     if inp == 'done': break
#     value = float(inp)
#     myList.append(value)
# average = sum(myList)/len(myList)

# print('Average: ', average)

# del list
## function to separate string value by delimiter
a = 'sdf-wer3-dsf-345-dsaf'
delimiter = '-'
b = a.split(delimiter)
# print(b)
# print(delimiter.join(b))
            
language = 'ewjkf;aldsgdlsj;ahgewfds'
newer_list = [letter for letter in language]
# print(newer_list)

# prev_list = [23,5346,654,274,43,534,26,468,5467,456423,451]
# newerer_list = [number*number for number in prev_list if number > 1000]
# print(newerer_list)

sentence = 'aksdl sdjk;aga;sga;lf ea;j fe;jawfae; jgaj;ge;ah fe;j anjskdf i;ewlawf sd;fh ;ae;owief'
def is_consonant(word):
    vowels = 'aeiou'
    return word.isalpha() and word.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)