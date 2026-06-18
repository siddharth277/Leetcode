class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for string in strs:
            if string.isalpha():
               res = max(res, len(string))
            elif string.isdigit():
                res = max(res, int(string))
            else :
                res = max(res, len(string))


        return res
        