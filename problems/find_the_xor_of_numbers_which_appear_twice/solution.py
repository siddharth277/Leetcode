class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums.sort()
        twice=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                twice.append(nums[i])
        xor=0
        for i in twice:
            xor ^= i
        return xor


        
        