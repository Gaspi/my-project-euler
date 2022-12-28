# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=106

n = 12

# enumerate all sets of size [size] composed from distincts indexes between [imin] and [imax]
def enumerate_sets(size,imin,imax):
    if size == 0:
        return [ [] ]
    if size > 1 + imax - imin:
        return []
    return enumerate_sets(size,1+imin,imax) + [ [imin]+s for s in enumerate_sets(size-1,1+imin,imax) ]

def sets_repr(s1,s2):
    s = ''
    cs1 = s1.copy()
    cs2 = s2.copy()
    j = -min(s1)
    for i in range(n):
        if len(cs1) and i == cs1[0]:
            cs1.pop(0)
            s+='1'
        else:
            if len(cs2) and j == cs2[0]:
                cs2.pop(0)
                s += '2'
            else:
                s += '0'
            j += 1
    return s

def wp(s):
    c = 0
    for i in s:
        if i == '1':
            c+=1
        elif i == '2':
            c-=1
        if c < 0:
            return False
    return True

set_count = []
for size_sets in range(1, n // 2 + 1):
    # we only consider pairs of same size sets.
    # Since they are disjoint : 2 * size_set <= n
    print('...',size_sets)
    for s1 in enumerate_sets(size_sets,0,n-1):
        for s2 in enumerate_sets(size_sets,0,n-size_sets-1-min(s1)):
            s =  sets_repr(s1,s2)
            if not wp(s):
                set_count.append(s)

print(set_count)
print(len(set_count))
