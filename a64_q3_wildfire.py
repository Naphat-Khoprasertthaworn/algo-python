import heapq,math,sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+" ")
n,m,k = [int(i) for i in input().split()]

b = [int(i) for i in input().split()]

q = [int(i) for i in input().split()]

M = [ [] for i in range(n) ]
for i in range(m):
    a,c = [int(i) for i in input().split()]
    M[a].append(c)
    
for i in range(k):
    queue = [q[i]]
    while True:
        if len(queue) == 0:
            break
        u = queue.pop(0)
        if b[u]==0:
            continue
        b[u] = 0
        for i in M[u]:
            queue.append(i)
    
    
    
    
    print(sum(b))
    
'''
4 3 3
10 20 30 40
2 1 0
0 1
1 2
2 3

4 3 4
5 10 15 20
1 2 3 1
0 1
1 2
1 3
'''