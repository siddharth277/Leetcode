class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while(k):
            mx = min(nums)
            i = nums.index(mx)
            nums[i]=mx*multiplier
            k-=1
        return nums

            
        