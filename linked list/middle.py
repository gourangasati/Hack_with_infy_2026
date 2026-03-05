#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        result = []
        while slow :
            result.append(slow.val)
            slow = slow.next
        return result
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

# Find the middle node and return the values from the middle to the end
solution = Solution()
result = solution.middleNode(head)

print(result)  # Output: [3, 4, 5]