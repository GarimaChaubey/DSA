class Solution(object):
    def minSwaps(self, grid):

        n = len(grid)
        trailing = []

        # Step 1: count trailing zeros for each row
        for row in grid:
            count = 0
            for j in range(n-1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing.append(count)

        swaps = 0

        # Step 2: greedy placement
        for i in range(n):

            needed = n - 1 - i
            j = i

            # find first row with enough zeros
            while j < n and trailing[j] < needed:
                j += 1

            if j == n:
                return -1   # impossible

            # bubble up
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                swaps += 1
                j -= 1

        return swaps