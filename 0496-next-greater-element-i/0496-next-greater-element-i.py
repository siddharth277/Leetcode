class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            
            flag = False
            for j in range(nums2.index(i) + 1, len(nums2)):
                if nums2[j] > i:
                    output.append(nums2[j])
                    flag = True
                    break

            if not flag:
                output.append(-1)

        return output