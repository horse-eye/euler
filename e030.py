# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def fps(n):
    return sum( int(i)**5 for i in str(n) )

# Don't know how to find upper bound, so ran it for 1M and none found after 195k

result =  sum( 
    p for n in range(2,200000) 
    if(p := fps(n)) == n )

print (result)

