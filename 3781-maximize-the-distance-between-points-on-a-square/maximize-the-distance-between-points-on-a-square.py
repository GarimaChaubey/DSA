import bisect

class Solution:
    def maxDistance(self, side, points, k):

        def pos(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            return 4 * side - y

        arr = sorted(pos(x, y) for x, y in points)
        n = len(arr)
        per = 4 * side

        ext = arr + [x + per for x in arr]

        def can(d):
            # next valid jump using two pointers
            nxt = [0] * (2 * n)
            j = 0

            for i in range(2 * n):
                if j < i + 1:
                    j = i + 1
                while j < 2 * n and ext[j] - ext[i] < d:
                    j += 1
                nxt[i] = j

            for start in range(n):
                cur = start
                cnt = 1

                while cnt < k:
                    cur = nxt[cur]
                    if cur >= start + n:
                        break
                    cnt += 1

                if cnt == k:
                    # closing circular gap
                    if per - (ext[cur] - ext[start]) >= d:
                        return True

            return False

        lo, hi = 0, 2 * side
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2

            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans