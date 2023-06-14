import sys
from collections import deque
input = sys.stdin.readline
#print = lambda s:sys.stdout.write(str(s)+" ")
sys.setrecursionlimit(999999)

def DFSInit( M,n ):
    V = [0]*n
    st = deque()
    for i in range(n):
        if V[i]==0:
            DFS(M,V,i,st)
    return st

def DFS( M,V,v,st ):
    V[v] = 1
    for i in M[v]:
        if V[i]==0:
            DFS(M,V,i,st)
    st.append(v)
    
def DFSforCount(M,n,st):
    V = [0]*n
    c = []
    while len(st) != 0:
        i = st.pop()
        t = [0]
        if V[i]==0:
            DFScount(M,V,i,t)
            c.append(t[0])
    c.sort()
    return c
        
def DFScount(M,V,v,t):
    V[v] = 1
    t[0] += 1
    for i in M[v]:
        if V[i]==0:
            DFScount(M,V,i,t)
    
n = int(input())
M = [ [] for i in range(n) ]
MT = [ [] for i in range(n) ]
for i in range(n):
    l = [int(i) for i in input().split()]
    for j in range(1,len(l)):
        M[i].append( l[j] )
        MT[l[j]].append(i)
#print(M)
st = DFSInit(MT,n)

#print(st)

lis = DFSforCount(M,n,st)
print(*lis)



'''
3
1 1
1 2
1 0

5
2 1 2
2 0 3
1 3
1 2
0

5
2 1 2
2 0 3
1 3 1
1 2
0

3
1 1
1 0
0
'''