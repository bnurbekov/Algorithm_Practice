def flip(A):
    best = value = 0
    bestIs = [1, 1]
    currIs = [1, 1]
    
    for i, el in enumerate(A):
        if el == "0":
            value += 1
        else:
            value -= 1
        
        #print value, bestInds, el

        if value < 0:
            currIs[0] = currIs[1] = i+1
            value = 0
        else:
            if value > best:
                best = value
                bestIs[1] = i+1
        
    return bestIs if best != 0 else []

if __name__ == "__main__":
 	print flip("011")