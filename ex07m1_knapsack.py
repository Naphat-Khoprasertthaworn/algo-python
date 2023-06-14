
def greedy( fs,idx,w ):
    global n
    c = 0
    for i in range(idx,n):
        if w >= fs[i][2]:
            w -= fs[i][2]
            c += fs[i][1]
        else:
            c += fs[i][0]*w
            break
    return c
ans = 0
def process( fs,idx,w,c ):
    global ans,n
    if idx == n:
        ans = max(ans,c)
        return
    if greedy(fs,idx,w) + c < ans:
        return
    if w >= fs[idx][2]:
        process( fs,idx+1,w-fs[idx][2],c+fs[idx][1] )
    process( fs,idx+1,w,c )
    

W,n = [float(i) for i in input().split()]
n = int(n)
vs = [float(i) for i in input().split()]
ws = [float(i) for i in input().split()]

fs = []
for i in  range(n):
    f = vs[i]/ws[i]
    fs.append( (f,vs[i],ws[i]) )

fs.sort(reverse=True)
print(fs)
process(fs,0,W,0)

print(ans)



'''
10.0 4
1.2 3.4 6.3 1.3
4.2 1.4 6.7 4.3

10 4
10 24 16 30
1 4 2 6
'''