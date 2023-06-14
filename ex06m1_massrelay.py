import sys,heapq
input = sys.stdin.readline
#print = lambda s:sys.stdout.write(str(s)+"\n")

def findSet(e,P):
    if P[e]==e:
        return e
    return findSet(P[e],P)

def unionSet(s,t,P,H):
    if H[s] > H[t]:
        P[t] = s
    else:
        P[s] = t
        if H[s] == H[t]:
            H[t] += 1


N,E,Q = [int(i) for i in input().split()]

listE = []
heapq.heapify(listE)
for i in range(E):
    a,b,r = [int(i) for i in input().split()]
    heapq.heappush( listE,(r,a,b) )
#print(listE)


P = [int(i) for i in range(N)]
H = [0]*N
pN = N
i = 0
Plist = list(listE)
edgeList = []
while True:
    if pN==1:
        break
    p = heapq.heappop(Plist)
    s1 = findSet(p[1],P)
    s2 = findSet(p[2],P)
    if s1 != s2:
        edgeList.append(p)
        unionSet( s1,s2,P,H )
        pN -= 1

for QQ in range(Q):
    comnum = int(input())
    print(edgeList[-comnum][0])



'''
5 6 4
0 1 20
0 2 10
2 3 30
1 3 10
2 4 40
3 4 50
1
2
3
4
'''