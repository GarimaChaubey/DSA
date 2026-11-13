
class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        LOG = n.bit_length()

        up = [[n] * (n + 1) for _ in range(LOG)]
        sm = [[0] * (n + 1) for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nxt[i]
            sm[0][i] = nums[i] * (nxt[i] - i)

        for p in range(1, LOG):
            for i in range(n):
                mid = up[p - 1][i]

                up[p][i] = up[p - 1][mid]
                sm[p][i] = sm[p - 1][i] + sm[p - 1][mid]

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def getCost(l, r):
            cur = l
            total = 0

            for p in range(LOG - 1, -1, -1):
                j = up[p][cur]

                if j <= r:
                    total += sm[p][cur]
                    cur = j

            total += nums[cur] * (r - cur + 1)

            total -= prefix[r + 1] - prefix[l]

            return total

        ans = 0
        left = 0

        for right in range(n):
            while getCost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans
