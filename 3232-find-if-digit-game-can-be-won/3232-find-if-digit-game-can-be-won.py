class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums.sort()
        sumnum1 =0
        sumnum2=0
        for i in nums:
            if i < 10 :
                sumnum1 += i 
            else :
                sumnum2 += i 
        return sumnum1 != sumnum2

        