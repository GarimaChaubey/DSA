class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        arr = []
        for x in nums:
            if x == target:
                arr.append(1)
            else:
                arr.append(-1)

        pref = [0]
        s = 0
        for x in arr:
            s += x
            pref.append(s)

        vals = sorted(set(pref))
        rank = {}
        for i, v in enumerate(vals):
            rank[v] = i + 1

        m = len(vals)
        bit = [0] * (m + 2)

        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0

        for p in pref:
            idx = rank[p]
            ans += query(idx - 1)   
            update(idx)

        return ans