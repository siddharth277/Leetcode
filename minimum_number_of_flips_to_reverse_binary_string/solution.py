class Solution:
    def minimumFlips(self, n: int) -> int:
        s=""
        while(n>=1):
            p = str( n%2 )
            n=n//2
            s= s+p
        
        low = 0
        high = len(s)-1
        count=0
        while(low<=high):
            if s[low]==s[high]:
                low+=1
                high-=1
            else:
                low+=1
                high-=1
                count+=2
        return count
        