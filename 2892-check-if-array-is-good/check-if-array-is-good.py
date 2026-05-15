class Solution:
    def isGood(self, nums):
        
        nums.sort()
        
        n = nums[-1]
        
        # expected length should be n+1
        if len(nums) != n + 1:
            return False
        
        # check 1 to n-1
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        
        # last two should be n
        return nums[-1] == n and nums[-2] == n