n,m,k = [int(i) for i in input().split()]

lis = []
for i in range(n):
    inp = [int(i) for i in input().split()]
    lis.append(inp)

newLis = [ [0]*(m+1) for i in range(n+1) ]

for i in range(1,n+1):
    
    for j in range(1,m+1):
        newLis[i][j] = lis[i-1][j-1] + newLis[i-1][j] + newLis[i][j-1] - newLis[i-1][j-1]

print(newLis)
for i in range(k):
    r1,c1,r2,c2 = [int(i) for i in input().split()]
    r1+=1
    c1+=1
    r2+=1
    c2+=1
    print( newLis[r2][c2] - newLis[r2][c1-1] - newLis[r1-1][c2] + newLis[r1-1][c1-1] )
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