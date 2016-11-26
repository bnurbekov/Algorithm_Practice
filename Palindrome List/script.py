# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLen(self, head):
        count = 0 
        while head:
            count += 1
            head = head.next
            
        return count
            
    def find(self, ind, head):
        curr_ind = 0
        while curr_ind != ind:
            if head is None:
                raise ValueError(str(ind) + " " + str(prev.val))
            
            head = head.next
            curr_ind += 1
        
        return head
        
    def revert(self, head):
        root = head
            
        prev = head.next
        while prev:
            #print head.val, prev.val, prev.next.val
            #head, prev, prev.next = prev, prev.next, head
            temp = prev.next
            prev.next = head
            head = prev
            prev = temp
            
        root.next = None
            
        return head
    
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        length = self.getLen(A)
        if length == 0 or length == 1:
            return True
            
        print length
        revStartInd = length/2 if (length % 2) == 0 else length/2+1
        print revStartInd
        revStartNode = self.find(revStartInd, A)
        print revStartNode.val
        revHead = self.revert(revStartNode)
        first = A
        second = revHead
        self.printList(A)
        
        self.printList(revHead)

        res = True
        ind = 0
        print length/2
        while ind != length/2:
            print first.val, second.val
            if first.val != second.val:
                res = False
                break
            
            ind += 1
            
        self.revert(revHead)
        self.printList(A)
        
        return int(res)

    def printList(self, temp):
        while temp is not None:
            print temp.val,
            temp = temp.next
        print ""

if __name__ == "__main__":
    l = [ 1 , 1 , 6 , 4 , 1 ]
    root = head = ListNode(l[0])
    for i in xrange(1, len(l)):
        head.next = ListNode(l[i])
        head = head.next

    temp = root

    print "Reverting"
    head = Solution().lPalin(root)