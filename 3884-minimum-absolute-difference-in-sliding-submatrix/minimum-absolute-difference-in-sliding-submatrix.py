class Solution:
    def minAbsDiff(self, grid, k):
        
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                
                vals = set()  
                
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        vals.add(grid[r][c])
                
                vals = sorted(vals)
                
                if len(vals) <= 1:
                    ans[i][j] = 0
                    continue
                
                min_diff = float('inf')
                
                for x in range(1, len(vals)):
                    min_diff = min(min_diff, vals[x] - vals[x-1])
                
                ans[i][j] = min_diff
        
        return ans