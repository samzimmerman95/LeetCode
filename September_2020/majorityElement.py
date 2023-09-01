# Day 22

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        op1, op2, op1C, op2C = 0,0,0,0
        for n in nums:
            if op1 == n:
                op1C += 1
            elif op2 == n:
                op2C += 1
                
            elif op1C == 0:
                op1 = n
                op1C += 1
            elif op2C == 0:
                op2 = n
                op2C += 1
            
            else:
                op1C -= 1
                op2C -= 1
        
        result = []
        options = []
        if op1C:
            options.append(op1)
        if op2C:
            options.append(op2)
 
        for n in options:
            if nums.count(n) > len(nums) // 3:
                result.append(n)
        return result
