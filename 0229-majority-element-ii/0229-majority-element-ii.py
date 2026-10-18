class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        from collections import Counter
        threshold = len(nums)/3
        counts = Counter(nums)
        return [num for num, count in counts.items() if count > threshold]
        