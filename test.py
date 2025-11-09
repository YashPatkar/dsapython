# Question: rotate the array to the right by k steps

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            if len(nums) == 1:
                return
            for _ in range(0, k):
                last = nums.pop()
                nums.insert(0, last)
        else:
            k_before = []
            k_after = []
            n = len(nums) - k
            print(n + 1)
            for i in nums[:n]:
                k_before.append(i)
            for i in nums[n:]:
                k_after.append(i)

            nums[:] = k_after + k_before