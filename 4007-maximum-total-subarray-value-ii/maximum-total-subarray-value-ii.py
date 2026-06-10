import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)

        LOG = (n).bit_length()

        st_max = [nums[:]]
        st_min = [nums[:]]

        j = 1
        while (1 << j) <= n:
            prev_max = st_max[j - 1]
            prev_min = st_min[j - 1]
            length = 1 << (j - 1)

            cur_max = [
                max(prev_max[i], prev_max[i + length])
                for i in range(n - (1 << j) + 1)
            ]
            cur_min = [
                min(prev_min[i], prev_min[i + length])
                for i in range(n - (1 << j) + 1)
            ]

            st_max.append(cur_max)
            st_min.append(cur_min)
            j += 1

        def range_value(l, r):
            length = r - l + 1
            p = length.bit_length() - 1

            mx = max(
                st_max[p][l],
                st_max[p][r - (1 << p) + 1]
            )

            mn = min(
                st_min[p][l],
                st_min[p][r - (1 << p) + 1]
            )

            return mx - mn

        heap = []

        for l in range(n):
            r = n - 1
            val = range_value(l, r)
            heapq.heappush(heap, (-val, l, r))

        ans = 0

        for _ in range(k):
            neg_val, l, r = heapq.heappop(heap)
            ans += -neg_val

            if r > l:
                nr = r - 1
                nval = range_value(l, nr)
                heapq.heappush(heap, (-nval, l, nr))

        return ans
        