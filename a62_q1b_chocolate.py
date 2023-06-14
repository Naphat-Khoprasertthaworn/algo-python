import sys
sys.setrecursionlimit(99999)


def process( n,lis,M ):
    if n==0:
        return 1
    if n<0:
        return 0
    if M[n] <= 0:
        s = 0
        for i in lis:
            if n-i >= 0:
                s = ( s + process( n-i,lis,M )%1000003 )%1000003
        M[n] = s
    return M[n]

n,m = [int(i) for i in input().split()]

lis = [int(i) for i in input().split()]
M = [0]*(n+1)
print(process(n,lis,M))

'''
4 2

1 3

10 5
1 2 4 6 8

999 5
1 2 4 50 999
'''