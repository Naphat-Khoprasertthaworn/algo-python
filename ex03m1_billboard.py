import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
sys.setrecursionlimit(200000)

def process(n,lis,M):
    if n<0:
        return 0
    
    if M[n]==0:
        M[n] = max( process(n-1,lis,M),process(n-2,lis,M) + lis[n] )
    return M[n]

n = int(input())

lis = [int(i) for i in input().split()]
M = [0]*n
print(process( n-1 ,lis,M))
#print(M)
'''
3
3 4 2

10
48 1 3 95 2 1 3 44 22 2
'''