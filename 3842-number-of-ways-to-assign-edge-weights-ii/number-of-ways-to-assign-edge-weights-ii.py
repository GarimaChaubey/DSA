class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        
        MOD = 10**9 + 7
        
        n = len(edges) + 1
        
        LOG = 17
        
        while (1 << LOG) <= n:
            LOG += 1
        
        graph = [[] for _ in range(n + 1)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]
        
        stack = [(1, 0)]
        
        while stack:
            node, parent = stack.pop()
            
            up[node][0] = parent
            
            for nxt in graph[node]:
                if nxt != parent:
                    depth[nxt] = depth[node] + 1
                    stack.append((nxt, node))
        
        for j in range(1, LOG):
            for node in range(1, n + 1):
                up[node][j] = up[up[node][j - 1]][j - 1]
        
        def lca(a, b):
            
            if depth[a] < depth[b]:
                a, b = b, a
            
            diff = depth[a] - depth[b]
            
            for j in range(LOG):
                if diff & (1 << j):
                    a = up[a][j]
            
            if a == b:
                return a
            
            for j in range(LOG - 1, -1, -1):
                if up[a][j] != up[b][j]:
                    a = up[a][j]
                    b = up[b][j]
            
            return up[a][0]
        
        ans = []
        
        for u, v in queries:
            
            ancestor = lca(u, v)
            
            length = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )
            
            if length == 0:
                ans.append(0)
            else:
                ans.append(pow(2, length - 1, MOD))
        
        return ans