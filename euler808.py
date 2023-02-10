# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=808
"""
It seems all reversible prime squares are squares of a prime p
- whose digits are in {0,1,2,3}
- whose reverse is also prime

10a+b = 100a² + 10ab + b²

"""


from pe_utils import *

def small_digits(n):
    while n:
        if n%10 >3:
            return False
        n //= 10
    return True

rev_primes = []

es = ErathostenesSieve(40_000_000)
for p1 in es.primes:
    #""" Condition 1
    n = p1**2
    m = rev_int_digits(n)
    p2 = math.isqrt(m)
    if p2 < p1 and es.is_prime(p2) and p2**2 == m:
        rev_primes.append(p1)
        rev_primes.append(p2)
    #"""
    """ Condition 2
    if small_digits(p1):
        p2 = rev_int_digits(p1)
        if p2 > p1 and rev_int_digits(p1**2) == p2**2 :
            rev_primes.append(p1)
            rev_primes.append(p2)
    #"""

rev_primes.sort()
print("Solution:",sum([ p**2 for p in rev_primes[:50] ]) )

