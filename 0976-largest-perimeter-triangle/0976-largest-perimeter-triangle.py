class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        peri=[0]
        for i in range(n-2):
            if nums[i]+nums[i+1] > nums[i+2] :
                peri.append(nums[i]+nums[i+1]+nums[i+2])
        return max(peri)





        