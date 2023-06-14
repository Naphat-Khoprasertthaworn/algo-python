import sys
sys.setrecursionlimit(999999999)

def TD( n1,n2,M ):
    #print(n1,n2)
    
    if M[n1][n2] == 0:
        
        if n1<=0 and n2<=0:
            return 1
        elif n1<=0:
            s = TD( n1-1,n2-2,M ) + TD( n1-1,n2-1,M )
        elif n2<=0:
            s = TD( n1-2,n2-1,M ) + TD( n1-1,n2-1,M )
        else: 
            s = TD( n1-2,n2-1,M ) + TD( n1-1,n2-2,M ) + TD( n1-1,n2-1,M )
        M[n1][n2] = s%100000007
        M[n2][n1] = M[n1][n2]
    return M[n1][n2]

n = int(input())

M = [ [0]*(n+1) for i in range(n+1) ]

print(TD(n,n,M))
print(M)

