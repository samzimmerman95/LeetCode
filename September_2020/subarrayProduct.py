# Day 28

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        prod = 1
        count = left = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1
        return count
            
