def max_product(arr):
    # initialize two variables to store two largest numbers
    max1, max2 = 0, 0 # O(1), constant time initialization b/c of initialization equaling an int
    for num in arr:
        if num > max1:
            max2 = max1
            # if the current number is greater than max2 but not max1, update max2
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2

print(max_product(arr=[23,434,65,47346,56,2,64,5768,856,43,2]))