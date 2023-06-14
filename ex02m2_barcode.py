import sys
sys.setrecursionlimit(4000)

def process( M,n,k,consec,maxConsec ):
    if n==0 or k==0:
        return 0
    if n==k:
        M[k][n] = 1
    
    if M[k][n] <=0:

        if n>k*maxConsec:
            M[k][n] = 0
        else:
            M[k][n] = process( M,n-1,k,consec+1,maxConsec ) + process( M,n-1,k-1,0,maxConsec ) 
            if n >= maxConsec + k:
                #print(n,maxConsec + k)
                M[k][n] -= M[k-1][k-1 + (n-(maxConsec + k)) ]
            
            
    return M[k][n]
    

    

n,m,k = [int(i) for i in input().split()]
k+=1
M = [ [0]*(n+1) for i in range(k+1)]
print(process( M,n,k,0,m ))
'''
for i in range(1,n+1):
    for j in range(1,k+1):
        process( M,i,j,0,m )
'''
print(M)