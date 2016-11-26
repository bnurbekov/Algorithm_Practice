class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        dp = [None] * (A*2+1)
        
        return self.chordCntHelper(A, dp)
    
    def chordCntHelper(self, A, dp):
        if A == 0 or A == 1:
            return 1
            
        if dp[A] == None:
            i = 1
            dp[A] = 0
            while i <= A*2-1:
                dp[A] += self.chordCntHelper((i-1)/2,dp) * self.chordCntHelper((A*2-i-1)/2,dp)
                print "DP:", dp[A], self.chordCntHelper((i-1)/2,dp), self.chordCntHelper((A-i-1)/2,dp),(A-i-1)/2, A, i, A-i, i
                i+=2

        return dp[A]

if __name__=="__main__":
    print Solution().chordCnt(2)