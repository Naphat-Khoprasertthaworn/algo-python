import heapq,math,sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

def BFS(M,s,K,n):
    V = [0]*n
    q = [s]
    k = 0
    while k<=K:
        newQ = []
        for i in q:
            V[i] = 1
            for j in M[i]:
                if V[j]==0:
                    newQ.append(j)
        q = newQ
        k+=1
    return sum(V)
        
#15:03
N,E,K = [int(i) for i in input().split()]
M = [ [] for i in range(N) ]
for i in range(E):
    a,b = [int(i) for i in input().split()]
    M[a].append(b)
    M[b].append(a)
maxi = 0
for i in range(N):
    maxi = max(maxi,BFS(M,i,K,N))
print(maxi)

'''
7 8 2
0 6
1 6
1 5
1 4
2 3
3 4
4 5
5 6
'''
