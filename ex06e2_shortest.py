import math
import sys
import heapq
input = sys.stdin.readline
#print = lambda s:sys.stdout.write(str(s)+"\n")
N,E,s = [int(i) for i in input().split()]

M = [ []*N for i in range(N) ]

for i in range(E):
    a,b,w = [int(i) for i in input().split()]
    M[a].append( (w,b) )
    #M[b].append( (w,a) )
    
D = [ math.inf ]*N
D[s] = 0

order = []
queue = [s]
V = [0]*N
while True:
    if len(queue)==0:
        break
    p = queue.pop(0)
    V[p] = 1
    order.append(p)
    for i in M[p]:
        if V[i[1]]==0:
            queue.append(i[1])
#print(order)

D = [math.inf]*N
D[s] = 0
for i in range(1,N):
    f = False
    for j in order:
        for k in M[j]:
            if D[j] + k[0] < D[k[1]]:
                f = True
                D[k[1]] = D[j] + k[0]
    if f== False:
        break

    #print(D)

nc = False
for j in order:
    for k in M[j]:
        if D[j] + k[0] < D[k[1]]:
            nc = True
            print(-1)
            break
    if nc==True:
        break
if nc == False:
    print(*D)

'''
4 3 0
0 1 -1
1 2 1
2 3 4

4 4 0
0 1 -1
1 2 -1
2 3 -1
3 1 -1
'''
    
    