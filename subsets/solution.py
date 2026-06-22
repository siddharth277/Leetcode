class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in range(len(nums)):
            temp = []
            for subset in res:
                temp.append(subset + [nums[i]])
            res.extend(temp)

        return res


        