class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def sqrt(a):
            return a ** 0.5

            
        for i in range(int(sqrt(c)) + 1):
            b = int(sqrt(c - i*i))
            if b * b == c - i*i:
                return True
        return False