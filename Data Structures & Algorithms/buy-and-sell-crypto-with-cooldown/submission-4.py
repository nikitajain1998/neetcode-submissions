class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        noStock = 0
        inHand = float("-inf")
        sold = 0

        for price in prices:
            no_stock = noStock
            in_hand = inHand
            old_sold = sold

            noStock = max(no_stock, sold)
            inHand = max(in_hand, no_stock - price )
            sold = in_hand + price
        
        return max(sold,noStock)