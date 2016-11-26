import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        random.seed(1000)

    def getLen(self, A):
        count = 0
        while A:
            count += 1
            A = A.next
            
        return count
    
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        return self.sortListHelper(A)
        
    def getValAtInd(self, A, ind):
        curr_ind = 0
        while ind != curr_ind:
            A = A.next
            curr_ind += 1
            
        return A.val
        
    def getTail(self, A):
        self.printList(A)
        while A.next:
            A = A.next
        
        return A
        
    def sortListHelper(self, A):
        count = self.getLen(A)
        if count == 0 or count == 1:
            return A
            
        #Randomly generate index for partition
        value = self.getValAtInd(A, random.randrange(count))
        leftHalf, partitionNode = self.partition(A, value)
        
        if partitionNode == None:
            leftHalf, partitionNode = self.partition(leftHalf, leftHalf.next.val)
            if not partitionNode:
                return leftHalf
        
        rightHalf = partitionNode.next
        partitionNode.next = None
        
        leftHalf = self.sortListHelper(leftHalf)
        rightHalf = self.sortListHelper(rightHalf)
        
        self.getTail(leftHalf).next = rightHalf
        
        return leftHalf
        
    def printList(self, temp):
        while temp is not None:
            print temp.val,
            temp = temp.next
        print ""

    def partition(self, A, B):
        if A is None or A.next is None:
            return None, A
            
        partL = None
        partR = A
        
        while partR and partR.val < B:
            partL = partR
            partR = partR.next

        if partR is None or partR.next is None:
            return partL, A
            
        prev = partR
        curr = prev.next
        
        while curr:
            if curr.val < B:
                nex = curr.next
                
                if partL is None:
                    A = partL = curr
                else:
                    partL.next = curr
                    partL = partL.next
                    
                partL.next = partR
                curr = nex
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return A, partL

if __name__ == "__main__":
    string  = "5 -> 66 -> 68 -> 42 -> 73 -> 25 -> 84 -> 63 -> 72 -> 20 -> 77 -> 38 -> 8 -> 99 -> 92 -> 49 -> 74 -> 45 -> 30 -> 51 -> 50 -> 95 -> 56 -> 19 -> 31 -> 26 -> 98 -> 67 -> 100 -> 2 -> 24 -> 6 -> 37 -> 69 -> 11 -> 16 -> 61 -> 23 -> 78 -> 27 -> 64 -> 87 -> 3 -> 85 -> 55 -> 22 -> 33 -> 62"
    l = string.split(" -> ")
    l = [int(exp) for exp in l]
    root = head = ListNode(l[0])
    for i in xrange(1, len(l)):
        head.next = ListNode(l[i])
        head = head.next
    Solution().sortList(root)