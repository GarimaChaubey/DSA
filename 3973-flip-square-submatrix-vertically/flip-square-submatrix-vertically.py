class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        for i in range(k // 2):
            for j in range(k):
                r1, c1 = x + i, y + j
                r2, c2 = x + k - 1 - i, y + j
                
                grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]
        
        return grid