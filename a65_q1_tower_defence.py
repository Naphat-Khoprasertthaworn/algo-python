n,m,k,w = [int(i) for i in input().strip().split()]

monsList = [int(i) for i in input().strip().split()]

monsPow = [int(i) for i in input().strip().split()]

towList = [int(i) for i in input().strip().split()]

sumPow = sum(monsPow)
monsDict = {}

for i in range(len(monsList)):
    if monsList[i] not in monsDict.keys():
        monsDict[monsList[i]] = monsPow[i]
    else:
        monsDict[monsList[i]] += monsPow[i]

#print( monsDict )
#monsDict = collections.OrderedDict(sorted(monsDict.items()))
monsDict =  dict(sorted(monsDict.items()))
towList.sort()

#print( monsDict )
#print( towList )

for i in towList:
    for j in range( max( 0,i-w ) , min( i+w+1,n )  ):
        if j in monsDict.keys() and monsDict[j] > 0:
            #print("thtis")
            monsDict[j] -= 1
            #print( monsDict[j] )
            sumPow -= 1
            break

print(sumPow)



'''
100 3 3 1
80 70 60
1 1 1
70 71 69

10 1 2 4
1
10
2 5

10 1 2 1
1
10
2 5


'''
    