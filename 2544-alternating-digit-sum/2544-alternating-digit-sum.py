class Solution:
    def alternateDigitSum(self, n: int) -> int:
        summ=0
        p=str(n)
        for i in range(len(p)):
            if i%2==0 or i==0 :
                summ+=int(p[i])
            else :
                summ-=int(p[i])
        return summ

        