import math
import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
n = int(input())

M = []

for i in range(n):
    m = [int(i) for i in input().split()]
    M.append(m)
sumM = [ [0]*(n+1) for i in range(n+1) ]
for i in range(1,n+1):
    for j in range(1,n+1):
        numS = min(i,j)
        sum = 0
        for k in range(numS):
            sum += M[i-k-1][j-k-1]
        sumM[i][j] = sum

maxi = -math.inf
for i in range(1,n+1):
    for j in range(1,n+1):
        numS = min(i,j)
        dif = 0
        for k in range(numS):
            dif = sumM[i][j] - sumM[i-1-k][j-1-k]
            maxi = max( dif,maxi )

print(maxi)

#maxi = -inf


#print(sumM)

'''
2
1 2
3 4

4
-1 -1 -1 -1
-1 -1 -1 -1
-1 -1 -1 -1
-1 -1 -1 -1

4
1 2 3 4
-2 -5 2 -5
6 3 -7 1
3 -2 7 -9
'''