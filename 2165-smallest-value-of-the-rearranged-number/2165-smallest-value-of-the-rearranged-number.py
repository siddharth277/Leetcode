class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        l = []
        s=abs(num) 
        while(s>0):
            p= s%10
            s = s//10
            l.append(p)
        l.sort()
        if num >= 0 :
            for i in range(len(l)):

                if l[i]!=0 :
                    l[0] , l[i] = l[i] , l[0]
                    break
            return int("".join(str(d) for d in l))

        else :
            return - int("".join(str(d) for d in l[::-1]))

            



        