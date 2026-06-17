class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p = int(a , 2)
        b = int(b , 2)
        return bin(p+b)[2:]