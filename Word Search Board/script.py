class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    # def exist(self, A, B):
    #     res = False
    #     for i in xrange(len(A)):
    #         for j in xrange(len(A[i])):
    #             if self.matches((i, j), A, B, 0, pri = False):
    #                 res = True
    #                 break
                
    #     return int(res)
        
    # adjDiff = ((0, 1), (1, 0), (0, -1), (-1, 0))
               
    # def validPos(self, pos, A):
    #     return 0 <= pos[0] < len(A) and 0 <= pos[1] < len(A[0])
              
    # def matches(self, pos, A, B, i, pri = False):
    #     if i >= len(B):
    #         if pri:
    #             print "-"*i, "Returning True"
    #         return True

    #     if B[i] != A[pos[0]][pos[1]]:
    #         if pri:
    #             print "-"*i, "Not matching"
    #         return False

    #     print "-"*i, i, "Visiting:", A[pos[0]][pos[1]], "Matching Letter:",B[i], " Neighbors:"
            
    #     res = False
    #     for diff in Solution.adjDiff:
    #         nbr = (pos[0]+diff[0], pos[1]+diff[1])
    #         if self.validPos(nbr, A):
    #             if pri:
    #                 print "-"*i, A[nbr[0]][nbr[1]]
    #             res |= self.matches(nbr, A, B, i+1, pri=True)
            
    #     return res

    def exist(self, A, B):
        res = False
        for i in xrange(len(A)):
            for j in xrange(len(A[i])):
                if self.matches((i, j), A, B, 0):
                    res = True
                    break
                
        return int(res)
        
    adjDiff = ((0, 1), (1, 0), (0, -1), (-1, 0))
               
    def validPos(self, pos, A):
        return 0 <= pos[0] < len(A) and 0 <= pos[1] < len(A[0])
              
    def matches(self, pos, A, B, i):
        if i >= len(B):
            return True
            
        if B[i] != A[pos[0]][pos[1]]:
            return False
            
        res = False
        for diff in Solution.adjDiff:
            nbr = (pos[0]+diff[0], pos[1]+diff[1])
            if self.validPos(nbr, A):
                res |= self.matches(nbr, A, B, i+1)
            
        return res
        
if __name__=="__main__":
    print Solution().exist([ "FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF" ], "BCDCB")
