import heapq,copy

def check(b):
    for i in range(16):
        if b[i] != (i+1)%16:
            return False
    return True

def greedy1( b ):
    s = 0
    idx = findZ(b)
    newB = list(b)
    newB[idx] = 16
    for i in range(15):
        realVal = (i+1)%16
        s += abs(newB[i]//4 - realVal//4) + abs(newB[i]%4 - realVal%4)
    return s

def greedy2( b ):
    cost = 0
    for i in range(16):
        if b[i]==0:
            continue
        if (b[i]-1)%16 != i:
            cost += abs(i%4 - ((b[i]-1)%16) %4) + abs((i//4) - ((b[i]-1)%16)//4)
    return cost
        
def findZ(b):
    for i in range(16):
        if b[i]==0:
            return i
    return -1

def BFS( B ):
    s = set()
    q = [ (greedy(B),B,0,findZ(B)) ]
    while len(q)!=0:
        
        g,b,rm,idx = heapq.heappop(q)
        if tuple(b) in s:
            continue
        if check(b):
            print(rm)
            return
        s.add(tuple(b))
        
        if idx%4 != 0:
            newB = copy.deepcopy(b)
            newB[idx] , newB[idx-1] = newB[idx-1] , newB[idx]
            heapq.heappush( q,(greedy(newB)+rm+1 , newB , rm+1 , idx-1) )

        if idx%4 != 3:
            newB = copy.deepcopy(b)
            newB[idx] , newB[idx+1] = newB[idx+1] , newB[idx]
            heapq.heappush( q,(greedy(newB)+rm+1 , newB , rm+1 , idx+1) )

        if idx > 3:
            newB = copy.deepcopy(b)
            newB[idx] , newB[idx-4] = newB[idx-4] , newB[idx]
            heapq.heappush( q,(greedy(newB)+rm+1 , newB , rm+1 , idx-4) )

        if idx < 12:
            newB = copy.deepcopy(b)
            newB[idx] , newB[idx+4] = newB[idx+4] , newB[idx]
            heapq.heappush( q,(greedy(newB)+rm+1 , newB , rm+1 , idx+4) )

b = []
for _ in range(4):
    a = [int(i) for i in input().split()]
    for j in a:
        b.append(j)

#print(greedy(b))

#BFS(b)
        
print(greedy1(b),greedy2(b))

'''
1 2 3 4
5 6 7 8
9 10 11 0
13 14 15 12

0 2 3 4
5 6 7 8
9 10 11 1
13 14 15 12

0 2 3 4
1 6 7 8
5 9 10 11
13 14 15 12

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 0

1 2 3 4
5 6 7 8
9 10 15 11
13 14 0 12

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 0

5 1 2 3
9 10 6 4
13 0 7 8
14 15 11 12
'''