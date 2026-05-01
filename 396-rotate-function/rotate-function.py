class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        
        total = sum(nums)
        
        F = sum(i * nums[i] for i in range(n))
        
        ans = F
        
        for k in range(1, n):
            F = F + total - n * nums[n - k]
            ans = max(ans, F)
        
        return ans