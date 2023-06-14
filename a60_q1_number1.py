def findLength(n):
    if( n == 0 or n == 1 ):
        return 1
    else:
        return 2*findLength( n//2 ) + 1

def process(n,left,right,l,r):
    mid = (left+right)//2
    if n<=1:
        if(mid >= l and mid <= r):
            return n
        else:
            return 0
    
    
    if mid < l:
        sRight = process(n//2,mid+1,right,l,r)
        sLeft = 0
    elif mid > r:
        sLeft = process(n//2,left,mid,l,r)
        sRight = 0
    else:
        sLeft = process(n//2,left,mid,l,r)
        sRight = process(n//2,mid+1,right,l,r)
    
    if mid >= l and mid <= r:
        return sLeft + sRight + (n%2)
    else:
        return sLeft + sRight
        

n,l,r = [int(i) for i in input().split()]
l = l-1
r = r-1

size = findLength(n)

print(process(n,0,size,l,r))





