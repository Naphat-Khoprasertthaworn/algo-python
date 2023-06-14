import heapq,copy,sys,math
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

ans = 0
def DFS( G,maxE,V,v,n,sumW ):
    global ans
    
    
    
    if v==n-1 and sum(V)==n-1:
        ans = max(ans,sumW)
        V[v] = 0
        return
    elif v==n-1:
        V[v] = 0
        return
    
    g = 0
    for i in range(n):
        if V[i]==0:
            g += maxE[i]
    if sumW + g < ans:
        return
    V[v] = 1
    for i in range(n):
        if i==v or V[i]==1:
            continue
        DFS( G,maxE,V,i,n,sumW + G[v][i] )
    
    V[v] = 0
    
    

n = int(input())

G = [  ]
maxE = [0]*n
for i in range(n):
    l = [int(j) for j in input().split()]
    G.append(l)
    maxE[i] = max(l)
#print(G)
#print(maxE)

V = [0]*n
DFS(G,maxE,V,0,n,0)
print(ans)


'''
4
0 1 -1 2
2 0 1 -3
1 15 0 13
3 -1 5 0

4
0 1 -1 2
2 0 1 -3
1 15 0 13
3 -1 5 0

4
0 1 -1 2
2 0 5 -3
1 15 0 3
3 -1 5 0

'''
