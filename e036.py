# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
from benchmark import timed

# double base palindrome
def is_dbp(n):    
    s10 = str(n)
    if s10 == s10[::-1]:
        s2 = bin(n)[2:]
        if s2 == s2[::-1]: 
            return True
    return False

@timed
def sum_dbp(N):
    return sum(filter(is_dbp, range(1,N)))    


result = sum_dbp(1000000)
print(result)