class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1

        if len(nums) == 0:
            return [-1, -1]

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                left = mid
                right = mid

                while left > 0 and nums[left - 1] == target:
                    left -= 1

                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1

                return [left, right]

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]