#14:50

import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")
def bSearch(newList,val,left,right):
    
    if right-left==1:
        return left+1
    mid = (left+right)//2
    
    if val > newList[mid]:
        return bSearch(newList,val,mid,right)
    else:
        return bSearch(newList,val,left,mid)
    
    
n,k,m = [int(i) for i in input().split()]

lis = [int(i) for i in input().split()]

newList = [0]
s = 0
for i in range(n):
    s += lis[i] - m
    newList.append(s)
    
#print(newList)

for i in range(k):
    st,de = [ int(i) for i in input().split() ]
    de += newList[st-1]
    print(bSearch(newList,de,0,n))

'''
7 5 2
4 6 2 7 3 5 9
1 1
1 6
1 14
4 7
6 3



'''