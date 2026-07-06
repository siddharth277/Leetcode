class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return (max(nums)-k ) - (min(nums)+k) if (max(nums)-k ) - (min(nums)+k) >0 else 0
        