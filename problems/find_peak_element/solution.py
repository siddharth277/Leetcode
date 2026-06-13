class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low =0
        high = len(nums)-1
        while(low<high):
            if(nums[low]<=nums[high]):
                low +=1
            else :
                high -=1
        return low



        