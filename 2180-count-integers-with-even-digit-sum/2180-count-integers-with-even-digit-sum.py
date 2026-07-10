class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range (2,num+1):
            digitsum=0
            while(i>0):
                digitsum+=i%10
                i = i//10
            if digitsum%2==0 :
                count+=1
        return count
        