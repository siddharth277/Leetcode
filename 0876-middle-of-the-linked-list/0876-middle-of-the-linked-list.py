# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        return slow.next
        