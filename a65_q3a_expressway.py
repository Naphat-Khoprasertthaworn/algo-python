import sys,heapq,math
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+" ")
sys.setrecursionlimit(9999999)
def DKJ(G,n):
    
    D = [ math.inf ]*n
    D[0] = 0
    q = [ (0,0) ]
    nl = 0
    while len(q)!=0 and nl != n:
        
        c,v = heapq.heappop(q)
        
        if c > D[v]:
            continue
        if v==1:
            return D[1]
        nl += 1
        
        
        for wi,i in G[v]:
            #print(i)
            if c+wi < D[i]:
                D[i] = c+wi
                heapq.heappush( q,(D[i],i) )
        
        
    

n,e = [int(i) for i in input().split()]

G = [ [] for i in range(n)  ]
G[0].append( (e,1) )
G[1].append( (e,0) )

for y in range(2,n):
    l = [int(i) for i in input().split()]
    
    for i in range(l[0]):
        a,c = l[ 2*i+1 ] , l[ 2*i+2 ]
        G[y].append( (c,a-1) )
        G[a-1].append( (c,y) )
    #print(G)
    print(DKJ(G,n))
    
'''
5 10
2 1 6 2 7
3 1 1 3 1 2 9
2 1 2 2 5
'''
