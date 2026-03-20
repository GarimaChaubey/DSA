class Solution:
    def numIslands(self, grid):
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            # boundary + water check
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # mark visited
            grid[r][c] = "0"
            
            # explore all 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count