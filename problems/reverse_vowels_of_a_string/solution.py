class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s=list(s)
        low = 0
        high = len(s)-1
        while(low<=high):
            if s[low] in vowels and s[high] in vowels :
                s[low] , s[high] = s[high] , s[low]
                low+=1
                high-=1
                continue
            if s[low] in vowels and s[high] not in vowels :
                high-=1
                continue
            if s[low] not in vowels and s[high] in vowels:
                low+=1
                continue
            else :
                low+=1
                high-=1
        return "".join(s)
        