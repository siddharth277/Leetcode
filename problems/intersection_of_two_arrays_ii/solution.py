class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
                p = nums2.index(i)
                nums2[p]=1001
        return result
        