# Question: rotate the array to the right by k steps

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        k_before = []
        k_after = []
        n = len(nums) - k
        
        for i in nums[:n]:
            k_before.append(i)
        for i in nums[n:]:
            k_after.append(i)

        nums[:] = k_after + k_before