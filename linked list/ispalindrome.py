class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) :
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        print(slow)
        current = slow  
        while current:
            nxt = current.next  
            current.next = prev 
            prev = current      
            current = nxt       
        print(prev)
        print(head)
        while prev :
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True


        