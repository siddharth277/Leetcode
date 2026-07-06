class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        p = str(num)
        count =0
        for i in range(len(p)-k +1):
            s = int(p[i:i+k])
            if s !=0 and num%s ==0:
                count+=1
        return count
