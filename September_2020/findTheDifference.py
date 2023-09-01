# Day 24

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        
        return t[-1]

        # Alternate solution, smart use of XOR
        # ans = 0
        # for l in s+t:
        #     ans = ans ^ ord(l)
        # return chr(ans)
    
