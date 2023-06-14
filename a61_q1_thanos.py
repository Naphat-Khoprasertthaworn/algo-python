#21:50
import math
import bisect

def countAV(av,left,right):
    return bisect.bisect_right(av, right, lo=0, hi=len(av)) - bisect.bisect_left(av, left, lo=0, hi=len(av))

def ta( av,left,right,A,B ):
    numAV = countAV( av,left,right-1 )
    #print(numAV,left,right)
    
    if numAV==0:
        return A
    
    if right-left == 1:
        return numAV*B
    
    
    mid = (left+right)//2
    rightSide = ta(av,mid,right,A,B)
    leftSide = ta(av,left,mid,A,B)
    allSide = B*numAV*(right-left)
    
    return min( rightSide+leftSide , allSide )

p,k,A,B = [int(i) for i in input().split()]

size = int(math.pow(2,p))

av = [int(i) for i in input().split()]
for i in range(len(av)):
    av[i] -= 1
#print(av)
av.sort()

print(ta(av,0,size,A,B))
#print( bisect.bisect_left(av, 4, lo=0, hi=len(av)) )
#print( bisect.bisect_right(av, 4, lo=0, hi=len(av)) )



'''

1 2 3 4
1 3 3 3 5

2 2 1 2
1 3

3 2 1 2
1 7

2 1 10 1
1
'''