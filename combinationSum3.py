# Day 12

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(combination, remaining, start):
            if len(combination) == k and remaining == 0:
                print(combination)
                result.append(combination[:])
                return
            
            elif remaining < 0 or len(combination) > k:
                return
            
            for i in range(start+1, 10):
                combination.append(i)
                backtrack(combination, remaining - i , i)
                combination.pop()
            
        backtrack([], n, 0)
    
        return result
