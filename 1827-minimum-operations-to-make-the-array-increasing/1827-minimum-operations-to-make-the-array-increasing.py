class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i] :
                continue
            else :
                p= ((nums[i]-nums[i+1])+1)
                count+=p
                nums[i+1]= nums[i]+1
        return count

        