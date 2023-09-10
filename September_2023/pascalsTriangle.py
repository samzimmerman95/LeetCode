"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for r in range(1, numRows):
            result.append([])
            for i in range(r+1):
                if i == 0 or i == r:
                    result[r].append(1)
                else:
                    result[r].append(result[r-1][i-1] + result[r-1][i])
        return result

        