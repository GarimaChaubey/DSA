class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """

        odd = 0
        even = 0

        for x in nums1:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1

        if odd == 0 or even == 0:
            return True

        return True