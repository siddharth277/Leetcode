class Solution:
    def maxDistance(self, moves: str) -> int:
      count_u=0
      count_l=0
      count_r=0
      count_d=0
      count_=0
      for i in moves:
        if i=="U":
          count_u+=1
        elif i=="L":
          count_l+=1
        elif i=="R":
          count_r+=1
        elif i=="D":
          count_d+=1
        elif i=="_":
          count_ +=1
      return abs(count_u-count_d)+abs(count_l-count_r)+count_
      
