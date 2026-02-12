# 905. Leetcode

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        odd, even = [], []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        result = []

        result.extend(even)
        result.extend(odd)
        return result