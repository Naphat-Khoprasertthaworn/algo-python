import math
import sys
import heapq
input = sys.stdin.readline

#print = lambda s:sys.stdout.write(str(s)+"\n")



r,c = [int(t) for t in input().split()]

M = [  ]

for i in range(r):
    st = [int(j) for j in input().split()]
    M.append(st)

V = [ [0]*c for i in range(r) ]
D = [ [0]*c for i in range(r) ]
queue = [ ]
heapq.heapify(queue)
heapq.heappush(queue,(0,0,0))

s = 0
while True:
    if s == r*c:
        break
    u,ix,iy = heapq.heappop(queue)
    if V[ix][iy]==1:
        continue
    
    V[ix][iy] = 1
    D[ix][iy] = u
    s+=1
    if ix<r-1 and V[ix+1][iy] == 0:
        heapq.heappush( queue,(u+M[ix+1][iy],ix+1,iy) )
    if iy<c-1 and V[ix][iy+1] == 0:
        heapq.heappush( queue,(u+M[ix][iy+1],ix,iy+1) )
    if ix>0 and V[ix-1][iy] == 0:
        heapq.heappush( queue,(u+M[ix-1][iy],ix-1,iy) )
    if iy>0 and V[ix][iy-1] == 0:
        heapq.heappush( queue,(u+M[ix][iy-1],ix,iy-1) )
#print(queue)
for i in range(r):
    print(*D[i])
#print(D)

    
'''
4 4
1 1 1 1
9 8 7 1
1 1 1 1
1 2 4 9
'''
        