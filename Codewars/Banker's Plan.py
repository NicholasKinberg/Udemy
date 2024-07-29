# John has some amount of money of which he wants to deposit a part f0 to the bank at the beginning of year 1. He wants to withdraw each year for his living an amount c0.

# Here is his banker plan:

# deposit f0 at beginning of year 1
# his bank account has an interest rate of p percent per year, constant over the years
# John can withdraw each year c0, taking it whenever he wants in the year; he must take account of an inflation of i percent per year in order to keep his quality of living. i is supposed to stay constant over the years.
# all amounts f0..fn-1, c0..cn-1 are truncated by the bank to their integral part
# Given f0, p, c0, i the banker guarantees that John will be able to go on that way until the nth year.

def fortune(f, p, c, n, i):
    for _ in range(n-1):
        f = int(f * (100 + p) / 100 - c)
        c = int(c * (100 + i) / 100)
        if f < 0:
            return False
    return True

def fortune(money, interest, withdraw, years, inflation):
    interest = 1 + (interest / 100)
    inflation = 1 + (inflation / 100)
    for _ in range(years - 1):
        money = int(money * interest - withdraw)
        if money < 0:
            return False
        withdraw *= inflation
    return True

def fortune(f0, p, c0, n, i):
    f = f0
    c = c0
    
    for year in range(n-1):
        f = int(f + f * (p/100)) - int(c)
        c = int(c + c * (i/100))
            
    return f >= 0

fortune=F=lambda f,p,c,n,i:F(f*(100+p)//100-c,p,c*(100+i)//100,n-1,i)if n>1 else f>=0

def fortune(f0, p, c0, n, i):  
    if n == 1:
        return f0 >= 0
    
    return fortune(int(f0 + p / 100 * f0 - c0), p, int(c0 + c0 * i / 100), n - 1, i)
    

fortune(10000.0, 0, 10000.0, 2, 0)