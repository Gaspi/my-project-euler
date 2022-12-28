# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=357
"""

if n = qk² then  qk + k  is prime avec k=1
hence n has no square divisor other than 1

n+1 is prime therefore either n=1 or n is even : n=2m with 2m+1 and m+2 prime
n=1, 2, 6, 10, 22, etc.

Mod  6 : if m = 1 mod 6 then 3 | 2m+1 therefore m = 3,5 mod 6
Mod 10 : m = 3,5,9,11 mod 6 with 

2 < n = 2*p1*...*pn with distincts pi

1) if n = 2p then p, p+2 and 2p+1 are prime
    if p = 1 mod 6 then 3 | 2p+1 therefore p = 5 mod 6
    if p = 3,7 mod 10 then 5 | p+2 therefore p = +- 1 mod 10
    therefore mod 30 : p = { 11, 29 }

2) if n = 2.p.p' then the smallest p is < sqrt(100_000_000 / 2)   (only 908 possible)

"""

import math
from pe_utils import *


# Brute force of smaller instances

somme = 0

def brute_force_check(n):
    global somme
    for d in range(1, math.isqrt(n)+1 ):
        if n % d == 0:
            if not isprime( d + (n//d) ):
                return False
    somme += n
    print(n, "  ", all_prime_divisors(n))
    return True

for k in range(1,10_000):
    brute_force_check(k)
print('------')

# Case 1 : n=2*p with p prime

for p in range(11, 100_000_000//2 + 1, 30):
    if isprime(p) and isprime(p+2) and isprime(2*p+1):
        somme += 2*p
print("---2---")
for p in range(29, 100_000_000//2 + 1, 30):
    if isprime(p) and isprime(p+2) and isprime(2*p+1):
        somme += 2*p


# Case 2: n = 2*p1*p2*...


print(somme)

