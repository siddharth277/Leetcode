class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        block = 2 * k + 1
        rows_needed = (n + block - 1) // block
        cols_needed = (m + block - 1) // block
        return rows_needed * cols_needed
        