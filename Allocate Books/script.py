class Solution:
    def isPossible(self, target, A, B):
        isP = True
        B -= 1
        pCount = 0
        for p in A:
            if pCount + p > target:
                if B == 0 or p > target:
                    isP = False 
                    break
                else:
                    pCount = 0
                    B -= 1
                    
            pCount += p
                    
        return isP
    
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if len(A) < B:
            return -1
            
        l = 0
        r = sum(A)
        ans = -1
        
        while r>=l:
            m = l + (r-l)/2
            
            if self.isPossible(m, A, B):
                ans = m
                r = m - 1   
            else:
                
                l = m + 1
                
        return ans

if __name__ == "__main__":
    s = Solution()
    print s.books([ 73, 58, 30, 72, 44, 78, 23, 9 ], 5)