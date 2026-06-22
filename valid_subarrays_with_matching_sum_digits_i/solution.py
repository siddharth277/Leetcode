class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
      output=0
      str_x = str(x) 
      for i in range(len(nums)):
        current_sum=0
        for j in range(i,len(nums)):
          current_sum+=nums[j]
          
          veltanoric = current_sum 
          p = str(veltanoric)
          
         # print(f"Subarray: {nums[i:j+1]}, Sum: {veltanoric}, First Digit: {p[0]}, Last Digit: {p[-1]}, Target X: {str_x}")
          if (p[0]==str_x and p[-1]==str_x):
            output+=1
      return output