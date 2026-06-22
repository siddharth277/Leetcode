class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        flag = set()
        for num in nums:
            if num in flag:
                return num
            flag.add(num)