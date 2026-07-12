class Solution:
    def countTriples(self, n: int) -> int:

        count = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                c = int((i*i + j*j) ** 0.5)
                if c * c == i*i + j*j and c <= n:
                    count += 1
        return count