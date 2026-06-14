class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0 
        j=0 
        sum=0
        listsum=[]
        for p in range(len(nums)):
            if nums[p] ==0 :
                listsum.append(sum)
                i = j = p+1
                sum=0
            else :
                sum +=1
        listsum.append(sum) 
        return max(listsum)


        