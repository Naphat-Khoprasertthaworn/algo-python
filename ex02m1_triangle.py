import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
n = int(input())
lis = []
for i in range(n):
    m = [int(i) for i in input().split()]
    lis.append(m)

M = [ [0]*n for i in range(n) ]
maxi = 0
for i in range(n):
    for j in range(i+1):
        if i==0 and  j == 0:
            M[i][j] = lis[i][j]
        else:
            M[i][j] = max(M[i-1][j] ,M[i-1][max(j-1,0)]) + lis[i][j]
        maxi = max(M[i][j],maxi)
            
print(maxi)

'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''