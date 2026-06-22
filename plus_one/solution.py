class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in range(len(digits)):
            s= s + str(digits[i])
        p = int(s)
        p=p+1
        return list(map(int, str(p)))