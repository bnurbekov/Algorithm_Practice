class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        upper = B
        lower = 1
        res = [None]*B
        print "ResLen"+ " " + str(len(res))
        print "Alen"+ " " + str(len(A))

        for i in xrange(B-2, -1, -1):
            print i, i+1
            if A[i] == "I":
                res[i+1] = upper
                upper -= 1
            else:
                res[i+1] = lower
                lower += 1
                
        res[0] = lower
        
        return res

if __name__ == "__main__":
    print Solution().findPerm("DIDD", 5)