# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=122

res = [None, 0] + [None]*199

countdown = 199

# list of sorted lists of distincts computed exponents so far
possible_sets = [ [1] ]

for nb_steps in range(1,30):
    print('step:',nb_steps, ':', len(possible_sets))
    new_sets = {}
    for s in possible_sets:
        for i in range(len(s)):
            for j in range(i,len(s)):
                new_exp = s[i]+s[j]
                if new_exp <= 200 and new_exp not in s:
                    new_set = sorted( s+[new_exp] )
                    new_sets[ '-'.join([str(i)for i in new_set]) ] = new_set
                    if res[new_exp] is None:
                        res[new_exp] = nb_steps
                        countdown -= 1
                        if countdown % 5 == 0 or countdown < 10:
                            print('->',countdown)
                        if countdown == 0:
                            break
            if countdown == 0:
                break
        if countdown == 0:
            break
    if countdown == 0:
        break
    possible_sets = list(new_sets.values())

print(possible_sets)
print(res)

print(sum(res[1:200]))
#: Res : 1582