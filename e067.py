from benchmark import timed

@timed
def max_path_fold(tri):
    for r in range(len(tri)-1,0,-1):
        row = tri[r]
        for idx in range( 0, len(row)-1 ):
            x = max( row[idx], row[idx+1] )
            tri[r-1][idx] += x
    
    return tri[0][0]   


with open('resources/e067-triangle.txt') as f:
    content = f.read().splitlines()    

triangle = [ [int(s) for s in line.split()] for line in content ]
print( max_path_fold(triangle) )