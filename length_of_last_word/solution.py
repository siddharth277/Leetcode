class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lists = s.split()
        n = len(lists)-1
        return len(lists[n])

        