class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        if len(ransomNote) > len(magazine):
            return False

        for i in ransomNote:
            if i not in mag:
                return False
            mag[mag.index(i)] = '#'  
        return True