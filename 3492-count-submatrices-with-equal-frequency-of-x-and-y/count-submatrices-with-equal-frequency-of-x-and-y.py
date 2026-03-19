class Solution(object):
    def numberOfSubmatrices(self, grid):

        m = len(grid)
        n = len(grid[0])

        px = [[0]*n for _ in range(m)]
        py = [[0]*n for _ in range(m)]

        count = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 'X':
                    px[i][j] = 1
                elif grid[i][j] == 'Y':
                    py[i][j] = 1

                if i > 0:
                    px[i][j] += px[i-1][j]
                    py[i][j] += py[i-1][j]

                if j > 0:
                    px[i][j] += px[i][j-1]
                    py[i][j] += py[i][j-1]

                if i > 0 and j > 0:
                    px[i][j] -= px[i-1][j-1]
                    py[i][j] -= py[i-1][j-1]

                if px[i][j] == py[i][j] and px[i][j] > 0:
                    count += 1

        return count