import heapq,math,sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+" ")

n,m,k = [int(i) for i in input().split()]

begin = int(input())

end = [int(i) for i in input().split()]
M = [ [] for i in range(n) ]
for i in range(m):
    a,b,w = [int(i) for i in input().split()]
    M[b].append( (w,a) )

D = [math.inf]*n
q = [ (0,begin) ]
V = [0]*n
heapq.heapify(q)
s = 0
while True:
    if s==n or len(q)==0:
        break
    
    u = heapq.heappop(q)
    D[ u[1] ] = u[0]
    V[ u[1] ] = 1
    s+=1
    for i in M[u[1]]:
        if D[i[1]] > u[0] + i[0] and V[i[1]]==0:
            D[i[1]] = u[0] + i[0]
            heapq.heappush( q,(D[i[1]],i[1]) )

#print(M)
#print(D)
mini = math.inf
for i in end:
    mini = min(mini,D[i])
print(mini)

'''
5 4 2
4
0 1
0 1 1
1 2 1
2 4 1
3 4 2

6 6 4
5
4 3 0 1
0 1 10
1 2 5
1 3 7
2 5 -4
3 2 2
1 4 8
'''