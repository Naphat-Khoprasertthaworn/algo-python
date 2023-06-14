def fibo(n,M):
    if(n<=1):
        return n
    s = 0
    if M[n-1] == 0:
        M[n-1] = fibo(n-1,M)
    
    if M[n-2] == 0:
        M[n-2] = fibo(n-2,M)
    s = M[n-2] + M[n-1]
    M[n] = s
    return s

n = int(input())
M = [0]*(n+1)
print(fibo(n,M))