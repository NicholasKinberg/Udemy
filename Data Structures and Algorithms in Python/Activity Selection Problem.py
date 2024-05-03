# Divide and conquer algorithms are about solving sub-problems of the major problem to yield solution to major problem
# Problem statement: given N number of activities with their start and end times, need to select max number of activities that can be performed by single person, assuming that person can only work on single activity at a time

activities = [["A1", 0, 6],
             ["A2", 3, 4],
             ["A3", 1, 2],
             ["A4", 5, 8],
             ["A5", 5, 7],
             ["A6", 8, 9]]

def printMaxActivities(activities):
    activities.sort(key = lambda x: x[2]) # referencing the ending time for an activity
    i = 0 # index variable
    for j in range(len(activities)):
        if activities[i][1] > activities[i][2]:
            print(activities[j][0]) # prints activities where ending time is greater in first activity than second, thus identifying activities one can accomplish without conflict
            i = j

printMaxActivities(activities)