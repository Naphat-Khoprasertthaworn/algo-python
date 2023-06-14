import math
n,e,K = [int(i) for i in input().split()]
n+=1
M = [ [] for i in range(n) ]

for i in range(e):
    a,b = [int(i) for i in input().split()]
    M[a].append(b)
    M[b].append(a)
q = [0]
k = 0
V = [math.inf]*n
while k<=K:
    newQ = []
    for i in q:
        if V[i] != math.inf:
            continue
        V[i]=k
        for j in M[i]:
            newQ.append(j)
    
    q = newQ
    k += 1
c = 0
for i in V:
    if K==i:
        c+=1
print(c)
    
'''
3 4 1
0 1
1 2
1 3
0 3

3 4 2
0 1
1 2
2 3
1 3



'''