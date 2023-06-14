

def biSearch(order,left,right,ask):
    
    if right-left == 1:
        if ask >= order[left]:
            return left
        else:
            return -1
    mid = (left+right)//2
    
    if order[mid] <= ask:
        return biSearch(order,mid,right,ask)
    else:
        return biSearch(order,left,mid,ask)
        


n,m = [int(i) for i in input().split()]

order = [int(i) for i in input().split()]

ask = [int(i) for i in input().split()]

for i in range(m):
    print(biSearch( order,0,n,ask[i] ))

