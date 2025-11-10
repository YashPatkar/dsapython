# Question: 268. Missing Number [Leetcode]

class Solution(object):
    def sortit(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        left = [i for i in nums[1:] if i <= pivot]
        right = [i for i in nums[1:] if i > pivot]
        return self.sortit(left) + [pivot] + self.sortit(right)
  
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] != 0:
                return 0
            return nums[0] + 1
        nums[:] = self.sortit(nums)
        n = len(nums) - 1
        while n >= 1:
            if nums[n] - 1 != nums[n - 1]:
                return nums[n] - 1
            n-=1
        if nums[0] != 0:
            return 0
        return nums[-1] + 1