class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr)-1
        while (low<=high):
            mid = low + (high-low)//2
            miss = arr[mid]-(mid+1)
            if k<= miss :
                high = mid-1
            else :
                low = mid+1
        return low + k




        