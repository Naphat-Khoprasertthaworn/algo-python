
def biSearch(l,left,right,ask):
    
    if right-left == 1:
        if l[left]<=ask:
            return l[left]
        else:
            return -1
    
    mid = (left+right)//2
    
    if l[mid] > ask:
        return biSearch( l,left,mid,ask )
    else:
        return biSearch( l,mid,right,ask )
    


n,m = [ int(i) for i in input().split() ]

l = [ int(i) for i in input().split() ]

ask = [ int(i) for i in input().split() ]

for i in range(m):
    print(biSearch( l,0,n,ask[i] ))
    