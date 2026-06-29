class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        p = list(set(nums))
        p.sort()
        if len(p)>=3 :
            return p[-3]
        else :
            return max(p)

        