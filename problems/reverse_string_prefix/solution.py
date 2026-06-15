class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        p = list(s)
        for i in range(k):
            p[i] = s[k - 1 - i]

        return ''.join(p)