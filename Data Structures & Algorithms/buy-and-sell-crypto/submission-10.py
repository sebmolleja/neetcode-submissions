class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, r, l = 0, 0, 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
                r = l
            else:
                profit = max(profit, prices[r] - prices[l])
                r += 1
        
        return profit