# Question: Remove Duplicates from Sorted Array [ in place ]
class Solution:
    def removeDuplicates(self, nums):
        current_val = nums[0]
        count = 1
        for i in nums[1:]:
            if i != current_val:
                nums[count] = i
                count += 1
                current_val = i
        return count