class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        listr  = [int(digit) for digit in str(x)]
        sum1 = sum(listr)
        if x%sum1==0:
            return sum1
        else :
            return -1

        