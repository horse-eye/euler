import pyprimesieve as pp
from benchmark import timed

max_prime = 1000000
primes = pp.primes(max_prime)
max_idx = len(primes)-1
cache = set( primes )

# optimize:
# work from max slice down (and return first result), not min slice up

@timed
def find_longest_slice(min_slice):
    result=0
    longest_slice = min_slice
    for idx in range(0, max_idx - min_slice):
        slice = min_slice
        while (subset := sum(primes[idx:idx+slice])) <= max_prime:
            if subset in cache:
                if slice > longest_slice:
                    longest_slice = slice
                    result = subset
            slice +=1
    return (result, longest_slice, idx)        

result = find_longest_slice(21)
print( result )        









