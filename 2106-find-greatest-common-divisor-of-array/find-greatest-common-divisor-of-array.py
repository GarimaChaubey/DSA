class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        return self.gcd(mn, mx)