class Solution:
    def maxDivScore(self, nums: List[int], d: List[int]) -> int:
        m=0
        sum={}
        s=[]
        for i in range(len(d)):
            c=0
            for j in range(len(nums)):
                if(nums[j]%d[i]==0):
                    c+=1
            if(m<=c):
                m=c
            sum[d[i]]=c
        for i in sum:
            if(sum[i]==m):
                s.append(i)
        n=min(s)
         
        return n

        