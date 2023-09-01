# Day 11

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# Brute force method. Works for smaller inputs
#         maximum = min(nums)
#         for i in range(len(nums)):
#             total = 0
#             for j in range(i, len(nums)):
#                 if i == j:
#                     total = nums[i]
#                 else:
#                     total *= nums[j]
#                 if total > maximum:
#                     maximum = total
                    
#         return maximum

        maximum = prevMax = prevMin = nums[0]
        for n in nums[1:]:
            op1 = prevMax * n
            op2 = prevMin * n
            op3 = n
            
            curMax = max(op1, op2, op3)
            curMin = min(op1, op2, op3)
            
            if curMax > maximum:
                maximum = curMax
            
            prevMax = curMax
            prevMin = curMin
            
        return maximum
        
        
