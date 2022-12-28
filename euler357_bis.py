# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=357
"""
n+1 is prime therefore either n=1 or n is even : n=2m with 2m+1 and m+2 prime
n=1, 2, 6, 10, 22, etc.
"""

import math
from pe_utils import erathostenes_sieve, all_prime_divisors

N = 100_000_000
#N=100

primes, sieve = erathostenes_sieve( N )
print(len(primes)) # 5761455

# Fast primality check for p > 2
def isprime(p):
    return  p & 1 and sieve[ (p-1)//2 ]


def brute_force_check(n):
    # Note : we don't recheck 1 (n+1) and 2 (n/2+2)
    for d in range(3, math.isqrt(n)+1):
        if n % d == 0:
            if not isprime( d + (n//d) ):
                return False
    return True


print(1, "  ", all_prime_divisors(1))
somme = 1  # 1 and 2
# Find all n such that n=2m with 2m+1 and m+2 prime
for m in range(1, N//2, 2):
    if isprime(m+2) and isprime(2*m+1): # 458461 cases
        n=2*m
        if brute_force_check(n):
            somme += n
            if True or n < 1_000:
                print(n, "  ", all_prime_divisors(n))

print("Result:",somme)

