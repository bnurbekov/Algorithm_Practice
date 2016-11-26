# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
        # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        return self.convertToLL(self.parseNum(A) + self.parseNum(B))
        
    def convertToLL(self, num):
        head = None
        
        while num:
            digit = num % 10
            if head:
                node.next = ListNode(digit)
                node = node.next
            else:
                head = node = ListNode(digit)
            num /= 10

        print head.val, head.next.val, head.next.next.val
            
        return head
        
    def parseNum(self, head):
        num = 0
        c = 0
        while head:
            num = num+head.val*10**c
            c += 1
            head = head.next
            
        return num

if __name__ == "__main__":
    A = ListNode(9)
    A.next = ListNode(9)
    A.next.next = ListNode(1)
    B = ListNode(1)
    print Solution().addTwoNumbers(A, B)