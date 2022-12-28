# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=98

# Step 1 : precompute all square anagrams for length < 6

import csv, math
with open('words.txt', 'r') as file:
    words = csv.reader(file).__next__()

for i in range(15):
    print(i,len([w for w in words if len(w)==i]))

anagrams = {}
singles = {}

for word in words:
    key = ''.join(sorted([l for l in word]))
    if key in anagrams:
        anagrams[key].append(word)
    elif key in singles:
        anagrams[key] = [ singles[key], word ]
        del singles[key]
    else:
        singles[key] = word
del singles

def compute_perm(str1, str2):
    perm = {}
    revperm = {}
    for k,v in zip(str1,str2):
        if k in perm and perm[k] != v:
            return None
        if v in revperm and revperm[v] != k:
            return None
        perm[k]=v
        revperm[v]=k
    return perm

def apply_perm(perm, s):
    try:
        return ''.join([perm[l] for l in s])
    except:
        return None

def is_square(n):
    return n == math.isqrt(n) ** 2

# Prints all groups of anagrams sorted by decreasing length (longest is 9)
for (length, words) in sorted([ (len(k), anagrams[k])  for k in anagrams], reverse=True):
    print(length, words)
    minsqrt = 10**(length//2  )   if length%2==1 else math.isqrt(10**(length-1))+1
    maxsqrt = 10**(length//2  )-1 if length%2==0 else math.isqrt(10**length)
    for c in range(minsqrt, maxsqrt+1):
        n = c**2
        for i1 in range(len(words)-1):
            w1 = words[i1]
            perm = compute_perm(w1,str(n))
            if perm is not None:
                for i2 in range(1,len(words)):
                    w2 = words[i2]
                    m = apply_perm(perm, words[i2])
                    if m is not None and is_square(int(m)):
                        print(w1,c,n,w2,m,math.isqrt(int(m)))