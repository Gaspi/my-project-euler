# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=132
"""

111...11 (1e9 occurences of 1, length 1_000_000_000)
=
11 *  1010...101 (499999999 periods of 2 + final 1, length 999_999_999)
=
11 * 101 * 10001000...10001 (length 999_999_997, 249999999 periods of 4 + final 1)
=
11 * 101 * 10001 * 10000000_1000...10001 (length 999_999_993, 124999999 periods of 8 + final 1)
=
11 * 101 * 10001 * 100000001 * ... (length 999_999_993, 124999999 periods of 8 + final 1)


the product for i = 0 to n of 10^(2^i)+1  (100000...1)
is 11111 (repeated 2^(n+1) times)

eg : 
n=0    10^(2^0)+1 =                           11 = 11
n=1    10^(2^1)+1 =                     101 * 11 = 1111
n=2    10^(2^2)+1 =             10001 * 101 * 11 = 11111111
n=3    10^(2^3)+1 = 100000001 * 10001 * 101 * 11 = 1111111111111111

10^9 = 2^9 * 5^9
therefore :

the product for i = 0 to 8 is 1 repeated 2^9 times
which divides 1 repeated 10^9 times



2nd approach 
given a prime p, we need to study the cycle of the series
  u(0)   := 1
  u(n+1) := 10 *u(n)+1
in the field N/pN
if u(i) = u(i+k) then p divides 1111...1 if k | (10^9 - i)

exemples :
- mod 11 :
    u(0)=1
    u(1)=0
    u(2)=1   > i = 0, k = 2  and 2 | 10^9-0
- mod 101 :
    u(0)=1
    u(1)=11
    u(2)=10
    u(3)=0
    u(4)=1  > i = 0, k = 4 and 4 | 10^9-0

10n+1 = 10k+1 mod p   ==> 10(n-k) = 0 mod p ==> n=k  (or p=2 or p=5)
therefore i = 0

"""



import math
from pe_utils import *

N = 10**9
nbsols = 40

#N = 10
#nbsols = 4

def check(p):
    u = 1
    n = 1
    while u != 0:
        u = (10*u+1) % p
        n+=1
    #print(p,n)
    return N % n == 0

primes, _ = erathostenes_sieve(250_000)

sol = []

for p in primes[3:]:
    if check(p):
        sol.append(p)
        print(len(sol),"/",nbsols," --> ",p)
        if len(sol) == nbsols:
            break
        
print(len(sol), sol)
print("Result:", sum(sol))



