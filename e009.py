#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import benchmark as bm

# awfully inefficient
def triplet(n=1000):
    r = range(1,n+1)
    #return next((a,b,c) for a in r for b in r for c in r if a<b and c>b and a+b+c == n and (a**2 + b**2 == c**2)  ) 
    return next( (a,b,c,a*b*c) for a in range(1,n+1)\
        for b in range(a+1,n+1)\
            for c in range(b+1,n+1) if a+b+c == n and (a**2 + b**2 == c**2)  ) 


def triplet2(n=1000):
    return next( (a,b,n-(a+b)) for a in range(1,n+1)\
        for b in range(a+1,n-a-1)\
            if (a**2 + b**2 == ((n-(a+b)))**2)  ) #a+b+(n-(a+b)) == n and 

def triplet3(n=1000):
    return next((a,b,n-(a+b)) for a in range(1,n+1) for b in range(a+1,n-a) if b < n//2 and (a**2 + b**2 == ((n-(a+b)))**2)) 


print(triplet2(1000))
print(triplet3(1000))

#bm.time("t", triplet)
bm.time("t2", triplet2)
bm.time("t2", triplet3)

#n=10
#x = ( (a,b,n-(a+b)) for a in range(1,n+1)\
#        for b in range(a+1,n-a) if b< n//2) #a+b+(n-(a+b)) == n and 
