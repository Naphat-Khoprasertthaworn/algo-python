

def process( seq,i,n,rule ):
    if i==n:
        print(*seq)
#     print(seq,i)


    
    for j in range(i,n):
        seq[i],seq[j] = seq[j],seq[i]
        if seq[i] in rule.keys():
            f = False
            for k in range(i):
                if seq[k] == rule[seq[i]]:
                    f = True
                    break
            if not f:
                seq[i],seq[j] = seq[j],seq[i]
                continue   
        process(seq,i+1,n,rule)
        seq[i],seq[j] = seq[j],seq[i]



n,m = [int(i) for i in input().split()]

seq = list(range(n))
rule = dict()
for _ in range(m):
    f,s = [int(i) for i in input().split()]
    rule[s] = f

process(seq,0,n,rule)
'''
4 2
3 2
0 1

3 1
1 2
'''