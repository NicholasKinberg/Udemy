# Greed is a dice game played with five six-sided dice. 
# Your mission, should you choose to accept it, is to score a throw according to these rules. 
# You will always be given an array with five six-sided dice values.
# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point
# A single die can only be counted once in each roll. 
# For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
# 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
# 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
# 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
############################################################
def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0] # initializing counter, points, and extra arrays that will each synchronize on the same index position
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1 # adding one for each time a number appears, so if 5 appears three times, the index position for 5 will be 3
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) # referring to points array adding to sum if any of the numbers appears three or more times, else 0
    + extra[i] * (count%3) # then adding the extra for each i, multiplying i (the number of times a number appears) by the remainder of count divided by 3, accounting for the appearance count of any numbers beyond the usual three

  return sum # then return sum
############################################################
def score(dice):
    # dice scores  [1   ,   2,   3,   4, 5,   6]
    scores_3same = [1000, 200, 300, 400, 500, 600]
    scores_single = [100 ,   0,   0,   0,  50,   0]
    
    sum = 0
    for i in range(1,7): # remember that range(1,7) goes from 1 through 6 but never reaches 7
        count_i = dice.count(i) # initialize counting variable to count the number of times each number appears
        sum += (count_i // 3) * scores_3same[i-1] + (count_i % 3) * scores_single[i-1] # obtain quotient divided by 3 without remainder by using the // method, then multiply those quotients by the three-scores, then obtain remainder divided by 3 using the % method and multiply those numbers by the scores_single array
            
    return sum # then return sum
############################################################
from collections import Counter as count

def score(dice):
    threes, ones, c = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}, {1: 100, 5: 50}, count(dice) # dictionary method where we implement a dictionary for threes and a dictionary for ones and a counter for each die roll
    return sum((c[v]//3)*threes[v] + (c[v]%3)*ones.get(v, 0) for v in c) # again a division by 3 without remainder by using the // method, then multiplied by the threes dictionary, then the same for the ones dictionary (but we use the get() command to return 0 for those that return 0)
############################################################
SCORES = [
  # triples
  ["111", 1000],
  ["666", 600],
  ["555", 500],
  ["444", 400],
  ["333", 300],
  ["222", 200],
  # singles
  ["1", 100],
  ["1", 100],
  ["5", 50],
  ["5", 50] ]

def score(dice):
    dice = "".join(str(d) for d in sorted(dice))
    total = 0
    
    for key, val in SCORES:
        if key in dice:
            total += val
            dice = dice.replace(key, "", 1)
    
    return total
############################################################
score=lambda d:100*(sum(i+9*(i==1)for i in range(7)if d.count(i)>2)+d.count(1)%3+d.count(5)%3/2)