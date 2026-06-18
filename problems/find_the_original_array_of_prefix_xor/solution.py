class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        s = [pref[0]]

        for i in range(1, len(pref)):
            s.append(pref[i-1] ^ pref[i])

        return s