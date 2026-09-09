class Solution(object):
    def countCommas(self, n):
        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = start * 1000 - 1

            if end > n:
                end = n

            count = end - start + 1
            ans += count * commas

            start *= 1000
            commas += 1

        return ans