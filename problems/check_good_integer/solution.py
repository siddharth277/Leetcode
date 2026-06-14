class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        p = str(n)
        sum=0
        square=0
        for i in p :
            sum += int(i)
            square += int(i)*int(i)
        return (square-sum)>=50
        