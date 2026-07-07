class Solution:
    def sumAndMultiply(self, n: int) -> int:
        p = str(n)
        s=""
        sum1=0
        for char in p :
            if char != "0" :
                s += char
                sum1 += int(char)
        if s == "":
            return 0
        return int(s)*sum1
         

            
        