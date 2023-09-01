# Day 06

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        pointsA = []
        pointsB = []
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c]:
                    pointsA.append((r, c))
                if B[r][c]:
                    pointsB.append((r, c))

        vectorCount = {}

        for ra, ca in pointsA:
            for rb, cb in pointsB:
                v = (rb-ra, cb-ca)
                if v in vectorCount:
                    vectorCount[v] += 1
                else:
                    vectorCount[v] = 1

        return max(vectorCount.values() or [0])
