# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=173
"""

given a external side length r and an internal side length s < r,
for symetry reasons, r and s have the same parity and
the square takes r² - s² tiles

eg: 32 = 6² - 2² = 9² - 7²

We need to count all pairs (a,b) such that
    a > b > 0
    a-b = 0 mod 2
    a²-b² <= N

The smallest number of tiles for a side a is : a²-(a-2)² = 4a-4
We must have   4a-4 <= N  (a <= N//4 + 1)

For all such possible a, we count all k > 0 such that
    b = a-2k > 0   (k <= (a-1)//2)
    b² >= a² - N
    b² > a² - N - 1
    b > sqrt(a² - N - 1)
    a - 2k > sqrt(a² - N - 1)
    2k < a - sqrt(a² - N - 1)
    2k <= a - sqrt(a² - N - 1) - 1
    k <= (a - sqrt(a² - N - 1) - 1) // 2

"""

import math

N = 1_000_000

somme = 0
for a in range(3,N//4+2):
    tmp = a*a-N-1
    tmp2 = 0 if tmp < 1 else math.isqrt(tmp)
    upper_bound = (a - tmp2 - 1) // 2
    if N < 1_000:
        for k in range(1,upper_bound+1):
            b = a - 2*k
            print(a,b,a*a-b*b)
    somme += upper_bound

print(somme)
