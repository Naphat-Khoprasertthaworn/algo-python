#19.05
import heapq,math

ans = math.inf
def process(pool,m,k,sumW,idx,n):
    global ans
    if ans==0:
        return
    if m==0:
        ans = min(ans,abs(sumW-k))
        return
    low = sum(pool[idx:idx+m]) + sumW
    if low > k and low-k>ans:
        return
    process( pool,m-1,k,sumW + pool[idx],idx+1,n )
    if n-idx > m:
        process( pool,m,k,sumW,idx+1,n )

n,m,k = [int(i) for i in input().split()]
pool = [int(i) for i in input().split()]
pool.sort()
process(pool,m,k,0,0,n)
print(ans)


'''
4 4 10
1 4 2 3



4 2 10
1 4 2 3

4 2 6
1 6 4 7



10 2 32
50 25 45 29 38 7 22 8 15 29
'''
