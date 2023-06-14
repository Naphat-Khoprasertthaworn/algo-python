
numCourses = 2
prerequisites = [ [1,0] ]
def DFS(M,V,v,b):
    if b[0]==True:
        return
    V[v] = 1
    for i in M[v]:
        if V[i]==0:
            DFS(M,V,i,b)
            if b[0]==True:
                return
        elif V[i] == 1:
            b[0] = True
            return
    V[v] = 2
    
n = numCourses
M = [[] for i in range(n)]
for i,j in prerequisites:
    M[i].append(j)
    print(M)
    V = [0]*n
    b = [False]
    for i in range(n):
        if V[i]==0:
            DFS(M,V,i,b)
            if b[0]==True:
                print("false")
                #return False
    if b[0]==False:
        print("true")
        #return True

