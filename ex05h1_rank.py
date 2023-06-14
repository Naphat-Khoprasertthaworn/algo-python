from collections import deque
import copy,sys,gc
input = sys.stdin.readline
sys.setrecursionlimit(999999999)

def DFS( M,V,v,st ):
    V[v] = 1
    for i in M[v]:
        if V[i]==0:
            DFS( M,V,i,st )
    st.append(v)

def newGraph( M,st,n ):
    V = [0]*n
    group = [0]*n
    num = 0
    while len(st) != 0:
        i = st.pop()
        if V[i]==0:
            g = []
            DFSgroup(M,V,i,g)
            for i in g:
                group[i] = num
            num += 1
    
    newM = [ [] for i in range(num) ]
    newMT = [ [] for i in range(num) ]
    for i in range(n):
        for j in M[i]:
            if group[j] not in newM[ group[i] ]:
                newM[ group[i] ].append( group[j] )
            if group[i] not in newM[ group[j] ]:
                newMT[ group[j] ].append( group[i] )
                
    return newM,newMT,group,num
        
def DFSgroup(M,V,v,g):
    V[v] = 1
    g.append(v)
    for i in M[v]:
        if V[i]==0:
            DFSgroup(M,V,i,g)

def DP(M,v,gOrder):
    if len(M[v])==0:
        gOrder[v] = 1
        return
    
    for i in M[v]:
        if gOrder[i] == -1:
            DP(M,i,gOrder)
    maxR = -1
    for i in M[v]:
        maxR = max(maxR,gOrder[i])
    gOrder[v] = maxR + 1

n,e = [int(i) for i in input().split()]

M = [ [] for i in range(n) ]
MT = [ [] for i in range(n) ]
for i in range(e):
    a,b = [int(i) for i in input().split()]
    M[a].append(b)
    MT[b].append(a)
    
st = deque()
V = [0]*n
for i in range(n):
    if V[i]==0:
        DFS( MT,V,i,st )

newM,newMT,group,num = newGraph(M,st,n)
del st
del MT
del M
gc.collect()
newSt = deque()
V = [0]*num
for i in range(num):
    if V[i]==0:
        DFS( newM,V,i,newSt )


gOrder = [-1]*num
while len(newSt)!=0:
    i = newSt.pop()
    if gOrder[i]==-1:
        DP(newMT,i,gOrder)

outputList = [0]*max(gOrder)
for i in range(max(gOrder)):
    for j in range(len(gOrder)):
        if gOrder[j]-1==i:
            outputList[i] += group.count(j)

print(*outputList)

'''
6 7
0 1
1 2
2 0
2 3
1 3
4 1
5 3

4 3
0 1
1 2
2 3

10 2
5 6
0 1
'''