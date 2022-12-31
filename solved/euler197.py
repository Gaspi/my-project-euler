# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=197

"""
f(x) = floor( 2^(30.403243784-x2) ) × 10^(-9)

f(0) = 1 . 420 000 000


"""

import math

u = 1_000_000_000

def f(n):


while True:
    u = math.floor( 2 ** (30.403243784 - ( (u**2) * 1e-18)) )
    print(u)

# Eventually loops :
# 1029461839
# 681175878
# 1029461839
# 681175878
# 1029461839
# u_n + u_(n+1) = (681175878 + 1029461839) * 1e-9
# Solution : 1.710637717