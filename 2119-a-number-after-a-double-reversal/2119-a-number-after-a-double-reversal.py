class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
       p=str(num)
       return p[len(p)-1] !='0' or num==0
        