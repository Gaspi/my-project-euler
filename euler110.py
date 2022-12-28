# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=110


"""

n(x+y) = xy


x = ny/(y-n) > 0

# solutions = # { y > 0 | ny == 0 mod (y-n)  and y > n }
#           = # { z > 0 | n(z+n) == 0 mod z }
#           = # { z | n² == 0 mod z }
#           = # diviseurs de n²

Exemple n = 1260

1260² = 1587600 == 0 mod z
for z = 1
    y = 1261
    x = 1260 * 1261 / 1 = 1 588 860
for z = 392

# x = y is counted once, the rest is double counted
# Solution : (1 + divisors of n²)/2

We are looking for the smallest n such that
n² has (strictly) more than 8 000 001 divisors

"""

"""
Counting divisors :
1260 = 2 × 2 × 3 × 3 × 5 × 7

divisors are counted :
    2 can be taken 0, 1, 2
    3 can be taken 0, 1, 2
    5 can be taken 0, 1
    7 can be taken 0, 1
3*3*2*2 = 36

For n² :
    2 can be taken 0, 1, 2, 3, 4
    3 can be taken 0, 1, 2, 3, 4
    5 can be taken 0, 1, 2
    7 can be taken 0, 1, 2
5*5*3*3 = 225

"""

L = 15
# First primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def nb_div(dec):
    res = 1
    for i in range(L):
        res *= (1 + 2*dec[i])
    return (res+1)//2

def recompose(dec):
    n = 1
    for i in range(L):
        n *= primes[i] ** dec[i]
    return n


# On peut vérifier que le produits des 15 premiers nombres premiers, n=614889782588491410
# fournit bien un candidat au score inférieur à 4 millions : 7 174 454
# Note : pour 14 cela ne marche pas
dec_base = [1]*15
print( recompose(dec_base) )
print( nb_div(dec_base) )


mini_n = recompose(dec_base)
stack = [dec_base]

while True:
    dec = stack.pop(0)
    #last non zéro index in dec
    last_index = max([i for i in range(L) if dec[i] > 0] )
    ndiv = nb_div(dec)
    if ndiv > 4_000_000:
        n = recompose(dec)
        if n < mini_n:
            mini_n = n
            print()
            print(mini_n)
            print(dec)
        stack.append( [ dec[i] if i != last_index else dec[i]-1 for i in range(L) ] )
    else:
        for j in range(last_index):
            if j == 0 or dec[j] < dec[j-1]:
                stack.append( [ dec[i] if i != j else dec[i]+1 for i in range(L) ] )

# à interrompre rapidement, la solution est le troisième meilleur









