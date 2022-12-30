# -*- coding: utf-8 -*-
# Useful functions

import math

# Returns smallest prime divisor of num
def prime_divisor(num):
    if num % 2 == 0:
        return 2
    if num % 3 == 0:
        return 3
    a = math.isqrt( abs(num) )
    b = 5
    while b <= a:
        if num % b == 0:
            return b
        if num % (b+2) == 0:
            return b+2
        b=b+6
    return abs(num)

def all_prime_divisors(num):
    res = []
    while num > 1:
        d = prime_divisor(num)
        res.append(d)
        num //= d
    return res

def isprime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0:
        return False
    if num < 9:
        return True
    if num%3 == 0:
        return False
    a = math.isqrt( abs(num) )+1
    for d in range(5,a,6):
        if num % d == 0:
            return False
    for d in range(7,a,6):
        if num % d == 0:
            return False
    return True

def isprime_precomputed(n, primes):
    lim = math.isqrt(n)
    i = 2
    while primes[i] <= lim:
        if n % primes[i] == 0:
            return False
        i+=1
    return True

def _add_if_prime(n, primes):
    if isprime_precomputed(n,primes):
        primes.append(n)

def enumerate_primes(maxp):
    primes = [2,3,5,7]
    n = 11
    while n <= maxp:
        _add_if_prime(n  , primes)
        _add_if_prime(n+2, primes)
        n += 6
    return primes

def erathostenes_sieve(maxp):
    primes = [2]
    sieve_size = 1 + (maxp-1)//2
    # sieve[i] == True  means that 2i+1 is prime
    sieve = [ True for i in range(sieve_size)  ]
    sieve[0] = False
    stop = (math.isqrt(maxp)-1) // 2
    for i in range(1,stop+1):
        if sieve[i]:
            p = 2*i+1
            primes.append(p)
            for k in range(p, maxp // p+1, 2):
                sieve[ (p*k-1)//2 ] = False
    for i in range(stop+1,sieve_size):
        if sieve[i]:
            primes.append(2*i+1)
    return primes, sieve

class ErathostenesSieve:
    def __init__(self, max_prime=100_000, min_step=10_000):
        self.min_step = min_step
        # sieve[i] == True  means that 2i+1 is prime
        self.primes = [2]
        self.sieve = [False]
        # Current state of the computation
        self.sieve_size = 1
        self.max_prime = 2
        self.stop = 0
        # Extend the sieve
        self.extend(max_prime)
    
    def extend(self, new_max_prime):
        if new_max_prime <= self.max_prime:
            return
        # Retain old values
        old_sieve_size = self.sieve_size
        old_max_prime = self.max_prime
        old_stop = self.stop
        # Increase max_prime by a minimum step
        self.max_prime = max(new_max_prime, old_max_prime+self.min_step)
        self.sieve_size = 1+self.max_prime//2
        # Extend the sieve
        self.sieve = [ i >= old_sieve_size or self.sieve[i] for i in range(self.sieve_size)  ]
        self.stop = (math.isqrt(self.max_prime)-1) // 2
        # Apply already found primes to the new sieve
        for p in self.primes[1:]:
            if p > 2*old_stop+1:
                break
            for k in range( 1+2*((old_max_prime // p + 1)//2), self.max_prime // p + 1, 2):
                self.sieve[ (p*k-1)//2 ] = False
        # Proceed with the sieve algorithm
        for i in range(old_stop+1, self.stop+1):
            if self.sieve[i]:
                p = 2*i+1
                if p >= old_max_prime:
                    self.primes.append(p)
                for k in range(p, self.max_prime // p + 1, 2):
                    self.sieve[ (p*k-1)//2 ] = False
        for i in range( max(old_sieve_size,self.stop+1), self.sieve_size):
            if self.sieve[i]:
                self.primes.append(2*i+1)
    
    def is_prime(self, n):
        if n%2 == 0 or n < 3:
            return n == 2
        self.extend(n)
        return self.sieve[n//2]



# Returns u,v,gcd(a,b) such that a.u + b.v = gcd(a,b)
def extended_euclid(a,b):
    r0 = abs(a)
    r1 = abs(b)
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    # Invariant : a.s + b.t = r  (for both values of s,t,r)
    while r1 > 0:
        q = r0 // r1
        (r0, r1) = (r1, r0 - q*r1)
        (s0, s1) = (s1, s0 - q*s1)
        (t0, t1) = (t1, t0 - q*t1)
    return (s0,t0,r0)


def perfect_cube(x):
    x = abs(x)
    res = int(round(x ** (1. / 3)))
    if res ** 3 == x:
        return res


# Assumes a>0 and gcd(a,m) = 1
# Returns the smallest u > 0 such that a.u = 1 mod m
def invert_mod(a,b):
    (u,v,gcd) = extended_euclid(a,b)
    return u % b



