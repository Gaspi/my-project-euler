# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=94


"""
Case 1 :  Triangles  n/n/n+1

n² = ( (n+1)/2 )² + h²
h = sqrt(3n²-2n-1)/2

h*(n+1)/2 entier
=>
sqrt(3n²-2n-1) * (n+1) == 0 mod 4



Cas 2: Triangles  n/n/n-1

n² = ( (n-1)/2 )² + h²
h = sqrt(3n²+2n-1)/2

h*(n-1)/2 entier
=>
sqrt(3n²+2n-1) * (n-1) == 0 mod 4



Modulo 4 :
n          0 1 2 3
n²         0 1 0 1
3n²+2n-1   3 0 3 0
3n²-2n-1   3 0 3 0

=> si n pair, 3n²-2n-1 ne peut pas être un carré
=> si n impair, sqrt(...)  (s'il est entier)  et n+1 sont pairs  => la condition est vérifiée
Il suffit de trouver les n=2k+1 impairs tels que
1)   3n²-2n-1
     3(2k+1)²-2(2k+1)-1
     3(4k²+4k+1)-4k-2-1
     12k²+8k
     est un carré  (ie 3k²+2k carré)
     > ajouter  3n+1 = 3*(2k+1)+1 = 6k+4

ou

2)   3n²+2n-1
     3(2k+1)²+2(2k+1)-1
     3(4k²+4k+1)+4k+2-1
     12k²+16k+4
     est un carré (ie 3k²+4k+1 carré)
     > ajouter  3n-1 = 3*(2k+1)-1 = 6k+2

Il suffit de trouver les k tels que
Pour k = 0 to 150_000_000,
Si  3(2k+1)²-2(2k+1)-1 = 3(4k²+4k+1)-4k-2-1 = 12k²+8k  est un carré
    donc si 3k²+2k
> ajouter  3*(2k+1)+1 = 6k+4
Si  3(2k+1)²+2(2k+1)-1 = 3(4k²+4k+1)+4k+2-1 = 12k²+16k+4  est un carré
    donc si 3k²+2k+1
> ajouter  3*(2k+1)-1 = 6k+2

"""

import math

def is_square(n):
    return n == math.isqrt(n) ** 2

acc = 0
for k in range(1,166_666_666):
    k2_3 = 3*(k**2)
    if is_square(k2_3 + 2*k):
        acc += 6*k+4
        if k < 100:
            print(2*k+1,2*k+1,2*k+2)
    if is_square(k2_3 + 4*k + 1):
        acc += 6*k+2
        if k < 100:
            print(2*k+1,2*k+1,2*k)
    if k % 1_000_000 == 0:
        print( (10000 * k // 166_666_666)/100.0,"%")

print(acc)

