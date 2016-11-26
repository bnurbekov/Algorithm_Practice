from Queue import Queue

class Solution:
    # @param A : integer
    # @return a string
    def multiple(self, A):
        if A == 0:
            return "0"
        
        value = dict()
        
        rem = 1%A
        value[rem] = "1"
        q = Queue()
        q.put(rem)
        
        res = None
        
        while not q.empty():
            curr = q.get()
            
            if curr == 0:
                break
            else:
                rem = (curr*10)%A
                if rem not in value:
                    value[rem] = value[curr]+"0"
                    q.put(rem)
                
                rem += 1
                if rem >= A:
                    rem -= A
                
                if rem not in value:
                    value[rem] = value[curr]+"1"
                    q.put(rem)
                    
        return value[0]

if __name__ == "__main__":
    print Solution().multiple(999)