'''
def TD(lis,left,right):
    
    if right-left == 1:
        return lis[left],lis[left]
    if right-left==0:
        return 0
    
    s = -9999999
    SUM = -999999
    for i in range(left+1,right):
        l,sl = TD(lis,left,i)
        r,sr = TD(lis,i,right)
        summa = l+r
        s = max(summa,s,l,r)
        SUM = max(SUM,summa)
    return s , SUM
'''

n = int(input())

lis = [int(i) for i in input().split()]

s = lis[0]
maxi1 = lis[0]
st = 0
ed = 0
ST = 0
ED = 0
for i in range(1,len(lis)):
    if s + lis[i] >= 0 and s+lis[i] > lis[i]:
        ed += 1
        s += lis[i]
    else:
        st = i
        ed = st
        s = lis[i]
    
    if maxi1 < s or maxi1 < lis[i]:
        ST = st
        ED = ed
        maxi1 = max(s,lis[i])
        
#print(maxi1,ST,ED)

newLis = []
for i in range(len(lis)):
    if i >= ST and i <= ED:
        continue
    else:
        newLis.append( lis[i] )
        
#print(newLis)

s = newLis[0]
maxi2 = newLis[0]
st = 0
ed = 0
ST = 0
ED = 0
for i in range(1,len(newLis)):
    if s + newLis[i] >= 0 and s+newLis[i] > newLis[i]:
        ed += 1
        s += newLis[i]
    else:
        st = i
        ed = st
        s = newLis[i]
    
    if maxi2 < s or maxi2 < newLis[i]:
        ST = st
        ED = ed
        maxi2 = max(s,newLis[i])

#print(maxi2,ST,ED)

print(max( maxi1,maxi1+maxi2 ))

'''
5
1 1 -10 1 1

5
1 2 3 4 5

4
-4 -2 -3 -1

6
-1 -1 10 -1 -1 -2

10
-1 3 -1 2 -4 -5 7 -3 8 -4
'''
