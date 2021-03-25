# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def fac(n):
    return 1 if n<=1 else n*fac(n-1)

# Don't know how to find upper bound, so ran it for 10M and none found after 40585

digifac = {n:fac(n) for n in range(0,10)}
result =  sum( n for n in range(3,50000) if(p := sum( digifac[int(i)] for i in str(n) )) == n )

print(result)    