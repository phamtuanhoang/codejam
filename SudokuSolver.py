import sys,os
from sys import stdin


testcase = int(stdin.readline().split()[0])
dimension = int(stdin.readline().split()[0])

lang   = "".join(stdin.readline() for i in range(dimension*dimension))
print lang
#for i, line in enumerate(l.strip() for l in stdin.readlines()):
    
def cross(A,B):
    "cross product of elements in A and elements in B"
    return [a+b for a in A for b in B]
digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

squares = cross(rows, cols)
unitlist = ([cross(rows,c) for c in cols] +
            [cross(r,cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123','456', '789')]
            )
units = dict((s, [u for u in unitlist if s in u])
            for s in squares)
peers = dict((s, set(sum(units[s],[])) -set([s]))
                for s in squares)

