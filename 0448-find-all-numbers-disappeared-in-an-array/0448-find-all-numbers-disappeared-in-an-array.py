class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = set(nums)
        arr=[]
        for i in range(1 , len(nums)+1):
            if i not in numbers :
                arr.append(i)
        return arr
        