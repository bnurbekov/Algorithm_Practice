class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        shiftCount = 0
        prevEl = None
        for i in xrange(len(A)):
            prevIndex = i - 2
            if prevIndex >= 0 and A[prevIndex] == A[i]:
                shiftCount += 1
            
            A[i-shiftCount] = A[i]
                
        return len(A) - shiftCount

if __name__=="__main__":
    s = Solution()
    a=[ 0, 0, 0, 1, 1, 2, 2, 3 ]
    l= s.removeDuplicates(a)
    print l, a[0:l]