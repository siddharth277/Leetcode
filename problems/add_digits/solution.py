class Solution:
    def addDigits(self, num: int) -> int:
        p = str(num)
        out =0
        for i in range(len(p)):
            out +=  int(p[i])
        if out >9:
            return self.addDigits(out)
        else :
            return out
        