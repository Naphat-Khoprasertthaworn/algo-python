def process( n,m,lis,M ):
    
    if n<0 or m<0:
        return 0
    
    if M[n][m] <= 0:
        s1,s2,s3 = [0,0,0]
        if m-1>=0 and n-1 >=0:
            s1 = process(n-1,m-1,lis,M) + 2*lis[n][m]
        if m-1>=0:
            s2 = process(n,m-1,lis,M) + lis[n][m]
        if n-1>=0:
            s3 = process(n-1,m,lis,M) + lis[n][m]
        
        if m-1<0 and n-1<0:
            M[n][m] = lis[n][m]
        else:
            M[n][m] = max(s1,s2,s3)
    else:
        print("work")
    return M[n][m]


n,m = [int(i) for i in input().split()]

lis = []

for i in range(n):
    mm = [int(i) for i in input().split()]
    lis.append(mm)
    
M = [ [0]*(m) for i in range(n) ]



#print(lis)

print(process(n-1,m-1,lis,M))
#print(M)
'''
3 3
1 1 10
1 7 10
1 10 20

'''