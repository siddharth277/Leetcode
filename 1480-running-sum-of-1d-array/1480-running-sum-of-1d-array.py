class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        rs=[]
        sum1=0
        for i in range(len(nums)) :
            sum1+=nums[i]
            rs.append(sum1)
            
        return rs
        