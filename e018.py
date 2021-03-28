
from benchmark import timed

tri = [\
   [3],
  [7,4],
 [2,4,6],
[8,5,9,3]
]

tri = [\
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

def paths(path=[], row=0, idx=0):
    path.append( tri[row][idx] )
    
    if row == len(tri)-1:
        #print(path, sum(path))
        yield sum(path)
        return
    
    yield from paths(path,row+1,idx)
    path.pop()

    yield from paths(path, row+1, idx+1)
    path.pop()

@timed
def max_path_recusrive():
    return max( paths([],0,0) )

@timed
def max_path_fold():
    for r in range(len(tri)-1,0,-1):
        row = tri[r]
        for idx in range( 0, len(row)-1 ):
            x = max( row[idx], row[idx+1] )
            tri[r-1][idx] += x
    
    return tri[0][0]          
            

print( max_path_recusrive() )

print ( max_path_fold() )

