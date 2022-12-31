# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=118
"""
All nine-1-to-9-distinct-digits numbers (e.g. 897654321) are divisible by 3
"""

from pe_utils import isprime

digits = [str(i) for i in range(1,10)]

print("Generating all nine-1-to-9-distinct-digits primes...")

distinct_digits_primes = []

distinct_digits = ['']
for l in range(1,9):
    new_distinct_digits = []
    for n in distinct_digits:
        for d in digits:
            if d not in n:
                m = d+n
                new_distinct_digits.append(m)
                im = int(m)
                if isprime(im):
                    distinct_digits_primes.append( {'val':im, 'set':set(m), 'size':len(m)} )
    distinct_digits = new_distinct_digits

print('9-distinct-digits primes by size:', {
    size : len([1 for p in distinct_digits_primes if p['size']==size]) for size in range(1,9) } )


#solutions = []
solution_count = 0
def enumerate_sets(cur_set, available, depth=0):
    if cur_set['size'] == 9:
        global solution_count
        #solutions.append(cur_set)
        solution_count += 1
    while available:
        choice = available.pop()
        if choice['size'] + cur_set['size'] > 9:
            break
        new_set = {
            'vals' : cur_set['vals'].union([choice['val']]),
            'size': cur_set['size'] + choice['size']
        }
        max_size = 9-new_set['size']
        new_ava = [ n
            for n in available
            if n['set'].isdisjoint(choice['set']) and n['size'] <= max_size
        ]
        enumerate_sets(new_set, new_ava, depth+1)

available = distinct_digits_primes.copy()

available.reverse()
print("Testing combinations...")
enumerate_sets( { 'vals':set(), 'size':0 }, available)

print('Answer:', solution_count )
#print('Answer:', len(solutions) )

