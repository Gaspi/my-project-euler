# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=144
"""

Assuming a ray going to (a,b) to (c,d)

Inbound vector : (c-a, d-b)
Slope at contact : -4c/d
Vector along slope at contact : (d, -4c)
Orthogonal vector towards center at contact : (-4c,-d)
Outbound vector :
    (u,v) such that  ( u-(c-a) , v-(d-b) ) . (-4c, -d) = 0
    4c * (u-c+a) + d * (v-d+b) = 0
    4c * (u-c+a) + d * (v-d+b) = 0
    4cu+dv = 4c(c-a) + d(b-d)
    > ( 1,  (4c(c-a) + d(b-d) - 4c )/d )
      and
      ( (4c(c-a) + d(b-d) - d) / 4c , 1)
    or
      ( d,  4c(c-a) + d(b-d) - 4c )
      and
      ( 4c(c-a) + d(b-d) - d , 4c)


outbound equation :
      (c,d) + t * ( 4c(c-a) + d(b-d) - d , 4c)

we need to solve (for t) :
    4(c + t(4c(c-a) + d(b-d) - d) )² + (d+4ct)² = 0

    4 (c² + )  (c + t(4c(c-a) + d(b-d) - d) )² + (d+4ct)² = 0






"""