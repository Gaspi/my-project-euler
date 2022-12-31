# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=111


"""
La plupart des cas ont 8 ou 9 digits identiques, cela réduit considérablement
le nombre de premiers à tester
"""

N = 10

# Problems besides 0
problems = [] if N == 4 else ['2','8']

def isprime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0:
        return False
    if num < 9:
        return True
    if num%3 == 0:
        return False
    a = int(num**0.5)
    b = 5
    while b <= a:
        if num%b == 0:
            return False
        if num%(b+2) == 0:
            return False
        b=b+6
    return True



digits = [str(i) for i in range(10)]

S = { d:0 for d in digits }

def check(s):
    if isprime( int(s) ):
        print('>',s)
        return int(s)
    else:
        return 0

print("Checking that no 10-same-digits is prime")
for d in digits:
    S[d] += check( d*N )

for d in digits:
    if d != '0' and d not in problems:
        print("Checking all-but-one-digits prime for d =",d)
        for e in digits:
            if e != d:
                for p in range(N):
                    if p > 0 or e != '0':
                        S[d] += check( d*p + e + d*(N-p-1) )
# M(10,d) is 9 for all d notin {0, 2}


print("Checking all-but-two-digits primes for d=0")
# for d = 0: the leading must be non zero
for d0 in digits[1:]:
    for d in digits[1:]:
        for p in range(N-1):
            S['0'] += check( d0 + '0'*p + d + '0'*(N-2-p) )


for d in problems:
    print("Checking all-but-two-digits primes for d =",d)
    for d1 in digits:
        for d2 in digits:
            for p1 in range(N-1):
                if p1 > 0 or d1 != '0':
                    for p2 in range(N-1-p1):
                        S[d] += check( d*p1 + d1 + d*p2 + d2 + d*(N-2-p1-p2) )

print(S)

print("Résultat:",sum(S.values()))
