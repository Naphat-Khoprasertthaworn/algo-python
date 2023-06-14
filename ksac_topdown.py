
def K( dic,plsit,wlist,n,w ):
    
    if n < 0:
        return 0
    
    if (w,n) not in dic :
        case1 = 0
        if w-wlist[n] >= 0:
            case1 = K( dic,plist,wlist,n-1,w-wlist[n] ) + plist[n]
        case2 = K( dic,plist,wlist,n-1,w )
        dic[ (w,n) ] = max(case1,case2)
    
    return dic[ (w,n) ]

n,w = [int(i) for i in input().split()]
plist = [int(i) for i in input().split()]
wlist = [int(i) for i in input().split()]



dic = {}

print( K(dic,plist,wlist,n-1,w) )
print(dic)

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

