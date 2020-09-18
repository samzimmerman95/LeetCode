# Day 18

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        minimum = max(prices)
        maxProfit = 0
        
        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            maxProfit = max(maxProfit, prices[i] - minimum)
                
        return maxProfit
