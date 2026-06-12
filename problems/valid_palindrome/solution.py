class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        s=s.lower()
        for i in s:
            if i.isalnum() :
                p += i
        low = 0 
        high = len(p)-1
        while(low<=high):
            if (p[low]==p[high]):
                low +=1
                high -=1
            else :
                return False
        return True
            
        
        

        