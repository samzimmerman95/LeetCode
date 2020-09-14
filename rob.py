# Day 14

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        
        onePrevious = 0
        twoPrevious = 0
        
        for i in range(len(nums)):
            t = onePrevious
            current = max(twoPrevious+nums[i], onePrevious)
            onePrevious = current
            twoPrevious = t
        
        
        return onePrevious
