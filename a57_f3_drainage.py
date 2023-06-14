hn,ln = [int(i) for i in input().split()]

h = [ int(i) for i in input().split() ]

h.sort()
n = h[-1]
l = [0]*n
for i in h:
    l[i-1] = 1

#print(l)
ans = 0
i=0
while i<n:
    if l[i]==1:
        i += ln
        ans += 1
    else:
        i += 1
print(ans)
'''
6 3
2 1 3 12 7 8

5 6
2 4 9 11 14
'''


