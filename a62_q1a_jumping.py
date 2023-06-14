import math,sys
sys.setrecursionlimit(999999)
def process( lis,n,start,M ):
    
    if start == n:
        return 0
    
    if M[start] == -math.inf:
        
        s1 = -99999999
        s2 = -99999999
        s3 = -99999999
        if start+1 <= n:
            s1 = process( lis,n,start+1,M ) + lis[start]
        if start+2 <= n:
            s2 = process( lis,n,start+2,M )+ lis[start+1]
        if start+3 <= n:
            s3 = process( lis,n,start+3,M )+lis[start+2]
        M[start] = max(s1,s2,s3)
    return M[start]


n = int(input())

lis = [int(i) for i in input().split()]
M = [ -math.inf ]*(n+1)
print( process(lis,n,1,M) + lis[0] )


'''
3
1 1 1
3
1 -1 1

7

1 -1 -1 -1 -1 -1 1

10
-1 -2 -3 -1 -5 -7 6 8 -9 3
'''