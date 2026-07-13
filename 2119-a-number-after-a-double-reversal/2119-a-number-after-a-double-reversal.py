class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
       
       return str(num)[len(str(num))-1] !='0' or num==0
        