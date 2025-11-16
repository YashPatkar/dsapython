# Question: 121. Best Time to Buy and Sell Stock [Leetcode]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        large = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    large = max(large, prices[j] - prices[i])
        return large