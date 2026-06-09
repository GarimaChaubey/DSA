class Solution(object):
    def maxTotalValue(self, nums, k):
        mx = max(nums)
        mn = min(nums)
        
        return k * (mx - mn)
        