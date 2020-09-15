# Day 15

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        if len(l):
            return len(l[-1])
        else:
            return 0
