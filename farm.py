import heapq,math,copy

def check(G,F,V,n,m):
    newF = copy.deepcopy(F)
    s = 0
    for i in range(n):
        if V[i]==1:
            for j in G[i]:
                if (i,j) in newF.keys() and newF[(i,j)] == 0:
                    newF[(i,j)] = 1
                    s += 1
                elif (j,i) in newF.keys() and newF[(j,i)] == 0:
                    newF[(j,i)] = 1
                    s += 1
    return s==m
       
def process( G,n,F,m,v,V,sumV ):
    global ans
    if sumV>ans:
        return
    if check(G,F,V,n,m):
        ans = min(ans,sum(V))
        return
    if v==n:
        return
    V[v] = 1
    process( G,n,F,m,v+1,V,sumV+1 )
    V[v] = 0
    process( G,n,F,m,v+1,V,sumV )
    
    
    
    
T = int(input())

for _ in range(T):
    ans = math.inf  
    n,m = [int(i) for i in input().split()]

    G = [ [] for i in range(n) ]
    F  = {}
    for _ in range(m):
        a,b = [int(i) for i in input().split()]
        G[a].append(b)
        G[b].append(a)
        F[ (a,b) ] = 0
    V = [0]*n
    process(G,n,F,m,0,V,0)
    print(ans)

'''
3 3
1 2
1 0
2 0

4 3
1 2
1 3
1 0

5 6
0 2
0 3
1 3
1 2
1 4
2 4

5 8
0 1
0 3
0 4
1 2
1 4
3 4
3 2
2 4

4 2
0 1
2 3

6 9
0 4
4 3
1 2
2 0
2 3
5 3
4 1
4 2
5 0

17 7
12 9
11 8
9 16
11 2
5 14
7 6
8 14

16 23
10 13
11 3
7 14
14 3
9 11
7 8
0 9
8 14
10 8
0 4
6 15
6 12
2 5
10 2
7 11
13 12
15 13
5 3
15 0
6 2
12 9
5 1
1 4

'''
