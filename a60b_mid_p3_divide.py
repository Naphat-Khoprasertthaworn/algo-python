



n , k = [int(i) for i in input().split()]
M = [[0]*(n+1) for i in range(k+1) ]
'''
for i in range(1,n+1):
    if i<k:
        M[i] = 0
    elif i==k or ( k==1 and i>0 ):
        M[i] = 1
    else:
        M[i] =  (M[i-1]*k)
'''
for i in range(1,k+1):
    
    for j in range(1,n+1):
        if j < i:
            M[i][j] = 0
        elif i==j or (i==1 and j>0):
            M[i][j] = 1
        else:
            M[i][j] = M[i][j-1]*i + M[i-1][j-1]
            
print(M[k][n])

