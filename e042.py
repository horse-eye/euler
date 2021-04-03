from benchmark import timed
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1)
# Using words.txt how many are triangle words?

with open('resources/e042-words.txt') as f:
    words = f.read().strip('"').split('","')

@timed
def tw():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = lambda word : sum(alphabet.index(w)+1 for w in word)
    triangles = set( int(n/2 * (n+1)) for n in range(1,200) )
    return sum( 1 for word in words if score(word) in triangles )

print ( tw() )