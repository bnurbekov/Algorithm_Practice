class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        D = [[None]*(len(A)) for i in xrange(len(A[0]))]
        
        m = len(A)
        n = len(A[0])

        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if A[i][j] == 0:
                    continue

                if i == m-1 and j == n-1:
                    D[m-1][n-1] = (m-1, n-1)
                elif i == m-1:
                    D[i][j]=(i, j if A[i][j+1]==0 else D[i][j+1][1])
                elif j == n-1:
                    D[i][j]=(i if A[i+1][j]==0 else D[i+1][j][0], j)
                else:
                    if A[i+1][j] == 0 and A[i][j+1] == 0:
                        y = i
                        x = j
                    elif A[i][j+1] == 0:
                        x = j
                        y = D[i+1][j][0]
                    elif A[i+1][j] == 0:
                        y = i
                        x = D[i][j+1][1]
                    else: 
                        if 1+D[i+1][j][0]-i >= D[i][j+1][0]-i:
                            y = D[i][j+1][0]
                        else:
                            y = D[i+1][j][0]
 
                        if 1+D[i][j+1][1]-j >= D[i+1][j][1]-i:
                            x = D[i+1][j][1]
                        else:
                            x = D[i][j+1][1]
                    
                    D[i][j] = (y, x)
                  
        with open('data.csv', 'w') as f:          
            for row in D:
                f.write(",".join([str(col[0])+";"+str(col[1]) if col != None else "None" for col in row]) + "\n")

        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j] == 1:
                    res = max(res, (D[i][j][0]-i+1)*(D[i][j][1]-j+1))
                    
        return res

if __name__ == "__main__":
    print Solution().maximalRectangle([
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
])