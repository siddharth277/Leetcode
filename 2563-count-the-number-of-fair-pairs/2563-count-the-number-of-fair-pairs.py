class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()

        def count(target):
            low = 0
            high = len(nums) - 1
            ans = 0

            while low < high:

                if nums[low] + nums[high] <= target:
                    ans += high - low
                    low += 1
                else:
                    high -= 1

            return ans

        return count(upper) - count(lower - 1)