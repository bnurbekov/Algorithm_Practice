import sys

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        if len(A) < len(B):
            A,B=B,A
        
        A_len = len(A)
        B_len = len(B)
        
        if B_len == 0:
            return A[A_len/2] if A_len%2 == 1 else (A[A_len/2-1]+A[A_len/2])/2.0
        
        l = (A_len-B_len+1)/2
        r = (A_len+B_len+1)/2

        print r, l
        
        median = None
        
        while r>=l:
            m = l + (r-l)/2
            j = (A_len + B_len + 1)/2 - m
            
            if j!=0 and m!=A_len and A[m] < B[j-1]:  
                l = m + 1
            elif m!=0 and j!=B_len and B[j] < A[m-1]:
                r = m - 1
            else:
                print m, j
                maxALeft = maxBLeft = -sys.maxint-1
                minARight = minBRight = sys.maxint
                if A_len > m:
                    minARight = A[m]
                    
                if m > 0:
                    maxALeft = A[m-1]

                if B_len > j:
                    minBRight = B[j]

                if j > 0:
                    maxBLeft = B[j-1]
                
                if (A_len+B_len)%2 == 0:
                    median = (max(maxALeft, maxBLeft) + min(minARight, minBRight))/2.0
                else:
                    median = max(maxALeft, maxBLeft)
                    
                break
                
        return median

if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays([ 35 ], [ 1, 26, 35, 49 ])