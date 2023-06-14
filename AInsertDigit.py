t = int(input())

for _ in range(t):
    n,d = [int(i) for i in input().split()]
    
    l = [int(i) for i in input()]
    s = ""
    f = False
    for i in range(n):
        #print(s)
        if d>l[i]:
            f = True
            s += str(d)
            s += "".join(str(e) for e in l[i:])
            break
        else:
            s += str(l[i])
    if f==False:
        s += str(d)
    print(s)
'''
1
6 2
986512

11
5 4
76543
1 0
1
2 5
44
3 6
666
5 6
13579
5 8
97531
19 4
9876543210123456789
5 7
73737
8 1
20000000
7 0
7058959
12 1
828127127732
'''