class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        mx = max(nums)
        mn = min(nums)
        return gcd(mx,mn)
        