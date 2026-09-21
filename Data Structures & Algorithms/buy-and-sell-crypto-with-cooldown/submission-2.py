class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # noStock → not holding, not in cooldown
        # inHand  → currently holding stock
        # sold    → sold today
        noStock = 0
        inHand = float("-inf")
        sold = 0
        
        for price in prices:
            no_stock = noStock
            in_hand = inHand
            soldd = sold
            noStock = max(no_stock, soldd)
            inHand = max(no_stock-price, in_hand)
            sold = in_hand + price
        
        return max(sold,noStock)
            
        