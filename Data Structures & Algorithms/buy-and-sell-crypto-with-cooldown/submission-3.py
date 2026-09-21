class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I don't own a stock and I'm allowed to buy
        noStock = 0

        # I currently own a stock
        # Impossible before buying anything
        inHand = float("-inf")

        # I sold a stock today
        sold = 0

        for price in prices:

            # Save yesterday's states
            no_stock = noStock
            in_hand = inHand
            soldd = sold

            # Either:
            # 1. Continue having no stock
            # 2. Come out of cooldown after selling
            noStock = max(no_stock, soldd)

            # Either:
            # 1. Buy today
            # 2. Continue holding yesterday's stock
            inHand = max(no_stock - price, in_hand)

            # Sell today's stock
            sold = in_hand + price

        # We cannot finish while holding a stock.
        # So choose the best completed state.
        return max(sold, noStock)
            
        