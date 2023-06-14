import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

def process( lis,ind,m,M ):
    if ind<0:
        return 0
    if M[ind][m] > 0:
        return M[ind][m]
    
    if lis[ind] <= m:
        M[ind][m] = max( process(lis,ind-1,m,M),process(lis,ind-1,lis[ind],M) + 1 )
        return M[ind][m]
    else:
        M[ind][m] = process(lis,ind-1,m,M)
        return M[ind][m]
    

n = int(input())

lis = [int(i) for i in input().split()]
maxi = max(lis)
M = [ [0]*(maxi+1) for i in range(n) ]

print(process( lis,n-1,maxi,M))
print(M)

'''
5
3 1 4 5 2

13
7 0 10 21 1 6 22 4 3 5 9 8 71
'''
