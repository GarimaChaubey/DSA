from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums, queries):
        
        n = len(nums)
        
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = []
        
        for q in queries:
            val = nums[q]
            indices = pos[val]
            
            if len(indices) == 1:
                ans.append(-1)
                continue
            
            idx = bisect.bisect_left(indices, q)
            
            left = indices[idx - 1] if idx > 0 else indices[-1]
           
            if idx + 1 < len(indices):
                right = indices[idx + 1]
            else:
                right = indices[0]
     
            d1 = abs(q - left)
            d2 = abs(q - right)
        
            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)
            
            ans.append(min(d1, d2))
        
        return ans