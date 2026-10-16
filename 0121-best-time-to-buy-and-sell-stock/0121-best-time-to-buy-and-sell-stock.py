class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        profit = 0

        for p in prices[1:]:
            if bp > p:
                bp = p
            
            profit = max(profit, p - bp)
        
        return profit