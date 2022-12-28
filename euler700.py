# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=700
"""
If m > n such that
n.P = a mod M
m.P = b mod M
a > b >= 0

then (m-n) P = (b-a) mod M  such that b-a < 0 and  a-b <= a

Assuming we have found a new Euler coin P.n = a mod M
We look for the smallest k such that
 k.P = c mod M with  -a <= c < 0  (i.e.   M-a <= M+c = (k*P % M)  )
Then the next Euler coin is P.(n+k) = a+c < a  mod M
It is indeed the next since any all k' < k such that P.(n+k') = a+c' < a mod M
would have been found first.

We memoize the list of k and remove them as soon as they become larger than the current Euler

"""

import pe_utils

M = 4503599627370517
P = 1504170715041707


inv = pe_utils.invert_mod(P,M)
ninv = -inv % M
# inv = 1051942428084853 is such that inv * P = -1 mod M
# far too big for brute force
print(inv)
print(ninv)


divisors = pe_utils.all_prime_divisors(P)
print(divisors)
# [17, 1249, 12043, 5882353]  prime decomposition of P
# M is prime  (N/MN is a field)  P.k % M is therefore cyclic of period M

# Manual inefficient computing of the first euler coins
if False:
    n = 0
    mini = M
    u=0
    while True:
        u = (u+P) % M
        n += 1
        if u < mini:
            print(n,u)
            mini = u
        if u < 20_000_000:
            break
    print('-------------------')

# Supposedly more efficient computation (should yield the same results)
n = 0
eulercoin = M
somme = 0

k = 1
c = P
while eulercoin > 0:
    while c < M - eulercoin:
        k += 1
        c = (c+P) % M
        if k % 10_000_000 == 0:
            print("k -> ",k)
    eulercoin -= M-c
    n = n+k
    print(n,eulercoin)
    somme += eulercoin
    if eulercoin < 20_000_000:
        break

"""
To proceed with the computation of eulercoins, it should be faster
to compute the increasing serie of k = inv*u < eulercoin  mod M  for all the u < eulercoin

"""

# Returns a list of the "last" eulercoins: those u < eulercoin such that
# k.P = u mod M

last = M
# Note : 1 is always a eulercoins if M is prime
# (since only P.M = 0 mod M and inv < m such that P.inv = 1 mod M)
for u in range(1,eulercoin):
    k = inv * u % M
    if k < last: # if this value occurs before the next smallest eulercoin then it is the previous eulercoin
        print(k,u)
        somme += u
        last = k
    if u % 1_000_000 == 0:
        print(u,"/",eulercoin,":",0.1 * ((1000*u)//eulercoin),"%")

print("Result :", somme)


