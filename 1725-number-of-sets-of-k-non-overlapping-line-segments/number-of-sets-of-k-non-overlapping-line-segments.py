class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        r = 2 * k
        N = n + k - 1

        ans = 1

        for i in range(1, r + 1):
            ans = ans * (N - i + 1) // i

        return ans % MOD