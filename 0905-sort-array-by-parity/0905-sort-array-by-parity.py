class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i=0 
        j=0
        while (i<=j & j<len(nums)) :
            if nums[j]%2 ==0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
            j+=1
        return nums

        