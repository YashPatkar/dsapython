# Question: 485. Max Consecutive Ones [Leetcode]

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        count = 0
        for i in nums:
            if i == 0:
                if count > total:
                    total = count
                    count = 0
                else:
                  count = 0
            else:
                count+=1
        return max(total, count)