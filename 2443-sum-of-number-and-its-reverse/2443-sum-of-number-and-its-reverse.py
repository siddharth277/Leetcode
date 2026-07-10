class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def isreverse(a,b):
            p=""
            while(a > 0):
                p+= str(a%10)
                a=a//10
            if p == "":
                p = "0"

            return int(p) ==b
        
        for i in range(num+1) :
            if isreverse(i , num-i) :
                return True
        return False

        