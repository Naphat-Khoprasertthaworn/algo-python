#10.58
from collections import deque
import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

N,M,K = [int(i) for i in input().split()]
lis = []
for _ in range(K):
    D,E,L = [int(i) for i in input().split()]
    lis.append( (D,E,L) )
    
lis.sort()

#print(lis)
    
s = deque()
q = deque()

for d,e,l in lis:
    if e==0:
        s.append( l )
    elif e==1:
        q.append( l )
    
    if len(q)==0 or len(s)==0:
        print(0)
    else:
        if e==0:
            s.popleft()
            print(q.popleft())
        else:
            print(s.popleft())
            q.popleft()

    
'''
2 2 3
3 1 2
1 0 2
2 0 1

3 3 7
5 0 3
1 1 1
3 1 1
2 1 2
4 0 3
7 0 3
6 1 1
'''