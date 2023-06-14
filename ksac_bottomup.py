n,w = [int(i) for i in input().split()]
plist = [int(i) for i in input().split()]
plist = [0]+plist
wlist = [int(i) for i in input().split()]
wlist = [0]+wlist
dic = {}
curW = 0
curP = 0
for i in range(0,n+1):
    for j in range(0,w+1):
        if i==0 or j==0:
            dic[ (i,j) ] = 0
        else:
            if j-wlist[i] <0:
                dic[ (i,j) ] = dic[ (i-1,j) ]
            else:
                dic[ (i,j) ] = max( dic[ (i-1,j-wlist[i]) ] + plist[i] , dic[ (i-1,j) ] )

print(dic[(n,w)])
'''
3 50
60 100 120
10 20 30


5 5
3 10 6 3 5
5 5 3 1 1

5 3
6 9 5 4 3
2 3 1 1 2

3 5
2 2 4
1 4 5
'''