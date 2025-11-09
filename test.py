# Question: 283. Move Zeroes to the end of list [Leetcode]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        non_zeros = []
  
        for i in nums:
            if i == 0:
                zeros +=1
            else:
                non_zeros.append(i)
        
        count = 0
        for _ in range(0, len(non_zeros)):
            nums[count] = non_zeros[count]
            count+=1
            
        for _ in range(count, len(nums)):
            nums[count] = 0
            count+= 1