# Day 04

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        while S:

            rev = S[::-1]
            start = S.find(S[0])
            # print(start)
            end = rev.find(S[0])
            end = len(S) - end - 1
            # print(end)

            i = 0
            while i < end:
                newEnd = rev.find(S[start + i])
                newEnd = len(S) - newEnd - 1
                if newEnd > end:
                    end = newEnd
                i += 1

            S = S[end+1:]
            # print(S)
            result.append(end+1)

        return result
