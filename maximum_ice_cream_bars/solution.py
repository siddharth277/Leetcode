class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        total = 0
        i = 0

        while i < len(costs) and total + costs[i] <= coins:
            total += costs[i]
            i += 1

        return i