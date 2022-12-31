# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=719
"""

We look instead for all i^2
such that i is a sum of a decomposition of i^2

Assuming i^2 has k digits
We start by looking at candidate for the longest number in the decomposition
It should not be much smaller (in length) than i since i^2 has approximately
twice as many digits as i

Assuming a sequence of size S, the largest number you can get
by using a largest of length L at position P is :
    
    10^L-1         (size of the largest number extract if all 9)
  + 10^(P)-1       (largest decomposition before: all together)
  + 10^(S-P-L)-1   (largest decomposition after : all together)

Assuming a position p in the sequence of digits:




"""

N = 1_000_000
#N = 100

def to_list(n):
    return [ int(d) for d in list(str(n)) ]
def from_list(l):
    acc = 0
    for d in l:
        acc=10*acc+d
    return acc


answer = 0
for i in range(2,N+1):
    I = len(list(str(i)))
    if N > 100 and i % 10_000 == 0:
        print(100*i/N, "%")
    digits = to_list(i**2)
    decompositions = [ (i, digits) ]
    while decompositions:
        (n, remain) = decompositions.pop()
        S = len(remain)
        if S == 0:
            if n == 0:
                # print(i, "-> ",i**2)
                answer += i**2
                break
            continue
        acc = 0
        for j in range(S):
            acc = 10*acc + remain[j]
            if acc > n or (acc+1) * 10**(S-j-1) <= n:
                break
            if n-acc <= 10**(S-j-1)-1:
                decompositions.append( (n-acc, remain[j+1:]) )

print("Answer:", answer)

