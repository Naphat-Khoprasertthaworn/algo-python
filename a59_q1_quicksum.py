#def sum(M,r1,c1,r2,c2):
import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")


r,c,m = [int(i) for i in input().split()]

M = []

for i in range(r):
    l = [int(j) for j in input().split()]
    M.append(l)
    
newM = [ [0]*(c+1) for i in range(r+1) ]
    
#print(M)

for i in range(1,r+1):
    
    for j in range(1,c+1):
        newM[i][j] = newM[i-1][j] + newM[i][j-1] - newM[i-1][j-1] + M[i-1][j-1]


for i in range(m):
    r1,c1,r2,c2 = [int(i) for i in input().split()]
    
    print( newM[r2+1][c2+1] - newM[r2+1][c1] - newM[r1][c2+1] + newM[r1][c1] )
#print(newM)



'''
3 5 7
1 2 3 4 5
6 6 6 6 6
7 7 3 1 1
0 0 0 0
0 0 1 1
1 1 2 1
1 1 2 3
1 0 2 2
0 1 2 2
0 0 2 4
'''