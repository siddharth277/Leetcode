class Solution:
    def reverseWords(self, s: str) -> str:
        list = s.split()
        return " ".join(reversed(list))
        