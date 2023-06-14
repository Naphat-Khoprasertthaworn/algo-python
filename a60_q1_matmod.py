def addMod( lhs,rhs,k ):
    return ( lhs%k + rhs%k )%k

def mulMod( lhs,rhs,k ):
    return ( lhs%k * rhs%k )%k

def matMul(lhs,rhs,k):
    l = [0]*4
    l[0] = addMod(mulMod( lhs[0],rhs[0],k ) , mulMod( lhs[1],rhs[2],k ) ,k)
    l[1] = addMod(mulMod( lhs[0],rhs[1],k ) , mulMod( lhs[1],rhs[3],k ) ,k)
    l[2] = addMod(mulMod( lhs[2],rhs[0],k ) , mulMod( lhs[3],rhs[2],k ) ,k)
    l[3] = addMod(mulMod( lhs[2],rhs[1],k ) , mulMod( lhs[3],rhs[3],k ) ,k)
    return l

def matMod( matrix,n,k ):
    if(n==1):
        return matrix
    
    mid = n//2
    frac = n%2
    halfMat = matMod(matrix,mid,k)
    
    newMat = matMul( halfMat,list(halfMat),k );
    if(frac==1):
        newMat = matMul( newMat,matrix,k )
    return newMat
    
    
n,k = [int(i) for i in input().split()]

matrix = [int(i) for i in input().split()]

newMat = matMod(matrix,n,k)
for i in range(4):
    print( str(newMat[i]),end = " " )

