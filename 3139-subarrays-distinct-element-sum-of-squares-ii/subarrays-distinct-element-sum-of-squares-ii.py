class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, delta):
            length = r - l + 1
            old_sum = tree_sum[node]

            tree_sq[node] = (
                tree_sq[node]
                + 2 * delta * old_sum
                + delta * delta * length
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + delta * length
            ) % MOD

            lazy[node] += delta

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            d = lazy[node]

            apply(node * 2, l, mid, d)
            apply(node * 2 + 1, mid + 1, r, d)

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for r, x in enumerate(nums):
          
            p = last.get(x, -1)

            update(1, 0, n - 1, p + 1, r)

            ans = (ans + tree_sq[1]) % MOD

            last[x] = r

        return ans
        