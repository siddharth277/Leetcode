class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                n -= 1
            else:
                i += 1
        return n
        #nums = [x for x in nums if x != val]
    
                    

