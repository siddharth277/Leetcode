class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_val = 0
        for char in s:
            xor_val ^= ord(char)
        for char in t:
            xor_val ^= ord(char)
        
        return chr(xor_val)
        
        