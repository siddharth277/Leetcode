class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        p = str(n)
        score = 0
        for char in p :
            score += int(char)

        return score

        