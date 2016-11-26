def findLCS(A, B):
    m = len(A)
    n = len(B)

    D = [[None]*(n+1) for i in xrange(m+1)]
    
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                D[i][j] = 0
            elif A[i-1] == B[j-1]:
                D[i][j] = 1 + D[i-1][j-1]
            else:
                D[i][j] = D[i-1][j] if D[i-1][j] > D[i][j-1] else D[i][j-1]

    print D
                
    return D[i][j]

if __name__ == "__main__":
    print findLCS("a", "avvvvada")