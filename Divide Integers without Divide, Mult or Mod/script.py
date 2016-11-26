import sys

class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0 or (dividend == -sys.maxint-1 and divisor == -1):
            return sys.maxint
            
        if (dividend < 0) ^ (divisor < 0):
            mult = -1
        else:
            mult = 1
        
        dividend, divisor = abs(dividend), abs(divisor)
    
        result = 0
        
        while dividend >= divisor:
            numOfShifts = 0
            while (divisor << numOfShifts) <= dividend:
                numOfShifts += 1
                
            numOfShifts -= 1
                
            result += 1 << numOfShifts
            
            dividend -= (divisor << numOfShifts)
            
        return result * mult

if __name__ == "__main__":
    sol = Solution()
    print sol.divide(-2147483648, -1)