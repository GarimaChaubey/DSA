class Solution(object):
    def getBiggestThree(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        s = set()

        for i in range(m):
            for j in range(n):

                s.add(grid[i][j])   # radius = 0

                k = 1
                while True:

                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break

                    total = 0

                    x = i-k
                    y = j

                    for t in range(k):
                        total += grid[x+t][y+t]

                    for t in range(k):
                        total += grid[i+t][j+k-t]

                    for t in range(k):
                        total += grid[i+k-t][j-t]

                    for t in range(k):
                        total += grid[i-t][j-k+t]

                    s.add(total)
                    k += 1

        res = sorted(s, reverse=True)

        return res[:3]