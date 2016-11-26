class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        D = [-1]*(B+1)
        D[0] = 1
        
        for i in xrange(1, B+1):
            D[i] = 0
            
            for el in A:
                if i-el >= 0:
                    D[i] += D[i-el]

            print D[i]
        
        return D[i]

if __name__ == "__main__":
	sol = Solution()
	print sol.coinchange2([ 1, 2, 3 ], 4)