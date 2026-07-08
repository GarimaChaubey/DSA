from bisect import bisect_left, bisect_right

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        m = len(digits)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix value of concatenated digits
        prefVal = [0] * (m + 1)
        for i in range(m):
            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD

        # prefix digit sums
        prefSum = [0] * (m + 1)
        for i in range(m):
            prefSum[i + 1] = prefSum[i] + digits[i]

        ans = []

        for l, r in queries:

            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (
                prefVal[right + 1]
                - prefVal[left] * pow10[length]
            ) % MOD

            digit_sum = prefSum[right + 1] - prefSum[left]

            ans.append((x * digit_sum) % MOD)

        return ans