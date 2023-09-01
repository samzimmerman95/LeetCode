# Day 03

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        substring = ''

        for i in range(len(s)//2):
            substring = s[:i+1]
            if len(s) % len(substring):
                continue
            else:
                repeats = len(s) // len(substring)
                compare = substring * repeats
                if compare == s:
                    return True

        return False
