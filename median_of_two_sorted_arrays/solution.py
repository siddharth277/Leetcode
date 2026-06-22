class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1 + nums2
        c.sort()
        p = len(c)
        if(p%2==0):
            return (c[int((p-1)/2)] + c[int((p+1)/2)])/2
        else : 
            return c[int(p/2)]
        