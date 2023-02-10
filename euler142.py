# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=142
"""

x-y and x+y squares means

x-y = a²>0
x+y = a² + 2y = (a+u)²

=>  2au + u² = 2y
so u=2b>0 and

y = 2ab+2b²=2(a+b)b
x = a²+2ab+2b² = a²+y
with a,b > 0

Note : the lower of the two, y, must be even (and so must z).




We look for the smallest x
We compute the (x,y) pairs and memoize them
When a new candidate (x,y) is found, we look into the memoized pairs to see if
there is an other (x,z) already encountered
for each such choices, we check wether (y,z) is also a memoized pair



We also have 

z = 2(c+d)d
x = c²+z

z = 2(e+f)f
y = e²+z

e is even and therefore

z = 2(2e+f)f     = 2(c+d)d
y = 2(a+b)b      = 4e² + 2(2e+f)f  =  4e²+z
x = c² + 2(c+d)d = a² + 2(a+b)b
x = c²+z = a²+y

x = c(c+2d)+2d² = a(a+2b)+2b²


z = 2(2e+f)f     = 2(c+d)d
for e,f,c,d such that c>e>0, d>f>0 and

(c²+z) - (e²+z) = c²-e²     is square
(c²+z) + (e²+z) = c²+e²+2z  is square



We could look for the smallest z instead

"""

max_X = 100_000_000

pairs = {}

for a in range(1,max_X):
    a2 = a**2
    if a2 + 2*(a+1) > max_X:
        break
    for c in range(1,max_X):
        y = 2*c*(a+c)
        x = a2 + y
        if x > max_X:
            break
        if x not in pairs:
            pairs[x] = set()
        if y in pairs and pairs[y].intersection( pairs[x] ):
            print("Found:",x,y,pairs[y].intersection( pairs[x] ))
        pairs[x].add(y)

