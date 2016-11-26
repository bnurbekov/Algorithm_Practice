#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        if A is None or A.next is None:
            return A
            
        partL = None
        partR = A
        print "Hi"
        while partR and partR.val < B:
            partL = partR
            partR = partR.next
            print partR.val
            
        if partR is None or partR.next is None:
            return A
            
        prev = partR
        curr = prev.next
        while curr:
            print curr.val
            if curr.val < B:
                nex = curr.next
                
                if partL is None:
                    A = partL = curr
                else:
                    partL.next = curr
                    partL = partL.next
                    
                partL.next = partR
                prev.next = nex
                curr = nex
            else:
                prev = curr
                
        return A

if __name__ == "__main__":
    l = [1,4,3,2,5,2]
    root = head = ListNode(l[0])
    for i in xrange(1, len(l)):
        head.next = ListNode(l[i])
        head = head.next
    print Solution().partition(root, 3)