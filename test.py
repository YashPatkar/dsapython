# Question: 53. Maximum Subarray [Leetcode]

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        total = 0
        max_total = float("-inf")
        for index, i in enumerate(nums):
            for j in range(index, len(nums)):
                total += nums[j]
                if total > max_total:
                    max_total = total
            total = 0
        return max_total