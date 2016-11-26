class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, A):
        cache = dict()
        
        A.sort()
        sz = None
        for size in xrange(1, len(A)):
            res = []
            if self.isPossible(0, size, float(sum(A))/len(A)*size, cache, A):
                sz = size
                break
    
        res = [[],[]]
            
        if sz == None:
            return []
    
        self.reconstruct(0, sz, float(sum(A))/len(A)*size, cache, A, res)
        
        return res
        
    def isPossible(self, ind, curr_size, curr_sum, cache,A):
        if curr_size == 0:
            if 0.005 >= curr_sum >= -0.005:
                print curr_sum 
            return curr_sum == 0
            
        if ind >= len(A):
            return False
        
        curr_item = (ind, curr_size, curr_sum)
        
        if curr_item not in cache:
            cache[curr_item] = False
            if self.isPossible(ind+1, curr_size-1, curr_sum-A[ind], cache,A):
                cache[curr_item] = True
            if not cache[curr_item]:
                if self.isPossible(ind+1, curr_size, curr_sum, cache, A):
                    cache[curr_item] = True
        
        return cache[curr_item]
        
    def reconstruct(self, ind, curr_size, curr_sum, cache, A, res):
        if ind >= len(A):
            return
        
        if self.isPossible(ind+1, curr_size-1, curr_sum-A[ind], cache,A):
            res[0].append(A[ind])
            self.reconstruct(ind+1, curr_size-1, curr_sum-A[ind], cache, A, res)
        elif self.isPossible(ind+1, curr_size, curr_sum, cache, A):
            res[1].append(A[ind])
            self.reconstruct(ind+1, curr_size, curr_sum, cache, A, res)
        
if __name__ == "__main__":
    print Solution().avgset([ 16, 42, 18, 48, 26, 45, 46, 26, 25, 7, 7, 48, 30, 10, 10, 3, 1, 11, 33, 14, 21, 15 ])