
# 80. Leetcode
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                if freq[i] <= 1:
                    freq[i] += 1
        print(freq)
        count = 0
        for key, value in freq.items():
            for i in range(value):
                nums[count] = key
                count += 1
        print(nums)
        return count