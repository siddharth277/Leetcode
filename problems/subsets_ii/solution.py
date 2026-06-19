class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        for i in range(len(nums)):
            temp = []
            for subset in res:
                temp.append(subset + [nums[i]])
            res.extend(temp)
        
        s = list(set(tuple(x) for x in res))
        return [list(x) for x in s]


        