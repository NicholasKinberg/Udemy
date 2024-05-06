
############################################################
def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 
############################################################
def score(dice):
    # dice scores  [1   ,   2,   3,   4, 5,   6]
    scores_3same = [1000, 200, 300, 400, 500, 600]
    scores_single = [100 ,   0,   0,   0,  50,   0]
    
    sum = 0
    for i in range(1,7):
        count_i = dice.count(i)
        sum += (count_i // 3) * scores_3same[i-1] + (count_i % 3) * scores_single[i-1]
            
    return sum
############################################################
from collections import Counter as count

def score(dice):
    threes, ones, c = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}, {1: 100, 5: 50}, count(dice)
    return sum((c[v]//3)*threes[v] + (c[v]%3)*ones.get(v, 0) for v in c)
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
############################################################
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