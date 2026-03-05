class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def getIntersectionNode(self, headA, headB):
        currentA = headA
        currentB = headB
        while currentA:
            while currentB:
                if currentA.val == currentB.val:
                    return currentA.val
                currentB = currentB.next
            currentA = currentA.next
        error