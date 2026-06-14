# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        sums = []
        for i in range(len(nums) // 2):
            sums.append(nums[i] + nums[len(nums) - 1 - i])
        return max(sums)