def findCeilingIndex(el, tailList, tlLen):
    l = 0
    r = tlLen - 1
    
    while l < r:
        mid = l + (r - l)/2
        if tailList[mid] < el:
            l = mid + 1
        else:
            r = mid
            
    return l

if __name__ == "__main__":
    a = [0, 1, 6, 8, 9, 12]
    print findCeilingIndex(8.5, a, len(a))