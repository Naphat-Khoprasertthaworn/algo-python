import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
sys.setrecursionlimit(9999999)


def DFS(M,V,P,v,l,t):
    if t[0]!=0:
        return
    V[v] = l
    for i in M[v]:
        if i==P[v]:
            continue
        elif V[i] == -1:
            P[i] = v
            DFS(M,V,P,i,l+1,t)
            if t[0]!=0:
                return
        elif V[i]!=-1:
            t[0] = l-V[i] + 1
            return
    
    
e = int(input())

M = [ [] for i in range(e) ]

for i in range(e):
    a,b = [int(i) for i in input().split()]
    M[a].append(b)
    M[b].append(a)
    
V = [-1]*e
t = [0]
P = [0]*e
DFS(M,V,P,0,0,t)
print(*t)