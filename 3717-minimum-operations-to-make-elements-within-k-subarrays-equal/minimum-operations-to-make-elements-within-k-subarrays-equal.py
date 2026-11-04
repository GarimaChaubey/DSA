
class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)

        values = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(values)}
        size = len(values)

        count = [0] * (size + 1)
        total = [0] * (size + 1)

        def update(bit, i, val):
            while i <= size:
                bit[i] += val
                i += i & -i

        def query(bit, i):
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & -i
            return result

        def get_kth(kth):
            idx = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= size and count[nxt] < kth:
                    kth -= count[nxt]
                    idx = nxt

                step >>= 1

            return idx + 1

        def window_cost():

            mid_idx = get_kth((x + 1) // 2)
            median = values[mid_idx - 1]

            left_count = query(count, mid_idx)
            left_sum = query(total, mid_idx)

            right_count = x - left_count

            all_sum = query(total, size)
            right_sum = all_sum - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        for i in range(x):
            idx = rank[nums[i]]
            update(count, idx, 1)
            update(total, idx, nums[i])

        costs = [window_cost()]

        for i in range(x, n):

            old_idx = rank[nums[i - x]]
            update(count, old_idx, -1)
            update(total, old_idx, -nums[i - x])

            new_idx = rank[nums[i]]
            update(count, new_idx, 1)
            update(total, new_idx, nums[i])

            costs.append(window_cost())

        INF = float('inf')

        prev = [0] * (n + 1)

        for t in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                curr[i] = curr[i - 1]

                if i >= x:
                    start = i - x

                    curr[i] = min(
                        curr[i],
                        prev[start] + costs[start]
                    )

            prev = curr

        return prev[n]
