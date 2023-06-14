s = 0

def mergeSort(lis,left,right):
    if right-left == 1:
        return [ lis[left] ]
    
    mid = (left+right)//2
    leftLis = mergeSort( lis,left,mid )
    rightLis = mergeSort( lis,mid,right )
    
    newLis = []
    il = 0
    ir = 0
    while il != len(leftLis) or ir != len(rightLis):
        global s
        if il == len(leftLis):
            while ir != len(rightLis):
                newLis.append( rightLis[ir] )
                ir += 1
        elif ir == len(rightLis):
            while il != len(leftLis):
                newLis.append( leftLis[il] )
                il += 1
        else:
        
            if leftLis[il] <= rightLis[ir]:
                newLis.append( leftLis[il] )
                il += 1
            else:
                newLis.append( rightLis[ir] )
                s += len(leftLis) - il
                ir += 1
                 
        
    return newLis

n = int(input())

lis = [ int(i) for i in input().split() ]

print( mergeSort(lis,0,n) )
print(s)

'''
4
10 30 40 20

6
1 5 4 2 3 -1

7
2 1 3 0 -1 7 6
'''