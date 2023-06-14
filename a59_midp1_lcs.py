def process(M,x,y,n,m):
    
    if n==0 or m==0:
        return ""
    '''
    if x[n-1]==y[m-1]:
        return process( M,x,y,n-1,m-1 ) + x[n-1]
    else:
        if M[n-1][m] == M[n][m]:
            return process( M,x,y,n-1,m )
        else:
            return process( M,x,y,n,m-1 )
    '''
    if M[n-1][m] == M[n][m]:
        return process( M,x,y,n-1,m )
    elif M[n][m-1] == M[n][m]:
        return process( M,x,y,n,m-1 )
    else:
        return process( M,x,y,n-1,m-1 ) + x[m-1]


n,m = [int(i) for i in input().split()]
sys.setrecursionlimit(n+m)
x = input()
y = input()

M = []

for i in range( n+1 ):
    mm = [ int(i) for i in input().split() ]
    M.append(mm)



#print(M)

print( process(M,x,y,n,m))



'''
4 5
hero
hello
0 0 0 0 0 0
0 1 1 1 1 1
0 1 2 2 2 2
0 1 2 2 2 2
0 1 2 2 2 3

9 9
abczzzdef
defxxxabc
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 1 2 2
0 0 0 0 0 0 0 1 2 3
0 0 0 0 0 0 0 1 2 3
0 0 0 0 0 0 0 1 2 3
0 0 0 0 0 0 0 1 2 3
0 1 1 1 1 1 1 1 2 3
0 1 2 2 2 2 2 2 2 3
0 1 2 3 3 3 3 3 3 3

'''