class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 =f"{num1:04d}"
        num2=f"{num2:04d}"
        num3=f"{num3:04d}"

        p=""
        for i in range(4):
            p+=min(num1[i] , num2[i] , num3[i])

        return int(p)

        