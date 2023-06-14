import math
def minIndex(V,inH):
    mini = math.inf
    i = 0
    for j in range(n):
        if inH[j]==1:
            continue
        if V[j]<mini:
            mini = V[j]
            i = j
    return i

n = int(input())
M = [ [0]*n for i in range(n) ]
for i in range(n-1):
    l = [int(j) for j in input().split()]
    for k in range(len(l)):
        M[i][i+1+k] = l[k]
        M[i+1+k][i] = l[k]
        

V = [ math.inf ]*n
inH = [0]*n
V[0] = 0
for i in range(n):
    u = minIndex(V,inH)
    inH[u] = 1
    for j in range(n):
        if inH[j]==0:
            if V[j] == -1:
                V[j] = M[u][j]
            else:
                V[j] = min(V[j],M[u][j])
    #print(V)
                
#print(V)
print(sum(V))
                
    

'''
4
1 3 4
2 7
6

5
4 3 6 7
4 2 5
6 5
7
'''