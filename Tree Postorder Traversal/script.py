class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        st = [A]
        res = []
        cameFrom = None

        while st:
            current = st[-1]
            if cameFrom != None and (cameFrom is current or cameFrom is current.right):
                res.append(current.val)
                cameFrom = current
                st.pop()
            elif cameFrom is current.left:
                cameFrom = current
            else:
                if current.right:
                    st.append(current.right)
                if current.left:
                    st.append(current.left)
                cameFrom = current  
                
        return res

    def createTree(self, l):
    	i = 1
    	tn = [None]*2*len(l)
    	tn[0] = TreeNode(l[i-1], None, None) if l[i-1] else None
    	print "Len l:", len(l)
    	while i <= len(l):
    		if l[i-1] != -1:
    			print i, i*2-1, i*2, l[i-1]
    			left = None if i*2-1 >= len(l) or l[i*2-1] == -1 else TreeNode(l[i*2-1], None, None)
    			right = None if i*2 >= len(l) or l[i*2] == -1 else TreeNode(l[i*2], None, None)
    			tn[i-1].left = left
    			tn[i-1].right = right
    			tn[i*2-1]=left
    			tn[i*2]=right

    		i += 1


    	return tn[0]

    def isSymmetric(self, A):
        if not A:
            return True

        st1 = [A.left]
        st2 = [A.right]
        
        while st1 and st2:
            c1 = st1.pop()
            c2 = st2.pop()
            
            if not c1 and not c2:
                continue
            
            if not c1 or not c2 or c1.val != c2.val:
                return False
            
            st1.append(c1.left)
            st1.append(c1.right)
            st2.append(c2.left)
            st2.append(c2.right)
            
        return True  

    def connect(self, root):
        next_root_p = root
        
        while next_root_p:
            print next_root_p.val
            root_p = next_root_p
            next_root_p = None
            prev_p = None
            while root_p:
            	print root_p.val
                if root_p.left:
                    print "Appended left"
                    if not next_root_p:
                        next_root_p = root_p.left
                        
                    if prev_p:
                        prev_p.next = root_p.left
                            
                    prev_p = root_p.left
                    
                if root_p.right:
                    print "Appended right"
                    if not next_root_p:
                        next_root_p = root_p.right
                        
                    if prev_p:
                        prev_p.next = root_p.right
                            
                    prev_p = root_p.right
                    
                root_p = root_p.next

    # @param inorder : list of integers denoting inorder traversal
    # @param postorder : list of integers denoting postorder traversal
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        return self.buildTreeHelper(0, len(inorder)-1, len(postorder)-1, inorder, postorder) 
        
    def buildTreeHelper(self, i_b, i_e, p, inorder, postorder):
        if i_e - i_b < 0:
            return None
            
        arr = inorder[i_b:i_e+1]
        print arr, i_b, i_e, i_e-i_b
        root_ind = arr.index(postorder[p])
        
        root = TreeNode(postorder[p])
        root.right = self.buildTreeHelper(root_ind+1, i_e, p-1, inorder, postorder)
        root.left = self.buildTreeHelper(i_b, root_ind-1, p-1-(i_e-root_ind), inorder, postorder)
        
        return root

if __name__ == "__main__":
	#a = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5, None, None), TreeNode(6, None, None)), TreeNode(4, TreeNode(7, None, None), TreeNode(8, None, None))), TreeNode(9, None, None))
	b = "67 0 4 4 10 6 6 10 16 3 14 9 9 14 3 16 13 -1 7 11 -1 -1 -1 15 15 -1 -1 -1 11 7 -1 13 -1 12 -1 1 -1 -1 -1 -1 -1 -1 -1 -1 1 -1 12 -1 8 -1 5 2 2 5 -1 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"
	b = [int(st) for st in b.split(" ")]
	Solution().buildTree([ 2, 1, 3 ], [ 2, 3, 1 ])
	#print Solution().postorderTraversal(a)