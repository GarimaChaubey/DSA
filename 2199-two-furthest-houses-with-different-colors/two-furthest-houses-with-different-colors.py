class Solution:
    def maxDistance(self, colors):
        
        n = len(colors)

        if colors[0] != colors[n - 1]:
            return n - 1
        
        ans = 0

        for i in range(n):
            if colors[i] != colors[n - 1]:
                ans = max(ans, n - 1 - i)
                break
      
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                ans = max(ans, j)
                break
        
        return ans