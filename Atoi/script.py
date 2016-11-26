import sys

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        maxNegative = -sys.maxint-1
        maxPositive = sys.maxint
        num = 0
        signPositive = True
        foundChar = False
        for c in A:
            if (c == " " or c == "+") and not foundChar:
                continue
            elif c == "-" and not foundChar:
                signPositive = False
                continue
            elif c == " " or ord(c) < ord("0") or ord(c) > ord("9"):
                break
            else:
                foundChar = True
                    
                if signPositive:
                    num = num*10 + ord(c)-ord("0")
                    num = num if num <= maxPositive else maxPositive
                else:
                    print c, str(num), num*10   
                    num = num*10 - ord(c)+ord("0")
                    print  -ord(c)+ord("0"), str(num)
                    num = num if num >= maxNegative else maxNegative
                
        return num

if __name__ == "__main__":
    print Solution().atoi(" -88297 248252140B12 37239U4622733246I218  9 1303   44 A83793H3G2 1674443R591 4368 7  97")
