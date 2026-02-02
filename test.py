# Question: 2149. Rearrange Array Elements by Sign [Leetcode]

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = [0 for _ in range(len(nums))]

        pos, neg = 0, 1
        
        for i in nums:
            if i > 0:
                result[pos] = i
                pos+=2
            else:
                result[neg] = i
                neg+=2
        return result