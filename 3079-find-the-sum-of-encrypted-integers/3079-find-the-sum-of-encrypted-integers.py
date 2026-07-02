class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        arr=[]
        for dig in nums:
            list1 = [int(digit) for digit in str(dig)]
            mx = max(list1)
            p = str(mx)*len(list1)
            arr.append(int(p))
        return sum(arr)

        