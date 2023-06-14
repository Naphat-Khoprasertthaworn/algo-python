import math
def DFS( G,v,C ):
    global n
    D = [ 0 ]*n
    for i in G[v]:
        if C[i]==-1:
            continue
        D[C[i]] = 1
    
    for i in range(n):
        if D[i]==0:
            C[v] = i
            break
    
    for i in G[v]:
        if C[i] == -1:
            DFS( G,i,C )
    

n,e = [int(i) for i in input().split()]
G = [ [] for i in range(n) ]
for _ in range(e):
    a,b = [int(i) for i in input().split()]
    G[a].append(b)
    G[b].append(a)
ans = math.inf
for i in range(n):
    C = [-1]*n
    for j in range(n):
        DFS(G,(j+i)%n,C)
    ans = min( ans,max(C) )
#print(C)
print(ans+1)
'''
4 6
0 1
0 2
0 3
1 2
1 3
2 3

4 5
0 1
0 3
1 2
1 3
2 3

5 10
0 1
0 2
0 3
0 4
1 2
1 3
1 4
2 3
2 4
3 4

5 7
0 1
0 2
0 3
1 4
1 3
2 3
3 4

4 4
0 1
0 2
1 3
2 3

3 3
0 1
0 2
1 2


4 5
0 1
0 3
1 3
1 2
2 3

5 7
0 1
0 2
0 4
1 2
1 3
2 3
3 4

4 3
0 1
1 2
1 3


'''