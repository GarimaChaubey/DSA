from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = []

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        L = len(litter)

        if L == 0:
            return 0

        litter_id = {}
        for i, pos in enumerate(litter):
            litter_id[pos] = i

        target = (1 << L) - 1

        queue = deque()
        queue.append((start[0], start[1], 0, energy, 0))

        visited = {}
        visited[(start[0], start[1], 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mask, power, moves = queue.popleft()

            if mask == target:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_power = power - 1

                if new_power < 0:
                    continue

                new_mask = mask

                if (nr, nc) in litter_id:
                    bit = litter_id[(nr, nc)]
                    new_mask |= (1 << bit)

                if classroom[nr][nc] == 'R':
                    new_power = energy

                key = (nr, nc, new_mask)

                if key in visited and visited[key] >= new_power:
                    continue

                visited[key] = new_power
                queue.append(
                    (nr, nc, new_mask, new_power, moves + 1)
                )

        return -1