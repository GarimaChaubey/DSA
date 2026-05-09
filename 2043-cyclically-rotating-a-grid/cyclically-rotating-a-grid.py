class Solution:
    def rotateGrid(self, grid, k):
        
        m, n = len(grid), len(grid[0])
        
        layers = min(m, n) // 2
        
        for layer in range(layers):
            
            vals = []
            
            top = layer
            bottom = m - 1 - layer
            left = layer
            right = n - 1 - layer
            
            # top row
            for c in range(left, right + 1):
                vals.append(grid[top][c])
            
            # right column
            for r in range(top + 1, bottom + 1):
                vals.append(grid[r][right])
            
            # bottom row
            for c in range(right - 1, left - 1, -1):
                vals.append(grid[bottom][c])
            
            # left column
            for r in range(bottom - 1, top, -1):
                vals.append(grid[r][left])
            
            # ----- rotate -----
            rot = k % len(vals)
            vals = vals[rot:] + vals[:rot]
            
            idx = 0
            
            # ----- fill back -----
            
            # top row
            for c in range(left, right + 1):
                grid[top][c] = vals[idx]
                idx += 1
            
            # right column
            for r in range(top + 1, bottom + 1):
                grid[r][right] = vals[idx]
                idx += 1
            
            # bottom row
            for c in range(right - 1, left - 1, -1):
                grid[bottom][c] = vals[idx]
                idx += 1
            
            # left column
            for r in range(bottom - 1, top, -1):
                grid[r][left] = vals[idx]
                idx += 1
        
        return grid