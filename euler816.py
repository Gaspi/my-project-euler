# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=816
"""

"""

import math

N = 2_000_000
#N = 14

s = 290797
def next():
    global s
    a = s
    s = (s * s) % 50515093
    return a
P = [ (next(), next()) for i in range(N)]
print("Generation done.")

min_sq_dst = 50515093

if N < 100:
    min_sq_dst = min( [ (a-c)**2 + (b-d)**2 for (a,b) in P for (c,d) in P if a > c or b > d ] )

elif False:
    
    nb_blocks = 1_000
    def block(x):
        return (x * nb_blocks) // 50515093
    
    blocks = [ [ [] for i in range(nb_blocks) ] for i in range(nb_blocks) ]
    
    for (a,b) in P:
        blocks[ block(a) ][ block(b) ].append( (a,b) )
    
    
    min_sq_dst = 50515093
    for i in range(nb_blocks-1):
        for j in range(nb_blocks-1):
            for (a,b) in blocks[i][j]:
                for di in range(-1 if i > 0 else 0, 2):
                    for dj in range(-1 if j > 0 else 0, 2):
                        for (c,d) in blocks[i+di][j+dj]:
                            if a != c or b != d:
                                min_sq_dst = min(min_sq_dst, (a-c)**2 + (b-d)**2 )

else:
    # Lucky solution (does not work for all set of points)
    
    P.sort(key=lambda x: x[0])
    print("Sorted")
    (a,b) = P[0]
    for i in range(1,N):
        (c,d) = P[i]
        min_sq_dst = min(min_sq_dst, (a-c)**2 + (b-d)**2 )
        a=c
        b=d


print("Solution:", round( math.sqrt(min_sq_dst),9))
