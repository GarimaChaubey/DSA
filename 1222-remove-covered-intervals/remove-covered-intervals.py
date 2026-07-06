class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        maxEnd = 0

        for start, end in intervals:

            if end > maxEnd:
                ans += 1
                maxEnd = end

        return ans