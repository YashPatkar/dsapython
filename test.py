# Question: 268. Missing Number [Leetcode]

class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_sum = 0
        for i in nums:
            num_sum += i
        
        n = len(nums)
        n_sum = 0
        for i in range(n + 1):
            n_sum += i
        
        return n_sum - num_sum