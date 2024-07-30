# You will be given two dimensions

# a positive integer length
# a positive integer width
# You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res

def sqInRect(a, b):
    if a == b:
        return None
    
    res = []
    
    while b:
        b, a = sorted([a, b])
        res += [b]
        a, b = b, a-b
    
    return res

# Recursive solution
def sqInRect(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]            # If this is original function call, return None for equal sides (per kata requirement);
                                               # if this is recursion call, we reached the smallest square, so get out of recursion.
    lesser = min(lng, wdth)
    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)

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