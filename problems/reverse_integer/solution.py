class Solution:
    def reverse(self, x: int) -> int:
        
        if x<0 :
            x= -x
            s_x = str(x)
            reversed_s_x = ""
            for i in range(len(s_x) - 1, -1, -1):
                reversed_s_x += s_x[i]
            reversed_x = -int(reversed_s_x)
        else :
            s_x = str(x)
            reversed_s_x = ""
            for i in range(len(s_x) - 1, -1, -1):
                reversed_s_x += s_x[i]
            reversed_x = int(reversed_s_x)
            
        if not (-(2**31) <= reversed_x <= (2**31) - 1):
            return 0

        return reversed_x
