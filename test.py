# 75. Leetcode

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        index = 0
        for key, value in freq.items():
            for i in range(value):
                nums[index] = key
                index+=1
        print(nums)
