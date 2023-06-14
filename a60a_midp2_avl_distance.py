import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

def anotherProcess(node,nodeList,k,use):
    if k==use:
        return 1
    if len(nodeList[node]) == 0:
        return 0
    if len(nodeList[node]) == 1:
        return anotherProcess( nodeList[node][0],nodeList,k,use+1 )
    
    return anotherProcess( nodeList[node][0],nodeList,k,use+1 ) + anotherProcess( nodeList[node][1],nodeList,k,use+1 ) 
    
def process(node,nodeList,k):
    s = 0
    if len(nodeList[node]) == 2:
        s += anotherProcess( nodeList[node][0],nodeList,k,1 ) + anotherProcess( nodeList[node][1],nodeList,k,1 )
        for i in range(1,k):
            s += anotherProcess( nodeList[node][0],nodeList,i,1 ) * anotherProcess( nodeList[node][1],nodeList,k-i,1 ) 
    elif len(nodeList[node]) == 1:
        s += anotherProcess( nodeList[node][0],nodeList,k,1 )
    return s
            
n,k = [int(i) for i in input().split()]

nodeList = [[] for e in range(n)]
#print(nodeList)

for i in range(n-1):
    a,b = [int(j) for j in input().split()]
    nodeList[a-1].append(b-1)
print(nodeList)
s = 0
for i in range(n):
    s += process( i,nodeList,k )
    
print(s)


