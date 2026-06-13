class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for g in grid :
            for i in g:
                if i<0:
                    count +=1
        return count

        