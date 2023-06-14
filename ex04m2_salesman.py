import copy,heapq,math,sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

def path( a,b,sumA,P ):
    f = abs(P[a]-P[b])
    return min( f,sumA-f )

N,M = [ int(i) for i in input().split() ]

order = [ int(i) for i in input().split() ]

pp = [ int(i) for i in input().split() ]
sumA = 0
P = [0]*M
for i in range(M):
    P[i] = sumA
    sumA += pp[i]
#print(P)


for _ in range(N):
    a,b = [int(i) for i in input().split()]
    minPath = 0
    for i in range(M):
        p1 = path( order[i],order[(i+1)%M],sumA,P )
        p2 = path( order[i],a,sumA,P ) + path( b,order[(i+1)%M],sumA,P )
        p3 = path( order[i],b,sumA,P ) + path( a,order[(i+1)%M],sumA,P )
        minPath += min(p1,p2,p3)
    print(minPath)


    
'''
1 4
0 1 2 3
5 3 3 3
0 1

2 4
0 2 1 3
5 6 7 3
0 1
2 3
'''
    