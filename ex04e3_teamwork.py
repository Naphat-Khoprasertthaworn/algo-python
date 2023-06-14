#13:09

n,m = [int(i) for i in input().split()]

task = [int(i) for i in input().split()]

task.sort()

s = [0] * n
c = [0] * n
#print(c)
#print(s)
summ = 0
for i in range(m):
    s[i%n] += task[i]
    #print(s)
    summ += s[i%n]
    c[i%n] += 1
av = summ/m
print(av)

'''
1 4
3 9 4 2

3 10
4 3 2 4 1 2 5 3 4 5
'''