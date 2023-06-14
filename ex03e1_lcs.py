import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
'''
def lcs(x,y,i,j):
    if i<0 or j<0:
        return 0
    
    if x[i] == y[j]:
        return lcs(x,y,i-1,j-1) + 1
    else:
        return max(lcs(x,y,i-1,j) , lcs(x,y,i,j-1))
'''


    
    
x = str(input().strip())
y = str(input().strip())
x = " "+x
y = " "+y

M = [ [0]*len(y) for i in range(len(x)) ]
#print(M)

for i in range(1,len(x)):
    for j in range(1,len(y)):
        if x[i]==y[j]:
            M[i][j] = M[i-1][j-1] + 1
        else:
            M[i][j] = max( M[i][j-1],M[i-1][j] )

print(M[len(x)-1][len(y)-1])
#print(lcs(x,y,len(x)-1,len(y)-1))
#acbdegcedbg
#begcfeubk