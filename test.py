# Question: 1. Two Sum [Leetcode]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq = {}
        for index, i in enumerate(nums):
            remain = target - i
            if remain in freq:
                return [freq[remain], index]
            freq[i] = index