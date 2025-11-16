# Question: 53. Maximum Subarray [Leetcode]

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = float('-inf')
        total = 0
        for i in nums:
            total += i
            if total > maxi:
                maxi = total
            if total < 0:
                total = 0
        return maxi