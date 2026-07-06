class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def isinterval(p1, p2):
            if p2[0] <= p1[0] and p1[1] <= p2[1]:
                return True
            return False

        count = 0
        for i in range(len(intervals)):
            flag = False
            for j in range(len(intervals)):
                if i == j:
                    continue
                if isinterval(intervals[i], intervals[j]):
                    flag = True
                    break
            if not flag:
                count += 1
        return count


