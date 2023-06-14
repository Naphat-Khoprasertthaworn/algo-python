import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
def DC( lis,left,right ):
    
    if right-left == 1:
        return [ lis[left] ]
    
    mid = (left+right)//2
    
    leftLis = DC(lis,left,mid)
    rightLis = DC(lis,mid,right)
    
    for i in range(len(leftLis)-1,-1,-1):
        if leftLis[i][1] > rightLis[0][1]:
            rightLis = [leftLis[i]]+rightLis
    return rightLis

n = int(input())
lis = []

for i in range(n):
    x,y = [int(i) for i in input().split()]
    lis.append( (x,y) )
    
lis.sort()


print(len(DC( lis,0,n )))

'''
4
20 40
21 21
40 20
41 41

3
10 10
20 20
30 30

3
50 10
30 30
10 50


'''