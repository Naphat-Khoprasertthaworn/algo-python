



def T(tile,n,dif,M):
    if n < 0:
        if dif!=0:
            return 9999999
        return 0
    
    if dif > 0:
        if (tuple(sorted(tile)) , n) not in M:
            mini = 99999999
            i = tile[n]
            temp = tile[n]
            while(True):
                if i*i - temp*temp > dif:
                    break
                tile[n] = i
                newMini = T(tile,n-1,dif - (i*i - temp*temp),M ) + (temp-i)*(temp-i)
                mini = min(mini,newMini)
                i+=1
            tile[n] = temp
            M[(tuple(sorted(tile)) , n)] = mini
        return M[(tuple(sorted(tile)) , n)]
            
    elif dif < 0:
        if (tuple(sorted(tile)) , n) not in M:
            mini = 99999999
            temp = tile[n]
            for i in range( tile[n],0,-1 ):
                if i*i - temp*temp < dif:
                    break
                tile[n] = i
                newMini = T(tile,n-1,dif - (i*i - temp*temp),M ) + (temp-i)*(temp-i)
                mini = min(mini,newMini)
            tile[n] = temp
            M[(tuple(sorted(tile)) , n)] = mini
        return M[(tuple(sorted(tile)) , n)]
    else:
        return 0

n,m = [int(i) for i in input().split()]
tile = []
s = 0
for i in range(n):
    inp = int(input())
    s += inp*inp
    tile.append(inp)
dif = m-s
tile.sort()
    
M = dict()
re = T(tile,n-1,dif,M)
print(M)
if re == 9999999:
    print(-1)
else:
    print(re)
    
    


'''
3 6
3
3
1

3 30
5
6
7

5 5
1
2
3
4
5

'''
