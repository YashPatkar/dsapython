class Solution:
     
    def func(self, nums):
        nums = sorted(nums)
        largest = nums[len(nums) - 1]
        second_largest = float('-inf')
        for i in nums:
            if i >= second_largest and i != largest:
                second_largest = i
        if second_largest in [largest, float('-inf')]:
            return -1
        return second_largest
        
    def getSecondLargest(self, arr):
        return self.func(arr)

solution = Solution()
nums = [10, 10, 10]
call = solution.getSecondLargest(nums)
print(call)