class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            if len(str(i)) % 2 == 0 :
                num_str = str(i)
                mid = len(num_str) // 2

                if sum(int(d) for d in num_str[:mid]) == sum(int(d) for d in num_str[mid:]) :
                    count+=1
        return count

                
        