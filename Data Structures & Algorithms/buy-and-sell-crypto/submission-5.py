class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, l, r = 0, 0, 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = max(profit, prices[r] - prices[l])
                r += 1

        return profit

    """
    [10,1,5,6,7,1]
        ^
          ^

    if profit is neg we'll just increment l and r = l and try again
    then if profit is positive, calculate the curr_profit and store in max then only increment r to see
    if theres a better profit

    increment r while r < len(nums) then when done l += 1 and r = l again.


    [10,8,7,5,2]
              ^
              ^

    """
