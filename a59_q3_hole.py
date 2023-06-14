import sys
input = sys.stdin.readline

def BFS(V,q,r,c):
    h = 0
    while len(q)!=0:
        newQ = []
        for i,j in q:
            if V[i][j] != 0:
                if V[i][j]==2:
                    newQ.append((i,j))
                continue
            V[i][j] = 1
            if i == 0 or i == r-1 or j == 0 or j == c-1:
                print(h)
                return
            if V[i-1][j] != 1:
                newQ.append( (i-1,j) )
            if V[i][j-1] != 1:
                newQ.append( (i,j-1) )
            if V[i+1][j] != 1:
                newQ.append( (i+1,j) )
            if V[i][j+1] != 1:
                newQ.append( (i,j+1) )
                
        if len(newQ)==0:
            break
        flag = False
        for cx,cy in newQ:
            if V[cx][cy]==0:
                flag = True
                break
        
        if flag == False:
            h+=1
            for cx,cy in newQ:
                if V[cx][cy]==2:
                    V[cx][cy] = 0
        
        q = newQ
    print(h)
    
    
    
    

N,a,b = [int(i) for i in input().split()]
a-=1
b-=1
r=1000
c=1000
            
V = [ [0]*c for i in range(r) ]
for i in range(N):
    ir,ic = [int(i)-1 for i in input().split()]
    V[ir][ic] = 2

q = [(a,b)]
BFS(V,q,r,c)

#print(h)             
'''
7 6 3
6 2
5 2
4 3
2 1
7 3
5 4
6 4
'''