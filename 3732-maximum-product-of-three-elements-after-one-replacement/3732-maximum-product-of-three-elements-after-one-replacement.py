class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(max(nums[-1]*nums[-2]*100000, 100000*nums[0]*nums[1]), -100000*nums[0]*nums[-1] )
        