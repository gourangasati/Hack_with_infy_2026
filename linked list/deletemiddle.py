# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head) :
        slow = head
        fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        current = head
        while current.val == slow.val:
            current = current.next
        current.next = slow.next
        return ListNode

        