from math import sqrt

####################################################
# DIVISORS
####################################################

def countdivs(n):    
    sq = int(sqrt(n))
    r = range(2,sq+1)   
    y = [n / i for i in r if n%i==0]
    return len(y)*2 + 2

def sumdivs(n):   
    sq, s = int(math.sqrt(n)), 1 
    for x in (n/i for i in range(2,sq+1) if n%i==0):
        s += x
        y = n/x
        if y!=x: s+=y 
    return s

def get_divisors(n): 
    sq = int(sqrt(n))
    divs = [i for i in range(2,sq+1) if n%i==0]
    divs.extend( [n//i for i in divs] )
    return divs

####################################################
# PRIME NUMBERS
####################################################

primecache = {}
def isprime(n):
    if n in primecache: 
        return primecache[n]
    sq = int(sqrt(n))
    primecache[n] = x = all( n%i > 0 for i in range(2,sq+1) )
    return x 

def get_primefactors(n):
    while n%2 == 0:
        yield 2
        n//=2
    for i in range(3, int(sqrt(n)+1),2):
        while n%i == 0:
            yield i
            n//=i
    if n>2: yield n 

def get_primefactors_alt(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

# get all primes <= n
def get_all_primes_naive(n):
    return filter(isprime, (n for n in range(n,1,-1)) )    

# Sieve of Eratosthenes
def prime_sieve(n):
    A = [1 for i in range(2,n+1)]
    i, sq = 2, int(sqrt(n))+1
    while (i<sq):
        if A[i-2]:
            j = i*i
            while (j<=n):
                A[j-2]=0
                j+=i
        i+=1
    return [idx+2 for idx, p in enumerate(A) if p==1] # can change to generator

####################################################
# STRINGS
####################################################

def ispalindrome(a,b):
    return str(a)==str(b)[::-1]

def rotations(n):
    yield n
    if n < 10:
        return
    s = str(n)
    for _ in range(len(s)-1):
        s = s[1:]+s[0]
        yield int(s)     