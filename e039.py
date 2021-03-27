from benchmark import timed

# Lowest triplet is 12. Only check for even n. b must be < n//2 
# a*a is much faster than a**2 !
@timed
def most_triplets():
    py_triplets = lambda n : (n,len( [n for a in range(1,n+1) for b in range(a+1,n//2) if (a*a + b*b == ((n-(a+b)))*(n-(a+b)))] ))
    return max( (py_triplets(n) for n in range(12,1001,2)), key=lambda x: x[1] )

print (most_triplets())


quit()

@timed
def triplets(n):
    return [ (a,b,(n-(a+b)),n) for a in range(1,n+1) for b in range(a+1,n//2) if (a*a + b*b == ((n-(a+b)))*(n-(a+b))) ]

print(triplets(1000))
print(triplets(1500))    