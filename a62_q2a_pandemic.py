#15:16
import sys,heapq,math
from collections import deque
sys.setrecursionlimit(999999999)
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
r,c,T = [int(i) for i in input().split()]

table = []
q = []
for i in range(r):
    k = [int(i) for i in input().split()]
    table.append(k)
    for j in range(c):
        if k[j]==1:
            q.append((i,j))
            table[i][j] = 0
    
    
dic = {}

for i in range(r):
    for j in range(c):
        #if table[i][j] == 2:
        #    continue
        dic[(i,j)] = []
        if i==0 and j==0:
            continue
        if j>0:
            dic[ (i,j) ].append( (i,j-1) )
            dic[ (i,j-1) ].append( (i,j) )
        if i>0:
            dic[ (i,j) ].append( (i-1,j) )
            dic[ (i-1,j) ].append( (i,j) )
        
#print(table)
#print(dic)
#print(q)
count = 0
for t in range(T+1):
    newQ = []
    for ir,ic in q:
        if table[ir][ic]==1:
            continue
        table[ir][ic] = 1
        count += 1
        for iR,iC in dic[ (ir,ic) ]:
            if table[iR][iC] == 0:
                newQ.append( (iR,iC) )
    q = newQ
#print(table)
print(count)
'''
5 4 3
0 0 0 0
0 0 0 0
0 0 0 0
0 2 1 0
0 0 0 0

3 3 2
0 0 1
0 0 0
0 0 1

1 12 3
0 1 0 0 0 0 0 0 0 1 0 0
'''