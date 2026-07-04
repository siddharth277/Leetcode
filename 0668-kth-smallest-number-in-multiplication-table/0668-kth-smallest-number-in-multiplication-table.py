class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m*n
        while low < high:
            mid, count = (low+high)//2, 0
            for i in range(1, m+1):
                count += n if n<mid//i else mid//i
            if count>=k:  
                high = mid
            else:  
                low = mid+1
        return low