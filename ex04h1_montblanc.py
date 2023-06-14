

n,D = [int(i) for i in input().split()]

height = [ int(i) for i in input().split() ]

inte = max(height[-1]//D,height[0])

for i in range(n-1):
    inte = max( inte,height[i+1]-height[i] )
#print(inte)

for h in range(inte,height[-1]+1):
    d = 1
    s = 0
    for i in range( n ):
        if height[i] <= s+h:
            continue
        else:
            s = height[i-1]
            d += 1

    if d > D:
        continue
    else:
        print(h,d)
        break



'''

9 3
10 30 50 70 90 110 120 170 180

9 1
10 30 50 70 90 110 120 170 180

9 3
10 30 50 70 90 110 120 170 200

6 4
30 60 90 120 150 180

1 5
180

3 3
100 210 300

9 0
10 30 50 70 90 110 120 170 180

10 3
10 30 50 60 70 90 110 140 170 180

6 4
30 60 90 120 150 180
'''
        