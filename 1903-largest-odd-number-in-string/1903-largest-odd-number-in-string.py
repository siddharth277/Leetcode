class Solution:
    def largestOddNumber(self, num: str) -> str:
        n= len(num)
        while(n):
            if int(num[n-1])%2 !=0:
                return num[:n]
            n-=1
        return ""
        