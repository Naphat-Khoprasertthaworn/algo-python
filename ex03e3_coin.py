
def process( M,m,lis ):
    if m <= 0:
        return 0
    
    if M[m] <= 0:
        s = 999999
        for i in lis:
            if m-i < 0:
                continue
            s = min(s,process( M,m-i,lis )+1)
        M[m] = s
    
    return M[m]

n,m = [int(i) for i in input().split()]

lis = [int(i) for i in input().split()]

M = [0]*(m+1)

print( process(M,m,lis) )
'''

3 13
5 4 1

4 28
10 5 2 1
'''