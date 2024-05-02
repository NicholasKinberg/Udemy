# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
import numpy as np
import array as arr

### function to collect number of temperatures, so terminal should ask "What is today's temperature?"...
### ...to which user will respond with a value between -50 and 150 (set that and throw ValueError if not)
### to raise value error, use raise ValueError('bla bla bla') under if condition

### more specifically, the function should ask "What is today's high temperature?"...
### ...to which user will respond with a value between -50 and 150 (set that and throw ValueError if not)
### function will calculate average high temperature and return it like 'Average = ' followed by value
### function will also count number of days where temperature exceeded average high temperature

# count = 0
# for i in myList:
#     if i > mean(myList):
#        count += 1

# or

# count = 0
# for i in myList:
#     if i > sum(myList) / len(myList):
#        count += 1



# myList = list()
# while (True):
#     inp = input('For today, what is the high temperature? ')
#     if inp == 'done': break
#     value = float(inp)
#     if value > 150:
#         raise ValueError('It could not possibly be that hot!')
#     if value < -50:
#         raise ValueError('It could not possibly be that cold!')
#     myList.append(value)
# average = sum(myList)/len(myList)
# count = 0
# for i in myList:
#     if i > average:
#        count += 1

# print('Average: ', average, '.', 'Number of day(s) above average:', count, '.')


######################## OR
numDays = int(input("How many day's temperature?"))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day " + str(i+1) + "'s high temperature:"))
    temp.append(nextDay)
    total += temp[i]

average = round(total/numDays, 2)
print("\nAverage = ", str(average))