class Solution:
    def minimumSum(self, num: int) -> int:
        temp = []

        while num > 0:
            temp.append(num % 10)
            num //= 10

        temp.sort()

        x = temp[0] * 10 + temp[2]
        y = temp[1] * 10 + temp[3]

        return x + y