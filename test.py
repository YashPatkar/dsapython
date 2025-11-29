# Question: 2149. Rearrange Array Elements by Sign [Leetcode]

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        non_neg, neg = [], []
        for i in nums:
            if i > 0:
                non_neg.append(i)
            else:
                neg.append(i)
        
        result = []
        for i in range(min(len(non_neg), len(neg))):
            result.append(non_neg[i])
            result.append(neg[i])
        
        return result