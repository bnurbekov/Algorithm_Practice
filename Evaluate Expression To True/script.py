import operator

class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        trueDP = [[None] * len(A) for i in xrange(len(A))]
        falseDP = [[None] * len(A) for i in xrange(len(A))]
        
        for i in xrange(len(A)):
            if A[i] == "T":
                trueDP[i][i] = 1
                falseDP[i][i] = 0
            elif A[i] == "F":
                trueDP[i][i] = 0
                falseDP[i][i] = 1
                
        for size in xrange(3, len(A)+1, 2):
            for i in xrange(0, len(A)-size+1, 2):
                j = i+size-1
                trueDP[i][j] = falseDP[i][j] = 0  
                for k in xrange(i, j+1):  
                    if A[k] == "|" or A[k] == "^" or A[k] == "&":
                        print "I,J,K:", i, j, k, A[k], "TRUE, FAlse, True, False", trueDP[i][k-1], falseDP[i][k-1], trueDP[k+1][j], falseDP[k+1][j], str(i) + "-" + str(k-1), str(k+1) + "-" + str(j)
                        if A[k] == "|":
                            trueDP[i][j] += trueDP[i][k-1]*falseDP[k+1][j] + falseDP[i][k-1]*trueDP[k+1][j] \
                            + trueDP[i][k-1]*trueDP[k+1][j]
                        elif A[k] == "&":
                            trueDP[i][j] += trueDP[i][k-1]*trueDP[k+1][j]
                        elif A[k] == "^":
                            trueDP[i][j] += trueDP[i][k-1]*falseDP[k+1][j] + falseDP[i][k-1]*trueDP[k+1][j]
                            
                        if A[k] == "|":
                            falseDP[i][j] += falseDP[i][k-1]*falseDP[k+1][j]
                        elif A[k] == "&":
                            falseDP[i][j] += falseDP[i][k-1]*falseDP[k+1][j] + trueDP[i][k-1]*falseDP[k+1][j] \
                            + falseDP[i][k-1]*trueDP[k+1][j] 
                        elif A[k] == "^":
                            falseDP[i][j] += falseDP[i][k-1]*falseDP[k+1][j] + trueDP[i][k-1]*trueDP[k+1][j]

                        print "After", trueDP[i][j], falseDP[i][j]
                        print falseDP[2][4]
                        
        print trueDP
        print falseDP
        return trueDP[0][len(A)-1]

if __name__ == "__main__":
    print Solution().cnttrue("F|T^T&F")