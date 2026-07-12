class Solution:
    def countQuadruplets(self, A: List[int]) -> int:
        count=0
        for w in range(len(A)):
            for x in range(w + 1, len(A)):
                for y in range(x + 1, len(A)):
                    for z in range(y + 1, len(A)):
                        if (A[w] + A[x] + A[y] == A[z]) :
                            count+=1
        return count