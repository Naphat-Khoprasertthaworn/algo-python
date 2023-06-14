import heapq,math
def Prim(G,n):
    
    q = [ (0,0) ]
    D = [math.inf]*n
    V = [0]*n
    nl = 0
    while len(q)!=0 and nl != n:
        
        c,v = heapq.heappop(q)
        V[v] = 1
        if c > D[v]:
            continue
        D[v] = c
        nl += 1
        for i in range(n):
            if V[i]==0 and -(N[v]^N[i]) < D[i]:
                D[i] = -(N[v]^N[i])
                heapq.heappush( q,(-(N[v]^N[i]),i) )
    print(-sum(D))
        
    
    
    
n = int(input())

N = []
for i in range(n):
    b = int(input())
    N.append(b)
G = [ [0]*n for i in range(n) ]


Prim(N,n)
        

'''
4
3
10
9
6


'''