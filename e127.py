"""The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000"""

from math import sqrt, prod
import benchmark as bm
import numpy as np
import time

def get_pfs_distinct(n):
    primfac = set({})
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.add(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.add(n)
    return primfac

def getrad(n):
    dpfs = get_pfs_distinct(n)
    return prod(dpfs)

def getrads(n):
    for i in range(1,n):
        dpfs = get_pfs_distinct(i)
        p = prod(dpfs) 
        if(p <= i): 
            yield i,p

def getbase3(n):
    a=1
    while a<n:
        b=a+1
        a_iseven = a%2==0
        while b+a<n:
            yield (a,b,a+b)
            b += 2 if a_iseven else 1
        a+=1
        #if(a%1000==0): print(a)    

def israd(t):
    a,b,c = t[0],t[1],t[2]
    ra = radcache[a]
    rb = radcache[b]
    rc = radcache[c]
    return (ra*rb*rc)<c

def isncd(t): 
    a,b = t[0],t[1]
    return np.gcd(a,b) == 1

N = 120000

radcache = {i:n for (i,n) in getrads(N)}

radlets = filter(israd, getbase3(N))
abchits = filter(isncd, radlets)

e = time.time()

sumc = sum(abc[2] for abc in abchits)

t = time.time()

print( sumc )

print(t-e)


#print (getrad(504))
#print(dict(getrads(N)))
#x = list(getbase3(N))
#print (x)