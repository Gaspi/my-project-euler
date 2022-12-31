# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=129

n = 1_000_001
while True:
    k = 1
    rk = 1
    while rk != 0:
        rk = (10*rk + 1) % n
        k += 1
    if k > 1_000_000:
        print("A(",n,") =",k)
        break
    n += 4 if n%5 == 3 else 2

