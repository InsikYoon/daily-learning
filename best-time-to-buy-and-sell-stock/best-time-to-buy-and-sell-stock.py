class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minval = prices[0]
        profit = 0
        for i in prices:
            minval = min(i, minval)
            profit = max(profit, i-minval)
        
        return profit
            