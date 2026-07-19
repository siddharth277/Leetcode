class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer=[]
        for i in range(len(queries)):
            count=0
            sum=0
            for j in range(len(nums)):
                if (sum+nums[j])<=queries[i]:
                    sum +=nums[j]
                    count+=1
            answer.append(count)
        return answer

        