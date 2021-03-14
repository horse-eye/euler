# Pandigital Prime
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
import math
import benchmark as bm
import itertools as it
import functools as ft

def isprime(n):
    sq = int(math.sqrt(n))
    return all( n%i > 0 for i in range(2,sq+1) )

def pdp(N):
    digits = list(reversed(range(1,N+1)))    
    perms = it.permutations(digits)
    for seq in perms: 
        res = ft.reduce(lambda total, d: 10 * total + d, seq, 0) 
        if(isprime(res)): return res

# more functional style
def pdp2(N):
    digits = list(reversed(range(1,N+1)))     
    perms = it.permutations(digits)
    num = lambda seq: ft.reduce(lambda total, d: 10 * total + d, seq, 0)
    return next( filter(isprime, (num(seq) for seq in perms)), None )

def find_pdp():
    return next(filter(None, (pdp2(n) for n in range(9,1,-1))))
  

x = find_pdp()
print(x)

bm.time( "e41-8", lambda: pdp(8) )
bm.time( "e41-pdp2-8", lambda: pdp2(8) )
bm.time( "e41-8", lambda: pdp(8) )
bm.time( "e41-pdp2-8", lambda: pdp2(8) )

quit()

bm.time( "e41-9", lambda: pdp(9) )
bm.time( "e41-8", lambda: pdp(8) )
bm.time( "e41-7", lambda: pdp(7) )
bm.time( "e41-find", lambda: find_pdp() )

