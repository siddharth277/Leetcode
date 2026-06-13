class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        reverse = "zyxwvutsrqponmlkjihgfedcba"
        mp = {}
        output = ""
        sum=0
        for i in range(26):
            mp[chr(ord('a') + i)] = weights[i]
        for w in words:
            
            for ch in w:
                sum += mp[ch]
            output += reverse[sum % 26]
            sum=0
        return output