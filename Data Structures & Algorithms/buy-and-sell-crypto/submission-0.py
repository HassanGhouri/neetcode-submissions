class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        best_sell_price = [0] * n
        best_sell_price[n-1] = prices[n-1] 

        for i in range(n-2, -1, -1):
            best_sell_price[i] = max(best_sell_price[i + 1], prices[i])

        for i in range(n):
            if best_sell_price[i] - prices[i] > max_profit:
                max_profit = best_sell_price[i] - prices[i]
        
        return max_profit

        
        
            
