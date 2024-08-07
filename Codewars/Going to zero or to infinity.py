# Which will win: 1 / n! or (1! + 2! + 3! + ... + n!)?

# Are these numbers going to 0 because of 1/n! or to infinity due to the sum of factorials or to another number?

def going(n):  
    s = 1.0
    for i in range(2, n + 1):
        s = s/i + 1
    return int(s * 1e6) / 1e6

def going(n):
    factor = 1.0
    acc = 1.0
    for i in range(n, 1, -1):
        factor *= 1.0 / i
        acc += factor
    return int(acc * 1e6) / 1e6

def going(n):
    a = 1.
    for i in range(2, n+1):
        a/=i
        a+=1
    return float(str(a)[:8])

def going(n):
    p=1
    s=0
    for i in range(1,n+1):
        p*=i
        s+=p
    return s/p