n = int(input())
lis = [ int(i) for i in input().split() ]

M = [ [0]*n for i in range(n) ]
for i in range(n):
    
    
    for j in range( n-i ):
        #print( j,j+i )
        if i==0:
            M[j][i+j] = 0
            continue
        else:
            mini = 999999
            for k in range(i):
                newMini = M[j+k+1][i+j] + M[j][j+k] + lis[j]*lis[i+j+1]*lis[j+k+1]
                mini = min(mini,newMini)
            M[j][i+j] = mini
       
    
            
            
print(M[0][n-1])


'''
7
92 32 7 3 29 74 57 93

3
10 10 10 1

7
3 2 1 4 5 6 2 9
'''