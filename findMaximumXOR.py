# Day 16

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = 0
        l = len(bin(max(nums))[2:])
        for i in range(l)[::-1]:
            largest = largest << 1
            pre = {n >> i for n in nums}
            largest = largest + any(largest^1 ^p in pre for p in pre)
        return largest
                
        
