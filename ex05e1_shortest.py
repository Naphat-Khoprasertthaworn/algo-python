#14:30
import sys
input = sys.stdin.readline
print = lambda s:sys.stdout.write(str(s)+"\n")

def BFS(table,r,c):
    V = [ [0]*c for i in range(r) ]
    M = [ [] ]
    for i in range(r):
        for j in range(c):
            if table[i][j] == ".":
                V[i][j] = 0
            else:
                V[i][j] = 2
    q = [(0,0)]
    d = 0
    f = False
    while len(q)!=0:
        newQ = []
        for ix,iy in q:
            if ix==r-1 and iy==c-1:
                f=True
                break
            V[ix][iy] = 1
            if ix-1>=0 and V[ix-1][iy]==0:
                newQ.append( (ix-1,iy) )
            if iy-1>=0 and V[ix][iy-1]==0:
                newQ.append( (ix,iy-1) )
            if ix+1<r and V[ix+1][iy]==0:
                newQ.append( (ix+1,iy) )
            if iy+1<c and V[ix][iy+1]==0:
                newQ.append( (ix,iy+1) )
            if f==True:
                break
        if f==True:
            break
        q = newQ
        d+=1
    if f==True:
        print(d)
    else:
        print(-1)
    
r,c = [int(i) for i in input().split()]

table = [ [] for i in range(r) ]
for i in range(r):
    l = input()
    for j in range(c):
        table[i].append(l[j])
#print(table)
BFS(table,r,c)




'''
5 5
.....
...##
...#.
..##.
.###.


5 5
.#...
.#...
.#...
.#.#.
...#.
'''