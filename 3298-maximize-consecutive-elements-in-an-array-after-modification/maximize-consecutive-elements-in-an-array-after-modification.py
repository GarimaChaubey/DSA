class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()

        dp = {}
        ans = 1

        for x in nums:
            a = dp.get(x - 1, 0) + 1
            b = dp.get(x, 0) + 1

            dp[x] = max(dp.get(x, 0), a)
            dp[x + 1] = max(dp.get(x + 1, 0), b)

            ans = max(ans, dp[x], dp[x + 1])

        return ans