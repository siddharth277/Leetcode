class Solution:
    def climbStairs(self, n: int) -> int:
        x, p = 1, 2
        for _ in range(3, n + 1):
            x, p = p, x + p

        return n if n <= 2 else p