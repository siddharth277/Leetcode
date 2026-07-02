class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0]==nums[1]==nums[2]:
            return "equilateral"
        nums.sort()
        if not nums[0]+nums[1]>nums[2] :
            return "none"
        else :
            if nums[0]==nums[1] or nums[1]==nums[2] :
                return "isosceles"
            else :
                return "scalene"


        