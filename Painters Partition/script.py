def isPossible(target, nPainters, bLenList, painterSpeed):
        isP = True
        
        nPainters -= 1
        alreadyDoing = 0
        for bLen in bLenList:
            time = painterSpeed * bLen
            print alreadyDoing + time
            if alreadyDoing + time > target:
                if nPainters == 0 or time > target:
                    isP = False
                    break
                else:
                    print "Selected new painter."
                    nPainters -= 1
                    alreadyDoing = 0
            
            alreadyDoing += time
            
                    
        return isP

if __name__ == "__main__":
    print isPossible(11880, 3, [ 640, 435, 647, 352, 8, 90, 960, 329, 859 ], 10)