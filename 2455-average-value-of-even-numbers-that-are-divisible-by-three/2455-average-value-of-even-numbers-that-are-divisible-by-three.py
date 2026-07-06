class Solution:
    def averageValue(self, nums: List[int]) -> int:
        arr =[]
        for i in nums :
            if i%3 ==0 and i%2==0:
                arr.append(i)
        return sum(arr) // len(arr) if len(arr)>0 else 0
        