n,e = [int(i) for i in input().split()]

M = [ [] for i in range(n) ]

for i in range(e):
    a,b = [int(i)-1 for i in input().split()]
    M[b].append(a)
    
for NNN in range(5):
    plan = [int(i)-1 for i in input().split()]
    V = [0]*n
    f = True
    for i in plan:
        V[i]=1
        for j in M[i]:
            if V[j]==0:
                print("FAIL")
                f = False
                break
        if f == False:
            break
    if f==True:
        print("SUCCESS")

'''
3 2
1 2
1 3
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1

4 3
1 2
2 3
3 4
1 2 3 4
1 3 4 2
1 4 2 3
4 3 2 1
3 1 2 4
'''
