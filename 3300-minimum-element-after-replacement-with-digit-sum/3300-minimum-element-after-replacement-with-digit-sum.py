class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for i in nums :
            sum=0
            while(i>0):
                sum+= i%10
                i=i//10
            arr.append(sum)
        return min(arr)

        