class Solution:
    def maximum69Number(self, num: int) -> int:
        p = list(str(num))
        for i in range(len(p)):
            if p[i] == "6":
                p[i] = "9"
                break

        return int("".join(p))