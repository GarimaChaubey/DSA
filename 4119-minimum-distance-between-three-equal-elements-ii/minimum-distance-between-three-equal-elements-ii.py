from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        
        pos = defaultdict(list)
        ans = float('inf')
        
        for i, val in enumerate(nums):
            pos[val].append(i)
            
            # check only last 3
            if len(pos[val]) >= 3:
                a, b, c = pos[val][-3:]
                
                dist = abs(a-b) + abs(b-c) + abs(c-a)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1