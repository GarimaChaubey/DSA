
class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        right = [[-1] * n for _ in range(m)]
        down = [[-1] * n for _ in range(m)]

        # Precompute reflection destinations
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if grid[i][j] == 0:
                    right[i][j] = i * n + j
                    down[i][j] = i * n + j

                else:
                    # Entering mirror while moving right
                    if i + 1 < m:
                        right[i][j] = down[i + 1][j]

                    # Entering mirror while moving down
                    if j + 1 < n:
                        down[i][j] = right[i][j + 1]

        # DP to count paths
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):

                ways = dp[i][j]

                if ways == 0:
                    continue

                # Try moving right
                if j + 1 < n:
                    dest = right[i][j + 1]

                    if dest != -1:
                        x = dest // n
                        y = dest % n

                        dp[x][y] = (dp[x][y] + ways) % MOD

                # Try moving down
                if i + 1 < m:
                    dest = down[i + 1][j]

                    if dest != -1:
                        x = dest // n
                        y = dest % n

                        dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]
