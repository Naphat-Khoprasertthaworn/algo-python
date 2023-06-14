#14:20
import heapq,math,sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")


n,m,k = [int(i) for i in input().split()]

gotAtk = [int(i) for i in input().split()]

time = [int(i) for i in input().split()]

M = [ [] for i in range(n) ]

for i in range(m):
    a,b = [int(i) for i in input().split()]
    M[a].append(b)
    M[b].append(a)
    
q = [  ]
for i in gotAtk:
    q.append( (time[i],i) )

heapq.heapify(q)

V = [0]*n
D = [math.inf]*n
nl = 0
while len(q)!=0 and nl != n:
    u = heapq.heappop(q)
    V[u[1]] = 1
    D[u[1]] = u[0]
    nl += 1
    for i in M[u[1]]:
        if V[i]==0:
            if D[i] > u[0]+time[i]:
                D[i] = u[0]+time[i]
                heapq.heappush(q,(D[i],i))

print(max(D))

'''
3 2 1
1
3 5 1
0 1
1 2

4 4 1
0
2 5 3 1
0 1
0 2
1 3
2 3

4 3 2
0 3
4 3 2 1
0 1
1 2
2 3
'''
    
    