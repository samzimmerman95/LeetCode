# Day 01

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
            :type A: List[int]
            :rtype: str
            """
        maxHours = 24
        maxMins = 60
        possibleHs = []
        possibleMs = []
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    op1 = int(str(A[i]) + str(A[j]))
                    op2 = int(str(A[j]) + str(A[i]))

                    if op1 < maxHours:
                        possibleHs.append(op1)
                    if op2 < maxHours:
                        possibleHs.append(op2)
                    if op1 < maxMins:
                        possibleMs.append(op1)
                    if op2 < maxMins:
                        possibleMs.append(op2)
        possibleHs.sort(reverse=True)
        possibleMs.sort(reverse=True)
        # print("Hours: ", possibleHs)
        # print("Mins: ", possibleMs)

        d = {}
        nums = [str(x) for x in A]
        for element in nums:
            d[element] = [0, nums.count(element)]

        for h in possibleHs:
            for m in possibleMs:
                hour = str(h).zfill(2)
                minute = str(m).zfill(2)
                d[hour[0]][0] += 1
                d[hour[1]][0] += 1
                d[minute[0]][0] += 1
                d[minute[1]][0] += 1

                if all(x[0] == x[1] for x in d.values()):
                    return hour + ":" + minute
                else:
                    for e in d:
                        d[e][0] = 0
        return ""
