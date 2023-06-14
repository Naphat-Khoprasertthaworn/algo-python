import sys
sys.setrecursionlimit(99999999)
def process(ans,lis,s1,s2,n,m,M):
    #print(n,m)

    if n==0 or m==0:
        return ans
    if M[n][m] == []:
        if s1[n-1] == s2[m-1]:
            ans3 = process(ans,lis,s1,s2,n-1,m-1,M)
            ans3 = ans3 + [s1[n-1]]
            #print( s1[n-1],n,m )
            M[n][m] = ans3
        else:
            ans1 = process(ans,lis,s1,s2,n,m-1,M)
            ans2 = process(ans,lis,s1,s2,n-1,m,M)
            if len(ans1) > len(ans2):
                M[n][m] = ans1
            else:
                M[n][m] = ans2
                

    return M[n][m]
    
    
n,m = [int(i) for i in input().split()]

s1 = input()
s2 = input()

lis = []
for i in range(n+1):
    inp = [int(i) for i in input().split()]
    lis.append(inp)
    
#print(lis)
ans = []
M = [ [ [] ]*(m+1) for i in range(n+1) ]
s3 = process(ans,lis,s1,s2,n,m,M)

print("".join(s3))
print(M)
#print(ans)

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