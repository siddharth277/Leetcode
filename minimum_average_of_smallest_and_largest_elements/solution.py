class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        aver = []
        nums.sort()
        n = len(nums)
        low = 0
        high = n-1
        for i in range(n//2):
            aver.append((nums[low]+nums[high])/2)
            low+=1
            high-=1
        return min(aver)
