#09:00
import sys,heapq,math
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
sys.setrecursionlimit(9999999)

def greedy( G,V,v,n ):
    s = 0
    newV = list(V)
    while True:
        maxi = 0
        idx = -1
        for nv,c in G[v]:
            if c > maxi and newV[nv]==0:
                maxi = c
                idx = nv
        if idx!=-1:
            newV[idx]=1
            s += maxi
        else:
            break
        v = idx
    return s

def DFS( G,V,v,sumW,ask,n ):
    if sumW>ask:
        return False
    g = greedy(G,V,v,n)
    if sumW+g < ask:
        return False
    V[v] = 1
    if sumW==ask:
        return True
    for nv,c in G[v]:
        if V[nv]==0:
            if DFS( G,V,nv,sumW+c,ask,n ):
                return True
    V[v] = 0
    return False


n,m = [ int(i) for i in input().split() ]

ASK = [ int(i) for i in input().split() ]

G = [ [] for i in range(n) ]

for i in range(m):
    a,b,c = [int(j) for j in input().split()]
    G[a].append((b,c))
    G[b].append((a,c))
    
for ask in ASK:
    f = False
    for i in range(n):
        V = [0]*n
        if DFS(G,V,i,0,ask,n):
            f = True
            break
    if f:
        print("YES")
    else:
        print("NO")


'''
4 4
10 20 30 40 50 60 70 80
0 1 10
0 2 15
1 2 5
0 3 35



4 4
50
0 1 10
0 2 15
1 2 5
0 3 35

4 5
65
0 1 10
0 2 15
1 2 5
0 3 35
2 3 5

4 4
50
0 1 10
0 2 15
1 2 5
0 3 35
'''