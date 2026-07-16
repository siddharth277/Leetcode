class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        p = sorted(score, reverse=True)

        n = len(score)
        i = 0
        answer = [""] * n
        while i < n:
            c = score.index(p[i])
            if i == 0:
                answer[c] = "Gold Medal"
            elif i == 1:
                answer[c] = "Silver Medal"
            elif i == 2:
                answer[c] = "Bronze Medal"
            else:
                answer[c] = str(i + 1)
            i += 1
        return answer