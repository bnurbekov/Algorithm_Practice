class Solution:
    def getDigNum(self, num):
        count = 0
        while num > 0:
            count += 1
            num /= 10
            
        return count

    def stepNumHelper(self, l, num, A, B, res):        
        if num < A/(10**l) or num > (B/(10**l) if B/(10**l) != 0 else 9):
            if l == 0:
                print "L0", num, A/(10**l), (B/(10**l) if B/(10**l) != 0 else 9)
            return

        if l == 0:
            res.append(num)
            return
        
        lastD = num%10
        if lastD - 1 >= 0:
            self.stepNumHelper(l-1, num*10+lastD-1, A, B, res)
            
        if lastD + 1 <= 9:
            self.stepNumHelper(l-1, num*10+lastD+1, A, B, res)
            
        

    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        self.cache = dict()
        res = []
        dn_B = self.getDigNum(B)
        dn_A = self.getDigNum(A)
        
        for level in xrange(dn_A, dn_B+1): 
            for i in xrange(0, 10):
                self.stepNumHelper(level, i, A, B, res)
            
        return res

if __name__ == "__main__":
    print Solution().stepnum(10, 20)