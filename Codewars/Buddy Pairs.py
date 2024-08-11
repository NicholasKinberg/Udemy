# Buddy pairs
# You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. In the following description, divisors will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

# Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:

# (n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

# For example 48 & 75 is such a pair:

# Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
# Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
# Task
# Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n

# If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil or (for Dart) null; (for Lua, Pascal, Perl, D) [-1, -1]; (for Erlang {-1, -1}).
def div_sum(n):
    divs = set()
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return sum(divs)

def buddy(start, limit):
    for n in range(start, limit+1):
        buddy = div_sum(n)
        
        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]
    
    return "Nothing"

####################################################

def buddy(start, limit):
    for n in range(start, limit + 1):
        m = s(n)
        if m > n and n == s(m):
            return [n, m]
            
    return "Nothing"
    
def s(n):
    s = 0
    for i in range(2, round(n ** 0.5)):
        if n % i == 0:
            s += i
            s += n // i
    return s

####################################################

import itertools as it
from math import sqrt, ceil
from functools import reduce, lru_cache
from operator import mul
from collections import Counter

class Primes:
    def __init__ (self):
        self.cache = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    def _weak_test (self, n):
        return all(n % div for div in self.cache)
    def find_next (self):
        for candidate in it.count(self.cache[-1] + 1):
            if self._weak_test(candidate):
                return candidate
    def __iter__ (self):
        yield from self.cache
        while True:
            p = self.find_next()
            self.cache.append(p)
            yield p
    def factorize (self, n):
        factors = []
        candidates = iter(self)
        div = next(candidates)
        while n > 1:
            if div**2 > n:
                factors.append(n)
                break
            quot, rem = divmod(n, div)
            if not rem:
                factors.append(div)
                n = quot
            else:
                div = next(candidates)
        return factors

PRIMES = Primes()

def product (factors, counts):
    factors = (num ** exp for num, exp in zip(factors, counts))
    return reduce(mul, factors, 1)

def divisors (n):
    factors = Counter(PRIMES.factorize(n))
    ranges = (range(k+1) for k in factors.values())
    selections = it.product(*ranges)
    counted_factors = zip(it.repeat(tuple(factors)), selections)
    return [product(*pair) for pair in counted_factors]

def proper_divisors (n):
    divs = divisors(n)
    divs.pop()
    return divs

@lru_cache(None)
def potential_buddy (n):
    return sum(proper_divisors(n)) - 1

def buddy (start, limit):
    for n in range(start, limit+1):
        m = potential_buddy(n)
        if potential_buddy(m) == n and m > n:
            return [n, m]
    return 'Nothing'
