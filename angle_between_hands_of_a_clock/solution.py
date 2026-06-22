class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mindegree=minutes*6
        hourdegree=(hour*60 + minutes)*0.5
        if abs(hourdegree-mindegree)>=180:
            return (360-abs(hourdegree-mindegree))
        else : 
            return abs(hourdegree-mindegree)


        