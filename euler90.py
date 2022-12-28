# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=90

# We first generate all combination of dices
combinations = [ set() ]
for i in range(10):
    combinations += [ c.union([i]) for c in combinations ]
combinations = [ c for c in combinations if len(c) == 6]

# Self explanatory, avoids repeating boolean formula
def m(l,r,a,b):
    return (a in l and b in r) or (b in l and a in r)

acc = []
for l in combinations:
    for r in combinations:
        # 01, 04, 25 and 81 are easy
        # 09, 16, 36, 49 and 64 need to account for 9-6 equivalence
        if  m(l,r,0,1) and m(l,r,0,4) and m(l,r,8,1) and m(l,r,2,5) and \
            ( m(l,r,0,6) or m(l,r,0,9)) and \
            ( m(l,r,1,6) or m(l,r,1,9)) and \
            ( m(l,r,3,6) or m(l,r,3,9)) and \
            ( m(l,r,4,6) or m(l,r,4,9)):
            acc.append( (l,r) )

print("Result:",len(acc)//2)
print("Example", acc[0])
