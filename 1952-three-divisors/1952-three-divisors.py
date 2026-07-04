class Solution:
    def isThree(self, n: int) -> bool:
        a=2
        for i in range(2,n,1):
            if n%i==0:
                a+=1
        return a==3