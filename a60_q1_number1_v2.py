import math

n,l,r = [int(i) for i in input().strip().split()]
l-=1
r-=1
suma = 0
def DC( left,right,n ):
    global l,r,suma
    mid = (left+right)//2
    if n == 1:
        if l <= mid and mid <= r:
            suma += 1
        return
    if n==0:
        return
    
    if mid >=l and mid <= r:
        if n%2==1:
            suma += 1
        DC(left,mid,n//2)
        DC(mid,right,n//2)
    elif mid > r:
        DC(left,mid,n//2)
    else:
        DC(mid,right,n//2)
    

ns = n
size = 1
i = 1
while(True):
    if ns == 1 or ns == 0:
        break
    ns = ns//2
    size += int(math.pow(2,i))
    i+=1

DC(0,size,n)
    
#print(size)
print(suma)

'''
9 2 8
7 2 5
10 3 10
'''
    