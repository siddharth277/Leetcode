class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, n in enumerate(nums):
            right_sum = total_sum - left_sum - n
            if left_sum == right_sum:
                return i  
                
            left_sum += n
            
        return -1
