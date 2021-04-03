# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
from benchmark import timed

@timed
def max_palindrome():
    r = range(999,100,-1)
    ispalindrome = lambda x : x[:3] == x[-3:][::-1]
    return max(a*b for a in r for b in r if ispalindrome(str(a*b)))

print ( max_palindrome() )
