# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=131
"""


n²(n+p) = k^3

Supposons
n=m^3
k=q.m^2

m^3 + p = q^3


We look for all primes that are differences of cubes

(m+1)^3 - m^3 = 3m²+3m+1 > 3m²




Soit n = u*v  et k = u*w
tel que n^3 + n^2*p = k^3


u^3 v^3 + u^2 v^2 p = u^3 w^3

v^2 (uv+p) = u w^3


n^3 + p n^2 = (n+k)^3 
n^3 + p n^2 = n^3 + 3*k*n^2 + 3 * k^2 * n + k^3

p n^2 = 3*k*n^2 + 3 * k^2 * n + k^3

donc k | n,   n = k*u

p n^2 = 3*k*n^2 + 3 * k^2 * n + k^3

p n^2 = 3*k*n^2 + 3 * k^2 * n + k^3


"""

from pe_utils import erathostenes_sieve, perfect_cube
N = 1_000_000
#N = 100

primes,_ = erathostenes_sieve(N)
print(len(primes))

def check(p):
    for n in range(2,p):
        m = perfect_cube( (n**3) - p )
        if m is not None:
            print("Found:",p,n,m)
            return True
        if 3*n*n+3*n+1 > p:
            return False

cnt = 0
for p in primes:
    if check(p):
        cnt += 1
print("Result:",cnt)






