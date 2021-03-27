#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

from benchmark import timed

# ~36ms @ n=1000 ( a*a is much faster than a**2 )
@timed
def py_triplet(n=1000):
    return next((a,b,(n-(a+b)),(a*b*(n-(a+b)))) for a in range(12,n+1) for b in range(a+1,n//2) if (a*a + b*b == ((n-(a+b)))*(n-(a+b)))) 

print(py_triplet(1000))



quit()

# first attempt - awfully inefficient
# 12s @ n=1000
def triplet(n=1000):
    return next( (a,b,c,a*b*c) for a in range(1,n+1)\
        for b in range(a+1,n+1)\
            for c in range(b+1,n+1) if a+b+c == n and (a**2 + b**2 == c**2)  ) 

# revised 
# ~250ms @ n=1000
def triplet2(n=1000):
    return next( (a,b,n-(a+b)) for a in range(1,n+1)\
        for b in range(a+1,n-a-1)\
            if (a**2 + b**2 == ((n-(a+b)))**2)  ) #a+b+(n-(a+b)) == n and 

# better still, ~150ms @ n=1000
def py_triplet(n=1000):
    return next((a,b,(n-(a+b)),(a*b*(n-(a+b)))) for a in range(12,n+1) for b in range(a+1,n-a) if b < n//2 and (a**2 + b**2 == ((n-(a+b)))**2)) 
