# Question: Check if an array is sorted
class Solution:
    def isSorted(self, arr) -> bool:
        nums = arr
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True