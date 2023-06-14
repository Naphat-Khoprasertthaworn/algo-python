#15:10
import sys
sys.setrecursionlimit(9999999)
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")


n,w,k = [int(i) for i in input().split()]
M = [[0]*(k+1) for i in range(n+1) ]

def select( firstSide,secondSide,k,n,w ):
    global M
    if n<=0:
        return 0
    if k <= 0:
        return 0
    #if M[n][k] == 0:
    case1 = select(secondSide,firstSide,k-1,n-w-1,w) + firstSide[n-1]
    case2 = select(firstSide,secondSide,k,n-1,w)
    return max(case1,case2)
    #return M[n][k]


def save(k,n,w,leftBB,rightBB):
    global M
    
    
    r = select(rightBB,leftBB,k,n,w)
    l = select(leftBB,rightBB,k,n,w)
    M[n][k] = max(r,l)


leftBB = [int(i) for i in input().split()]
rightBB = [int(i) for i in input().split()]

for i in range(1,k+1):
    for j in range(1,n+1):
        save(i,j,w,leftBB,rightBB)

print(M[n][k])
print(M)
'''
5 1 5
1 1 10 1 1
1 1 1 20 1

5 1 5
90 1 90 1 99
1 1 1 1 1

5 2 5
90 1 90 1 99
1 1 1 1 1

5 1 2
1 1 9 1 1
9 1 1 1 9

10 1 3
2 5 7 8 4 3 9 5 1 4
9 5 7 3 1 6 8 4 2 5

'''
