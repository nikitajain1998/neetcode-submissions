class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l represents the cheapest day we've found so far, and r represents the     current selling day.
        l = r = 0
        maxP = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP