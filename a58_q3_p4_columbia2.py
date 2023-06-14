import heapq,math,sys
input = sys.stdin.readline
#print = lambda s:sys.stdout.write(str(s)+" ")
    
def findCheckList( r,c,R,C ):
    l = []
    for i in range(-2,3):
        for j in range(-2,3):
            if 1<=abs(i)+abs(j)<=2 and 0 <= r+i < R and 0 <= c+j < C:
                l.append( (r+i,c+j) )
    return l
    
def DJT(D,r,c):
    M = [ [math.inf]*c for i in range(r) ]
    M[0][0] = 0
    V = [ [0]*c for i in range(r) ]
    q = [ (0,0,0) ]
    nl = 0
    order = []
    while len(q)!=0 and nl != r*c:
        w,ir,ic = heapq.heappop(q)
        if V[ir][ic] == 1:
            continue
        V[ir][ic] = 1
        nl += 1
        M[ir][ic] = w
        order.append( (ir,ic) )
        if ir-1 >= 0 and V[ir-1][ic] == 0:
            #M[ir-1][ic] = w + D[ir-1][ic]
            heapq.heappush( q, (w + D[ir-1][ic],ir-1,ic) )
        if ic-1 >= 0 and V[ir][ic-1] == 0:
            #M[ir][ic-1] = w + D[ir][ic-1]
            heapq.heappush( q, (w + D[ir][ic-1],ir,ic-1) )
        if ir+1 < r and V[ir+1][ic] == 0:
            #M[ir+1][ic] = w + D[ir+1][ic]
            heapq.heappush( q, (w + D[ir+1][ic],ir+1,ic) )
        if ic+1 < c and V[ir][ic+1] == 0:
            #M[ir][ic+1] = w + D[ir][ic+1]
            heapq.heappush( q, (w + D[ir][ic+1],ir,ic+1) )
    return M,order
    

r,c = [int(i) for i in input().split()]

D = [  ]
for i in range(r):
    st = [int(j) for j in input().split()]
    D.append(st)
    
M0,order = DJT(D,r,c)
#print(order)
#print(M0)
for i in range(r):
    print(*M0[i])
print("======================")
for k in range(2):
    M1 = [ [math.inf]*c for i in range(r) ]
    M1[0][0] = 0
    newOrder = []
    for i,j in order:
        checkList = findCheckList( i,j,r,c )
        #minR = 0
        #minC = 0
        for a in range(-1,2):
            for b in range(-1,2):
                if abs(a)+abs(b)==1 and 0<= i+a < r and 0<= j+b < c and M1[i+a][j+b] + D[i][j] < M1[i][j]:
                    M1[i][j] = M1[i+a][j+b] + D[i][j]
                    #minR = i+a
                    #minC = j+b
        for ir,ic in checkList:
            if M0[ir][ic] < M1[i][j]:
                M1[i][j] = M0[ir][ic]
                #minR = ir
                #minC = ic
        #newOrder.append( (minR,minC) )
    #order = newOrder
    M0 = M1
    for i in range(r):
        print(*M0[i])
    print("======================")
#for i in range(r):
#    print(" ".join([str(j) for j in M1[i]]))
for i in range(r):
    print(*M0[i])




'''
4 4
1 1 1 1
9 8 7 1
1 1 1 1
1 2 4 9

3 10
668 620 394 104 771 342 411 520 35 537
783 486 619 392 292 49 625 241 926 647
52 728 316 16 530 392 977 948 983 367

5 5
1 2 1 2 9
9 9 9 9 9
1 1 1 9 4
9 9 9 9 8
2 2 2 8 8

10 10
668 620 394 104 771 342 411 520 35 537
783 486 619 392 292 49 625 241 926 647
52 728 316 16 530 392 977 948 983 367
672 695 15 860 485 782 221 150 305 57
107 302 53 475 833 552 595 615 445 282
870 845 719 493 942 562 401 506 648 457
67 836 423 865 732 420 873 856 503 552
88 315 588 49 392 980 813 969 401 934
102 474 354 306 643 901 100 976 704 560
541 590 627 677 129 432 941 303 639 677

6 7
1 99 99 1 1 1 1
1 99 99 1 99 99 1
1 99 99 1 99 99 1
1 99 99 99 99 99 1
1 99 99 99 99 99 1
1 1 1 1 1 1 1


'''