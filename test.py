# Question: Merge 2 Sorted Arrays Without Duplicates [GeeksForGeeks]

class Solution:
    def sortit(self, nums):
      if len(nums) <= 1:
        return nums
      pivot = nums[0]
      left = []
      right = []
      for i in nums[1:]:
        if i <= pivot:
          left.append(i)
        else:
          right.append(i)
      return self.sortit(left) + [pivot] + self.sortit(right)

    def findUnion(self, a, b):
      non_dup = []
      for i in a:
        if i not in non_dup:
          non_dup.append(i)
      for i in b:
        if i not in non_dup:
          non_dup.append(i)
      
      nums = self.sortit(non_dup)
      return nums
