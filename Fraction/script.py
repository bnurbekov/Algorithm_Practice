class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        output = []
        if (numerator < 0 or denominator < 0) and (numerator > 0 or denominator > 0) and abs(numerator) < abs(denominator):
            output.append("-")
        
        output.append(str(int(float(numerator)/denominator)))
        output.append(".")
        
        denominator = abs(denominator)
        
        remainder_dict = dict()
        remainder = abs(numerator)%denominator
        
        while remainder != 0:
            print remainder
            if remainder in remainder_dict:
                output.insert(remainder_dict[remainder], "(")
                output.append(")")
                break
            
            remainder_dict[remainder] = len(output)
            
            remainder *= 10
            
            while remainder < denominator:
                output.append("0")
                remainder *= 10
                
            fractionalPart = str(remainder / denominator)
    
            output.append(fractionalPart)
            remainder = remainder % denominator
            
        if output[-1] == ".":
            output.pop()
            
        return ''.join(output)


sol = Solution()
print sol.fractionToDecimal(826, 393)