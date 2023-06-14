#14:12
def hasCycle(M,n):
    V = [0]*n
    b = [True]
    for i in range(n):
        if V[i]==0:
            DFS(M,i,V,b,i)
            if b[0] == False:
                return True
    return False

def DFS(M,v,V,b,f):
    V[v] = 1
    if b[0]==False:
        return
    for i in M[v]:
        if V[i]==0:
            DFS(M,i,V,b,v)
        elif V[i]==1 and i!= f:
            b[0]=False
    

N = int(input())
for nn in range(N):
    v,e = [int(i) for i in input().split()]
    M = [ [] for i in range(v) ]
    for i in range(e):
        a,b = [int(i) for i in input().split()]
        M[a].append(b)
        M[b].append(a)
        
    b = hasCycle( M,v )
    if b==True:
        print("YES")
    else:
        print("NO")
        
'''
4
4 0
4 4
2 3
0 1
1 2
2 0
4 3
0 1
1 2
2 0
4 1
1 3
'''