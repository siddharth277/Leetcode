class Solution:
    def processStr(self, s: str, k: int) -> str:
        lens = []

        cur = 0
        for ch in s:
            if 'a' <= ch <= 'z':
                cur += 1
            elif ch == '*':
                if cur > 0:
                    cur -= 1
            elif ch == '#':
                cur *= 2
            else:  
                pass

            lens.append(cur)

        if k >= cur:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev = lens[i - 1] if i > 0 else 0

            if 'a' <= ch <= 'z':
                if k == prev:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                if k >= prev:
                    k -= prev

            else:  
                k = prev - 1 - k

        return '.'