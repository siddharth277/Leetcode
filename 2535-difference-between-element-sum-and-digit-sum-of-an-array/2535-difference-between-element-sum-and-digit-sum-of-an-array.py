class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementsum=0
        digitsum=0
        for i in nums:
            elementsum+=i
            while(i>0):
                p=i%10
                i=i//10
                digitsum+=p
        return abs(elementsum-digitsum)

        