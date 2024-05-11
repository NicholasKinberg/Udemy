# Problem statement: From wikipedia https://en.wikipedia.org/wiki/Partition_(number_theory)
# In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition.
# For example, 4 can be partitioned in five distinct ways:
# 4, 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 1 + 1 + 1.
# We can write:
# enum(4) -> [[4],[3,1],[2,2],[2,1,1],[1,1,1,1]] and
# enum(5) -> [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]].
# The number of parts in a partition grows very fast. For n = 50 number of parts is 204226, for 80 it is 15,796,476 It would be too long to tests answers with arrays of such size. So our task is the following:
# 1 - n being given (n integer, 1 <= n <= 50) calculate enum(n) ie the partition of n. We will obtain something like that:
# enum(n) -> [[n],[n-1,1],[n-2,2],...,[1,1,...,1]] (order of array and sub-arrays doesn't matter). This part is not tested.
# 2 - For each sub-array of enum(n) calculate its product. If n = 5 we'll obtain after removing duplicates and sorting:
# prod(5) -> [1,2,3,4,5,6]
# prod(8) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18]
# If n = 40 prod(n) has a length of 2699 hence the tests will not verify such arrays. Instead our task number 3 is:
# 3 - return the range, the average and the median of prod(n) in the following form (example for n = 5):
# "Range: 5 Average: 3.50 Median: 3.50"
# Range is an integer, Average and Median are float numbers rounded to two decimal places (".2f" in some languages).
# Notes:
# Range : difference between the highest and lowest values.
# Mean or Average : To calculate mean, add together all of the numbers in a set and then divide the sum by the total count of numbers.
# Median : The median is the number separating the higher half of a data sample from the lower half. (https://en.wikipedia.org/wiki/Median)
# Hints:
# Try to optimize your program to avoid timing out.
# Memoization can be helpful but it is not mandatory for being successful.

#################################################
# A utility function to print an
# array p[] of size 'n'
# def printArray(p, n):
# 	for i in range(0, n):
# 		print(p[i], end = " ")
# 	print()

# def printAllUniqueParts(n):
# 	p = [0] * n	 # An array to store a partition
# 	k = 0		 # Index of last element in a partition
# 	p[k] = n	 # Initialize first partition
# 				# as number itself

# 	# This loop first prints current partition, 
# 	# then generates next partition.The loop 
# 	# stops when the current partition has all 1s
# 	while True:
		
# 			# print current partition
# 			printArray(p, k + 1)

# 			# Generate next partition

# 			# Find the rightmost non-one value in p[]. 
# 			# Also, update the rem_val so that we know
# 			# how much value can be accommodated
# 			rem_val = 0
# 			while k >= 0 and p[k] == 1:
# 				rem_val += p[k]
# 				k -= 1

# 			# if k < 0, all the values are 1 so 
# 			# there are no more partitions
# 			if k < 0:
# 				print()
# 				return

# 			# Decrease the p[k] found above 
# 			# and adjust the rem_val
# 			p[k] -= 1
# 			rem_val += 1

# 			# If rem_val is more, then the sorted 
# 			# order is violated. Divide rem_val in 
# 			# different values of size p[k] and copy 
# 			# these values at different positions after p[k]
# 			while rem_val > p[k]:
# 				p[k + 1] = p[k]
# 				rem_val = rem_val - p[k]
# 				k += 1

# 			# Copy rem_val to next position 
# 			# and increment position
# 			p[k + 1] = rem_val
# 			k += 1

# # Driver Code
# print('All Unique Partitions of 2')
# printAllUniqueParts(2)

# print('All Unique Partitions of 3')
# printAllUniqueParts(3)

# print('All Unique Partitions of 4')
# printAllUniqueParts(4)

# print('All Unique Partitions of 10')
# printAllUniqueParts(10)

# This code is contributed 
# by JoshuaWorthington
#################################################
import statistics as stats
import numpy as np
def part(n):
    if n == 0:
        result = [[]]
	# if n in memo:
	# 	result[n] = memo[n]
    else:
        result = []
        for i in range(1, n + 1):
            for parts in part(n - i):
                result.append([i] + parts)
				# memo = result
    return result

def flattenHeterogeneous(result):
	flattened_array = []
	for element in result:
		if isinstance(element, list):
			flattened_array.extend(flattenHeterogeneous(element))
		else:
			result.append(element)
	return result

def summaryStatistics(result):
	result = np.array(result)
	result = result.flatten()
	maxResult = max(result)
	minResult = min(result)
	rangeOfResult = maxResult - minResult
	averageResult = stats.mean(result)
	medianResult = stats.median(result)
	return "Range: " + str(rangeOfResult) + " Average: " + str(averageResult) + " Median: " + str(medianResult)
  

result = part(5)
print(flattenHeterogeneous(result))
print(summaryStatistics(result))
#################################################
# def P(n):
#     # base case of recursion: zero is the sum of the empty list
#     if n == 0:
#         yield []
#         return

#     for p in P(n-1):        
#         p.append(1)
#         yield p
#         p.pop()
#         if p and (len(p) < 2 or p[-2] > p[-1]):
#             p[-1] += 1
#             yield p
# print(P(6))
#################################################