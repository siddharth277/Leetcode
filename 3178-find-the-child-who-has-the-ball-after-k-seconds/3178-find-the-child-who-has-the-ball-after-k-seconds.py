class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        quo = k//(n-1)
        rem= k%(n-1)
        if quo%2==0:
            return rem
        else:
            return n-1-rem
        