def process( s,i,n,rule ):
    global ans
    if i==n:
        print(s)
        for r,c in rule:
            sc = 0
            for i in range(n):
                if s[i]==r[i]:
                    sc += 1
                if sc >= c:
                    print("YES")
                    break
            if sc < c:
                print("NO")
                ans -= 1
                break
            
            
        
        return
    
    s[i] = 1
    process(s,i+1,n,rule)
    s[i] = 0
    process(s,i+1,n,rule)


n,m = [int(i) for i in input().split()]

rule = []


for i in range(m):
    s,j = input().split()
    j = int(j)
    rule.append( ([int(k) for k in s],j) )
    
s = [0]*n
ans = 1<<n
print(ans)
print(rule)
process(s,0,n,rule)
print(ans)
    

'''
6 3
000000 2
010100 4
111100 2


'''