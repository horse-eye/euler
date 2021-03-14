"""The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:
Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.
If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000)."""

from math import sqrt, prod
import benchmark as bm
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
    for i in range(1,n+1):
        dpfs = get_pfs_distinct(i)
        #if any(pf >= i for pf in dpfs):
            #continue
        p = prod(dpfs) 
        if(p <= i): 
            yield i,p

N = 10000

x = {i:n for (i,n) in getrads(N)}
y = [(n,r) for n, r in sorted(x.items(), key=lambda item: item[1])]

#print( y[9996:10002], y[9999])
#print ( y[-20:] )
'''
(1947, 1947), 
(5841, 1947), 
(17523, 1947), 
(21417, 1947), 
(52569, 1947), 
(64251, 1947), '''