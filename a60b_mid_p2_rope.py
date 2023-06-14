import sys
sys.setrecursionlimit(999999)

def process(lis,n,M):
    if n == 0:
        return 0 
    if M[n]>0:
        return M[n]
    elif M[n]==-1:
        return -1
    
    else:
        maxi = 0
        for i in lis:
            if n-i>=0:
                maxi = max( process(lis,n-i,M)+1 ,maxi )

        if maxi==0:
            M[n] = -1
            return -1
        else:
            M[n] = maxi
            return M[n]
        

n,a,b,c = [int(i) for i in input().split()]

lis = [a,b,c]

M = [0]*(n+1)

print(process(lis,n,M))
#print(M)