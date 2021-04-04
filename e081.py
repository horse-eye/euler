# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt, containing an 80 by 80 matrix.
from benchmark import timed
import numpy as np

with open('resources/e081-matrix.txt') as f:
    content = f.read().splitlines()    
matrix = np.array([ [int(s) for s in line.split(',')] for line in content ])


@timed
def min_path_fold():
    for r in range(len(matrix)-1,-1,-1):
        row = matrix[r]
        for idx in range(len(row)-1,-1,-1 ):
            right = row[idx+1] if idx < len(row)-1 else -1
            below = matrix[r+1][idx] if r < len(matrix)-1 else -1
            if right==-1 or below == -1: 
                x = max(right, below)
            else: 
                x = min( right, below )
            if x != -1:
                row[idx] += x
    return matrix[0][0]   


print(min_path_fold())


'''
matrix = np.array(\
[[131,673,234,103,18],
[201,96,342,965,150],
[630,803,746,422,111],
[537,699,497,121,956],
[805,732,524,37,331]])
'''