
def BMF(M,n):
    
    D = [0]*n
    D[0] = 1
    for I in range(n):
        flag = False
        for j in range(n):
            for k in range(n):
                if k==j:
                    continue
                if D[k] < D[j]*M[j][k]:
                    D[k] = D[j]*M[j][k]
                    flag = True
        if flag==False:
            return True
        print(D)
        
    for j in range(n):
        for k in range(n):
            if k==j:
                continue
            if D[k] < D[j]*M[j][k]:
                return False
    return True

N = int(input())

for NNN in range(N):
    n = int(input())
    M = [ [0]*n for i in range(n)]
    
    for i in range(n):
        l = [float(j) for j in input().split()]
        for j in range(n):
            M[i][j] = l[j]
    
    b = BMF(M,n)
    if b:
        print("NO")
    else:
        print("YES")
            
    
    #print(M)
    
    
'''
2
3
1 0.7 1.2
1.1 1 2
0.75 0.7 1
2
1 0.7
1.2 1

1
3
1 0.9 0.6
1.1 1 0.6
1.5 1.51 1
'''