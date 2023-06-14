def biSearch( M,val,left,right ):
    
    if right-left==1:
        return left+1
    mid = int( (left+right)/2  )
    
    if val <= M[mid]:
        return biSearch( M,val,left,mid )
    else:
        return biSearch( M,val,mid,right )
    

n = int(input())
M = [0]*1000000
pointer = 2
M[1] = 1
M[2] = 3
for i in range(3,1000000):
    if i > M[pointer]:
        pointer += 1
    
    M[i] = M[i-1] + pointer


for i in range(n):
    inp = int(input())
    print(biSearch( M,inp,0,1000000 ))

'''
4
100
9999
123456
1000000000



3
2
4
10

'''
