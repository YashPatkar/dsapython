class Solution:
    def func(self, nums):
      if len(nums) <= 1:
        return nums
        
      largest = nums[0]
      for i in nums[1:]:
        if i >= largest:
          largest = i
      
      second_largest = -1
      for i in nums:
        if i >= second_largest and i != largest:
          second_largest = i

      return second_largest
      
    def getSecondLargest(self, arr):
        return self.func(arr)
    
solution = Solution()
nums = [10, 10, 10]
call = solution.getSecondLargest(nums)
print(call)