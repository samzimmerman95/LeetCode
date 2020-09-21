# Day 20

class Solution(object):
    paths = 0 
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        freeSpaces = 0
        startRow, startCol = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                current = grid[r][c]
                if current >= 0:
                    freeSpaces += 1
                if current == 1:
                    startRow, startCol = r, c
               
        
        def backtrack(r, c, remaining):
            if grid[r][c] == 2 and remaining == 1:
                self.paths += 1
                return 
            
            t = grid[r][c]
            grid[r][c] = -2
            remaining -= 1
            
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for row, col in directions:
                nextR, nextC = r + row, c + col
                
                if not ( 0 <= nextR < len(grid) and 0 <= nextC < len(grid[0])):
                    continue
                if grid[nextR][nextC] < 0:
                    continue
                backtrack(nextR, nextC, remaining)
            grid[r][c] = t
        
        backtrack(startRow, startCol, freeSpaces)
        
        return self.paths
        
