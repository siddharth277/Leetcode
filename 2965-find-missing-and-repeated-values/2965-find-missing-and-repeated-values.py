class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n =  len(grid)
        arr = []
        for row in grid :
            arr.extend(row)



        sumreal = sum(range(1, (n*n)+1))
        sumactual = sum(arr) 
        for j in range(1 , (n*n)+1):
            if j not in arr:
                b = j
             
        return [(sumactual-sumreal)+b , b]
        
                




        