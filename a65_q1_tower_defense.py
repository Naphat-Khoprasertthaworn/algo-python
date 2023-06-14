import bisect
n,m,k,w = [int(i) for i in input().split()]

p = [int(i) for i in input().split()]

h = [int(i) for i in input().split()]

t = [int(i) for i in input().split()]

t.sort()

M = []
sumH = 0
for i in range(m):
    M.append( [p[i],h[i]] )
    sumH += h[i]

M.sort()

for i in range(k):
    idx_left = bisect.bisect_left( M,[t[i]-w,0] )
    idx_right = bisect.bisect_left( M,[t[i]+w,0] )
    if idx_left==idx_right and M[idx_left][0] != t[i]-w and M[idx_left][0] != t[i]+w:
        continue
    M[idx_left][1] -= 1
    sumH -= 1
    if M[idx_left][1] == 0:
        del M[idx_left]
print(sumH)
'''
10 1 2 1
1
10
2 5

10 1 2 4
1
10
2 5

100 3 2 1 
80 70 60
1 1 1
70 71 69

100 8 8 0
37 100 38 5 74 6 72 32
1 1 1 1 1 1 1 1
58 13 15 59 24 70 100 4
'''