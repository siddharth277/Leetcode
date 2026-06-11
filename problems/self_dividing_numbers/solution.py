class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right + 1):
            s = str(i)
            for ch in s:
                if ch == '0' or i % int(ch) != 0:
                    break
            else:
                ans.append(i)
        return ans