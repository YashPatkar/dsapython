# Question: Merge 2 Sorted Arrays Without Duplicates [GeeksForGeeks]

class Solution:
    def findUnion(self, nums1, nums2):
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                if nums1[i] not in result:
                    result.append(nums1[i])
                i+=1
            elif nums2[j] <= nums1[i]:
                if nums2[j] not in result:
                    result.append(nums2[j])
                j+=1
          
        for k in nums1[i:]:
            if k not in result:
                result.append(k)
        
        for k in nums2[j:]:
            if k not in result:
                result.append(k)
        
        return result