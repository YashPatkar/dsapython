# 1480. Leetcode

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        for index, i in enumerate(nums):
            total += i
            nums[index] = total
        
        return nums