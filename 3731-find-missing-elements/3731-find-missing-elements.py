class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        low = nums[0]
        high = nums[len(nums)-1]
        res=[]
        for i in range (low , high):
            if i not in nums :
                res.append(i)
        return res

        