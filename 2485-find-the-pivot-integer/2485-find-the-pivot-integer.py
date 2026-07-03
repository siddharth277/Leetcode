class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = list(range(1, n + 1))
        i=0
        while(i<n+1):
            if (i*(i+1)//2) == ((n*(n+1)//2)-(i*(i-1)//2)):
                return i
                break
            i+=1
        return -1

        
    


        