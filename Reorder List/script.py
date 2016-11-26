# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLen(self, A):
        count = 0
        while A:
            count+=1
            A = A.next
            
        return count
    
    def reverseList(self, A):
        prev = None
        curr = A
        
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
        return prev
    
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        lLen = self.getLen(A)
        revStartInd = lLen/2-1 if lLen%2==0 else lLen/2
        revStart = A
        while revStartInd > 0:
            revStart = revStart.next
            revStartInd-=1
            
        root = A
        B = self.reverseList(revStart.next)
        revStart.next = None
        self.printList(root)
        self.printList(B)
        
        while B:
            nex_A = A.next
            nex_B = B.next
            A.next = B
            B.next = nex_A
            A = nex_A
            if not nex_B and lLen%2 != 0:
                B.next = A
                A.next = None
            B = nex_B

        self.printList(root)
        return root

    def printList(self, temp):
        while temp is not None:
            print temp.val,
            temp = temp.next
        print ""
        
        
if __name__ == "__main__":
    string  = "90 -> 34 -> 57 -> 26 -> 46 -> 101 -> 1 -> 75 -> 73 -> 45 -> 99 -> 61 -> 98 -> 96 -> 5 -> 74 -> 31 -> 91 -> 11 -> 36 -> 32 -> 70 -> 79 -> 100 -> 52 -> 14 -> 20 -> 19 -> 58 -> 33 -> 88 -> 23 -> 38 -> 55 -> 17 -> 65 -> 81 -> 44 -> 78 -> 85 -> 15 -> 49 -> 10 -> 51 -> 47 -> 77 -> 41 -> 12 -> 4 -> 43 -> 87 -> 24"
    l = string.split(" -> ")
    l = [int(exp) for exp in l]
    root = head = ListNode(l[0])
    for i in xrange(1, len(l)):
        head.next = ListNode(l[i])
        head = head.next

    head = Solution().reorderList(root)
