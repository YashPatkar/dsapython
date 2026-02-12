# 1672. Leetcode

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = 0
        for account in accounts:
            result = max(result, sum(account))
        return result