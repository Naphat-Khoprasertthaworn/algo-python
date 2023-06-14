n = int(input())


M = [0]*(n+1)
M[0] = 1
M[1] = 2
M[2] = 4
M[3] = 7
M[4] = 12
for i in range(5,n+1):
    M[i] = ((2*M[i-1]))
            #- M[i-3] + M[i-5] ) % 100000007
    b = True
    for j in range( i-3,-1,-2 ):
        if b:
            M[i] -= M[j]
            b = False
        else:
            M[i] += M[j]
            b = True
#print(M)
print(M[n]% 100000007)