# Day 25
import functools
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(s1, s2):
            op1 = s1+s2
            op2 = s2+s1
            if op1 > op2:
                return 1
            elif op2 > op1:
                return -1
            else:
                0
                
        strList = list(map(str, nums))
        strList.sort(key=functools.cmp_to_key(compare), reverse=True)
        
        result = ''.join(strList)
        if result[0] == '0':
            return '0'
        else:
            return result
        
