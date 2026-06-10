class Solution:
    def isPalindrome(self, x: int) -> bool:
        pred = False 
        p = str(x)
        reverse =""
        for i in range(len(p) - 1, -1 , -1):
            reverse = reverse + p[i]
        if p == reverse :
            pred = True 
        else :
            pred = False 
        return pred 
        