class Solution:
    def largestFunc(self, arr):
      largest = arr[0]
      index = 0
      for i in range(len(arr)):
        if arr[i] >= largest:
          largest = arr[i]
          index = i
      return [index, largest]
      
    def getSecondLargest(self, arr):
      dup_num = []
      for i in range(len(arr)):
        dup_num.append(arr[i])
      object_call = self.largestFunc(dup_num)
      largest_var = object_call[1]
      
      dup_num[object_call[0]] = float("-inf")
      second_largest_var = dup_num[0]
      
      for i in range(len(dup_num)):
        if i >= second_largest_var:
          second_largest_var = dup_num[i]
      print(second_largest_var, largest_var, dup_num)
      if second_largest_var != largest_var:
        return second_largest_var
      return -1
    
solution = Solution()
nums = [10, 5, 10]
call = solution.getSecondLargest(nums)
print(call)