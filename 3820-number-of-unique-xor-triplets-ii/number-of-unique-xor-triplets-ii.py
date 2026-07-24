class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = list(set(nums))
        MAXX = 2048  # 2^11

        dp = [False] * MAXX
        dp[0] = True

        for _ in range(3):
            ndp = [False] * MAXX
            for x in range(MAXX):
                if dp[x]:
                    for v in vals:
                        ndp[x ^ v] = True
            dp = ndp

        ans = 0
        for ok in dp:
            if ok:
                ans += 1
        return ans