class Solution:
    def findMin(self, nums):
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            mid = (left + right) // 2
            
            # minimum on right side
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # minimum on left side including mid
            elif nums[mid] < nums[right]:
                right = mid
            
            # duplicates
            else:
                right -= 1
        
        return nums[left]