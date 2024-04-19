### Write a program to find all pairs of integers whose sum equals given number
# def pairs_equal_number(list, n):
#     #new_list = []
#     for i in range(len(list)):
#         for j in range(len(list)):
#             if i + j == n:
#                 print(i, j)
#     ### nested for loop, for i in list, for j in list, if i + j == n, store (i,j) in new_list
#     ### new_list should contain pairs of integers whose sum equals given number
#     #print(new_list)

# list = [1,2,3,4,5,6,7,8,9]
# pairs_equal_number(list, 10)

################################ ADVANCED SOLUTION
##### This solution is better because it uses O(1) time instead of O(n^2)
##### This solution also returns the index positions of the numbers equaling target instead of numbers themselves
def two_sum(nums, target):
    # {} creates empty dictionary seen to store numbers and their indices
    seen = {}
    # use enumerate() command to iterate over values and their indices, index is i and value is num
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            # the below line of code calls the complement and its index number, the difference between target and num
            return [seen[complement], i]
        seen[num] = i

nums = (2,7,11,15)
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")