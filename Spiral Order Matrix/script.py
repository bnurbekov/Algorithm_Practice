class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        res = [[None]*A for i in xrange(A)]
        
        res[0][0] = 1
        prevPointer = [0,0]
        nextPointer, offset = self.getNext(prevPointer, 0, A)
        while nextPointer != None:
        	print "PP: ", prevPointer, "NP: ", nextPointer
        	res[nextPointer[1]][nextPointer[0]] = res[prevPointer[1]][prevPointer[0]] + 1
        	prevPointer = nextPointer
        	nextPointer, offset = self.getNext(prevPointer, offset, A)
        
        return res
            
    def getNext(self, currentInd, offset, size):
        if size % 2 == 0:
            x = size/2-1
            y = size/2
        else:
            x = y = size/2
        
        if currentInd[0] == x and currentInd[1] == y:
            return (None, offset)
        
        maxInd = size - 1
        if currentInd[1] == offset:
            if currentInd[0] == maxInd-offset:
                currentInd[1] += 1
            else:
                currentInd[0] += 1
        elif currentInd[0] == maxInd-offset:
            if currentInd[1] == maxInd-offset:
                currentInd[0] -= 1
            else:
                currentInd[1] += 1
        elif currentInd[1] == maxInd-offset:
            if currentInd[0] == offset:
                currentInd[1] -= 1
            else:
                currentInd[0] -= 1
        elif currentInd[0] == offset:
            if currentInd[1] == offset+1:
                offset += 1
                currentInd[0] += 1
            else:
                currentInd[1] -= 1
                
        return (currentInd, offset)

if __name__ == "__main__":
	print Solution().generateMatrix(4)