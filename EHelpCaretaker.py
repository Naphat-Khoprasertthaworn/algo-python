

def to_tuple(lst):
    return tuple(to_tuple(i) if isinstance(i, list) else i for i in lst)

def process(r,c,R,C,S,B,countT):
    
    if r==3 and c==3:
        print()
    global ans
    ans = max(ans,countT)
    if to_tuple(B) in S:
        return
    S.add(to_tuple(B))
    if (R-r<3 or C-c<3):
        ans = max(ans,countT)
        return
    
    if B[r][c] == '.' and B[r][c+1] == '.' and B[r][c+2] == '.' and B[r+1][c+1] == '.' and B[r+2][c+1] == '.':
        B[r][c] = '#'
        B[r][c+1] = '#'
        B[r][c+2] = '#'
        B[r+1][c+1] = '#'
        B[r+2][c+1] = '#'
        if c+3>=C:
            process(r+1,0,R,C,S,B,countT+1)
        else:
            process(r,c+1,R,C,S,B,countT+1)
        B[r][c] = '.'
        B[r][c+1] = '.'
        B[r][c+2] = '.'
        B[r+1][c+1] = '.'
        B[r+2][c+1] = '.'
        
    if B[r+1][c] == '.' and B[r+1][c+1] == '.' and B[r+1][c+2] == '.' and B[r][c+2] == '.' and B[r+2][c+2] == '.':
        B[r+1][c] = '#'
        B[r+1][c+1] = '#'
        B[r+1][c+2] = '#'
        B[r][c+2] = '#'
        B[r+2][c+2] = '#'
        if c+3>=C:
            process(r+1,0,R,C,S,B,countT+1)
        else:
            process(r,c+1,R,C,S,B,countT+1)
        B[r+1][c] = '.'
        B[r+1][c+1] = '.'
        B[r+1][c+2] = '.'
        B[r][c+2] = '.'
        B[r+2][c+2] = '.'
        
        
    if B[r+2][c] == '.' and B[r+2][c+1] == '.' and B[r+2][c+2] == '.' and B[r][c+1] == '.' and B[r+1][c+1] == '.':
        B[r+2][c] = '#'
        B[r+2][c+1] = '#'
        B[r+2][c+2] = '#'
        B[r][c+1] = '#'
        B[r+1][c+1] = '#'
        if c+3>=C:
            process(r+1,0,R,C,S,B,countT+1)
        else:
            process(r,c+1,R,C,S,B,countT+1)
        B[r+2][c] = '.'
        B[r+2][c+1] = '.'
        B[r+2][c+2] = '.'
        B[r][c+1] = '.'
        B[r+1][c+1] = '.'
        
    if B[r][c] == '.' and B[r+1][c] == '.' and B[r+2][c] == '.' and B[r+1][c+1] == '.' and B[r+1][c+2] == '.':
        B[r][c] = '#'
        B[r+1][c] = '#'
        B[r+2][c] = '#'
        B[r+1][c+1] = '#'
        B[r+1][c+2] = '#'
        if c+3>=C:
            process(r+1,0,R,C,S,B,countT+1)
        else:
            process(r,c+1,R,C,S,B,countT+1)
        B[r][c] = '.'
        B[r+1][c] = '.'
        B[r+2][c] = '.'
        B[r+1][c+1] = '.'
        B[r+1][c+2] = '.'
        

R,C = [int(i) for i in input().split()]
ans = 0
S = set()
B = [ ["."]*C for i in range(R) ]
process(0,0,R,C,S,B,0)
print(ans)
print(S)
        