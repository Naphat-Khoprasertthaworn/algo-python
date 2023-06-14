ans = 0

def check(b,i):
    
    for j in range( 1,i+1 ):
        if b[ i-j ] == b[i]-j or b[ i-j ] == b[i]+j:
            return False
    return True

def process(b,i):
    global ans,n
    #print(b)
    if not check(b,i):
        return
    if i==n-1:
        ans += 1
        #print()
        return
    for j in range( i+1,n ):
        b[i+1],b[j] = b[j],b[i+1]
        process( b,i+1 )
        b[i+1],b[j] = b[j],b[i+1]

n = int(input())

b = list(range(n))

for i in range(n):
    b[0],b[i] = b[i],b[0]
    process( b,0 )
    b[0],b[i] = b[i],b[0]
# n = 4
# print(check( [3, 1, 0, 2],3 ))
print(ans)