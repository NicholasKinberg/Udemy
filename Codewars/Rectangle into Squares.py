# You will be given two dimensions

# a positive integer length
# a positive integer width
# You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

def sqInRect(lng, wdth):
    if lng == wdth: # if length equals width, the object is a square, so return None
        return None
    if lng < wdth:
        wdth, lng = lng, wdth # if length is less than width, switch the values of length and width (which will not change area of rectangle)
    res = [] # initializing list in which we will store squares summing to area of rectangle
    while lng != wdth: # while length does not equal width...
        res.append(wdth) # append the width...
        lng = lng - wdth # ...and set length equal to length minus width
        if lng < wdth: # and if length is less than width...
            wdth, lng = lng, wdth # ...switch the values again
    res.append(wdth) # this feels like an intricate mathematical theorem
    return res

def sqInRect(a, b):
    if a == b: # if a equals b, it's a square, return None
        return None
    
    res = [] # initialize square list
    
    while b: # initialize while loop
        b, a = sorted([a, b])
        res += [b]
        a, b = b, a-b # mathematical theorem to return squares
    
    return res

# Recursive solution
def sqInRect(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]            # If this is original function call, return None for equal sides (per kata requirement);
                                               # if this is recursion call, we reached the smallest square, so get out of recursion.
    lesser = min(lng, wdth)
    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1) # another form of the theorem from the other solutions
                                                                    # notice that lesser is assigned to length in sqInRect, then takes absolute value of difference between length and width

def sqInRect(lng, wdth):
    if lng==wdth:
        return None
    a=[]
    while lng>0 and wdth>0:
        if lng>=wdth:
            a.append(wdth)
            lng-=wdth
        elif lng<wdth:
            a.append(lng)
            wdth-=lng
    return a