# Champernowne's constant
# An irrational decimal fraction is created by concatenating the positive integers: 0.123456789101112...
# Find d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
from math import prod
from benchmark import timed

@timed
def champernowne():
    c = ['0','1','2','3','4','5','6','7','8','9']
    for n in range(10,185200): 
        c.extend( str(n)  )
    return prod( int(c[n]) for n in [1,10,100,1000,10000,100000,1000000] )


print(champernowne())    