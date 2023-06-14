import sys
print = sys.stdout.write
input = sys.stdin.readline

n,m = [int(i) for i in input().split(" ")]
l = [-1]*n
for i in range(m):
    b,a = [int(i) for i in input().split()]
    l[ b ] = a

ans = [False]*n;

    
def process(s,ans,stringLen):
    if(stringLen == n):
        print(s + "\n")
        return
    for i in range(n):
        if ans[i] == 0 and ( l[i] == -1 or ans[ l[i] ] != 0 ):
            ans[i] = True
            process( s + str(i) + " ",ans,stringLen+1 )
            ans[i] = False
        
    
process("",ans,0)