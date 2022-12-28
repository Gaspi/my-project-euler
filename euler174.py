# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=174
"""

given a external side length r and an internal side length s < r,
for symetry reasons, r and s have the same parity and
the square takes r² - s² tiles

eg: 32 = 6² - 2² = 9² - 7²

We need to enumerate all pairs (a,b) such that
    a > b > 0
    a-b = 0 mod 2
    a²-b² <= N

The smallest number of tiles for a side a is : a²-(a-2)² = 4a-4
We must have   4a-4 <= N  (a <= N//4 + 1)

"""

import math

max_size = 1_000_000


# N(n) = N[n-1] for 1 <= n <= 10
N = [0 for i in range(max_size+1)]


for a in range( max_size//4+2,2,-1):
    a2 = a*a
    for b in range(a-2,0,-2):
        if a2 - b*b > max_size:
            break
        N[a2 - b*b] += 1
    if a % 1000 == 0:
        print(a)

print( sum([1 for i in range(1,max_size+1) if N[i] > 0 and N[i] <= 10 ]) )

