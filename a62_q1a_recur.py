import math
import sys
sys.setrecursionlimit(9999999)
def recur( M,b,left,right,top,bottom ):
    
    if right-left==1:
        M[top][left] = b
        return
    
    mid = (left+right)//2
    mmm = (top+bottom)//2
    
    recur(M,b,left,mid,top,mmm)
    recur(M,b-1,mid,right,top,mmm)
    recur(M,b+1,left,mid,mmm,bottom)
    recur(M,b,mid,right,mmm,bottom)

a,b = [int(i) for i in input().split()]

size = int(math.pow( 2,a ))

M = [ [0]*size for i in range(size) ]

recur(M,b,0,size,0,size)

for i in range(size):
    print(" ".join(map(str,M[i])) )
