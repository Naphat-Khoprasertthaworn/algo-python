import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
sys.setrecursionlimit(9999999)

def check(V1,V2,V3,n):
    for i in range(n):
        if V1[i] == 1 and V2[i] == 1 and V3[i] == 1:
            return True
    return False

def BFS(G,t,n):
    V1 = [0]*n
    V2 = [0]*n
    V3 = [0]*n
    q1 = [ t[0] ]
    q2 = [ t[1] ]
    q3 = [ t[2] ]
    c = 0
    while True:
        newQ1 = []
        newQ2 = []
        newQ3 = []
        for i in q1:
            V1[i] = 1
            for j in G[i]:
                if V1[j]==0:
                    newQ1.append(j)
        
        for i in q2:
            V2[i] = 1
            for j in G[i]:
                if V2[j]==0:
                    newQ2.append(j)
                    
        for i in q3:
            V3[i] = 1
            for j in G[i]:
                if V3[j]==0:
                    newQ3.append(j)
        
        if check(V1,V2,V3,n):
            return c
        q1 = newQ1
        q2 = newQ2
        q3 = newQ3
        
        c += 1
        
        
        


n = int(input())

t = [int(i)-1 for i in input().split()]
G = [ [] for i in range(n) ]
for i in range(n):
    l = [int(j) for j in input().split()]
    for k in range(l[0]):
        G[i].append( l[k+1]-1 )
        #G[ l[k+1]-1 ].append(i)

#print(G)
print(BFS(G,t,n))

'''
5
1 3 5
1 2
2 1 3
2 2 4
2 3 5
1 4

10
2 5 10
2 2 4
1 3
1 1
1 5
1 6
1 7
1 8
1 9
1 4
2 8 9
'''