

def mcm(l,r,lis,M):
    
    if r-l==1:
        return 0
    
    if M[l][r]==0:
        
        mini = 9999999
        for i in range(l+1,r):
            newMini = lis[l]*lis[r]*lis[i] + mcm(l,i,lis,M) + mcm(i,r,lis,M)
            mini = min(mini,newMini)
        M[l][r] = mini
    return M[l][r]

n = int(input())

lis = [ int(i) for i in input().split() ]

M = [[0]*(n+1) for i in range(n+1)]

print(mcm(0,n,lis,M))
print(M)


'''
7
92 32 7 3 29 74 57 93

3
10 10 10 1

7
3 2 1 4 5 6 2 9
'''
        