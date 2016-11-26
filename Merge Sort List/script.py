import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLen(self, A):
        count = 0
        while A:
            count += 1
            A = A.next
            
        return count
    
    def findNodeAt(self, A, ind):
        while ind > 0:
            A = A.next
            ind -= 1
        return A
    
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if A is None:
            return None
        elif A.next is None:
            return A
        
        lLen = self.getLen(A)
        
        left_tail = self.findNodeAt(A, lLen/2-1)
        right_head = left_tail.next
        left_tail.next = None
        sorted_left = self.sortList(A)
        sorted_right = self.sortList(right_head)
        print "Left, right"
        self.printList(sorted_left) 
        self.printList(sorted_right)
        res = self.merge(sorted_left, sorted_right)
        print "Merged:"
        self.printList(res)
        return res
        
    def merge(self, left, right):
        root = None
        if not right or left and left.val <= right.val:
            root = curr = left
            left = left.next
        else:
            root = curr = right
            right = right.next
            
        while left or right:
            if not right or left and left.val <= right.val:
                curr.next = left
                curr = left
                left = left.next
            else:
                curr.next = right
                curr = right
                right = right.next
                
        return root

    def printList(self, temp):
        while temp is not None:
            print temp.val,
            temp = temp.next
        print ""
      
if __name__ == "__main__":
    string  = "5 -> 66 -> 68 -> 42 -> 73 -> 25 -> 84 -> 63 -> 72 -> 20 -> 77 -> 38 -> 8 -> 99 -> 92 -> 49 -> 74 -> 45 -> 30 -> 51 -> 50 -> 95 -> 56 -> 19 -> 31 -> 26 -> 98 -> 67 -> 100 -> 2 -> 24 -> 6 -> 37 -> 69 -> 11 -> 16 -> 61 -> 23 -> 78 -> 27 -> 64 -> 87 -> 3 -> 85 -> 55 -> 22 -> 33 -> 62"
    l = string.split(" -> ")
    l = [int(exp) for exp in l]
    root = head = ListNode(l[0])
    for i in xrange(1, len(l)):
        head.next = ListNode(l[i])
        head = head.next

    head = Solution().sortList(root)