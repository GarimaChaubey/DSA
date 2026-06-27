class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        cnt = Counter(nums)
        ans = 1

       
        if 1 in cnt:
            if cnt[1] % 2:
                ans = max(ans, cnt[1])
            else:
                ans = max(ans, cnt[1] - 1)

        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt.get(cur, 0) >= 2:
                length += 2
                cur = cur * cur

            if cnt.get(cur, 0) >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans