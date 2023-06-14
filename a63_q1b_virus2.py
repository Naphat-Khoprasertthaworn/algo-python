

def recur(s,i,j):
    
    if j-i == 2:
        return True
    
    m = (i+j)//2
    if abs(sum(s[i:m]) - sum(s[m:j])) > 1:
        return False
    if not recur(s,i,m):
        return False
    if not recur(s,m,j):
        return False
    return True
    

n,m = [int(i) for i in input().split()]

r = 1<<m
#print(r)



for _ in range(n):
    s = [int(i) for i in input().split()]
    if recur(s,0,r):
        print("yes")
    else:
        print("no")

'''
5 2
0 0 0 0
0 0 1 1
0 1 1 1
1 0 0 0
0 1 0 1

3 4
1 1 1 1 1 1 1 0 0 1 1 1 1 1 0 0
1 1 1 1 1 1 1 0 0 1 1 1 1 1 0 1
1 1 1 0 0 1 1 1 1 0 0 1 1 0 1 1
'''
    
    