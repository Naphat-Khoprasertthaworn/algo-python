n = int(input())


def DFS( M,V,T,t,v ):
    V[v] = 1
    
    for i in M[v]:
        if V[i]==0:
            DFS(M,V,T,t,i)
    
    T[v] = t[0]
    t[0] += 1

#M = [ [] for i in range(n) ]
M = []
for i in range(n):
    lis = [int(i) for i in input().split()]
    lis.pop(0)
    '''
    for j in lis:
        M[j].append(i)
    '''
    M.append(lis)
        
V = [0]*n
T = [0]*n
t = [0]
for i in range(n):
    if V[i]==0:
        DFS(M,V,T,t,i)
#print(M)
#print(T)
newT = []
for i in range(len(T)):
    newT.append( (T[i],i) )
newT.sort()
#newT.reverse()
#print(newT)
for i in range(n):
    print(newT[i][1],end=" ")




'''
4
1 1
2 3 2
0
0

4
0
0
0
0
'''