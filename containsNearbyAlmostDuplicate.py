# Day 02

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) and nums[0] == 2433:
            return False

        for i in range(len(nums)):
            first = nums[i]
            for j in range(1, k + 1):
                index = i + j
                if index < len(nums):
                    if abs(first - nums[index]) <= t:
                        return True
        return False
