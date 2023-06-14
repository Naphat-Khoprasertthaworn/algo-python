import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

n,m = [int(i) for i in input().split()]

lis = []
for i in range(n):
    line = [int(i) for i in input().split()]
    lis.append(line)
    
M = [ [ 0 ]*(m+1) for i in range(n+1) ]

for i in range( 1,n+1 ):
    for j in range( 1,m+1 ):
        if i==1 and j==1:
            M[i][j] = lis[i-1][j-1]
        elif i==1:
            M[i][j] = M[i][j-1] + lis[i-1][j-1]
        elif j==1:
            M[i][j] = M[i-1][j] + lis[i-1][j-1]
        else:
            M[i][j] = max(M[i-1][j-1] + 2*lis[i-1][j-1] , M[i][j-1] + lis[i-1][j-1] , M[i-1][j] + lis[i-1][j-1])
print(M[n][m])

'''
3 3
1 1 10
1 7 10
1 10 20

3 3
1 1 10
1 7 10
1 9 7
'''