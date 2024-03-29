class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        
        buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = max(profit, prices[i]-buy)
        
        return profit
        
        