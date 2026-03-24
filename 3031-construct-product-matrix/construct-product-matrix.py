class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        
        n, m = len(grid), len(grid[0])
  
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j] % MOD)
        
        size = len(arr)

        res = [1] * size
    
        left = 1
        for i in range(size):
            res[i] = left
            left = (left * arr[i]) % MOD
  
        right = 1
        for i in range(size - 1, -1, -1):
            res[i] = (res[i] * right) % MOD
            right = (right * arr[i]) % MOD
        
        
        ans = [[0] * m for _ in range(n)]
        
        for i in range(size):
            r = i // m
            c = i % m
            ans[r][c] = res[i]
        
        return ans