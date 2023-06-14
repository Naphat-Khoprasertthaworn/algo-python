#12:46

n = int(input())

s = [int(i) for i in input().split()]

f = [int(i) for i in input().split()]

l = []

for i in range(n):
    l.append( (f[i],s[i]) )

l.sort()

#print(l)

f = 0
c = 0
for i in range(n):
    if l[i][1] >= f:
        c += 1
        f = l[i][0]
print(c)

'''
3
1 4 6
5 7 10

4
1 2 3 4
2 3 4 5
'''