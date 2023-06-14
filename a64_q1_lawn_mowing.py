import bisect,sys

input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

def process(priceList,glassList,a,b):
    b+=priceList[a]
    i = bisect.bisect_left( priceList,b )
    if( i >= len(priceList) or priceList[i]>b  ):
        i = i-1
    #print("bisect",i)
    return glassList[i]-glassList[a]

#testList = [0,3,5,7]

#print( testList[bisect.bisect_left( testList,4 )] )

n,m,k = [int(i) for i in input().split()]

g = [int(i) for i in input().split()]
glassList = [0]*(n+1)
priceList = [0]*(n+1)
s = 0
sp = 0
for i in range(n):
    s+=g[i]
    sp+=g[i]+k
    glassList[i+1] = s
    priceList[i+1] = sp
    

#print(glassList)
#print(priceList)
for i in range(m):
    a,b = [int(i) for i in input().split()]
    print(process( priceList,glassList,a,b ))


