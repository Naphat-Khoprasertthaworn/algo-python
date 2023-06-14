

f,w,n = [int(i) for i in input().split()]

t = [0]*n

ch = [int(i) for i in input().split()]

for i in ch:
    t[i-1] = 1
i = 0
lig = 0
while i < n:
    if t[i] == 1:
        i += 2*w+1
        lig += 1
    else:
        i += 1
print(lig)

'''
3 0 10
1 3 4

5 1 10
1 2 3 5 6

10 5 10
1 10 9 2 3 4 8 7 5 6


'''