
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for p in range(len(s)):
            if s[p] != " " and (p == 0 or s[p-1] == " "):
                count += 1
        return count
