import sys

class Solution:
    def countEntropy(self, i_b, i_e, A):
        whiteCount = 0
        blackCount = 0
        assert 0<=i_b<len(A), 0<=i_e<len(A)
        print "IB< IE:", i_b, i_e

        for i in xrange(i_b, i_e+1):
            if A[i] == "b":
                blackCount += 1
            elif A[i] == "w":
                whiteCount += 1
            else:
                raise ValueError("Unrecognized character is present in the input string.")
                
        #print whiteCount, blackCount, i_b, i_e

        return whiteCount*blackCount
    
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, B):
        if A is None or len(A) == 0 or B > len(A)-1:
            return -1
        A = A.lower()
        dp = [[None]*(len(A)) for i in xrange(B)] #1 based string indices

        for st_i in xrange(0, B):
            i_b, i_e = (st_i if st_i != B-1 else len(A)-1), len(A)-B+st_i
            
            print i_b, i_e+1
            for i in xrange(i_b,i_e+1):
                if st_i == 0:
                	print 0, i, self.countEntropy(0, i, A)
	                dp[st_i][i] = self.countEntropy(0, i, A)
                else:
                    minScore = sys.maxint
                    for j in xrange(st_i-1, i):
                        score = dp[st_i-1][j] + self.countEntropy(j+1, i, A)
                        minScore = score if score < minScore else minScore
                        print "J, I, VAL:", j, i, dp[st_i-1][j]
                
                    dp[st_i][i] = minScore

                #print dp[st_i][i], st_i, i
        
        print dp
        return dp[st_i][i]

if __name__ == "__main__":
	print Solution().arrange("WBWB", 2)
	#print Solution().countEntropy(0, 0, "wbwb")