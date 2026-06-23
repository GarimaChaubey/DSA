class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7

        m = r - l + 1

        if n == 1:
            return m % MOD

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        # length = 2
        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v

        if n == 2:
            return (sum(up) + sum(down)) % MOD

        for _ in range(3, n + 1):

            newUp = [0] * (m + 1)
            newDown = [0] * (m + 1)

            pref = 0
            for v in range(1, m + 1):
                newUp[v] = pref
                pref = (pref + down[v]) % MOD

            suff = 0
            for v in range(m, 0, -1):
                newDown[v] = suff
                suff = (suff + up[v]) % MOD

            up = newUp
            down = newDown

        return (sum(up) + sum(down)) % MOD