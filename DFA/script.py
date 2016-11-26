class Solution:
    def automata(self, A, B, C, D, E):
        return self.autoH(A, B, set(C), D, E)
        
    def autoH(self, zeroN, oneN, finalSs, initS, maxD):
        stack = [initS]
        res = 0
        nextState = [0] * len(oneN)
        while len(stack) != 0:
            currS = stack[-1]
            if len(stack) - 1 == maxD:
                if currS in finalSs:
                    res += 1
                #print currS, stack
                stack.pop()
                continue
            
            d = len(stack) - 1
            print currS, d

            #print len(stack), d, nextState[d]
            if nextState[d] == 0:
                print zeroN[currS]
                stack.append(zeroN[currS])
                nextState[d] += 1
            elif nextState[d] == 1:
                print oneN[currS]
                stack.append(oneN[currS])
                nextState[d] = None
            else:
                stack.pop()
            
        return res
        
if __name__ == "__main__":
	Solution().automata([ 0, 2, 1 ], [ 1, 0, 2 ], [ 0 ], 0, 2)