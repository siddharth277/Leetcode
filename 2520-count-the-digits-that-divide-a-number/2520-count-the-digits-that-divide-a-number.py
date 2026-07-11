class Solution:
    def countDigits(self, num: int) -> int:
        p=str(num)
        count=0
        for i in p:
            if num%int(i)==0:
                count+=1
        return count
        