# Day 30

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        l = len(nums)
        for i in range(l):
            if nums[i] < 0 or nums[i] >= l:
                nums[i] = 0

        for i in range(len(nums)):
            nums[nums[i]%l] += l

        for i in range(len(nums)):
            if int(nums[i] / l) == 0:
                return i
    
        return l
        
