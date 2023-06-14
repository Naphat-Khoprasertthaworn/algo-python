n = int(input())

l = [int(i) for i in input().split()]

n1 = l.count(1)
n2 = l.count(2)
n3 = l.count(3)

n2in1 = l[:n1].count(2)
n3in1 = l[:n1].count(3)

n1in2 = l[n1:n1+n2].count(1)
n3in2 = l[n1:n1+n2].count(3)

n1in3 = l[n1+n2:].count(1)
n2in3 = l[n1+n2:].count(2)



ans = 0
ans += min(n2in1,n1in2)
print(ans)
ans += min(n3in1,n1in3)
print(ans)
ans += min(n2in3,n3in2)
print(ans)
ans += 2*(n1 - min(n2in1,n1in2) - min(n3in1,n1in3) - l[:n1].count(1))

print(ans)
'''
7
2 2 1 3 2 1 3

7
1 1 2 2 2 3 3

7
2 3 3 1 1 2 2

7
2 2 3 3 1 1 2

'''