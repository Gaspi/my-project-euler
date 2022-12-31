# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=327
"""

Reasonning backward to compute M(C,R)

To finish we need
- 0 keys at room R+1
- 1 key  at room R
- ...
- C keys at room R+1-C
then C+1 keys are not enough we need to
> first bring C-2 keys from the previous room
  using 2 keys
> then bring 2 more using one key (assuming C >= 3)

- C+3 at room R-C
- C+6 at room R-C-1
- ...

Assuming we need n keys at a room,
to get to the previous room we need :
- 1 extra key  if         n < C
- 3 extra keys if C    <= n < C +  (C-2) = 2C-2
- 5 extra keys if 2C-2 <= n < C + 2(C-2) = 3C-4
- ...
- In general : 1 + 2 * ( (n-2)//(C-2) )   keys


"""

def needed_keys(n,C):
    return 1 if n < C else 1 + 2*( (n-2)//(C-2) )

def M(C,R):
    nb_keys = 0
    for n in range(R+1):
        nb_keys += needed_keys(nb_keys,C)
    return nb_keys

print(3,3,M(3,3))
print(3,6,M(3,6))
print(4,6,M(4,6))

print(sum([M(C, 6) for C in range(3,5 )] ))
print(sum([M(C,10) for C in range(3,11)] ))

print("Solution:",
      sum([M(C,30) for C in range(3,41)] ))
