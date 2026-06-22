import re

class Solution:

    @staticmethod
    def is_special(char):
        return bool(re.match(r'[^a-zA-Z0-9]', char))

    def reverseByType(self, s: str) -> str:

        s = list(s)

        low = 0
        high = len(s) - 1

        while low < high:

            if s[low].isalpha() and s[high].isalpha():
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1

            elif not s[low].isalpha():
                low += 1

            else:
                high -= 1

        low = 0
        high = len(s) - 1

        while low < high:

            if self.is_special(s[low]) and self.is_special(s[high]):
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1

            elif not self.is_special(s[low]):
                low += 1

            else:
                high -= 1

        return ''.join(s)