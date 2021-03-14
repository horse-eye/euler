# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import benchmark as bm
from math import sqrt

def get_primefactors(n):
    while n%2 == 0:
        yield 2
        n//=2
    for i in range(3, int(sqrt(n)+1),2):
        while n%i == 0:
            yield i
            n//=i
    if n>2: yield n 

def lpf(n): # wrong, do not use
    r = range( int(sqrt(n))+1,1,-1) 
    isprime = lambda x: all( x%i> 0 for i in range(2,int(sqrt(x))+1) )    
    return next(filter(isprime, (i for i in r if n%i==0) )) 

print ( max(get_primefactors(13195)) ) 
print ( max(get_primefactors(600851475143) ) )
print ( max(get_primefactors( 100000001 ))  )

#print ( lpf(13195) )
#print ( lpf(600851475143) )
#print ( lpf( 100000001 )) # wrong!, 5882353

bm.time( "e003", lambda: max(get_primefactors(600851475143) ) )   