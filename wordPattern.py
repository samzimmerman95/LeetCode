# Day 07

class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = string.split()
        d = {}
        if len(l) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in d:
                if l[i] not in d.values():
                    d[pattern[i]] = l[i]
                else:
                    return False
            if d[pattern[i]] != l[i]:
                return False
            print(d)
        return True
