class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 0

        for x in nums:
            if x >= first:
                second = first
                first = x
            elif x > second:
                second = x

        return (first - 1) * (second - 1)