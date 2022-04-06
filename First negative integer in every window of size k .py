def printFirstNegativeInteger( A, N, K):
    i,j,neg=0,K-1,0
    if K>N:
        return [-1]
    l=[]
    while j<N:
        if neg<i:
            neg=i
        while neg<j:
            if A[neg]<0:
                break
            neg+=1
        if A[neg]<0:
            l.append(A[neg])
        else:
            l.append(0)
            
        i+=1
        j+=1
    return l
    
