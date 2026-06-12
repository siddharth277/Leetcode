class Solution:
    def maxArea(self, height: List[int]) -> int:
        low= 0
        high = len(height)-1
        area =[]
        while (low<=high):
            a = (high - low)*(min(height[low], height[high]))
            area.append(a)
            if(height[low]<=height[high]):
                low +=1
            else :
                high -=1
        return max(area)



        