# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755 
# Find the next triangle number that is also pentagonal and hexagonal
from benchmark import timed
from itertools import count

# Infinite generators starting at the next n for each seq
Tn = ( (n*n + n)//2 for n in count(start=286) )
Pn = ( n*(3*n-1)//2 for n in count(start=166) )
Hn = ( n*(2*n-1) for n in count(start=144) )

@timed
def find():
    hn, pn = 0, 0
    while(tn:=next(Tn)):
        while hn < tn:
            hn = next(Hn)
        while pn < tn:
            pn = next(Pn)
        if pn == hn == tn:
            return tn
        i+=1    

result = find()
print(result)