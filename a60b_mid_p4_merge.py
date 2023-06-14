n,k = [int(i) for i in input().split()]
k-=1
def suffle( lis,left,right ):
    global k
    #k -= 1
    if k<=0:
        return
    if right-left==1:
        return
    mid = (left+right)//2
    lis[mid],lis[mid-1] = lis[mid-1],lis[mid]
    k-=2
    suffle(lis,left,mid)
    suffle(lis,mid,right)
    
lis = []
for i in range(1,n+1):
    lis.append(i)

suffle( lis,0,n )
if k!=0:
    print(-1)
else:
    print(*lis)

