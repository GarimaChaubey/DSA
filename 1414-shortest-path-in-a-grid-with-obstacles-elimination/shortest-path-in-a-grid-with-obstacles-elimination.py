from collections import deque

class Solution:
    def shortestPath(self, grid, k):
        
        m, n = len(grid), len(grid[0])
        
       
        if k >= m + n - 2:
            return m + n - 2
        
        visited = set()
        q = deque([(0, 0, k, 0)]) 
        
        visited.add((0, 0, k))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            r, c, k_left, steps = q.popleft()
            
            if r == m-1 and c == n-1:
                return steps
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    
                    new_k = k_left - grid[nr][nc]
                    
                    if new_k >= 0 and (nr, nc, new_k) not in visited:
                        visited.add((nr, nc, new_k))
                        q.append((nr, nc, new_k, steps + 1))
        
        return -1