ans = 0
def process( i,n,sumW ):
    global ans

    if sumW==n:
        ans += 1
        return
    elif sumW > n:
        return
    if i+sumW > n:
        return
    process( i,n,sumW+i )
    process( i+1,n,sumW )
    
    


n = int(input())
V = [0]*n
process(1,n,0)

print(ans)

