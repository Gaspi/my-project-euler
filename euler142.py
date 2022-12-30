# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=142
"""

x-y and x+y squares means

x-y = a²>0
x+y = a² + 2y = (a+b)²

=>  2ab + b² = 2y
so b=2c>0 and

y = 2ac+2c²
x = a²+2ac+2c²




"""

for a in range(1,10):
    for c in range(1,10):
        x = a*a + 2*a*c + 2*c*c
        y = 2*a*c+2*c*c
        print(x,y,x-y,x+y)

