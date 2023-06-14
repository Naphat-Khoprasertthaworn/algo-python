import sys
input = sys.stdin.readline

def process(M,v,w,n,m,ans):
    
    if m<=0:
        return
    
    if m- w[n-1] >=0 and M[n-1][m- w[n-1]] + v[n-1] == M[n][m]:
        ans.append( n )
        process( M,v,w,n-1,m- w[n-1],ans )
    elif M[n-1][m] == M[n][m]:
        process( M,v,w,n-1,m,ans )


n,m = [int(i) for i in input().split()]

v = [int(i) for i in input().split()]

w = [int(i) for i in input().split()]

M = []

for i in range(n+1):
    mlis = [int(i) for i in input().split()]
    M.append(mlis)
    
#print(M)
ans = list()
#process(M,v,w,n,m,ans)

while(m>0 and n>0):
    if m-w[n-1]>=0 and M[n-1][m-w[n-1]] + v[n-1] == M[n][m]:
            ans.append(n)
            m = m-w[n-1]
            n = n-1
            
    else:
        n = n-1

print(len(ans))
print(*ans)



'''
5 5
3 10 6 3 5
5 5 3 1 1
0 0 0 0 0 0
0 0 0 0 0 3
0 0 0 0 0 10
0 0 0 6 6 10
0 3 3 6 9 10
0 5 8 8 11 14

5 3
6 9 5 4 3
2 3 1 1 2
0 0 0 0
0 0 6 6
0 0 6 9
0 5 6 11
0 5 9 11
0 5 9 11

3 5
2 2 4
1 4 5
0 0 0 0 0 0
0 2 2 2 2 2
0 2 2 2 2 4
0 2 2 2 2 4
'''