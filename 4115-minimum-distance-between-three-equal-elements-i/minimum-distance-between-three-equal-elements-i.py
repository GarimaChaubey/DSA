from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = float('inf')
        for indices in pos.values():
            
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                a = indices[i]
                b = indices[i+1]
                c = indices[i+2]
                
                dist = abs(a-b) + abs(b-c) + abs(c-a)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1