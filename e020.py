# Find the sum of the digits in the number 100!

from benchmark import timed

def fac(n):
    return 1 if n==1 else n*(fac(n-1))

@timed
def sum_fac_digits(n):
    return sum( int(d) for d in str(fac(n)) )    

result = sum_fac_digits(100)    
print (result)