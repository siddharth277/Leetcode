class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = num**0.5

        return ans==int(ans)