
def DFSinit(M,n):
    V = [0]*n
    c = 0
    for i in range(n):
        if V[i]==0:
            DFS(M,V,i)
            c+=1
    return c
            
def DFS(M,V,v):
    V[v] = 1
    for i in M[v]:
        if V[i]==0:
            DFS(M,V,i)
    
    
    
v,e = [int(i) for i in input().split()]

M = [ [] for i in range(v) ]

for i in range(e):
    a,b = [int(i)-1 for i in input().split()]
    M[a].append(b)
    M[b].append(a)

print(DFSinit(M,v))



    
'''
4 3
1 2
2 3
3 1

10 7
1 2
2 3
3 4
1 3
2 4
5 6
6 7

5 1
1 2

5 2
1 2
4 5


'''
            

    