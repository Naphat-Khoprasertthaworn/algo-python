
def mcm(l,r,lis,M):
    
    
    if r-l==1:
        return 0
    
    mini = 9999999
    for i in range(l+1,r-1):
        newMini = lis[l]*lis[r]*lis[i] + mcm(l,i,lis,M) + mcm(i,r,lis,M)
        mini = min(mini,newMini)
    return mini

n = int(input())

lis = [ int(i) for i in input().split() ]

M = [0]*n

print(mcm(0,n,lis,M))


'''

8
-1 -2 -2 -2 -2 -2 -2 -1
15
1 2 -1 5 3 -8 -2 4 3 -4 -5 7 -1 -2 4

'''