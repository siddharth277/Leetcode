class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        p = sorted(list(set(nums)))
        for ind, val in enumerate(p):
            nums[ind] = val
        return len(p)