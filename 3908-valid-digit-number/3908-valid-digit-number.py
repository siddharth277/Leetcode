class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        p = str(n)
        return str(x) in p and p[0] != str(x)