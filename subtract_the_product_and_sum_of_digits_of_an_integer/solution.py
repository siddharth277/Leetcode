class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        pro=1
        c=str(n)
        for i in range(len(c)):
            p = n%10
            sum +=p
            pro = pro*p
            n=n//10
        return pro-sum


        