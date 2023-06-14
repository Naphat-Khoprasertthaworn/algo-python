import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
sys.setrecursionlimit(200000)

n,m = [int(i) for i in input().split()]

M = []*n

for i in range(n):
    if m==0:
        continue
    mini = str(input().strip())
    M.append( [int(j) for j in mini] )

MM = [ [0]*(m+1) for i in range(n+1) ]

maxi = 0
for i in range(1,n+1):
    
    for j in range(1,m+1):
        '''
        if MM[i-1][j-1] == MM[i-1][j] and MM[i-1][j-1] == MM[i][j-1] and M[i-1][j-1] == 1:
            
            MM[i][j] = MM[i-1][j-1]+1
            if MM[i][j] > maxi:
                maxi = MM[i][j]
        elif M[i-1][j-1] == 1:
            MM[i][j] = max( MM[i-1][j-1],MM[i][j-1],MM[i-1][j] )
        else:
            MM[i][j] = 0
        '''
        if M[i-1][j-1]==0:
            MM[i][j] = 0
        else:
            MM[i][j] = min( MM[i-1][j-1],MM[i][j-1],MM[i-1][j] )+1
        maxi = max(maxi,MM[i][j])

print(maxi)

#print(MM)
'''
5 5
00010
01111
00111
00111
00111

5 5
00010
01111
00110
00110
00000

1 10
1111111011

7 5
11110
11110
11110
11110
01111
01111
01111


'''