# Day 09

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        one = version1.split('.')
        for i in range(len(one)):
            one[i] = int(one[i])

        two = version2.split('.')
        for i in range(len(two)):
            two[i] = int(two[i])

        while len(one) != len(two):
            if len(one) > len(two):
                two.append(0)
            else:
                one.append(0)
        print(one)
        print(two)

        for i in range(len(one)):
            if one[i] > two[i]:
                return 1
            elif one[i] < two[i]:
                return -1

        return 0
