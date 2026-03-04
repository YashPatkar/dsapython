# 75. Leetcode

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        
        left = 0
        right = len(nums) - 1

        i = 0
        while i <= right:
            if nums[i] == 2:
                # swap with right 
                temp = nums[right]
                nums[right] = nums[i]
                nums[i] = temp
                right-=1

            elif nums[i] == 0:
                # swap with left
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp

                left+=1
                i+=1
            
            else:
                i+=1
