class Solution:
    def isFascinating(self, n: int) -> bool:
        def ronaldo(num):
            if sorted(list(num))==["1","2","3","4","5","6","7","8","9"]:
                return(True)
            else:
                return False
        n=str(n)+str(n*2)+str(n*3)
        return ronaldo(n)