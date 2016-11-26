class ITNode:
    def __init__(self, r1, r2):
        self.c = 0
        self.r1 = r1
        self.r2 = r2
        self.left = None
        self.right = None

    def put(self, ind):
        self.c += 1
        
        res = None
        if self.r2 - self.r1 == 1:
            res = self.r1
        else:
            mid = self.r1 + (self.r2-self.r1)/2
            self.left = self.left if self.left else ITNode(self.r1, mid)
            self.right = self.right if self.right else ITNode(mid, self.r2)
            freeSlotsInLeft = mid - self.r1 - self.left.c
            if ind <= freeSlotsInLeft:
                res = self.left.put(ind)
            else:
                res = self.right.put(ind-freeSlotsInLeft)
                
        return res

    def pri(self, d):
        print "-"*d, "Node:", "[", self.r1, self.r2, "]", self.c
        if self.left:
            self.left.pri(d+1)
        if self.right:
            self.right.pri(d+1)

class Solution:
	# @param heights : list of integers
	# @param infronts : list of integers
	# @return a list of integers
    def order(self, heights, infronts):
        h_data = []
        for i in xrange(len(heights)):
            h_data.append((heights[i], infronts[i]))
            
        h_data.sort(key=lambda x:x[0])
        
        root = ITNode(0, len(h_data))
        res = [None]*len(h_data)
        print "H_data:", h_data
        for h in h_data:
            res[root.put(h[1]+1)] = h[0] 

        root.pri(0)

        return res

if __name__=="__main__":
    print "Res:", Solution().order([ 86, 92, 49, 21, 62, 27, 90, 59 ], [ 2, 0, 0, 2, 0, 2, 1, 3 ])