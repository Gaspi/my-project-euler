# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=134
"""

"""

from pe_utils import *

N = 1_000_003
primes = erathostenes_sieve(N)

somme = 0

p1 = None
p2 = primes[2]
for i in range(3, len(primes)):
    p1 = p2
    p2 = primes[i]
    base = 10 ** (1+int(math.log10(p1)))
    # we look for n such that  p2 | (n*base + p1)
    # i.e.   base * n = -p1 mod p2
    u,_,_ = extended_euclid(base, p2)
    # p2 is prime therefore gcd(base,p2)=1 and N/p2N is a field
    # u is such that u*base == 1 mod p2
    # is such that (u*-p1)*base == -p1 mod p2
    S = base * (  ( u * (-p1) ) % p2 ) + p1
    somme += S
    # print(p1,p2,S)


print("Resultat :", somme)