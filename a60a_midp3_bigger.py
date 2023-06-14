
def process( lis,M,n ):
    if n<0:
        return 0
    if M[n]<=0:
        M[n] = max( process( lis,M,n-3 )+lis[n] , process( lis,M,n-1 ) )
    return M[n]

n = int(input())

lis = [int(i) for i in input().split()]

M = [0]*n

print(process( lis,M,n-1 ))
#print(M)

'''
10
48 1 3 95 2 1 3 44 22 2
'''