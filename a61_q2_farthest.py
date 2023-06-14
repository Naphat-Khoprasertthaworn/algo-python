#9:57
import math
import sys
import heapq
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

def findMinIndex(D,n,V):
    mini = math.inf
    idx = 0
    for j in range(n):
        if D[j] < mini and V[j] == 0:
            mini = D[j]
            idx = j
    return idx
            
n = int(input())

M = []

for i in range(n):
    st = [int(i) for i in input().split()]
    M.append(st)

V = [0]*n
D = [math.inf]*n
D[0] = 0
s = 0
while True:
    if sum(V) == len(V) or s==n:
        break
    idx = findMinIndex(D,n,V)
    V[idx] = 1
    s += 1
    for i in range(len(M[idx])):
        if M[idx][i] > 0:
            D[i] = min(D[idx] + M[idx][i],D[i])
    #print(D)
if max(D)==math.inf:
    print(-1)
else:
    print(max(D))


'''
5
0 1 -1 -1 7
-1 0 2 3 5
-1 -1 0 4 -1
-1 4 2 0 -1
-1 -1 -1 4 0
'''