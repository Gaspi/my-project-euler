# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=88

# Générateurs
#   2 * n * 1^(2n-2) = 2 + n + 1*(n-2) = 2n   (taille 2n)
#   3 * n * 1^(2n-3) = 3 + n + 1*(2n-3) = 3n   (taille 2n-1)
# Si k   pair le "minimal product-sum" de taille k est au plus k
# Si k impair le "minimal product-sum" de taille k est au plus 3*(k+1)/2
# Pour k = 12000 on s'intéresse uniquement aux "minimal product-sum" <= 18_000

res = [ None for k in range(12001)]


current_set  = [0 for k in range(6000) ]
current_prod = 1
current_size = 0

def next():
    global current_set, current_prod, current_size
    k=2
    while True:
        if k >= 6000:
            return False
        current_set[k]+=1
        current_size  +=1
        current_prod *= k
        if current_prod > 18000:
            current_prod //= k ** current_set[k]
            current_size -= current_set[k]
            current_set[k] = 0
            k+=1
        elif current_size < 2:
            k=2
        else:
            break
    return True

while next():
    size = current_prod - sum([k*current_set[k] for k in range(2,6000)] ) + current_size
    if current_size > 1 and size < 12001 and (res[size] is None or current_prod < res[size]):
        res[size] = current_prod

print("Minimal product-sums:",res[2:20])
print("Result:", sum(set(res[2:12000])))

