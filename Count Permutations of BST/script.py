import math

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cntPermBST(self, A, B):
        dp=[[None]*(A+1) for i in xrange(B+1)]
        for num in xrange(2, A+1):
            dp[0][num] = 0

        for height in xrange(B+1):
            for num in xrange(A+1):
                if dp[height][num] == None:
                    if num <= 1:
                        if height == 0:
                            dp[height][num] = 1
                        else:
                            dp[height][num] = 0
                    else:
                        dp[height][num] = 0
                        for i in xrange(1, num+1):
                            x = i - 1
                            y = num - i
                            res = 0
        
                            for j in xrange(height-1):
                                res += dp[height-1][x] * dp[j][y] 
        
                            for j in xrange(height-1):
                                res += dp[height-1][y] * dp[j][x] 
                                
                            res += dp[height-1][x] * dp[height-1][y] 
        
                            res *= math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
                            dp[height][num] += res
                            
        return dp[height][num]

    def cntPermBSTRec(self, A, B):
        dp=[[None]*(A+1) for i in xrange(B+1)]
        res = self.cntPermBSTH(1, A, B, dp)
        print dp

        return res

    def cntPermBSTH(self, indent, num, height, dp):
        if height < 0:
            return 0 
        print "-"*indent, "Called Func! N:", num, "H:", height
        if dp[height][num] == None:
            if num <= 1:
                if height == 0:
                    dp[height][num] = 1
                else:
                    dp[height][num] = 0
            else:
                print "-"*indent, "Doing work. Num:", num, "Height:" , height 
                dp[height][num] = 0
                for i in xrange(1, num+1):
                    x = i - 1
                    y = num - i
                    res = 0
                    print "-"*indent,"X:", x, "Y:", y
                    print "-"*indent,"Iterating through left heights"
                    for j in xrange(height-1):
                        res += self.cntPermBSTH(indent+1,x, height-1,dp) * self.cntPermBSTH(indent+1,y,j,dp) 
                    print "-"*indent,"RES", res
                    print "-"*indent,"Iterating through right heights"
                    for j in xrange(height-1):
                        res += self.cntPermBSTH(indent+1,y, height-1,dp) * self.cntPermBSTH(indent+1,x,j,dp) 
                    print "-"*indent,"RES", res
                    print "-"*indent,"Iterating equal height"
                    res += self.cntPermBSTH(indent+1,x, height-1,dp) * self.cntPermBSTH(indent+1,y, height-1,dp)
                    print "-"*indent,"RES", res 
                    res *= math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
                    print "-"*indent,"factorial", math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
                    dp[height][num] += res
                    print "-"*indent,"Final result:", dp[height][num]

        return dp[height][num]


if __name__ == "__main__":
    print Solution().cntPermBSTRec(5, 1)
    #print Solution().cntPermBSTRec(3, 2)