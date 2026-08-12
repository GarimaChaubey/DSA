class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            x = nums[right]

            freq[x] = freq.get(x, 0) + 1

            # Window is invalid
            while freq[x] > k:
                freq[nums[left]] -= 1
                left += 1

            # Current window is valid
            ans = max(ans, right - left + 1)

        return ans