class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        new_strs = [s for s in strs if s != smallest]
        output = ""
        for i in range(len(smallest)):
            ch = smallest[i]
            for s in new_strs:
                if s[i] != ch:
                    return output
            output =output + ch
        return output

        