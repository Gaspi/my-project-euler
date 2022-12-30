# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=130
"""



"""

import math


N = 1_000_000

# sieve[i] = True if 2i+1 is prime
sieve = [True for i in range(N // 2)]

sieve[0] = False

for i in range(1, math.isqrt(N)//2 ):
    if sieve[i]:
        p = 2*i+1
        for k in range(p, N // p + 1, 2):
            sieve[ (k*p) // 2 ] = False

def isprime(p):
    return p == 2 or (p&1 and sieve[p//2])

primes =  [2] + [ 2*i+1 for i in range(N // 2) if sieve[i] ]

print( len(primes) )

def divisors(n):
    acc = []
    for p in primes:
        if p > math.isqrt(n):
            acc.append(n)
            return acc
        while n % p == 0:
            acc.append(p)
            n //= p
            if n == 1:
                return acc

memA = {}
def A(n):
    if n in memA:
        return memA[n]
    u = 1
    k = 1
    while u:
        u = (10*u+1) % n
        k += 1
    memA[n] = k
    return k


def fast_check(n):
    if isprime(n):
        return False
    for d in set(divisors(n)):
        if d < 7:
            return False
        if (n-1) % A(d) > 0:
            return False
    return True

def check(n):
    return (n-1) % A(n) == 0

acc = []
n = 1
while len(acc) < 25:
    n += 2
    if fast_check(n) and check(n):
        acc.append(n)

print(acc)
print(len(acc))
print(sum(acc))



