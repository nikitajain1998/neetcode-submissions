class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")
        sold = 0
        cooldown = 0

        for price in prices:
            hold, sold, cooldown = (
                max(hold, cooldown - price),
                hold + price,
                max(cooldown, sold)
            )

        return max(sold, cooldown)
        