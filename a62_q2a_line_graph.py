#15:48

def DFSinit(M,n):
    V = [0]*n
    c = 0
    for i in range(n):
        b = [True]
        if V[i]==0:
            DFS(M,V,i,b,i)
            if b[0]==True:
                c+=1
    return c
            
def DFS(M,V,v,b,p):
    V[v]=1
    if len(M[v])>2:
        b[0] = False
    for i in M[v]:
        if V[i]==0:
            DFS(M,V,i,b,v)
        elif V[i]==1 and i != p:
            b[0] = False
        

v,e = [int(i) for i in input().split()]

M = [ [] for i in range(v) ]
for i in range(e):
    a,b = [int(i) for i in input().split()]
    M[a].append(b)
    M[b].append(a)
    
print(DFSinit(M,v))


'''
4 3
0 1
2 1
1 3

3 3
0 1
1 2
2 0

3 2
0 1
0 2

3 2
1 0
0 2

5 4
0 1
2 3
3 4
4 2

6 2
1 2
3 4

4 6
0 1
0 2
0 3
1 2
1 3
2 3

'''
