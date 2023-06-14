
N = int(input())

for I in range(N):
    R,C,n,T,r,c = [int(i) for i in input().split()]
    
    M = [ [0]*C for i in range(R) ]
    queue1 = []
    g = []
    for i in range(n):
        t,a,b = [int(i) for i in input().split()]
        g.append((t,a,b))
        #queue1.append( (a,b) )
    
    for i in range(R):
        st = input()
        for j in range(len(st)):
            if st[j] == "#":
                M[i][j] = 5
    
    queue2 = [(r,c)]
    
    ut = 0
    while True:
        if T < 0:
            break
        #print(T)
        
        for i in g:
            if ut == i[0]:
                queue1.append( (i[1],i[2]) )
        
        newQueue1 = []
        newQueue2 = []
        for p in queue1:
            if M[ p[0] ][ p[1] ] == 0 or M[ p[0] ][ p[1] ] == 2:
                M[ p[0] ][ p[1] ] = 1
                #if p[0]+1 >= R:
                    
                newQueue1.append( ( min(p[0]+1,R-1),p[1] ) )
                newQueue1.append( ( p[0],min(p[1]+1,C-1) ) )
                newQueue1.append( ( max(0,p[0]-1),p[1] ) )
                newQueue1.append( ( p[0],max(p[1]-1,0) ) )
                
        for p in queue2:
            if M[ p[0] ][ p[1] ] == 0:
                M[ p[0] ][ p[1] ] = 2
                newQueue2.append( ( min(p[0]+1,R-1),p[1] ) )
                newQueue2.append( ( p[0],min(p[1]+1,C-1) ) )
                newQueue2.append( ( max(0,p[0]-1),p[1] ) )
                newQueue2.append( ( p[0],max(p[1]-1,0) ) )

        queue1 = newQueue1
        queue2 = newQueue2
        T -= 1
        ut += 1
        
    f = False
    for i in range(R):
        for j in range(C):
            if M[i][j]==2:
                print("YES")
                f = True
                break
        if f==True:
            break
    if f==False:
        print("NO")
    #print(M)
                
        
        
        

'''
2
5 5 2 10 2 2
0 0 0
0 4 4
.....
.###.
.#.#.
.###.
.....
5 5 2 4 2 2
0 0 0
0 4 4
.....
.###.
...#.
.###.
.....


3
2 5 1 1 0 2
0 0 2
.....
.....
2 5 1 1 0 2
1 0 2
.....
.....
2 5 4 1 0 2
1 0 2
1 0 3
1 0 1
1 1 2
.....
.....

1
2 5 1 1 0 2
1 0 2
.....
.....
'''