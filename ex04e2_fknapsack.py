w,n = [float(i) for i in input().split()]
n = int(n)
V = [float(i) for i in input().split()]
W = [float(i) for i in input().split()]

F = []

for i in range(n):
    F.append( (V[i]/W[i] , V[i] , W[i]) )
    
F.sort(reverse=True)
val = 0
for i in range(n):
    if F[i][2] <= w:
        w -= F[i][2]
        val += F[i][1]
    else:
        val += F[i][0]*w
        break

print("%.4f" % val)
'''
6 3
5 3 3
4 3 3

5.5 4
2 3 4 5
1 2 3 4
'''